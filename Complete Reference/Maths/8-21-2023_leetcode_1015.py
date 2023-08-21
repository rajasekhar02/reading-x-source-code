from os import *
from sys import *
from collections import *
from math import *

"""Comment by Some User
I found myself unsure of why several statements in this problem were true. I think I figured it out eventually, so I'll just leave it here in case someone finds themselves in the same boat.

* I'll start with probably the silliest one, but I found that understanding it helped me with the one I found the most perplexing.
Why 1 % 3 is 1, i.e. when the divided number is smaller than the divisor, why the remainder is equal to the number itself?
Think of what happens when the first number is bigger than the divisor, for example,
20 % 7 = (14 + 6) % 7 = 6.
You can think of it as "take all of the 7s out of 20 you can (14), and the leftovers are the remainder". So when we consider 1 % 3, we basically need to take all the 3s out of 1 we can, which is 0 -- no 3s can fit in 1, so
1 % 3 = (0 * 3 + 1) % 3 = 1

* Why do we need to look at the remainders at most K times? When we think about something divided by 3, possible remainders are 0, 1, and 2. For 5, its 0, 1, 2, 3, 4. So there could be only k - 1 possible remainders that we can observe in the worst case, after that they will have to start to repeat (and in many cases they repeat much earlier than k) .

* Why can we discard the previous number and can just keep track of the remainders?
Take k = 17 as an example, and let's just consider one random case with n = 111.
The remainder will be 9: 111 % 17 = (6 * 17 + 9) % 17 = 9. Notice how 6 * 17 can be just ignored here and does not influence the remainder itself.
The next n will be 1111 * 10 + 1 = 11111. If we replace 1111 with 6 * 17 + 9, we get n = (6 * 17 + 9) * 10 + 1. Let's open the brackets: [6 * 17 * 10] + [9 * 10] + [1]. So we need to figure out the remainder of this whole number that consists of three sums. But 6 * 17 * 10 already has a k in it, 6 * 10 of them in fact. So we can just take 6 * 17 * 10 and ignore it completely, and then we're left with previous remainder 9 in place of the old number 111, so now 9 * 10 + 1 is what we need to be divisible by 17.
If you're unsure why we can get away with ignoring part of the sum that is divisible by k, consider a modulo of any sum. For example, what's remainder of (5 + 2 + 1) % 3?
We can just calculate the sum in the brackets and find the modulo of the result:
5 + 2 + 1 = 8
8 % 3 = 2
But we can also get to 2 by considering modulo of each of the numbers in the sum:
5 % 3 = 2
2 % 3 = 2
1 % 3 = 1
If you sum them up,
2 + 2 + 1 = 5
It's bigger than 3, so we need to modulo it one last time
5 % 3 = 2
And you get to the same modulo of 2.
So modulo of sum (a + b + c) % k = ([a % k] + [b % k] + [c % k]) % k

But I think I'd have very hard time figuring this out on a real interview : )
"""


def lengthOfNumber(k):
    # Write your code here.
    # if k % 2 == 0:
    # 	return -1
    N = 1
    remainder = 1
    seen_remainders = set()
    lenN = 1
    while N % k != 0:
        # key point 1: using only remainder instead of actual number
        N = remainder * 10 + 1
        remainder = N % k
        # key point 2: using remainders as signal for that the k doesnot divide N
        if remainder in seen_remainders:
            return -1
        seen_remainders.add(remainder)
        lenN += 1
    return lenN
