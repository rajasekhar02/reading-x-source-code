## Line Sweep Algorithms

[https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms](link)
Line Sweep (or Sweep Line) is an algorithmic technique where we sweep an imaginary line (x or y axis) and solve various problem.
There would be an event (entry or event) and based on that we update the information and then return result.

This is going to be a long post, so I have divided into 3 parts.

1. 1D Easy/Medium problem.
2. 1D Hard.
3. 2D geometric problems.

There could be errors, please post in comments.  
Also suggest more problem to be added to this list.  
Inviting @votrubac @lee215 to give suggestion for improvment.

### 1D Easy/Medium problem

[1854. Maximum Population Year](https://leetcode.com/problems/maximum-population-year/) [**Easy**]  
Here we are given birth & death year of persons.
Imagine this as a line , when a person born , population of that year +1 and when he expires population decreases by 1.  
![image](https://user-images.githubusercontent.com/20656683/173176474-fb0392a8-82c5-4620-8c1a-1cb54cf4cad6.png)

Plot the population year on a number line.
When a person is born increment by +1 and when he expire decrement by -1 .
Scan from left and accumulate the population, everytime check if current population is greater than global max , if yes update population count and year both.
This scanning from left to right is line sweep.

Time Complexity = O(n log n) (due to tree map) initiialization, iteration of map take O(n) time.

<details>
<summary>

#### Click to see Code

</summary>

    int maximumPopulation(vector<vector<int>>& logs) {
        map<int, int> line;
        for(auto& p : logs){
            ++line[p[0]];
            --line[p[1]];
        }
        int max_p = 0;
        int ans_year;
        int count = 0;
        for(auto& i : line){
            count += i.second;
            if(count > max_p){
                max_p = count;
                ans_year = i.first;
            }
        }
        return ans_year;
    }

</details>

More easy problem to practice:

[2848. Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/)

<details>
<summary>

#### Click to see Code

</summary>

       int numberOfPoints(vector<vector<int>>& nums) {
        int line [102] ={};
        for(auto& p : nums){
            line[p[0]]++;
            line[p[1]+1]--;
        }
        int ans =0;
        int count =0;
        for(int i =0; i <102; ++i){
            count += line[i];
            if(count > 0){
                ++ans;
            }
        }
        return ans;
    }

</details>

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) [ **Medium**]  
Same as above just we have to keep track of maximum count of rooms and return it.  
When a meeting start we plot +1 for end we do -1.
Now we scan the line, and store the value in `count` , if count is 1 that mean 1 meeting start, if its 2 that means 2nd meeting started before 1st ended, so we need 2 room atleast. This count we save in `ans` if `count > ans` .

```
class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        map<int, int> line;
        for(auto& i : intervals){
            line[i.start]++;
            line[i.end]--;
        }
        int ans = 0;
        int count;
        for(auto& p : line){
            count += p.second;
            ans = max(ans, count);
        }
        return ans;
    }
};
```

Time Complexity = O(n log n )

[731. My Calendar II](https://leetcode.com/problems/my-calendar-ii/) [ **Medium** ]  
We have to count if there are triple booking , so if at any time we have count >=3 (==3 is enough)  
We return false and also remove this booking from the entry.  
Same approach, use a map and +1 when booking start and -1 when booking end.  
Sweep the line from left to right.

Time Complexity = O(n^2 \* log n ) as for every booking we are sweeping entire line.

```
bool book(int start, int end) {
        ++m[start];
        --m[end];
        int count = 0;
        for(auto& i : m){
            count += i.second;
            if(count ==3){
                // we are not going to add this event
                // nullify line 10,11 changes
                --m[start];
                ++m[end];
                return false;
            }
        }
        return true;
    }
```

[2237. Count Positions on Street With Required Brightness](https://leetcode.com/problems/count-positions-on-street-with-required-brightness/) [ **Medium** ]  
Similar, here we are given a threshold of brightness for each index, first fill up the count by +1 and -1 index where brightness start and end.  
Now scan the vector and see if threshold achieved , if yes ++ans.

Time Complexity = O(n)

<details>
<summary>

#### Click to see Code

</summary>

     bool isCovered(vector<vector<int>>& ranges, int left, int right) {

      int line[52] = {};
    for (auto &r : ranges) {

        line[r[0]] += 1;
        line[(r[1]+1)] -= 1;
    }

    for (int i = 1, overlaps = 0; i <= 51; ++i) {
        overlaps += line[i];
        if (i>=left and i <=right and overlaps <= 0)
            return false;
    }

    return true;
    }

</details>

[1893. Check if All the Integers in a Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) [**Easy** ]  
Mark start and end( end+1 since its a closed interval] as +1/-1 respectively.  
Now scan the line from 1 to 50 , see which co-ordinate falls in given [left right] range and overlap is 0, that mean no range is covering , return false.

Time Complexity = O(n)

[370. Range Addition](https://leetcode.com/problems/range-addition/) [ **Medium**]  
Accumulate +update in start and -update in end+1  
After that sweep the line and accumulate sum in a variable and keep assigning to every index.

Time Complexity = O(n)

**Type 2**:
In this kind of problem, you may not be able to plot the point and arrive at solution. Instead you have to use **prev** technique.  
Lets see this example

[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) [ **Medium**]  
In this kind of problem, we dont use marking on axis, instead axis is already given, we sort it.

> Initial setup after sort

    ![image](https://assets.leetcode.com/users/images/73811d36-8aea-4576-b945-797c86573561_1689758547.3407717.png)

> Hitting first ballon

    ![image](https://assets.leetcode.com/users/images/94941364-9c75-4d32-9ec7-2b5c1ba8b300_1689759385.382266.png)

Now if we strike first ballon , we can strike at the end-most point i.e. **2**  
We save this as **prev = 2**  
Any ballon starting before we dont need extra arraow since this arrow is enough to burst the ballon.  
The moment start point > prev , we know we need a new ballon again we save the end-most point in the prev and repeat the process.  
Many problem can be solved using this technique.

```
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        auto cmp = [&](const vector<int>& a, const vector<int>& b){

            return a[1] < b[1];
        };
        sort(points.begin(), points.end(), cmp);
        int prev_end = points[0][1];
        int ans = 1;
        for(int i =1; i < points.size(); ++i){
            if(points[i][0] > prev_end){
                ++ans;
                prev_end = points[i][1];
            }
        }
        return ans;
    }
};
```

[435 Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) [ **Medium** ]

**Why Sorting with endTimes Works**
In many of the problem above we do sorting with endTime , this is an important concept to understand,
if you sort with endTime and then check other intervals you can easily find non-overlapping intervals like this, here prev is previous interval.

```
if(intervals[i][0] < intervals[prev][1])
```

Reason is if a new interval start is before previous end time that means a sure overlap.
While on the other hand if we sort by startTime, we dont know when this interval gonna end, there will be overlaps.
Here are some additional points to consider:

**Sorting by end time is a greedy algorithm**. This means that it makes the best possible choice at each step, without considering the future. As a result, it is usually more efficient than sorting by start time.
**Sorting by start time is a dynamic programming algorithm**. This means that it makes a choice at each step, based on the choices that it has made in the past. As a result, it is usually more robust to errors in the input data.
For practice try to solve this problem , which can be solved in both DP as well as Greey Way and see the difference

[646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)

[252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) [ **Easy**]  
Just scan and if ith start < i-1 end return false

**Insert Interval**  
Suppose we haev insert [3,7] to an existing interval [1, 10]  
For each start we do +1 and for end we do -1 on the number line (map).  
Next scan the line, if the count is 0, that mean a new line is going to start, so mark it as start  
And then accumulate the count, now if count is 0, that mean the interval has ended so insert this interval.

![image](https://assets.leetcode.com/users/images/f57fbab6-c436-4aeb-9231-fca64dc5a0c8_1694355372.721946.png)

[57. Insert Interval](https://leetcode.com/problems/insert-interval/) [ **Medium** ]

### Using Map counter

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        map<int, int> m;
        for(auto& p : intervals){
            ++m[p[0]];
            --m[p[1]];
        }
        ++m[newInterval[0]];
        --m[newInterval[1]];
        int count = 0;
        vector<vector<int>> ans;
        int start;
        for(auto& i : m){
            if(count==0){
                start = i.first;
            }
            count += i.second;
            if(count == 0){
                ans.push_back({start, i.first});
            }
        }
        return ans;
    }
};
```

### Using Interval

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {

        vector<vector<int>> ans;
        for(auto& i : intervals){
            if(i[1] < newInterval[0]){
                ans.push_back(i);
            }
            else if( newInterval[1] < i[0]){
                ans.push_back(newInterval);
                newInterval = i;
            }
            else if((i[1] >= newInterval[0])  or ( newInterval[1] <=i[0])){
                /*
                ------ [i]
                   ------- [new]

                ------
             ------
             */
             newInterval[0] = min(newInterval[0], i[0]);
             newInterval[1] = max(newInterval[1], i[1]);
            }
        }
        ans.push_back(newInterval);
        return ans;
    }
};
```

[1272. Remove Interval](https://leetcode.com/problems/remove-interval/) [ **Medium** ]

**Approach #1**:
increment at start and decrement end , while for remove interavl do reverse since we have to remove
standard logic of count==i.start and count > 0
and for closing interval count=0 and we have added previously(use a bool flag)

**Approach #2**:
Input is sorted, so we sweep and if removed_start > ith_end or remove_end < ith_start , we simply add the ith boundary to o/p.  
Otherwise if ith_start < remove_start -> add ith_start, remove_start  
Also if ith_end > remove_end then add [remove_end, ith_end]

Both approach coded for comparison, Merge Interval and Insert Interval can also be solved using similar approach.  
Please let me know in comment section which approach is preferable as I am still learning.  
Its a bit tough to come up Approach 1 for all problem but Approach 2 works for all.

### Using Map counter

```c++
        map<int, int> line;

	for(auto& i : intervals)
	{
		++line[i[0]];
		--line[i[1]];
	}
	--line[toBeRemoved[0]];
	++line[toBeRemoved[1]];
	vector<vector<int>> ans;
	int count =0; bool added =false;
	for(auto& i : line)
	{
		count += i.second;
		if(count ==1 ){
			ans.push_back({i.first, -1});
			added = true;
		}
		if(count==0 and added){
			ans.back()[1] = i.first;
			added = false;
		}
	}
	return ans;
```

### Using prev interval

```c++
	vector<vector<int>> ans;

	for(auto &i :  intervals)
	{
		int left = i[0];
		int right = i[1];
		if( (toBeRemoved[0] > right ) or (toBeRemoved[1] < left ))
		{
			ans.push_back({left, right});
		}
		else
		{
			if(left < toBeRemoved[0])
			{
				ans.push_back({left, toBeRemoved[0]});
			}
			if (right > toBeRemoved[1])
			{
				ans.push_back({toBeRemoved[1], right});
			}
		}
	}
```

**Approach 1 details**
For insert interval : when we start , `if count is 0` that essentially means a new begining , so record the start poisition.
Now after we are done adding line value to count and still count is 0 , that essentially mean interval ended, so use the previously recorded start and now this endging value to form a interval. Let see the example input this with a image, **before we start processing if count is 0 and we record as start of new interval** and **after processing** if it is still 0, that mean end of intervals.

![image](https://assets.leetcode.com/users/images/47947991-bf67-41a5-87e1-393045a17cfa_1700714223.3685725.png)
Before processing 1 , which is start of interval, count is 0 so we mark start =1, after we process count is 1
Process 2 , as it is start , count =2
Process 3 , as it is end , count =1
Process 5, as it is end count = 0 , now since count is 0 after process we insert [1, 5] in answer.
Process 6, since count is 0 **before process**, this is start of new interval, record start =6 and now process start - 6
Procss 9 , count will be 0 **after process** , so that mean its end , record [6, 9] in answer.

For **Remove Interval** sweep approach is similar except now we have to remove the interval , that we mark start as -ve and end as +ve marking on line ans tweak the sount logic.  
Now try to solve this problem using same count technique.

[1229. Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) [**Medium**]

Some pointers, we have 2 candidate, so if both have started only then only take there latest time, for example
suppose Person is available from [10:00 , 12:00] but person 2 is available from [11:00 , 12:00]
after we sweep the line past [11:00] count would be 2 and then we can take [11:00] as candidate start time as this time is common to both person.

Next whenever we encounter an end of time AND we have already noted down the common_time , check if we met the duration ? if yes return , because this earlies, otherwise reset the common_time, as now we have to find some common start all over again.

<details>
<summary>

#### Click to see Code

</summary>

    Interval earliestAppropriateDuration(vector<Interval> &slots1, vector<Interval> &slots2, int duration) {
        // --- write your code here ---
        map<int, int> m;
        for(auto& i : slots1){
            m[i.start]++;
            m[i.end]--;
        }
        for(auto& i : slots2){
            m[i.start]++;
            m[i.end]--;
        }
        int count = 0;
        Interval candidate(-1, -1);

        for(auto& p : m){
            int old = count;
            count += p.second;
            if(count ==2){
                candidate.start = p.first;
            }
            // If count is decreasing that mean some slot is ending
            if(count < old and candidate.start!=-1){
                if(p.first - candidate.start >= duration) // we found
                {
                    candidate.end = candidate.start+duration;
                    return candidate;
                }
                else{
                    candidate.start = -1;
                }
            }
        }
        return {-1, -1};
    }

</details>

[1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) [ **Medium** ]  
Step 1: Sort with start, if both start are same , give precedence to higher ending interval first.  
Step 2: Insert the first interval uncondtionally , after that scan the other interavl , following 3 possibility (see code comment can occur)

```
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {

        vector<vector<int>> ans;
        auto comp = [&](const vector<int>& i, const vector<int>& j){
            if(i[0]==j[0])
                return i[1] > j[1];
            return i[0] < j[0];
        };
        sort(intervals.begin(), intervals.end(), comp);
        ans.push_back(intervals[0]);
        int k =0;
        for(int i =1; i< intervals.size(); ++i){
            if( (intervals[i][0]>= ans.back()[0]) and (intervals[i][1] <= ans.back()[1]))
            {
			   // Scenario 1: Completely covered suppose existing interval in vector is [1, 8] and this ith interval is [2, 6] , this is completely inside i.e. start and end
			   // lies inside , hence this interval is surely removed, count this.
                ++k;
            }
            else if(intervals[i][0] > ans.back()[1]){
			// Scenario 2: Suppose vector has [1, 8]  and ith interval is  [9, 10] , totallly unrelated, so push this interval in vector as this is going to be used next time.
                ans.push_back(intervals[i]);
            }
            else if ((intervals[i][0] > ans.back()[0]) and (intervals[i][0] <= ans.back()[1]) )
			    // Scenario 3: vector has [1, 8] and ith interval is  [5, 10], so take maximum of both end point.
                ans.back()[1] = max(ans.back()[1], intervals[i][1]);
        }
        return intervals.size()- k;
    }
};
```

[1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) [ **Medium**]

Add detailed comments in code , please check , here the key idea is we are sweeping the day as a number line, it is given in input and we mark the events on that day line.

```
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        multiset<int> eventEndTime;
        int i =0;
        int ans = 0;
        int n = events.size();
        for(int d =1; d <=100000; ++d){
            //Delete expired event , example
            // Suppose 3 events are there  [1, 2] [1, 2] [1, 2]
            // at day 1 : attend 1st event and at day 2 attend 2md event , at day 3 , 3rd event is already expired, hence we need this kind of loop of loop to delete expired events
            while(!eventEndTime.empty() and *eventEndTime.begin() < d){
                eventEndTime.erase(eventEndTime.begin());
            }

            // put all candidate events whose start day is past the current day.

            //insert events if they can be start
            while(i < n and events[i][0] <=d){
                eventEndTime.insert(events[i][1]);
                i++;
            }

            // we can attend 1 event on 1 day , thats why if condition not while
            // adn we attend earliest ending event first , suppose we have [1, 2] & [1, 3]
            // and we are on day=2, we should attend [1,2] first otherwise at d=3 this would be expired
            if(!eventEndTime.empty() and *eventEndTime.begin()>=d){
                ++ans;
                eventEndTime.erase(eventEndTime.begin());
            }
        }
        return ans;
    }
};
```

[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) [ **Medium**]

### Using Map counter

```c++
    	class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        map<int, int> line;
        for(auto& i : intervals){
            ++line[i[0]];
            --line[i[1]];
        }

        int count = 0;
        vector<vector<int>> ans;
        int start = 0;
        for(auto& i : line){
            // that means its a new start, store the start
           if(count ==0){
               start = i.first;
           }
           count += i.second;
           // this mean interval ends, and we can push this as answer
           if(count==0){
               ans.push_back({start, i.first});
           }
        }
        return ans;
    }
};
```

### Using prev interval

```c++
	sort(intervals.begin(), intervals.end());// Sort y there start time
        vector<vector<int>> results;
        results.push_back(intervals[0]);
        for(int i =1; i < intervals.size(); ++i){
            if(intervals[i][0] > results.back()[1]) // a new begining
            {
                results.push_back(intervals[i]);
            }
            else
                results.back()[1] = max(results.back()[1], intervals[i][1]);
        }
        return results;
```

[1589. Maximum Sum Obtained of Any Permutation](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) [ **Medium**]  
[1943. Describe the Painting](https://leetcode.com/problems/describe-the-painting/) [ **Medium** ]  
[1674. Minimum Moves to Make Array Complementary](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) [ **Medium**]

### 1D Hard problem

These 1D Hard problem require scanning line for each input which can lead to O(n^2) algorithm.  
We have to do something special to optimize it.  
Lets see with an example.

[2158. Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/) [**Hard** ]  
In this problem each day we paint some section of a line.  
Brute force way is scan line for each input index.

Thanks to @cjcoax and @votrubac, I am putting both line sweep version and map interval method here.  
Similar problem
[2251. Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) [ **Hard**]

### Using Line Sweep

```c++
    	auto cmp =[&](const vector<int>& a, const vector<int>& b){
            return a[1]  < b[1];
        };
        int maxEnd = (*max_element(paint.begin(), paint.end(), cmp))[1];
        int n = paint.size();
        vector<int> ans(n, 0);
        vector<vector<pair<int, int>>> line(1 + maxEnd);
        // We are marking on line that co-oridnate is
	// painted/not-painted(true-false) between which date
        for(int i =0; i < n ; ++i){
            line[paint[i][0]].push_back(make_pair(i, 1));
            line[paint[i][1]].push_back(make_pair(i, 0));
        }

        set<int> days;
        //Scan the line
        for(int i =0; i < maxEnd; ++i){

            // Who all present on this x co-ordinate?
            for(auto& [day, state] : line[i]){

                if(state)
                    days.insert(day);
                else
                    days.erase(day);
            }
            //Only the first guy can paint this line
            if(!days.empty())
                ans[*(days.begin())]++;
        }
        return ans;
```

### Using Vector Interval

```c++
	map<int, int> m;
    vector<int> res;
    for (auto &p : pt) {
        int l = p[0], r = p[1];
        auto next = m.upper_bound(l), cur = next;

        // Step 1: suppose we have painted [1, 4] [ 5, 8] [10, 20]
        // Now a new interval [4, 21] comes upper_bound gives [5,8]
        // l = 4 then
        if (cur != begin(m) && prev(cur)->second >= l) {
            cur = prev(cur);
            l = cur->second;
        }
        else
            cur = m.insert({l, r}).first;
        int paint = r - l;
        // Next since r= 21 and that is  > 5, that means this paint is going to span
        // find how much shd we subtract :
        // get min of (21, 8) =  8 and then subtratc with start 5 = 3
        // now r shd be max of (21, 8) =21 , check further more intervals can be erased ?
        // in the end set curr->second = max(curr->second, r);
        while (next != end(m) && next->first < r) {
            paint -= min(r, next->second) - next->first;
            r = max(r, next->second);
            m.erase(next++);
        }
        cur->second = max(cur->second, r);
        res.push_back(max(0, paint));
    }
    return res;
```

[1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) [**Hard** ]
Key idea is at every point, find the maximum range.
Now sweep the line from 1 to n
if i > curr_max : not possible -1
else if i ==curr_max; current selected tap capacity is over, now we have select the next best tap which we have found in past. set that
else our current tap is good , no need to open any new tap, but keep recording next_best_tap.

```
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        // Find what is the max we can reach if we start opening the tap at every ith location
        vector<int> line (1+n, 0);
        for(int i =0; i <=n; ++i){
            int left = max(0, i - ranges[i]);
            int right = min(n, i + ranges[i]);
            line[left] = max(line[left], right);
        }
        // Sweep line
        // Lets 0th tap as best one
        int curr = line[0];
        int next_best = 0;
        int ans = 1;
        for(int i = 1; (i <=n) and (curr < n); ++i){
            // we cannot reach to this ith that means not possible at all !
            if( i > curr)
                return -1;
            else if ( i == curr){
                // curr reach its end , time to select next best
                next_best = max(next_best, line[i]);
                ++ans;
                curr = next_best; // assign next_best to curr
                next_best =0;//rest next_best as 0
            }
            else{
                // we still are in range of curr, no need to open a new tap but keep checking what next best tap of highest range we can open next.
                next_best = max(next_best, line[i]);
            }
        }
        return ans;;
    }
};
```

[732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/) [**Hard** ]  
Same as Meeting Room II as explained earlier.

[759. Employee Free Time](https://leetcode.com/problems/employee-free-time/) [**Hard**]  
Same conepts, mark start and end time on line, when will everyone is free i.e. when count is 0.
So whenever count is 0 , it mark the begining of an interval, also set a flag , so that after we non-zero from 0, we use that as closing interval.

```
	map<int, int> line;
        for(auto& s : schedule){
            for(auto& i :  s){
                ++line[i.start];
                --line[i.end];
            }
        }

        int count = 0;
        bool found = false;
        vector<Interval> ans;
        for(auto&x : line){
            count += x.second;
            if(found){
                ans.back().end = x.first;
                found = false;
            }
            if(count == 0){
                // mark begining of new interval
                ans.push_back(Interval(x.first, -1));
                found = true;
            }
        }
        ans.pop_back();
        return ans;
```

[1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) [**Hard**]  
We use multiset to track size of interval, multiset.begin() will always gives you smallest size interval which is still active.
Sweep the line,
If it is start of interval, insert the size in multiset,
If it is end of interval remove from multi set.
If there is a query here , just add the first (which is smallest size) to answer index

```
       map<int, set<pair<int, int>>> line;
        // -1 :  Entry  1 : Exit , 2 : Query & size of interval
        for(auto& i : intervals){
            int size = i[1] -i[0] + 1;
            line[i[0]].insert(make_pair(-1, size));
            line[i[1]+1].insert(make_pair(1, size));
        }

        for(int i =0; i < queries.size(); ++i){
            line[queries[i]].insert(make_pair(2, i));
        }
        vector<int> ans(queries.size(), -1);
        multiset<int> sizes;
        for(auto& [x, intervals] :  line){
            for(auto& i : intervals){
                if(i.first==-1)
                    sizes.insert(i.second);
                else if (i.first==1)
                    sizes.erase(sizes.lower_bound(i.second));
                else if (i.first ==2 and !sizes.empty())
                    ans[i.second] = *(sizes.begin());

            }

        }
        return ans;
```

### 2D Problem's

2D problems are slightly tricky as there extra dimension have to be tracked.  
Lets see this with an example.  
[850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

1. For each rectangle, first vertical line indicate rectangle is starting and second line indicates rectangle end.  
   So stores these events on x-axis, we need information line y_start, y_end and whether its a start event or end event.  
   **Sort these events on x-axis, if 2 rectangle start at same time, start event take precendence over end event**.  
   One of the test case has just straight line instead of rectangle.

2. Once we sweep the vertical line, we can get the width between two co-ordinate.

3. To get the height, we need to sum up the y-ordinate along the y-axis, which is a simple 1D problem as we did earlier.
   For example if we have the following intervals on yaxis [0,1] [0,2] [0, 3]  
   Total y length excluding duplicate is 3.
   Use the above 1D trick to solve this.

```
	int rectangleArea(vector<vector<int>>& rectangles) {

        vector<vector<int>> events;

        for(auto& r : rectangles){
            // x-cordinate, event_type(0 is open and 1 is close, y1, y2
            events.push_back({r[0], 0, r[1], r[3]});
            events.push_back({r[2], 1, r[1], r[3]});
        }

        auto cmp =[&](const vector<int>& a , const vector<int>& b){
            if(a[0]==b[0])
                return a[1] < b[1];
            return a[0] < b[0];
        };
        sort(events.begin(), events.end(), cmp);
        int area =0;
        int prev = INT_MIN; // sweep line is coming from far off
        multiset<pair<int, int>> yline; // y co-ordinate and whether entry or exit
        const int MOD = 1e9+7;
        // 1 -D line sweep
        auto get_area = [&](const int x){
            long long area = 0;
            long long prev = INT_MIN;
            int s =0;
            for(auto& y : yline){
                s += y.second;
                if(s==y.second) // mark the begining
                    prev = y.first;

                if(s==0)
                    area += (((y.first - prev)%MOD)* x)%MOD;

            }
            return area;
        };
        for(auto& e : events){
            // First calculate area
            if(prev!=INT_MIN)
                area  = (area + get_area(e[0] - prev))%MOD;

            if(e[1])
            {
                // delete both y co-ordinate
                yline.erase(yline.find(make_pair(e[2], 1)));
                yline.erase(yline.find(make_pair(e[3], -1)));
            }
            else{
                // insert both y co-ordinate of vertical line.
                yline.insert(make_pair(e[2], 1)); // Entry
                yline.insert(make_pair(e[3], -1)); // Exit
            }
            prev = e[0];
        }
        return area;
    }
```

Time Complexity would be O(n^2 log (n)) since for every x event we are trying to calculate the y sum which is 1D line sweep using multiset  
 and takes O(n log n)

[391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)

On Similar lines to above problem, two point to note.

1. Here we have to calculate exact cover which means, two rectangle cant intersect, lets understand this with an image.

![image](https://user-images.githubusercontent.com/20656683/174115549-d6ade836-d27c-407c-8731-9d10481df2ab.png)
![image](https://user-images.githubusercontent.com/20656683/174115717-12eacdd8-726a-405b-bd91-d84b5c4434cc.png)
![image](https://user-images.githubusercontent.com/20656683/174115644-e4b581d0-dacd-479f-b9c8-5a13f060950e.png)

Point to be noted that **new rectangle higher y-cordinate should be lower than equal to existing active rectangles** ( new rectangle is beneath) or **new rectangle lower y-cordinate should be greater than equal to to existing active rectangles** ( new rectangle is above).  
 2. **Sum of Height of the active rectangle** should always be exactly (ymax-ymin) else there would be hole and it wont be exact cover.

![image](https://user-images.githubusercontent.com/20656683/174116557-64e7fd04-40e1-48ad-b92b-79f8a8849332.png)

Here ymax is 3 and ymin is 0 , so everytime y height sum should be exactly 3 only then we would have exact cover.  
But in above example, sum of both y height is 2 and 2!=3 and hence return false.  
Thanks @wddd for his solution https://leetcode.com/problems/perfect-rectangle/discuss/87188/on-log-n-sweep-line-solution

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Why do we use **priority-queue(min-heap)**: Reason is we have to take decision whether to add skyline contour or not at the given x-cordinate.  
  So we try to pull out **all** the events for a given x , insert/delete as per event type and then decide whether to make contour or not.

- Why do we use multiset : Because multiple box of same height exist, if one box is removed that doesnt mean other box can be removed, hence multiset.

Logic: Before inserting height into multiset we note the maximum height available (thats why i used negative number in multiset).  
After processing of all events for a given x co-ordinate, check if the height changed ? if yes we have a contout here, otherwise skip.

```
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> ans;
        multiset<int> height;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> line; // min-heap
        for(auto& b : buildings){
            line.push({b[0], 0, b[2]});
            line.push({b[1], 1, b[2]});
        }
        while(!line.empty()){
            int before = height.empty() ? 0 : -*(begin(height));
            int x;
            do{
                x = line.top()[0];
                int event = line.top()[1];
                int yheight = line.top()[2];
                line.pop();
                if(event)
                    height.erase(height.find(-yheight));
                else
                    height.insert(-yheight);
            }while(!line.empty() and line.top()[0] == x);

            int after = height.empty() ? 0 : -*(begin(height));

            if(after != before)
                ans.push_back({x, after});
        }
        return ans;
    }
};
```

If you noticed in all above 3 problem, template remain same.

1. Store the events in either priority queue or vector in sorted manner of x-axis.  
   priority queue approach has an advantage of not worrying whether to keep entry event first or exit event first becauase your are popping out
   all events for same x-cordinate in one go and then deciding what to be done but if you use vector to store the interval and use custom comparator,
   you have to be careful about whether to add exit event first or entry event first because we pull event one by one.  
   See Skyline problem for priroity queue approach and Rectangle Area II for vector appraoch.
2. Use multiset of process of y-axis. This multiset can store Line Sweep Algorithms

---

Line Sweep (or Sweep Line) is an algorithmic technique where we sweep an imaginary line (x or y axis) and solve various problem.
There would be an event (entry or event) and based on that we update the information and then return result.

This is going to be a long post, so I have divided into 3 parts.

1. 1D Easy/Medium problem.
2. 1D Hard.
3. 2D geometric problems.

There could be errors, please post in comments.  
Also suggest more problem to be added to this list.  
Inviting @votrubac @lee215 to give suggestion for improvment.

### 1D Easy/Medium problem

[1854. Maximum Population Year](https://leetcode.com/problems/maximum-population-year/) [**Easy**]  
Here we are given birth & death year of persons.
Imagine this as a line , when a person born , population of that year +1 and when he expires population decreases by 1.  
![image](https://user-images.githubusercontent.com/20656683/173176474-fb0392a8-82c5-4620-8c1a-1cb54cf4cad6.png)

Plot the population year on a number line.
When a person is born increment by +1 and when he expire decrement by -1 .
Scan from left and accumulate the population, everytime check if current population is greater than global max , if yes update population count and year both.
This scanning from left to right is line sweep.

Time Complexity = O(n log n) (due to tree map) initiialization, iteration of map take O(n) time.

<details>
<summary>

#### Click to see Code

</summary>

    int maximumPopulation(vector<vector<int>>& logs) {
        map<int, int> line;
        for(auto& p : logs){
            ++line[p[0]];
            --line[p[1]];
        }
        int max_p = 0;
        int ans_year;
        int count = 0;
        for(auto& i : line){
            count += i.second;
            if(count > max_p){
                max_p = count;
                ans_year = i.first;
            }
        }
        return ans_year;
    }

</details>

More easy problem to practice:

[2848. Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/)

<details>
<summary>

#### Click to see Code

</summary>

       int numberOfPoints(vector<vector<int>>& nums) {
        int line [102] ={};
        for(auto& p : nums){
            line[p[0]]++;
            line[p[1]+1]--;
        }
        int ans =0;
        int count =0;
        for(int i =0; i <102; ++i){
            count += line[i];
            if(count > 0){
                ++ans;
            }
        }## Line Sweep Algorithms

Line Sweep (or Sweep Line) is an algorithmic technique where we sweep an imaginary line (x or y axis) and solve various problem.
There would be an event (entry or event) and based on that we update the information and then return result.

This is going to be a long post, so I have divided into 3 parts.

1. 1D Easy/Medium problem.
2. 1D Hard.
3. 2D geometric problems.

There could be errors, please post in comments.  
Also suggest more problem to be added to this list.  
Inviting @votrubac @lee215 to give suggestion for improvment.

### 1D Easy/Medium problem

[1854. Maximum Population Year](https://leetcode.com/problems/maximum-population-year/) [**Easy**]  
Here we are given birth & death year of persons.
Imagine this as a line , when a person born , population of that year +1 and when he expires population decreases by 1.  
![image](https://user-images.githubusercontent.com/20656683/173176474-fb0392a8-82c5-4620-8c1a-1cb54cf4cad6.png)

Plot the population year on a number line.
When a person is born increment by +1 and when he expire decrement by -1 .
Scan from left and accumulate the population, everytime check if current population is greater than global max , if yes update population count and year both.
This scanning from left to right is line sweep.

Time Complexity = O(n log n) (due to tree map) initiialization, iteration of map take O(n) time.

<details>
<summary>

#### Click to see Code

</summary>

    int maximumPopulation(vector<vector<int>>& logs) {
        map<int, int> line;
        for(auto& p : logs){
            ++line[p[0]];
            --line[p[1]];
        }
        int max_p = 0;
        int ans_year;
        int count = 0;
        for(auto& i : line){
            count += i.second;
            if(count > max_p){
                max_p = count;
                ans_year = i.first;
            }
        }
        return ans_year;
    }

</details>

More easy problem to practice:

[2848. Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/)

<details>
<summary>

#### Click to see Code

</summary>

       int numberOfPoints(vector<vector<int>>& nums) {
        int line [102] ={};
        for(auto& p : nums){
            line[p[0]]++;
            line[p[1]+1]--;
        }
        int ans =0;
        int count =0;
        for(int i =0; i <102; ++i){
            count += line[i];
            if(count > 0){
                ++ans;
            }
        }
        return ans;
    }

</details>

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) [ **Medium**]  
Same as above just we have to keep track of maximum count of rooms and return it.  
When a meeting start we plot +1 for end we do -1.
Now we scan the line, and store the value in `count` , if count is 1 that mean 1 meeting start, if its 2 that means 2nd meeting started before 1st ended, so we need 2 room atleast. This count we save in `ans` if `count > ans` .

```
class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        map<int, int> line;
        for(auto& i : intervals){
            line[i.start]++;
            line[i.end]--;
        }
        int ans = 0;
        int count;
        for(auto& p : line){
            count += p.second;
            ans = max(ans, count);
        }
        return ans;
    }
};
```

Time Complexity = O(n log n )

[731. My Calendar II](https://leetcode.com/problems/my-calendar-ii/) [ **Medium** ]  
We have to count if there are triple booking , so if at any time we have count >=3 (==3 is enough)  
We return false and also remove this booking from the entry.  
Same approach, use a map and +1 when booking start and -1 when booking end.  
Sweep the line from left to right.

Time Complexity = O(n^2 \* log n ) as for every booking we are sweeping entire line.

```
bool book(int start, int end) {
        ++m[start];
        --m[end];
        int count = 0;
        for(auto& i : m){
            count += i.second;
            if(count ==3){
                // we are not going to add this event
                // nullify line 10,11 changes
                --m[start];
                ++m[end];
                return false;
            }
        }
        return true;
    }
```

[2237. Count Positions on Street With Required Brightness](https://leetcode.com/problems/count-positions-on-street-with-required-brightness/) [ **Medium** ]  
Similar, here we are given a threshold of brightness for each index, first fill up the count by +1 and -1 index where brightness start and end.  
Now scan the vector and see if threshold achieved , if yes ++ans.

Time Complexity = O(n)

<details>
<summary>

#### Click to see Code

</summary>

     bool isCovered(vector<vector<int>>& ranges, int left, int right) {

      int line[52] = {};
    for (auto &r : ranges) {

        line[r[0]] += 1;
        line[(r[1]+1)] -= 1;
    }

    for (int i = 1, overlaps = 0; i <= 51; ++i) {
        overlaps += line[i];
        if (i>=left and i <=right and overlaps <= 0)
            return false;
    }

    return true;
    }

</details>

[1893. Check if All the Integers in a Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) [**Easy** ]  
Mark start and end( end+1 since its a closed interval] as +1/-1 respectively.  
Now scan the line from 1 to 50 , see which co-ordinate falls in given [left right] range and overlap is 0, that mean no range is covering , return false.

Time Complexity = O(n)

[370. Range Addition](https://leetcode.com/problems/range-addition/) [ **Medium**]  
Accumulate +update in start and -update in end+1  
After that sweep the line and accumulate sum in a variable and keep assigning to every index.

Time Complexity = O(n)

**Type 2**:
In this kind of problem, you may not be able to plot the point and arrive at solution. Instead you have to use **prev** technique.  
Lets see this example

[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) [ **Medium**]  
In this kind of problem, we dont use marking on axis, instead axis is already given, we sort it.

### Initial setup after sort

    ![image](https://assets.leetcode.com/users/images/73811d36-8aea-4576-b945-797c86573561_1689758547.3407717.png)

### Hitting first ballon

![image](https://assets.leetcode.com/users/images/94941364-9c75-4d32-9ec7-2b5c1ba8b300_1689759385.382266.png)

Now if we strike first ballon , we can strike at the end-most point i.e. **2**  
We save this as **prev = 2**  
Any ballon starting before we dont need extra arraow since this arrow is enough to burst the ballon.  
The moment start point > prev , we know we need a new ballon again we save the end-most point in the prev and repeat the process.  
Many problem can be solved using this technique.

```
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        auto cmp = [&](const vector<int>& a, const vector<int>& b){

            return a[1] < b[1];
        };
        sort(points.begin(), points.end(), cmp);
        int prev_end = points[0][1];
        int ans = 1;
        for(int i =1; i < points.size(); ++i){
            if(points[i][0] > prev_end){
                ++ans;
                prev_end = points[i][1];
            }
        }
        return ans;
    }
};
```

[435 Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) [ **Medium** ]

**Why Sorting with endTimes Works**
In many of the problem above we do sorting with endTime , this is an important concept to understand,
if you sort with endTime and then check other intervals you can easily find non-overlapping intervals like this, here prev is previous interval.

```
if(intervals[i][0] < intervals[prev][1])
```

Reason is if a new interval start is before previous end time that means a sure overlap.
While on the other hand if we sort by startTime, we dont know when this interval gonna end, there will be overlaps.
Here are some additional points to consider:

**Sorting by end time is a greedy algorithm**. This means that it makes the best possible choice at each step, without considering the future. As a result, it is usually more efficient than sorting by start time.
**Sorting by start time is a dynamic programming algorithm**. This means that it makes a choice at each step, based on the choices that it has made in the past. As a result, it is usually more robust to errors in the input data.
For practice try to solve this problem , which can be solved in both DP as well as Greey Way and see the difference

[646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)

[252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) [ **Easy**]  
Just scan and if ith start < i-1 end return false

**Insert Interval**  
Suppose we haev insert [3,7] to an existing interval [1, 10]  
For each start we do +1 and for end we do -1 on the number line (map).  
Next scan the line, if the count is 0, that mean a new line is going to start, so mark it as start  
And then accumulate the count, now if count is 0, that mean the interval has ended so insert this interval.

![image](https://assets.leetcode.com/users/images/f57fbab6-c436-4aeb-9231-fca64dc5a0c8_1694355372.721946.png)

[57. Insert Interval](https://leetcode.com/problems/insert-interval/) [ **Medium** ]

### Using Map counter

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        map<int, int> m;
        for(auto& p : intervals){
            ++m[p[0]];
            --m[p[1]];
        }
        ++m[newInterval[0]];
        --m[newInterval[1]];
        int count = 0;
        vector<vector<int>> ans;
        int start;
        for(auto& i : m){
            if(count==0){
                start = i.first;
            }
            count += i.second;
            if(count == 0){
                ans.push_back({start, i.first});
            }
        }
        return ans;
    }
};
```

### Using Interval

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {

        vector<vector<int>> ans;
        for(auto& i : intervals){
            if(i[1] < newInterval[0]){
                ans.push_back(i);
            }
            else if( newInterval[1] < i[0]){
                ans.push_back(newInterval);
                newInterval = i;
            }
            else if((i[1] >= newInterval[0])  or ( newInterval[1] <=i[0])){
                /*
                ------ [i]
                   ------- [new]

                ------
             ------
             */
             newInterval[0] = min(newInterval[0], i[0]);
             newInterval[1] = max(newInterval[1], i[1]);
            }
        }
        ans.push_back(newInterval);
        return ans;
    }
};
```

[1272. Remove Interval](https://leetcode.com/problems/remove-interval/) [ **Medium** ]

**Approach #1**:
increment at start and decrement end , while for remove interavl do reverse since we have to remove
standard logic of count==i.start and count > 0
and for closing interval count=0 and we have added previously(use a bool flag)

**Approach #2**:
Input is sorted, so we sweep and if removed_start > ith_end or remove_end < ith_start , we simply add the ith boundary to o/p.  
Otherwise if ith_start < remove_start -> add ith_start, remove_start  
Also if ith_end > remove_end then add [remove_end, ith_end]

Both approach coded for comparison, Merge Interval and Insert Interval can also be solved using similar approach.  
Please let me know in comment section which approach is preferable as I am still learning.  
Its a bit tough to come up Approach 1 for all problem but Approach 2 works for all.

### Using Map counter

```c++
        map<int, int> line;

	for(auto& i : intervals)
	{
		++line[i[0]];
		--line[i[1]];
	}
	--line[toBeRemoved[0]];
	++line[toBeRemoved[1]];
	vector<vector<int>> ans;
	int count =0; bool added =false;
	for(auto& i : line)
	{
		count += i.second;
		if(count ==1 ){
			ans.push_back({i.first, -1});
			added = true;
		}
		if(count==0 and added){
			ans.back()[1] = i.first;
			added = false;
		}
	}
	return ans;
```

### Using prev interval

```c++
	vector<vector<int>> ans;

	for(auto &i :  intervals)
	{
		int left = i[0];
		int right = i[1];
		if( (toBeRemoved[0] > right ) or (toBeRemoved[1] < left ))
		{
			ans.push_back({left, right});
		}
		else
		{
			if(left < toBeRemoved[0])
			{
				ans.push_back({left, toBeRemoved[0]});
			}
			if (right > toBeRemoved[1])
			{
				ans.push_back({toBeRemoved[1], right});
			}
		}
	}
```

**Approach 1 details**
For insert interval : when we start , `if count is 0` that essentially means a new begining , so record the start poisition.
Now after we are done adding line value to count and still count is 0 , that essentially mean interval ended, so use the previously recorded start and now this endging value to form a interval. Let see the example input this with a image, **before we start processing if count is 0 and we record as start of new interval** and **after processing** if it is still 0, that mean end of intervals.

![image](https://assets.leetcode.com/users/images/47947991-bf67-41a5-87e1-393045a17cfa_1700714223.3685725.png)
Before processing 1 , which is start of interval, count is 0 so we mark start =1, after we process count is 1
Process 2 , as it is start , count =2
Process 3 , as it is end , count =1
Process 5, as it is end count = 0 , now since count is 0 after process we insert [1, 5] in answer.
Process 6, since count is 0 **before process**, this is start of new interval, record start =6 and now process start - 6
Procss 9 , count will be 0 **after process** , so that mean its end , record [6, 9] in answer.

For **Remove Interval** sweep approach is similar except now we have to remove the interval , that we mark start as -ve and end as +ve marking on line ans tweak the sount logic.  
Now try to solve this problem using same count technique.

[1229. Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) [**Medium**]

Some pointers, we have 2 candidate, so if both have started only then only take there latest time, for example
suppose Person is available from [10:00 , 12:00] but person 2 is available from [11:00 , 12:00]
after we sweep the line past [11:00] count would be 2 and then we can take [11:00] as candidate start time as this time is common to both person.

Next whenever we encounter an end of time AND we have already noted down the common_time , check if we met the duration ? if yes return , because this earlies, otherwise reset the common_time, as now we have to find some common start all over again.

<details>
<summary>

#### Click to see Code

</summary>

    Interval earliestAppropriateDuration(vector<Interval> &slots1, vector<Interval> &slots2, int duration) {
        // --- write your code here ---
        map<int, int> m;
        for(auto& i : slots1){
            m[i.start]++;
            m[i.end]--;
        }
        for(auto& i : slots2){
            m[i.start]++;
            m[i.end]--;
        }
        int count = 0;
        Interval candidate(-1, -1);

        for(auto& p : m){
            int old = count;
            count += p.second;
            if(count ==2){
                candidate.start = p.first;
            }
            // If count is decreasing that mean some slot is ending
            if(count < old and candidate.start!=-1){
                if(p.first - candidate.start >= duration) // we found
                {
                    candidate.end = candidate.start+duration;
                    return candidate;
                }
                else{
                    candidate.start = -1;
                }
            }
        }
        return {-1, -1};
    }

</details>

[1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) [ **Medium** ]  
Step 1: Sort with start, if both start are same , give precedence to higher ending interval first.  
Step 2: Insert the first interval uncondtionally , after that scan the other interavl , following 3 possibility (see code comment can occur)

```
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {

        vector<vector<int>> ans;
        auto comp = [&](const vector<int>& i, const vector<int>& j){
            if(i[0]==j[0])
                return i[1] > j[1];
            return i[0] < j[0];
        };
        sort(intervals.begin(), intervals.end(), comp);
        ans.push_back(intervals[0]);
        int k =0;
        for(int i =1; i< intervals.size(); ++i){
            if( (intervals[i][0]>= ans.back()[0]) and (intervals[i][1] <= ans.back()[1]))
            {
			   // Scenario 1: Completely covered suppose existing interval in vector is [1, 8] and this ith interval is [2, 6] , this is completely inside i.e. start and end
			   // lies inside , hence this interval is surely removed, count this.
                ++k;
            }
            else if(intervals[i][0] > ans.back()[1]){
			// Scenario 2: Suppose vector has [1, 8]  and ith interval is  [9, 10] , totallly unrelated, so push this interval in vector as this is going to be used next time.
                ans.push_back(intervals[i]);
            }
            else if ((intervals[i][0] > ans.back()[0]) and (intervals[i][0] <= ans.back()[1]) )
			    // Scenario 3: vector has [1, 8] and ith interval is  [5, 10], so take maximum of both end point.
                ans.back()[1] = max(ans.back()[1], intervals[i][1]);
        }
        return intervals.size()- k;
    }
};
```

[1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) [ **Medium**]

Add detailed comments in code , please check , here the key idea is we are sweeping the day as a number line, it is given in input and we mark the events on that day line.

```
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        multiset<int> eventEndTime;
        int i =0;
        int ans = 0;
        int n = events.size();
        for(int d =1; d <=100000; ++d){
            //Delete expired event , example
            // Suppose 3 events are there  [1, 2] [1, 2] [1, 2]
            // at day 1 : attend 1st event and at day 2 attend 2md event , at day 3 , 3rd event is already expired, hence we need this kind of loop of loop to delete expired events
            while(!eventEndTime.empty() and *eventEndTime.begin() < d){
                eventEndTime.erase(eventEndTime.begin());
            }

            // put all candidate events whose start day is past the current day.

            //insert events if they can be start
            while(i < n and events[i][0] <=d){
                eventEndTime.insert(events[i][1]);
                i++;
            }

            // we can attend 1 event on 1 day , thats why if condition not while
            // adn we attend earliest ending event first , suppose we have [1, 2] & [1, 3]
            // and we are on day=2, we should attend [1,2] first otherwise at d=3 this would be expired
            if(!eventEndTime.empty() and *eventEndTime.begin()>=d){
                ++ans;
                eventEndTime.erase(eventEndTime.begin());
            }
        }
        return ans;
    }
};
```

[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) [ **Medium**]

### Using Map counter

```c++
    	class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        map<int, int> line;
        for(auto& i : intervals){
            ++line[i[0]];
            --line[i[1]];
        }

        int count = 0;
        vector<vector<int>> ans;
        int start = 0;
        for(auto& i : line){
            // that means its a new start, store the start
           if(count ==0){
               start = i.first;
           }
           count += i.second;
           // this mean interval ends, and we can push this as answer
           if(count==0){
               ans.push_back({start, i.first});
           }
        }
        return ans;
    }
};
```

### Using prev interval

```c++
	sort(intervals.begin(), intervals.end());// Sort y there start time
        vector<vector<int>> results;
        results.push_back(intervals[0]);
        for(int i =1; i < intervals.size(); ++i){
            if(intervals[i][0] > results.back()[1]) // a new begining
            {
                results.push_back(intervals[i]);
            }
            else
                results.back()[1] = max(results.back()[1], intervals[i][1]);
        }
        return results;
```

[1589. Maximum Sum Obtained of Any Permutation](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) [ **Medium**]  
[1943. Describe the Painting](https://leetcode.com/problems/describe-the-painting/) [ **Medium** ]  
[1674. Minimum Moves to Make Array Complementary](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) [ **Medium**]

### 1D Hard problem

These 1D Hard problem require scanning line for each input which can lead to O(n^2) algorithm.  
We have to do something special to optimize it.  
Lets see with an example.

[2158. Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/) [**Hard** ]  
In this problem each day we paint some section of a line.  
Brute force way is scan line for each input index.

Thanks to @cjcoax and @votrubac, I am putting both line sweep version and map interval method here.  
Similar problem
[2251. Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) [ **Hard**]

### Using Line Sweep

```c++
    	auto cmp =[&](const vector<int>& a, const vector<int>& b){
            return a[1]  < b[1];
        };
        int maxEnd = (*max_element(paint.begin(), paint.end(), cmp))[1];
        int n = paint.size();
        vector<int> ans(n, 0);
        vector<vector<pair<int, int>>> line(1 + maxEnd);
        // We are marking on line that co-oridnate is
	// painted/not-painted(true-false) between which date
        for(int i =0; i < n ; ++i){
            line[paint[i][0]].push_back(make_pair(i, 1));
            line[paint[i][1]].push_back(make_pair(i, 0));
        }

        set<int> days;
        //Scan the line
        for(int i =0; i < maxEnd; ++i){

            // Who all present on this x co-ordinate?
            for(auto& [day, state] : line[i]){

                if(state)
                    days.insert(day);
                else
                    days.erase(day);
            }
            //Only the first guy can paint this line
            if(!days.empty())
                ans[*(days.begin())]++;
        }
        return ans;
```

### Using Vector Interval

```c++
	map<int, int> m;
    vector<int> res;
    for (auto &p : pt) {
        int l = p[0], r = p[1];
        auto next = m.upper_bound(l), cur = next;

        // Step 1: suppose we have painted [1, 4] [ 5, 8] [10, 20]
        // Now a new interval [4, 21] comes upper_bound gives [5,8]
        // l = 4 then
        if (cur != begin(m) && prev(cur)->second >= l) {
            cur = prev(cur);
            l = cur->second;
        }
        else
            cur = m.insert({l, r}).first;
        int paint = r - l;
        // Next since r= 21 and that is  > 5, that means this paint is going to span
        // find how much shd we subtract :
        // get min of (21, 8) =  8 and then subtratc with start 5 = 3
        // now r shd be max of (21, 8) =21 , check further more intervals can be erased ?
        // in the end set curr->second = max(curr->second, r);
        while (next != end(m) && next->first < r) {
            paint -= min(r, next->second) - next->first;
            r = max(r, next->second);
            m.erase(next++);
        }
        cur->second = max(cur->second, r);
        res.push_back(max(0, paint));
    }
    return res;
```

[1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) [**Hard** ]
Key idea is at every point, find the maximum range.
Now sweep the line from 1 to n
if i > curr_max : not possible -1
else if i ==curr_max; current selected tap capacity is over, now we have select the next best tap which we have found in past. set that
else our current tap is good , no need to open any new tap, but keep recording next_best_tap.

```
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        // Find what is the max we can reach if we start opening the tap at every ith location
        vector<int> line (1+n, 0);
        for(int i =0; i <=n; ++i){
            int left = max(0, i - ranges[i]);
            int right = min(n, i + ranges[i]);
            line[left] = max(line[left], right);
        }
        // Sweep line
        // Lets 0th tap as best one
        int curr = line[0];
        int next_best = 0;
        int ans = 1;
        for(int i = 1; (i <=n) and (curr < n); ++i){
            // we cannot reach to this ith that means not possible at all !
            if( i > curr)
                return -1;
            else if ( i == curr){
                // curr reach its end , time to select next best
                next_best = max(next_best, line[i]);
                ++ans;
                curr = next_best; // assign next_best to curr
                next_best =0;//rest next_best as 0
            }
            else{
                // we still are in range of curr, no need to open a new tap but keep checking what next best tap of highest range we can open next.
                next_best = max(next_best, line[i]);
            }
        }
        return ans;;
    }
};
```

[732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/) [**Hard** ]  
Same as Meeting Room II as explained earlier.

[759. Employee Free Time](https://leetcode.com/problems/employee-free-time/) [**Hard**]  
Same conepts, mark start and end time on line, when will everyone is free i.e. when count is 0.
So whenever count is 0 , it mark the begining of an interval, also set a flag , so that after we non-zero from 0, we use that as closing interval.

```
	map<int, int> line;
        for(auto& s : schedule){
            for(auto& i :  s){
                ++line[i.start];
                --line[i.end];
            }
        }

        int count = 0;
        bool found = false;
        vector<Interval> ans;
        for(auto&x : line){
            count += x.second;
            if(found){
                ans.back().end = x.first;
                found = false;
            }
            if(count == 0){
                // mark begining of new interval
                ans.push_back(Interval(x.first, -1));
                found = true;
            }
        }
        ans.pop_back();
        return ans;
```

[1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) [**Hard**]  
We use multiset to track size of interval, multiset.begin() will always gives you smallest size interval which is still active.
Sweep the line,
If it is start of interval, insert the size in multiset,
If it is end of interval remove from multi set.
If there is a query here , just add the first (which is smallest size) to answer index

```
       map<int, set<pair<int, int>>> line;
        // -1 :  Entry  1 : Exit , 2 : Query & size of interval
        for(auto& i : intervals){
            int size = i[1] -i[0] + 1;
            line[i[0]].insert(make_pair(-1, size));
            line[i[1]+1].insert(make_pair(1, size));
        }

        for(int i =0; i < queries.size(); ++i){
            line[queries[i]].insert(make_pair(2, i));
        }
        vector<int> ans(queries.size(), -1);
        multiset<int> sizes;
        for(auto& [x, intervals] :  line){
            for(auto& i : intervals){
                if(i.first==-1)
                    sizes.insert(i.second);
                else if (i.first==1)
                    sizes.erase(sizes.lower_bound(i.second));
                else if (i.first ==2 and !sizes.empty())
                    ans[i.second] = *(sizes.begin());

            }

        }
        return ans;
```

### 2D Problem's

2D problems are slightly tricky as there extra dimension have to be tracked.  
Lets see this with an example.  
[850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

1. For each rectangle, first vertical line indicate rectangle is starting and second line indicates rectangle end.  
   So stores these events on x-axis, we need information line y_start, y_end and whether its a start event or end event.  
   **Sort these events on x-axis, if 2 rectangle start at same time, start event take precendence over end event**.  
   One of the test case has just straight line instead of rectangle.

2. Once we sweep the vertical line, we can get the width between two co-ordinate.

3. To get the height, we need to sum up the y-ordinate along the y-axis, which is a simple 1D problem as we did earlier.
   For example if we have the following intervals on yaxis [0,1] [0,2] [0, 3]  
   Total y length excluding duplicate is 3.
   Use the above 1D trick to solve this.

```
	int rectangleArea(vector<vector<int>>& rectangles) {

        vector<vector<int>> events;

        for(auto& r : rectangles){
            // x-cordinate, event_type(0 is open and 1 is close, y1, y2
            events.push_back({r[0], 0, r[1], r[3]});
            events.push_back({r[2], 1, r[1], r[3]});
        }

        auto cmp =[&](const vector<int>& a , const vector<int>& b){
            if(a[0]==b[0])
                return a[1] < b[1];
            return a[0] < b[0];
        };
        sort(events.begin(), events.end(), cmp);
        int area =0;
        int prev = INT_MIN; // sweep line is coming from far off
        multiset<pair<int, int>> yline; // y co-ordinate and whether entry or exit
        const int MOD = 1e9+7;
        // 1 -D line sweep
        auto get_area = [&](const int x){
            long long area = 0;
            long long prev = INT_MIN;
            int s =0;
            for(auto& y : yline){
                s += y.second;
                if(s==y.second) // mark the begining
                    prev = y.first;

                if(s==0)
                    area += (((y.first - prev)%MOD)* x)%MOD;

            }
            return area;
        };
        for(auto& e : events){
            // First calculate area
            if(prev!=INT_MIN)
                area  = (area + get_area(e[0] - prev))%MOD;

            if(e[1])
            {
                // delete both y co-ordinate
                yline.erase(yline.find(make_pair(e[2], 1)));
                yline.erase(yline.find(make_pair(e[3], -1)));
            }
            else{
                // insert both y co-ordinate of vertical line.
                yline.insert(make_pair(e[2], 1)); // Entry
                yline.insert(make_pair(e[3], -1)); // Exit
            }
            prev = e[0];
        }
        return area;
    }
```

Time Complexity would be O(n^2 log (n)) since for every x event we are trying to calculate the y sum which is 1D line sweep using multiset  
 and takes O(n log n)

[391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)

On Similar lines to above problem, two point to note.

1. Here we have to calculate exact cover which means, two rectangle cant intersect, lets understand this with an image.

![image](https://user-images.githubusercontent.com/20656683/174115549-d6ade836-d27c-407c-8731-9d10481df2ab.png)
![image](https://user-images.githubusercontent.com/20656683/174115717-12eacdd8-726a-405b-bd91-d84b5c4434cc.png)
![image](https://user-images.githubusercontent.com/20656683/174115644-e4b581d0-dacd-479f-b9c8-5a13f060950e.png)

Point to be noted that **new rectangle higher y-cordinate should be lower than equal to existing active rectangles** ( new rectangle is beneath) or **new rectangle lower y-cordinate should be greater than equal to to existing active rectangles** ( new rectangle is above).  
 2. **Sum of Height of the active rectangle** should always be exactly (ymax-ymin) else there would be hole and it wont be exact cover.

![image](https://user-images.githubusercontent.com/20656683/174116557-64e7fd04-40e1-48ad-b92b-79f8a8849332.png)

Here ymax is 3 and ymin is 0 , so everytime y height sum should be exactly 3 only then we would have exact cover.  
But in above example, sum of both y height is 2 and 2!=3 and hence return false.  
Thanks @wddd for his solution https://leetcode.com/problems/perfect-rectangle/discuss/87188/on-log-n-sweep-line-solution

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Why do we use **priority-queue(min-heap)**: Reason is we have to take decision whether to add skyline contour or not at the given x-cordinate.  
  So we try to pull out **all** the events for a given x , insert/delete as per event type and then decide whether to make contour or not.

- Why do we use multiset : Because multiple box of same height exist, if one box is removed that doesnt mean other box can be removed, hence multiset.

Logic: Before inserting height into multiset we note the maximum height available (thats why i used negative number in multiset).  
After processing of all events for a given x co-ordinate, check if the height changed ? if yes we have a contout here, otherwise skip.

```
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> ans;
        multiset<int> height;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> line; // min-heap
        for(auto& b : buildings){
            line.push({b[0], 0, b[2]});
            line.push({b[1], 1, b[2]});
        }
        while(!line.empty()){
            int before = height.empty() ? 0 : -*(begin(height));
            int x;
            do{
                x = line.top()[0];
                int event = line.top()[1];
                int yheight = line.top()[2];
                line.pop();
                if(event)
                    height.erase(height.find(-yheight));
                else
                    height.insert(-yheight);
            }while(!line.empty() and line.top()[0] == x);

            int after = height.empty() ? 0 : -*(begin(height));

            if(after != before)
                ans.push_back({x, after});
        }
        return ans;
    }
};
```

If you noticed in all above 3 problem, template remain same.

1. Store the events in either priority queue or vector in sorted manner of x-axis.  
   priority queue approach has an advantage of not worrying whether to keep entry event first or exit event first becauase your are popping out
   all events for same x-cordinate in one go and then deciding what to be done but if you use vector to store the interval and use custom comparator,
   you have to be careful about whether to add exit event first or entry event first because we pull event one by one.  
   See Skyline problem for priroity queue approach and Rectangle Area II for vector appraoch.
2. Use multiset of process of y-axis. This multiset can store Line Sweep Algorithms

---

Line Sweep (or Sweep Line) is an algorithmic technique where we sweep an imaginary line (x or y axis) and solve various problem.
There would be an event (entry or event) and based on that we update the information and then return result.

This is going to be a long post, so I have divided into 3 parts.

1. 1D Easy/Medium problem.
2. 1D Hard.
3. 2D geometric problems.

There could be errors, please post in comments.  
Also suggest more problem to be added to this list.  
Inviting @votrubac @lee215 to give suggestion for improvment.

### 1D Easy/Medium problem

[1854. Maximum Population Year](https://leetcode.com/problems/maximum-population-year/) [**Easy**]  
Here we are given birth & death year of persons.
Imagine this as a line , when a person born , population of that year +1 and when he expires population decreases by 1.  
![image](https://user-images.githubusercontent.com/20656683/173176474-fb0392a8-82c5-4620-8c1a-1cb54cf4cad6.png)

Plot the population year on a number line.
When a person is born increment by +1 and when he expire decrement by -1 .
Scan from left and accumulate the population, everytime check if current population is greater than global max , if yes update population count and year both.
This scanning from left to right is line sweep.

Time Complexity = O(n log n) (due to tree map) initiialization, iteration of map take O(n) time.

<details>
<summary>

#### Click to see Code

</summary>

    int maximumPopulation(vector<vector<int>>& logs) {
        map<int, int> line;
        for(auto& p : logs){
            ++line[p[0]];
            --line[p[1]];
        }
        int max_p = 0;
        int ans_year;
        int count = 0;
        for(auto& i : line){
            count += i.second;
            if(count > max_p){
                max_p = count;
                ans_year = i.first;
            }
        }
        return ans_year;
    }

</details>

More easy problem to practice:

[2848. Points That Intersect With Cars](https://leetcode.com/problems/points-that-intersect-with-cars/)

<details>
<summary>

#### Click to see Code

</summary>

       int numberOfPoints(vector<vector<int>>& nums) {
        int line [102] ={};
        for(auto& p : nums){
            line[p[0]]++;
            line[p[1]+1]--;
        }
        int ans =0;
        int count =0;
        for(int i =0; i <102; ++i){
            count += line[i];
            if(count > 0){
                ++ans;
            }
        }
        return ans;
    }

</details>

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) [ **Medium**]  
Same as above just we have to keep track of maximum count of rooms and return it.  
When a meeting start we plot +1 for end we do -1.
Now we scan the line, and store the value in `count` , if count is 1 that mean 1 meeting start, if its 2 that means 2nd meeting started before 1st ended, so we need 2 room atleast. This count we save in `ans` if `count > ans` .

```
class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        map<int, int> line;
        for(auto& i : intervals){
            line[i.start]++;
            line[i.end]--;
        }
        int ans = 0;
        int count;
        for(auto& p : line){
            count += p.second;
            ans = max(ans, count);
        }
        return ans;
    }
};
```

Time Complexity = O(n log n )

[731. My Calendar II](https://leetcode.com/problems/my-calendar-ii/) [ **Medium** ]  
We have to count if there are triple booking , so if at any time we have count >=3 (==3 is enough)  
We return false and also remove this booking from the entry.  
Same approach, use a map and +1 when booking start and -1 when booking end.  
Sweep the line from left to right.

Time Complexity = O(n^2 \* log n ) as for every booking we are sweeping entire line.

```
bool book(int start, int end) {
        ++m[start];
        --m[end];
        int count = 0;
        for(auto& i : m){
            count += i.second;
            if(count ==3){
                // we are not going to add this event
                // nullify line 10,11 changes
                --m[start];
                ++m[end];
                return false;
            }
        }
        return true;
    }
```

[2237. Count Positions on Street With Required Brightness](https://leetcode.com/problems/count-positions-on-street-with-required-brightness/) [ **Medium** ]  
Similar, here we are given a threshold of brightness for each index, first fill up the count by +1 and -1 index where brightness start and end.  
Now scan the vector and see if threshold achieved , if yes ++ans.

Time Complexity = O(n)

<details>
<summary>

#### Click to see Code

</summary>

     bool isCovered(vector<vector<int>>& ranges, int left, int right) {

      int line[52] = {};
    for (auto &r : ranges) {

        line[r[0]] += 1;
        line[(r[1]+1)] -= 1;
    }

    for (int i = 1, overlaps = 0; i <= 51; ++i) {
        overlaps += line[i];
        if (i>=left and i <=right and overlaps <= 0)
            return false;
    }

    return true;
    }

</details>

[1893. Check if All the Integers in a Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) [**Easy** ]  
Mark start and end( end+1 since its a closed interval] as +1/-1 respectively.  
Now scan the line from 1 to 50 , see which co-ordinate falls in given [left right] range and overlap is 0, that mean no range is covering , return false.

Time Complexity = O(n)

[370. Range Addition](https://leetcode.com/problems/range-addition/) [ **Medium**]  
Accumulate +update in start and -update in end+1  
After that sweep the line and accumulate sum in a variable and keep assigning to every index.

Time Complexity = O(n)

**Type 2**:
In this kind of problem, you may not be able to plot the point and arrive at solution. Instead you have to use **prev** technique.  
Lets see this example

[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) [ **Medium**]  
In this kind of problem, we dont use marking on axis, instead axis is already given, we sort it.

> Initial setup after sort

    ![image](https://assets.leetcode.com/users/images/73811d36-8aea-4576-b945-797c86573561_1689758547.3407717.png)

> Hitting first ballon

    ![image](https://assets.leetcode.com/users/images/94941364-9c75-4d32-9ec7-2b5c1ba8b300_1689759385.382266.png)

Now if we strike first ballon , we can strike at the end-most point i.e. **2**  
We save this as **prev = 2**  
Any ballon starting before we dont need extra arraow since this arrow is enough to burst the ballon.  
The moment start point > prev , we know we need a new ballon again we save the end-most point in the prev and repeat the process.  
Many problem can be solved using this technique.

```
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        auto cmp = [&](const vector<int>& a, const vector<int>& b){

            return a[1] < b[1];
        };
        sort(points.begin(), points.end(), cmp);
        int prev_end = points[0][1];
        int ans = 1;
        for(int i =1; i < points.size(); ++i){
            if(points[i][0] > prev_end){
                ++ans;
                prev_end = points[i][1];
            }
        }
        return ans;
    }
};
```

[435 Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) [ **Medium** ]

**Why Sorting with endTimes Works**
In many of the problem above we do sorting with endTime , this is an important concept to understand,
if you sort with endTime and then check other intervals you can easily find non-overlapping intervals like this, here prev is previous interval.

```
if(intervals[i][0] < intervals[prev][1])
```

Reason is if a new interval start is before previous end time that means a sure overlap.
While on the other hand if we sort by startTime, we dont know when this interval gonna end, there will be overlaps.
Here are some additional points to consider:

**Sorting by end time is a greedy algorithm**. This means that it makes the best possible choice at each step, without considering the future. As a result, it is usually more efficient than sorting by start time.
**Sorting by start time is a dynamic programming algorithm**. This means that it makes a choice at each step, based on the choices that it has made in the past. As a result, it is usually more robust to errors in the input data.
For practice try to solve this problem , which can be solved in both DP as well as Greey Way and see the difference

[646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)

[252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) [ **Easy**]  
Just scan and if ith start < i-1 end return false

**Insert Interval**  
Suppose we haev insert [3,7] to an existing interval [1, 10]  
For each start we do +1 and for end we do -1 on the number line (map).  
Next scan the line, if the count is 0, that mean a new line is going to start, so mark it as start  
And then accumulate the count, now if count is 0, that mean the interval has ended so insert this interval.

![image](https://assets.leetcode.com/users/images/f57fbab6-c436-4aeb-9231-fca64dc5a0c8_1694355372.721946.png)

[57. Insert Interval](https://leetcode.com/problems/insert-interval/) [ **Medium** ]

### Using Map counter

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        map<int, int> m;
        for(auto& p : intervals){
            ++m[p[0]];
            --m[p[1]];
        }
        ++m[newInterval[0]];
        --m[newInterval[1]];
        int count = 0;
        vector<vector<int>> ans;
        int start;
        for(auto& i : m){
            if(count==0){
                start = i.first;
            }
            count += i.second;
            if(count == 0){
                ans.push_back({start, i.first});
            }
        }
        return ans;
    }
};
```

### Using Interval

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {

        vector<vector<int>> ans;
        for(auto& i : intervals){
            if(i[1] < newInterval[0]){
                ans.push_back(i);
            }
            else if( newInterval[1] < i[0]){
                ans.push_back(newInterval);
                newInterval = i;
            }
            else if((i[1] >= newInterval[0])  or ( newInterval[1] <=i[0])){
                /*
                ------ [i]
                   ------- [new]

                ------
             ------
             */
             newInterval[0] = min(newInterval[0], i[0]);
             newInterval[1] = max(newInterval[1], i[1]);
            }
        }
        ans.push_back(newInterval);
        return ans;
    }
};
```

[1272. Remove Interval](https://leetcode.com/problems/remove-interval/) [ **Medium** ]

**Approach #1**:
increment at start and decrement end , while for remove interavl do reverse since we have to remove
standard logic of count==i.start and count > 0
and for closing interval count=0 and we have added previously(use a bool flag)

**Approach #2**:
Input is sorted, so we sweep and if removed_start > ith_end or remove_end < ith_start , we simply add the ith boundary to o/p.  
Otherwise if ith_start < remove_start -> add ith_start, remove_start  
Also if ith_end > remove_end then add [remove_end, ith_end]

Both approach coded for comparison, Merge Interval and Insert Interval can also be solved using similar approach.  
Please let me know in comment section which approach is preferable as I am still learning.  
Its a bit tough to come up Approach 1 for all problem but Approach 2 works for all.

### Using Map counter

```c++
        map<int, int> line;

	for(auto& i : intervals)
	{
		++line[i[0]];
		--line[i[1]];
	}
	--line[toBeRemoved[0]];
	++line[toBeRemoved[1]];
	vector<vector<int>> ans;
	int count =0; bool added =false;
	for(auto& i : line)
	{
		count += i.second;
		if(count ==1 ){
			ans.push_back({i.first, -1});
			added = true;
		}
		if(count==0 and added){
			ans.back()[1] = i.first;
			added = false;
		}
	}
	return ans;
```

### Using prev interval

```c++
	vector<vector<int>> ans;

	for(auto &i :  intervals)
	{
		int left = i[0];
		int right = i[1];
		if( (toBeRemoved[0] > right ) or (toBeRemoved[1] < left ))
		{
			ans.push_back({left, right});
		}
		else
		{
			if(left < toBeRemoved[0])
			{
				ans.push_back({left, toBeRemoved[0]});
			}
			if (right > toBeRemoved[1])
			{
				ans.push_back({toBeRemoved[1], right});
			}
		}
	}
```

**Approach 1 details**
For insert interval : when we start , `if count is 0` that essentially means a new begining , so record the start poisition.
Now after we are done adding line value to count and still count is 0 , that essentially mean interval ended, so use the previously recorded start and now this endging value to form a interval. Let see the example input this with a image, **before we start processing if count is 0 and we record as start of new interval** and **after processing** if it is still 0, that mean end of intervals.

![image](https://assets.leetcode.com/users/images/47947991-bf67-41a5-87e1-393045a17cfa_1700714223.3685725.png)
Before processing 1 , which is start of interval, count is 0 so we mark start =1, after we process count is 1
Process 2 , as it is start , count =2
Process 3 , as it is end , count =1
Process 5, as it is end count = 0 , now since count is 0 after process we insert [1, 5] in answer.
Process 6, since count is 0 **before process**, this is start of new interval, record start =6 and now process start - 6
Procss 9 , count will be 0 **after process** , so that mean its end , record [6, 9] in answer.

For **Remove Interval** sweep approach is similar except now we have to remove the interval , that we mark start as -ve and end as +ve marking on line ans tweak the sount logic.  
Now try to solve this problem using same count technique.

[1229. Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) [**Medium**]

Some pointers, we have 2 candidate, so if both have started only then only take there latest time, for example
suppose Person is available from [10:00 , 12:00] but person 2 is available from [11:00 , 12:00]
after we sweep the line past [11:00] count would be 2 and then we can take [11:00] as candidate start time as this time is common to both person.

Next whenever we encounter an end of time AND we have already noted down the common_time , check if we met the duration ? if yes return , because this earlies, otherwise reset the common_time, as now we have to find some common start all over again.

<details>
<summary>

#### Click to see Code

</summary>

    Interval earliestAppropriateDuration(vector<Interval> &slots1, vector<Interval> &slots2, int duration) {
        // --- write your code here ---
        map<int, int> m;
        for(auto& i : slots1){
            m[i.start]++;
            m[i.end]--;
        }
        for(auto& i : slots2){
            m[i.start]++;
            m[i.end]--;
        }
        int count = 0;
        Interval candidate(-1, -1);

        for(auto& p : m){
            int old = count;
            count += p.second;
            if(count ==2){
                candidate.start = p.first;
            }
            // If count is decreasing that mean some slot is ending
            if(count < old and candidate.start!=-1){
                if(p.first - candidate.start >= duration) // we found
                {
                    candidate.end = candidate.start+duration;
                    return candidate;
                }
                else{
                    candidate.start = -1;
                }
            }
        }
        return {-1, -1};
    }

</details>

[1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) [ **Medium** ]  
Step 1: Sort with start, if both start are same , give precedence to higher ending interval first.  
Step 2: Insert the first interval uncondtionally , after that scan the other interavl , following 3 possibility (see code comment can occur)

```
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {

        vector<vector<int>> ans;
        auto comp = [&](const vector<int>& i, const vector<int>& j){
            if(i[0]==j[0])
                return i[1] > j[1];
            return i[0] < j[0];
        };
        sort(intervals.begin(), intervals.end(), comp);
        ans.push_back(intervals[0]);
        int k =0;
        for(int i =1; i< intervals.size(); ++i){
            if( (intervals[i][0]>= ans.back()[0]) and (intervals[i][1] <= ans.back()[1]))
            {
			   // Scenario 1: Completely covered suppose existing interval in vector is [1, 8] and this ith interval is [2, 6] , this is completely inside i.e. start and end
			   // lies inside , hence this interval is surely removed, count this.
                ++k;
            }
            else if(intervals[i][0] > ans.back()[1]){
			// Scenario 2: Suppose vector has [1, 8]  and ith interval is  [9, 10] , totallly unrelated, so push this interval in vector as this is going to be used next time.
                ans.push_back(intervals[i]);
            }
            else if ((intervals[i][0] > ans.back()[0]) and (intervals[i][0] <= ans.back()[1]) )
			    // Scenario 3: vector has [1, 8] and ith interval is  [5, 10], so take maximum of both end point.
                ans.back()[1] = max(ans.back()[1], intervals[i][1]);
        }
        return intervals.size()- k;
    }
};
```

[1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) [ **Medium**]

Add detailed comments in code , please check , here the key idea is we are sweeping the day as a number line, it is given in input and we mark the events on that day line.

```
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        multiset<int> eventEndTime;
        int i =0;
        int ans = 0;
        int n = events.size();
        for(int d =1; d <=100000; ++d){
            //Delete expired event , example
            // Suppose 3 events are there  [1, 2] [1, 2] [1, 2]
            // at day 1 : attend 1st event and at day 2 attend 2md event , at day 3 , 3rd event is already expired, hence we need this kind of loop of loop to delete expired events
            while(!eventEndTime.empty() and *eventEndTime.begin() < d){
                eventEndTime.erase(eventEndTime.begin());
            }

            // put all candidate events whose start day is past the current day.

            //insert events if they can be start
            while(i < n and events[i][0] <=d){
                eventEndTime.insert(events[i][1]);
                i++;
            }

            // we can attend 1 event on 1 day , thats why if condition not while
            // adn we attend earliest ending event first , suppose we have [1, 2] & [1, 3]
            // and we are on day=2, we should attend [1,2] first otherwise at d=3 this would be expired
            if(!eventEndTime.empty() and *eventEndTime.begin()>=d){
                ++ans;
                eventEndTime.erase(eventEndTime.begin());
            }
        }
        return ans;
    }
};
```

[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) [ **Medium**]

### Using Map counter

```c++
    	class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        map<int, int> line;
        for(auto& i : intervals){
            ++line[i[0]];
            --line[i[1]];
        }

        int count = 0;
        vector<vector<int>> ans;
        int start = 0;
        for(auto& i : line){
            // that means its a new start, store the start
           if(count ==0){
               start = i.first;
           }
           count += i.second;
           // this mean interval ends, and we can push this as answer
           if(count==0){
               ans.push_back({start, i.first});
           }
        }
        return ans;
    }
};
```

### Using prev interval

```c++
	sort(intervals.begin(), intervals.end());// Sort y there start time
        vector<vector<int>> results;
        results.push_back(intervals[0]);
        for(int i =1; i < intervals.size(); ++i){
            if(intervals[i][0] > results.back()[1]) // a new begining
            {
                results.push_back(intervals[i]);
            }
            else
                results.back()[1] = max(results.back()[1], intervals[i][1]);
        }
        return results;
```

[1589. Maximum Sum Obtained of Any Permutation](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) [ **Medium**]  
[1943. Describe the Painting](https://leetcode.com/problems/describe-the-painting/) [ **Medium** ]  
[1674. Minimum Moves to Make Array Complementary](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) [ **Medium**]

### 1D Hard problem

These 1D Hard problem require scanning line for each input which can lead to O(n^2) algorithm.  
We have to do something special to optimize it.  
Lets see with an example.

[2158. Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/) [**Hard** ]  
In this problem each day we paint some section of a line.  
Brute force way is scan line for each input index.

Thanks to @cjcoax and @votrubac, I am putting both line sweep version and map interval method here.  
Similar problem
[2251. Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) [ **Hard**]

### Using Line Sweep

```c++
    	auto cmp =[&](const vector<int>& a, const vector<int>& b){
            return a[1]  < b[1];
        };
        int maxEnd = (*max_element(paint.begin(), paint.end(), cmp))[1];
        int n = paint.size();
        vector<int> ans(n, 0);
        vector<vector<pair<int, int>>> line(1 + maxEnd);
        // We are marking on line that co-oridnate is
	// painted/not-painted(true-false) between which date
        for(int i =0; i < n ; ++i){
            line[paint[i][0]].push_back(make_pair(i, 1));
            line[paint[i][1]].push_back(make_pair(i, 0));
        }

        set<int> days;
        //Scan the line
        for(int i =0; i < maxEnd; ++i){

            // Who all present on this x co-ordinate?
            for(auto& [day, state] : line[i]){

                if(state)
                    days.insert(day);
                else
                    days.erase(day);
            }
            //Only the first guy can paint this line
            if(!days.empty())
                ans[*(days.begin())]++;
        }
        return ans;
```

### Using Vector Interval

```c++
	map<int, int> m;
    vector<int> res;
    for (auto &p : pt) {
        int l = p[0], r = p[1];
        auto next = m.upper_bound(l), cur = next;

        // Step 1: suppose we have painted [1, 4] [ 5, 8] [10, 20]
        // Now a new interval [4, 21] comes upper_bound gives [5,8]
        // l = 4 then
        if (cur != begin(m) && prev(cur)->second >= l) {
            cur = prev(cur);
            l = cur->second;
        }
        else
            cur = m.insert({l, r}).first;
        int paint = r - l;
        // Next since r= 21 and that is  > 5, that means this paint is going to span
        // find how much shd we subtract :
        // get min of (21, 8) =  8 and then subtratc with start 5 = 3
        // now r shd be max of (21, 8) =21 , check further more intervals can be erased ?
        // in the end set curr->second = max(curr->second, r);
        while (next != end(m) && next->first < r) {
            paint -= min(r, next->second) - next->first;
            r = max(r, next->second);
            m.erase(next++);
        }
        cur->second = max(cur->second, r);
        res.push_back(max(0, paint));
    }
    return res;
```

[1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) [**Hard** ]
Key idea is at every point, find the maximum range.
Now sweep the line from 1 to n
if i > curr_max : not possible -1
else if i ==curr_max; current selected tap capacity is over, now we have select the next best tap which we have found in past. set that
else our current tap is good , no need to open any new tap, but keep recording next_best_tap.

```
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        // Find what is the max we can reach if we start opening the tap at every ith location
        vector<int> line (1+n, 0);
        for(int i =0; i <=n; ++i){
            int left = max(0, i - ranges[i]);
            int right = min(n, i + ranges[i]);
            line[left] = max(line[left], right);
        }
        // Sweep line
        // Lets 0th tap as best one
        int curr = line[0];
        int next_best = 0;
        int ans = 1;
        for(int i = 1; (i <=n) and (curr < n); ++i){
            // we cannot reach to this ith that means not possible at all !
            if( i > curr)
                return -1;
            else if ( i == curr){
                // curr reach its end , time to select next best
                next_best = max(next_best, line[i]);
                ++ans;
                curr = next_best; // assign next_best to curr
                next_best =0;//rest next_best as 0
            }
            else{
                // we still are in range of curr, no need to open a new tap but keep checking what next best tap of highest range we can open next.
                next_best = max(next_best, line[i]);
            }
        }
        return ans;;
    }
};
```

[732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/) [**Hard** ]  
Same as Meeting Room II as explained earlier.

[759. Employee Free Time](https://leetcode.com/problems/employee-free-time/) [**Hard**]  
Same conepts, mark start and end time on line, when will everyone is free i.e. when count is 0.
So whenever count is 0 , it mark the begining of an interval, also set a flag , so that after we non-zero from 0, we use that as closing interval.

```
	map<int, int> line;
        for(auto& s : schedule){
            for(auto& i :  s){
                ++line[i.start];
                --line[i.end];
            }
        }

        int count = 0;
        bool found = false;
        vector<Interval> ans;
        for(auto&x : line){
            count += x.second;
            if(found){
                ans.back().end = x.first;
                found = false;
            }
            if(count == 0){
                // mark begining of new interval
                ans.push_back(Interval(x.first, -1));
                found = true;
            }
        }
        ans.pop_back();
        return ans;
```

[1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) [**Hard**]  
We use multiset to track size of interval, multiset.begin() will always gives you smallest size interval which is still active.
Sweep the line,
If it is start of interval, insert the size in multiset,
If it is end of interval remove from multi set.
If there is a query here , just add the first (which is smallest size) to answer index

```
       map<int, set<pair<int, int>>> line;
        // -1 :  Entry  1 : Exit , 2 : Query & size of interval
        for(auto& i : intervals){
            int size = i[1] -i[0] + 1;
            line[i[0]].insert(make_pair(-1, size));
            line[i[1]+1].insert(make_pair(1, size));
        }

        for(int i =0; i < queries.size(); ++i){
            line[queries[i]].insert(make_pair(2, i));
        }
        vector<int> ans(queries.size(), -1);
        multiset<int> sizes;
        for(auto& [x, intervals] :  line){
            for(auto& i : intervals){
                if(i.first==-1)
                    sizes.insert(i.second);
                else if (i.first==1)
                    sizes.erase(sizes.lower_bound(i.second));
                else if (i.first ==2 and !sizes.empty())
                    ans[i.second] = *(sizes.begin());

            }

        }
        return ans;
```

### 2D Problem's

2D problems are slightly tricky as there extra dimension have to be tracked.  
Lets see this with an example.  
[850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

1. For each rectangle, first vertical line indicate rectangle is starting and second line indicates rectangle end.  
   So stores these events on x-axis, we need information line y_start, y_end and whether its a start event or end event.  
   **Sort these events on x-axis, if 2 rectangle start at same time, start event take precendence over end event**.  
   One of the test case has just straight line instead of rectangle.

2. Once we sweep the vertical line, we can get the width between two co-ordinate.

3. To get the height, we need to sum up the y-ordinate along the y-axis, which is a simple 1D problem as we did earlier.
   For example if we have the following intervals on yaxis [0,1] [0,2] [0, 3]  
   Total y length excluding duplicate is 3.
   Use the above 1D trick to solve this.

```
	int rectangleArea(vector<vector<int>>& rectangles) {

        vector<vector<int>> events;

        for(auto& r : rectangles){
            // x-cordinate, event_type(0 is open and 1 is close, y1, y2
            events.push_back({r[0], 0, r[1], r[3]});
            events.push_back({r[2], 1, r[1], r[3]});
        }

        auto cmp =[&](const vector<int>& a , const vector<int>& b){
            if(a[0]==b[0])
                return a[1] < b[1];
            return a[0] < b[0];
        };
        sort(events.begin(), events.end(), cmp);
        int area =0;
        int prev = INT_MIN; // sweep line is coming from far off
        multiset<pair<int, int>> yline; // y co-ordinate and whether entry or exit
        const int MOD = 1e9+7;
        // 1 -D line sweep
        auto get_area = [&](const int x){
            long long area = 0;
            long long prev = INT_MIN;
            int s =0;
            for(auto& y : yline){
                s += y.second;
                if(s==y.second) // mark the begining
                    prev = y.first;

                if(s==0)
                    area += (((y.first - prev)%MOD)* x)%MOD;

            }
            return area;
        };
        for(auto& e : events){
            // First calculate area
            if(prev!=INT_MIN)
                area  = (area + get_area(e[0] - prev))%MOD;

            if(e[1])
            {
                // delete both y co-ordinate
                yline.erase(yline.find(make_pair(e[2], 1)));
                yline.erase(yline.find(make_pair(e[3], -1)));
            }
            else{
                // insert both y co-ordinate of vertical line.
                yline.insert(make_pair(e[2], 1)); // Entry
                yline.insert(make_pair(e[3], -1)); // Exit
            }
            prev = e[0];
        }
        return area;
    }
```

Time Complexity would be O(n^2 log (n)) since for every x event we are trying to calculate the y sum which is 1D line sweep using multiset  
 and takes O(n log n)

[391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)

On Similar lines to above problem, two point to note.

1. Here we have to calculate exact cover which means, two rectangle cant intersect, lets understand this with an image.

![image](https://user-images.githubusercontent.com/20656683/174115549-d6ade836-d27c-407c-8731-9d10481df2ab.png)
![image](https://user-images.githubusercontent.com/20656683/174115717-12eacdd8-726a-405b-bd91-d84b5c4434cc.png)
![image](https://user-images.githubusercontent.com/20656683/174115644-e4b581d0-dacd-479f-b9c8-5a13f060950e.png)

Point to be noted that **new rectangle higher y-cordinate should be lower than equal to existing active rectangles** ( new rectangle is beneath) or **new rectangle lower y-cordinate should be greater than equal to to existing active rectangles** ( new rectangle is above).  
 2. **Sum of Height of the active rectangle** should always be exactly (ymax-ymin) else there would be hole and it wont be exact cover.

![image](https://user-images.githubusercontent.com/20656683/174116557-64e7fd04-40e1-48ad-b92b-79f8a8849332.png)

Here ymax is 3 and ymin is 0 , so everytime y height sum should be exactly 3 only then we would have exact cover.  
But in above example, sum of both y height is 2 and 2!=3 and hence return false.  
Thanks @wddd for his solution https://leetcode.com/problems/perfect-rectangle/discuss/87188/on-log-n-sweep-line-solution

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Why do we use **priority-queue(min-heap)**: Reason is we have to take decision whether to add skyline contour or not at the given x-cordinate.  
  So we try to pull out **all** the events for a given x , insert/delete as per event type and then decide whether to make contour or not.

- Why do we use multiset : Because multiple box of same height exist, if one box is removed that doesnt mean other box can be removed, hence multiset.

Logic: Before inserting height into multiset we note the maximum height available (thats why i used negative number in multiset).  
After processing of all events for a given x co-ordinate, check if the height changed ? if yes we have a contout here, otherwise skip.

```
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> ans;
        multiset<int> height;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> line; // min-heap
        for(auto& b : buildings){
            line.push({b[0], 0, b[2]});
            line.push({b[1], 1, b[2]});
        }
        while(!line.empty()){
            int before = height.empty() ? 0 : -*(begin(height));
            int x;
            do{
                x = line.top()[0];
                int event = line.top()[1];
                int yheight = line.top()[2];
                line.pop();
                if(event)
                    height.erase(height.find(-yheight));
                else
                    height.insert(-yheight);
            }while(!line.empty() and line.top()[0] == x);

            int after = height.empty() ? 0 : -*(begin(height));

            if(after != before)
                ans.push_back({x, after});
        }
        return ans;
    }
};
```

If you noticed in all above 3 problem, template remain same.

1. Store the events in either priority queue or vector in sorted manner of x-axis.  
   priority queue approach has an advantage of not worrying whether to keep entry event first or exit event first becauase your are popping out
   all events for same x-cordinate in one go and then deciding what to be done but if you use vector to store the interval and use custom comparator,
   you have to be careful about whether to add exit event first or entry event first because we pull event one by one.  
   See Skyline problem for priroity queue approach and Rectangle Area II for vector appraoch.
2. Use multiset of process of y-axis. This multiset can store either line or rectangle, depending on what problem is asking for.

Two more problems which I couldn't found on LeetCode(if its avaialable here, please let me know and will update the post) but without that line sweep is incomplete.

- Closest pair of points.
- Lines Intersection.

These problems involve line sweel and also geometric concepts which need a post of its own.  
Some of the important geometric concepts required for Algorithms, I can think of.

- Distance between between two co-ordinates.
- Finding orientation of new co-ordinate, this is useful in convex hull problem See [587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/).
- Finding intersection of two lines involves orientation.

@Leetcode , may be add few of the problems from here to leetcode tagged line sweep problem, which currently has just 4 of them.  
https://leetcode.com/tag/line-sweep/

My Other **Article** on Algorithmic techniques:

[Line Sweep Algorithms](https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms)  
[Solving kth kind of problems](https://leetcode.com/discuss/study-guide/1529866/solving-kth-kind-of-problems)  
[Binary Index Tree Template and Problem Solving](https://leetcode.com/discuss/study-guide/1569634/binary-index-tree-template-and-problem-solving)  
[BFS and its variations](https://leetcode.com/discuss/study-guide/1833581/bfs-and-its-variations)  
[Binary Lifting Technique](https://leetcode.com/discuss/study-guide/4299594/Binary-Lifting-Technique)  
debugger eval code:1:9
either line or rectangle, depending on what problem is asking for.

Two more problems which I couldn't found on LeetCode(if its avaialable here, please let me know and will update the post) but without that line sweep is incomplete.

- Closest pair of points.
- Lines Intersection.

These problems involve line sweel and also geometric concepts which need a post of its own.  
Some of the important geometric concepts required for Algorithms, I can think of.

- Distance between between two co-ordinates.
- Finding orientation of new co-ordinate, this is useful in convex hull problem See [587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/).
- Finding intersection of two lines involves orientation.

@Leetcode , may be add few of the problems from here to leetcode tagged line sweep problem, which currently has just 4 of them.  
https://leetcode.com/tag/line-sweep/

My Other **Article** on Algorithmic techniques:

[Line Sweep Algorithms](https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms)  
[Solving kth kind of problems](https://leetcode.com/discuss/study-guide/1529866/solving-kth-kind-of-problems)  
[Binary Index Tree Template and Problem Solving](https://leetcode.com/discuss/study-guide/1569634/binary-index-tree-template-and-problem-solving)  
[BFS and its variations](https://leetcode.com/discuss/study-guide/1833581/bfs-and-its-variations)  
[Binary Lifting Technique](https://leetcode.com/discuss/study-guide/4299594/Binary-Lifting-Technique)  
debugger eval code:1:9

        return ans;
    }

</details>

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) [ **Medium**]  
Same as above just we have to keep track of maximum count of rooms and return it.  
When a meeting start we plot +1 for end we do -1.
Now we scan the line, and store the value in `count` , if count is 1 that mean 1 meeting start, if its 2 that means 2nd meeting started before 1st ended, so we need 2 room atleast. This count we save in `ans` if `count > ans` .

```
class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        map<int, int> line;
        for(auto& i : intervals){
            line[i.start]++;
            line[i.end]--;
        }
        int ans = 0;
        int count;
        for(auto& p : line){
            count += p.second;
            ans = max(ans, count);
        }
        return ans;
    }
};
```

Time Complexity = O(n log n )

[731. My Calendar II](https://leetcode.com/problems/my-calendar-ii/) [ **Medium** ]  
We have to count if there are triple booking , so if at any time we have count >=3 (==3 is enough)  
We return false and also remove this booking from the entry.  
Same approach, use a map and +1 when booking start and -1 when booking end.  
Sweep the line from left to right.

Time Complexity = O(n^2 \* log n ) as for every booking we are sweeping entire line.

```
bool book(int start, int end) {
        ++m[start];
        --m[end];
        int count = 0;
        for(auto& i : m){
            count += i.second;
            if(count ==3){
                // we are not going to add this event
                // nullify line 10,11 changes
                --m[start];
                ++m[end];
                return false;
            }
        }
        return true;
    }
```

[2237. Count Positions on Street With Required Brightness](https://leetcode.com/problems/count-positions-on-street-with-required-brightness/) [ **Medium** ]  
Similar, here we are given a threshold of brightness for each index, first fill up the count by +1 and -1 index where brightness start and end.  
Now scan the vector and see if threshold achieved , if yes ++ans.

Time Complexity = O(n)

<details>
<summary>

#### Click to see Code

</summary>

     bool isCovered(vector<vector<int>>& ranges, int left, int right) {

      int line[52] = {};
    for (auto &r : ranges) {

        line[r[0]] += 1;
        line[(r[1]+1)] -= 1;
    }

    for (int i = 1, overlaps = 0; i <= 51; ++i) {
        overlaps += line[i];
        if (i>=left and i <=right and overlaps <= 0)
            return false;
    }

    return true;
    }

</details>

[1893. Check if All the Integers in a Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) [**Easy** ]  
Mark start and end( end+1 since its a closed interval] as +1/-1 respectively.  
Now scan the line from 1 to 50 , see which co-ordinate falls in given [left right] range and overlap is 0, that mean no range is covering , return false.

Time Complexity = O(n)

[370. Range Addition](https://leetcode.com/problems/range-addition/) [ **Medium**]  
Accumulate +update in start and -update in end+1  
After that sweep the line and accumulate sum in a variable and keep assigning to every index.

Time Complexity = O(n)

**Type 2**:
In this kind of problem, you may not be able to plot the point and arrive at solution. Instead you have to use **prev** technique.  
Lets see this example

[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) [ **Medium**]  
In this kind of problem, we dont use marking on axis, instead axis is already given, we sort it.

> Initial setup after sort

    ![image](https://assets.leetcode.com/users/images/73811d36-8aea-4576-b945-797c86573561_1689758547.3407717.png)

> Hitting first ballon

    ![image](https://assets.leetcode.com/users/images/94941364-9c75-4d32-9ec7-2b5c1ba8b300_1689759385.382266.png)

Now if we strike first ballon , we can strike at the end-most point i.e. **2**  
We save this as **prev = 2**  
Any ballon starting before we dont need extra arraow since this arrow is enough to burst the ballon.  
The moment start point > prev , we know we need a new ballon again we save the end-most point in the prev and repeat the process.  
Many problem can be solved using this technique.

```
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        auto cmp = [&](const vector<int>& a, const vector<int>& b){

            return a[1] < b[1];
        };
        sort(points.begin(), points.end(), cmp);
        int prev_end = points[0][1];
        int ans = 1;
        for(int i =1; i < points.size(); ++i){
            if(points[i][0] > prev_end){
                ++ans;
                prev_end = points[i][1];
            }
        }
        return ans;
    }
};
```

[435 Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) [ **Medium** ]

**Why Sorting with endTimes Works**
In many of the problem above we do sorting with endTime , this is an important concept to understand,
if you sort with endTime and then check other intervals you can easily find non-overlapping intervals like this, here prev is previous interval.

```
if(intervals[i][0] < intervals[prev][1])
```

Reason is if a new interval start is before previous end time that means a sure overlap.
While on the other hand if we sort by startTime, we dont know when this interval gonna end, there will be overlaps.
Here are some additional points to consider:

**Sorting by end time is a greedy algorithm**. This means that it makes the best possible choice at each step, without considering the future. As a result, it is usually more efficient than sorting by start time.
**Sorting by start time is a dynamic programming algorithm**. This means that it makes a choice at each step, based on the choices that it has made in the past. As a result, it is usually more robust to errors in the input data.
For practice try to solve this problem , which can be solved in both DP as well as Greey Way and see the difference

[646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)

[252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) [ **Easy**]  
Just scan and if ith start < i-1 end return false

**Insert Interval**  
Suppose we haev insert [3,7] to an existing interval [1, 10]  
For each start we do +1 and for end we do -1 on the number line (map).  
Next scan the line, if the count is 0, that mean a new line is going to start, so mark it as start  
And then accumulate the count, now if count is 0, that mean the interval has ended so insert this interval.

![image](https://assets.leetcode.com/users/images/f57fbab6-c436-4aeb-9231-fca64dc5a0c8_1694355372.721946.png)

[57. Insert Interval](https://leetcode.com/problems/insert-interval/) [ **Medium** ]

### Using Map counter

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        map<int, int> m;
        for(auto& p : intervals){
            ++m[p[0]];
            --m[p[1]];
        }
        ++m[newInterval[0]];
        --m[newInterval[1]];
        int count = 0;
        vector<vector<int>> ans;
        int start;
        for(auto& i : m){
            if(count==0){
                start = i.first;
            }
            count += i.second;
            if(count == 0){
                ans.push_back({start, i.first});
            }
        }
        return ans;
    }
};
```

### Using Interval

```c++
	class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {

        vector<vector<int>> ans;
        for(auto& i : intervals){
            if(i[1] < newInterval[0]){
                ans.push_back(i);
            }
            else if( newInterval[1] < i[0]){
                ans.push_back(newInterval);
                newInterval = i;
            }
            else if((i[1] >= newInterval[0])  or ( newInterval[1] <=i[0])){
                /*
                ------ [i]
                   ------- [new]

                ------
             ------
             */
             newInterval[0] = min(newInterval[0], i[0]);
             newInterval[1] = max(newInterval[1], i[1]);
            }
        }
        ans.push_back(newInterval);
        return ans;
    }
};
```

[1272. Remove Interval](https://leetcode.com/problems/remove-interval/) [ **Medium** ]

**Approach #1**:
increment at start and decrement end , while for remove interavl do reverse since we have to remove
standard logic of count==i.start and count > 0
and for closing interval count=0 and we have added previously(use a bool flag)

**Approach #2**:
Input is sorted, so we sweep and if removed_start > ith_end or remove_end < ith_start , we simply add the ith boundary to o/p.  
Otherwise if ith_start < remove_start -> add ith_start, remove_start  
Also if ith_end > remove_end then add [remove_end, ith_end]

Both approach coded for comparison, Merge Interval and Insert Interval can also be solved using similar approach.  
Please let me know in comment section which approach is preferable as I am still learning.  
Its a bit tough to come up Approach 1 for all problem but Approach 2 works for all.

### Using Map counter

```c++
        map<int, int> line;

	for(auto& i : intervals)
	{
		++line[i[0]];
		--line[i[1]];
	}
	--line[toBeRemoved[0]];
	++line[toBeRemoved[1]];
	vector<vector<int>> ans;
	int count =0; bool added =false;
	for(auto& i : line)
	{
		count += i.second;
		if(count ==1 ){
			ans.push_back({i.first, -1});
			added = true;
		}
		if(count==0 and added){
			ans.back()[1] = i.first;
			added = false;
		}
	}
	return ans;
```

### Using prev interval

```c++
	vector<vector<int>> ans;

	for(auto &i :  intervals)
	{
		int left = i[0];
		int right = i[1];
		if( (toBeRemoved[0] > right ) or (toBeRemoved[1] < left ))
		{
			ans.push_back({left, right});
		}
		else
		{
			if(left < toBeRemoved[0])
			{
				ans.push_back({left, toBeRemoved[0]});
			}
			if (right > toBeRemoved[1])
			{
				ans.push_back({toBeRemoved[1], right});
			}
		}
	}
```

**Approach 1 details**
For insert interval : when we start , `if count is 0` that essentially means a new begining , so record the start poisition.
Now after we are done adding line value to count and still count is 0 , that essentially mean interval ended, so use the previously recorded start and now this endging value to form a interval. Let see the example input this with a image, **before we start processing if count is 0 and we record as start of new interval** and **after processing** if it is still 0, that mean end of intervals.

![image](https://assets.leetcode.com/users/images/47947991-bf67-41a5-87e1-393045a17cfa_1700714223.3685725.png)
Before processing 1 , which is start of interval, count is 0 so we mark start =1, after we process count is 1
Process 2 , as it is start , count =2
Process 3 , as it is end , count =1
Process 5, as it is end count = 0 , now since count is 0 after process we insert [1, 5] in answer.
Process 6, since count is 0 **before process**, this is start of new interval, record start =6 and now process start - 6
Procss 9 , count will be 0 **after process** , so that mean its end , record [6, 9] in answer.

For **Remove Interval** sweep approach is similar except now we have to remove the interval , that we mark start as -ve and end as +ve marking on line ans tweak the sount logic.  
Now try to solve this problem using same count technique.

[1229. Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) [**Medium**]

Some pointers, we have 2 candidate, so if both have started only then only take there latest time, for example
suppose Person is available from [10:00 , 12:00] but person 2 is available from [11:00 , 12:00]
after we sweep the line past [11:00] count would be 2 and then we can take [11:00] as candidate start time as this time is common to both person.

Next whenever we encounter an end of time AND we have already noted down the common_time , check if we met the duration ? if yes return , because this earlies, otherwise reset the common_time, as now we have to find some common start all over again.

<details>
<summary>

#### Click to see Code

</summary>

    Interval earliestAppropriateDuration(vector<Interval> &slots1, vector<Interval> &slots2, int duration) {
        // --- write your code here ---
        map<int, int> m;
        for(auto& i : slots1){
            m[i.start]++;
            m[i.end]--;
        }
        for(auto& i : slots2){
            m[i.start]++;
            m[i.end]--;
        }
        int count = 0;
        Interval candidate(-1, -1);

        for(auto& p : m){
            int old = count;
            count += p.second;
            if(count ==2){
                candidate.start = p.first;
            }
            // If count is decreasing that mean some slot is ending
            if(count < old and candidate.start!=-1){
                if(p.first - candidate.start >= duration) // we found
                {
                    candidate.end = candidate.start+duration;
                    return candidate;
                }
                else{
                    candidate.start = -1;
                }
            }
        }
        return {-1, -1};
    }

</details>

[1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) [ **Medium** ]  
Step 1: Sort with start, if both start are same , give precedence to higher ending interval first.  
Step 2: Insert the first interval uncondtionally , after that scan the other interavl , following 3 possibility (see code comment can occur)

```
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {

        vector<vector<int>> ans;
        auto comp = [&](const vector<int>& i, const vector<int>& j){
            if(i[0]==j[0])
                return i[1] > j[1];
            return i[0] < j[0];
        };
        sort(intervals.begin(), intervals.end(), comp);
        ans.push_back(intervals[0]);
        int k =0;
        for(int i =1; i< intervals.size(); ++i){
            if( (intervals[i][0]>= ans.back()[0]) and (intervals[i][1] <= ans.back()[1]))
            {
			   // Scenario 1: Completely covered suppose existing interval in vector is [1, 8] and this ith interval is [2, 6] , this is completely inside i.e. start and end
			   // lies inside , hence this interval is surely removed, count this.
                ++k;
            }
            else if(intervals[i][0] > ans.back()[1]){
			// Scenario 2: Suppose vector has [1, 8]  and ith interval is  [9, 10] , totallly unrelated, so push this interval in vector as this is going to be used next time.
                ans.push_back(intervals[i]);
            }
            else if ((intervals[i][0] > ans.back()[0]) and (intervals[i][0] <= ans.back()[1]) )
			    // Scenario 3: vector has [1, 8] and ith interval is  [5, 10], so take maximum of both end point.
                ans.back()[1] = max(ans.back()[1], intervals[i][1]);
        }
        return intervals.size()- k;
    }
};
```

[1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) [ **Medium**]

Add detailed comments in code , please check , here the key idea is we are sweeping the day as a number line, it is given in input and we mark the events on that day line.

```
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        multiset<int> eventEndTime;
        int i =0;
        int ans = 0;
        int n = events.size();
        for(int d =1; d <=100000; ++d){
            //Delete expired event , example
            // Suppose 3 events are there  [1, 2] [1, 2] [1, 2]
            // at day 1 : attend 1st event and at day 2 attend 2md event , at day 3 , 3rd event is already expired, hence we need this kind of loop of loop to delete expired events
            while(!eventEndTime.empty() and *eventEndTime.begin() < d){
                eventEndTime.erase(eventEndTime.begin());
            }

            // put all candidate events whose start day is past the current day.

            //insert events if they can be start
            while(i < n and events[i][0] <=d){
                eventEndTime.insert(events[i][1]);
                i++;
            }

            // we can attend 1 event on 1 day , thats why if condition not while
            // adn we attend earliest ending event first , suppose we have [1, 2] & [1, 3]
            // and we are on day=2, we should attend [1,2] first otherwise at d=3 this would be expired
            if(!eventEndTime.empty() and *eventEndTime.begin()>=d){
                ++ans;
                eventEndTime.erase(eventEndTime.begin());
            }
        }
        return ans;
    }
};
```

[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) [ **Medium**]

### Using Map counter

```c++
    	class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        map<int, int> line;
        for(auto& i : intervals){
            ++line[i[0]];
            --line[i[1]];
        }

        int count = 0;
        vector<vector<int>> ans;
        int start = 0;
        for(auto& i : line){
            // that means its a new start, store the start
           if(count ==0){
               start = i.first;
           }
           count += i.second;
           // this mean interval ends, and we can push this as answer
           if(count==0){
               ans.push_back({start, i.first});
           }
        }
        return ans;
    }
};
```

### Using prev interval

```c++
	sort(intervals.begin(), intervals.end());// Sort y there start time
        vector<vector<int>> results;
        results.push_back(intervals[0]);
        for(int i =1; i < intervals.size(); ++i){
            if(intervals[i][0] > results.back()[1]) // a new begining
            {
                results.push_back(intervals[i]);
            }
            else
                results.back()[1] = max(results.back()[1], intervals[i][1]);
        }
        return results;
```

[1589. Maximum Sum Obtained of Any Permutation](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) [ **Medium**]  
[1943. Describe the Painting](https://leetcode.com/problems/describe-the-painting/) [ **Medium** ]  
[1674. Minimum Moves to Make Array Complementary](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) [ **Medium**]

### 1D Hard problem

These 1D Hard problem require scanning line for each input which can lead to O(n^2) algorithm.  
We have to do something special to optimize it.  
Lets see with an example.

[2158. Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/) [**Hard** ]  
In this problem each day we paint some section of a line.  
Brute force way is scan line for each input index.

Thanks to @cjcoax and @votrubac, I am putting both line sweep version and map interval method here.  
Similar problem
[2251. Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) [ **Hard**]

### Using Line Sweep

```c++
    	auto cmp =[&](const vector<int>& a, const vector<int>& b){
            return a[1]  < b[1];
        };
        int maxEnd = (*max_element(paint.begin(), paint.end(), cmp))[1];
        int n = paint.size();
        vector<int> ans(n, 0);
        vector<vector<pair<int, int>>> line(1 + maxEnd);
        // We are marking on line that co-oridnate is
	// painted/not-painted(true-false) between which date
        for(int i =0; i < n ; ++i){
            line[paint[i][0]].push_back(make_pair(i, 1));
            line[paint[i][1]].push_back(make_pair(i, 0));
        }

        set<int> days;
        //Scan the line
        for(int i =0; i < maxEnd; ++i){

            // Who all present on this x co-ordinate?
            for(auto& [day, state] : line[i]){

                if(state)
                    days.insert(day);
                else
                    days.erase(day);
            }
            //Only the first guy can paint this line
            if(!days.empty())
                ans[*(days.begin())]++;
        }
        return ans;
```

### Using Vector Interval

```c++
	map<int, int> m;
    vector<int> res;
    for (auto &p : pt) {
        int l = p[0], r = p[1];
        auto next = m.upper_bound(l), cur = next;

        // Step 1: suppose we have painted [1, 4] [ 5, 8] [10, 20]
        // Now a new interval [4, 21] comes upper_bound gives [5,8]
        // l = 4 then
        if (cur != begin(m) && prev(cur)->second >= l) {
            cur = prev(cur);
            l = cur->second;
        }
        else
            cur = m.insert({l, r}).first;
        int paint = r - l;
        // Next since r= 21 and that is  > 5, that means this paint is going to span
        // find how much shd we subtract :
        // get min of (21, 8) =  8 and then subtratc with start 5 = 3
        // now r shd be max of (21, 8) =21 , check further more intervals can be erased ?
        // in the end set curr->second = max(curr->second, r);
        while (next != end(m) && next->first < r) {
            paint -= min(r, next->second) - next->first;
            r = max(r, next->second);
            m.erase(next++);
        }
        cur->second = max(cur->second, r);
        res.push_back(max(0, paint));
    }
    return res;
```

[1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) [**Hard** ]
Key idea is at every point, find the maximum range.
Now sweep the line from 1 to n
if i > curr_max : not possible -1
else if i ==curr_max; current selected tap capacity is over, now we have select the next best tap which we have found in past. set that
else our current tap is good , no need to open any new tap, but keep recording next_best_tap.

```
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        // Find what is the max we can reach if we start opening the tap at every ith location
        vector<int> line (1+n, 0);
        for(int i =0; i <=n; ++i){
            int left = max(0, i - ranges[i]);
            int right = min(n, i + ranges[i]);
            line[left] = max(line[left], right);
        }
        // Sweep line
        // Lets 0th tap as best one
        int curr = line[0];
        int next_best = 0;
        int ans = 1;
        for(int i = 1; (i <=n) and (curr < n); ++i){
            // we cannot reach to this ith that means not possible at all !
            if( i > curr)
                return -1;
            else if ( i == curr){
                // curr reach its end , time to select next best
                next_best = max(next_best, line[i]);
                ++ans;
                curr = next_best; // assign next_best to curr
                next_best =0;//rest next_best as 0
            }
            else{
                // we still are in range of curr, no need to open a new tap but keep checking what next best tap of highest range we can open next.
                next_best = max(next_best, line[i]);
            }
        }
        return ans;;
    }
};
```

[732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/) [**Hard** ]  
Same as Meeting Room II as explained earlier.

[759. Employee Free Time](https://leetcode.com/problems/employee-free-time/) [**Hard**]  
Same conepts, mark start and end time on line, when will everyone is free i.e. when count is 0.
So whenever count is 0 , it mark the begining of an interval, also set a flag , so that after we non-zero from 0, we use that as closing interval.

```
	map<int, int> line;
        for(auto& s : schedule){
            for(auto& i :  s){
                ++line[i.start];
                --line[i.end];
            }
        }

        int count = 0;
        bool found = false;
        vector<Interval> ans;
        for(auto&x : line){
            count += x.second;
            if(found){
                ans.back().end = x.first;
                found = false;
            }
            if(count == 0){
                // mark begining of new interval
                ans.push_back(Interval(x.first, -1));
                found = true;
            }
        }
        ans.pop_back();
        return ans;
```

[1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) [**Hard**]  
We use multiset to track size of interval, multiset.begin() will always gives you smallest size interval which is still active.
Sweep the line,
If it is start of interval, insert the size in multiset,
If it is end of interval remove from multi set.
If there is a query here , just add the first (which is smallest size) to answer index

```
       map<int, set<pair<int, int>>> line;
        // -1 :  Entry  1 : Exit , 2 : Query & size of interval
        for(auto& i : intervals){
            int size = i[1] -i[0] + 1;
            line[i[0]].insert(make_pair(-1, size));
            line[i[1]+1].insert(make_pair(1, size));
        }

        for(int i =0; i < queries.size(); ++i){
            line[queries[i]].insert(make_pair(2, i));
        }
        vector<int> ans(queries.size(), -1);
        multiset<int> sizes;
        for(auto& [x, intervals] :  line){
            for(auto& i : intervals){
                if(i.first==-1)
                    sizes.insert(i.second);
                else if (i.first==1)
                    sizes.erase(sizes.lower_bound(i.second));
                else if (i.first ==2 and !sizes.empty())
                    ans[i.second] = *(sizes.begin());

            }

        }
        return ans;
```

### 2D Problem's

2D problems are slightly tricky as there extra dimension have to be tracked.  
Lets see this with an example.  
[850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

1. For each rectangle, first vertical line indicate rectangle is starting and second line indicates rectangle end.  
   So stores these events on x-axis, we need information line y_start, y_end and whether its a start event or end event.  
   **Sort these events on x-axis, if 2 rectangle start at same time, start event take precendence over end event**.  
   One of the test case has just straight line instead of rectangle.

2. Once we sweep the vertical line, we can get the width between two co-ordinate.

3. To get the height, we need to sum up the y-ordinate along the y-axis, which is a simple 1D problem as we did earlier.
   For example if we have the following intervals on yaxis [0,1] [0,2] [0, 3]  
   Total y length excluding duplicate is 3.
   Use the above 1D trick to solve this.

```
	int rectangleArea(vector<vector<int>>& rectangles) {

        vector<vector<int>> events;

        for(auto& r : rectangles){
            // x-cordinate, event_type(0 is open and 1 is close, y1, y2
            events.push_back({r[0], 0, r[1], r[3]});
            events.push_back({r[2], 1, r[1], r[3]});
        }

        auto cmp =[&](const vector<int>& a , const vector<int>& b){
            if(a[0]==b[0])
                return a[1] < b[1];
            return a[0] < b[0];
        };
        sort(events.begin(), events.end(), cmp);
        int area =0;
        int prev = INT_MIN; // sweep line is coming from far off
        multiset<pair<int, int>> yline; // y co-ordinate and whether entry or exit
        const int MOD = 1e9+7;
        // 1 -D line sweep
        auto get_area = [&](const int x){
            long long area = 0;
            long long prev = INT_MIN;
            int s =0;
            for(auto& y : yline){
                s += y.second;
                if(s==y.second) // mark the begining
                    prev = y.first;

                if(s==0)
                    area += (((y.first - prev)%MOD)* x)%MOD;

            }
            return area;
        };
        for(auto& e : events){
            // First calculate area
            if(prev!=INT_MIN)
                area  = (area + get_area(e[0] - prev))%MOD;

            if(e[1])
            {
                // delete both y co-ordinate
                yline.erase(yline.find(make_pair(e[2], 1)));
                yline.erase(yline.find(make_pair(e[3], -1)));
            }
            else{
                // insert both y co-ordinate of vertical line.
                yline.insert(make_pair(e[2], 1)); // Entry
                yline.insert(make_pair(e[3], -1)); // Exit
            }
            prev = e[0];
        }
        return area;
    }
```

Time Complexity would be O(n^2 log (n)) since for every x event we are trying to calculate the y sum which is 1D line sweep using multiset  
 and takes O(n log n)

[391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)

On Similar lines to above problem, two point to note.

1. Here we have to calculate exact cover which means, two rectangle cant intersect, lets understand this with an image.

![image](https://user-images.githubusercontent.com/20656683/174115549-d6ade836-d27c-407c-8731-9d10481df2ab.png)
![image](https://user-images.githubusercontent.com/20656683/174115717-12eacdd8-726a-405b-bd91-d84b5c4434cc.png)
![image](https://user-images.githubusercontent.com/20656683/174115644-e4b581d0-dacd-479f-b9c8-5a13f060950e.png)

Point to be noted that **new rectangle higher y-cordinate should be lower than equal to existing active rectangles** ( new rectangle is beneath) or **new rectangle lower y-cordinate should be greater than equal to to existing active rectangles** ( new rectangle is above).  
 2. **Sum of Height of the active rectangle** should always be exactly (ymax-ymin) else there would be hole and it wont be exact cover.

![image](https://user-images.githubusercontent.com/20656683/174116557-64e7fd04-40e1-48ad-b92b-79f8a8849332.png)

Here ymax is 3 and ymin is 0 , so everytime y height sum should be exactly 3 only then we would have exact cover.  
But in above example, sum of both y height is 2 and 2!=3 and hence return false.  
Thanks @wddd for his solution https://leetcode.com/problems/perfect-rectangle/discuss/87188/on-log-n-sweep-line-solution

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

- Why do we use **priority-queue(min-heap)**: Reason is we have to take decision whether to add skyline contour or not at the given x-cordinate.  
  So we try to pull out **all** the events for a given x , insert/delete as per event type and then decide whether to make contour or not.

- Why do we use multiset : Because multiple box of same height exist, if one box is removed that doesnt mean other box can be removed, hence multiset.

Logic: Before inserting height into multiset we note the maximum height available (thats why i used negative number in multiset).  
After processing of all events for a given x co-ordinate, check if the height changed ? if yes we have a contout here, otherwise skip.

```
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> ans;
        multiset<int> height;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> line; // min-heap
        for(auto& b : buildings){
            line.push({b[0], 0, b[2]});
            line.push({b[1], 1, b[2]});
        }
        while(!line.empty()){
            int before = height.empty() ? 0 : -*(begin(height));
            int x;
            do{
                x = line.top()[0];
                int event = line.top()[1];
                int yheight = line.top()[2];
                line.pop();
                if(event)
                    height.erase(height.find(-yheight));
                else
                    height.insert(-yheight);
            }while(!line.empty() and line.top()[0] == x);

            int after = height.empty() ? 0 : -*(begin(height));

            if(after != before)
                ans.push_back({x, after});
        }
        return ans;
    }
};
```

If you noticed in all above 3 problem, template remain same.

1. Store the events in either priority queue or vector in sorted manner of x-axis.  
   priority queue approach has an advantage of not worrying whether to keep entry event first or exit event first becauase your are popping out
   all events for same x-cordinate in one go and then deciding what to be done but if you use vector to store the interval and use custom comparator,
   you have to be careful about whether to add exit event first or entry event first because we pull event one by one.  
   See Skyline problem for priroity queue approach and Rectangle Area II for vector appraoch.
2. Use multiset of process of y-axis. This multiset can store either line or rectangle, depending on what problem is asking for.

Two more problems which I couldn't found on LeetCode(if its avaialable here, please let me know and will update the post) but without that line sweep is incomplete.

- Closest pair of points.
- Lines Intersection.

These problems involve line sweel and also geometric concepts which need a post of its own.  
Some of the important geometric concepts required for Algorithms, I can think of.

- Distance between between two co-ordinates.
- Finding orientation of new co-ordinate, this is useful in convex hull problem See [587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/).
- Finding intersection of two lines involves orientation.

@Leetcode , may be add few of the problems from here to leetcode tagged line sweep problem, which currently has just 4 of them.  
https://leetcode.com/tag/line-sweep/

My Other **Article** on Algorithmic techniques:

[Line Sweep Algorithms](https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms)  
[Solving kth kind of problems](https://leetcode.com/discuss/study-guide/1529866/solving-kth-kind-of-problems)  
[Binary Index Tree Template and Problem Solving](https://leetcode.com/discuss/study-guide/1569634/binary-index-tree-template-and-problem-solving)  
[BFS and its variations](https://leetcode.com/discuss/study-guide/1833581/bfs-and-its-variations)  
[Binary Lifting Technique](https://leetcode.com/discuss/study-guide/4299594/Binary-Lifting-Technique)  
debugger eval code:1:9
either line or rectangle, depending on what problem is asking for.

Two more problems which I couldn't found on LeetCode(if its avaialable here, please let me know and will update the post) but without that line sweep is incomplete.

- Closest pair of points.
- Lines Intersection.

These problems involve line sweel and also geometric concepts which need a post of its own.  
Some of the important geometric concepts required for Algorithms, I can think of.

- Distance between between two co-ordinates.
- Finding orientation of new co-ordinate, this is useful in convex hull problem See [587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/).
- Finding intersection of two lines involves orientation.

@Leetcode , may be add few of the problems from here to leetcode tagged line sweep problem, which currently has just 4 of them.  
https://leetcode.com/tag/line-sweep/

My Other **Article** on Algorithmic techniques:

[Line Sweep Algorithms](https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms)  
[Solving kth kind of problems](https://leetcode.com/discuss/study-guide/1529866/solving-kth-kind-of-problems)  
[Binary Index Tree Template and Problem Solving](https://leetcode.com/discuss/study-guide/1569634/binary-index-tree-template-and-problem-solving)  
[BFS and its variations](https://leetcode.com/discuss/study-guide/1833581/bfs-and-its-variations)  
[Binary Lifting Technique](https://leetcode.com/discuss/study-guide/4299594/Binary-Lifting-Technique)
