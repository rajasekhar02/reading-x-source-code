import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0])
        rooms = []
        
        for i in range(0, n):
            heapq.heappush(rooms, i)
        
        allocatedRoomQueue = []
        roomsMeetingCnt = [0]*n
        
        roomNo = heapq.heappop(rooms)
        heapq.heappush(allocatedRoomQueue, (meetings[0][1], roomNo))
        roomsMeetingCnt[0] += 1
        
        nextMeeting = 1
        while nextMeeting < len(meetings):
            endTime = allocatedRoomQueue[0][0]
            nextMeetStartTime = meetings[nextMeeting][0]
            # print(rooms)
            while nextMeetStartTime >= endTime:
                # if len(allocatedRoomQueue)>0:
                tEndTime, roomNo = heapq.heappop(allocatedRoomQueue)
                heapq.heappush(rooms, roomNo)
                if len(allocatedRoomQueue)>0:
                    endTime = allocatedRoomQueue[0][0]
                else:
                    break
            # print(rooms)
            if len(rooms) > 0:
                # allocating the available rooms
                roomNo = heapq.heappop(rooms)
                heapq.heappush(allocatedRoomQueue, (meetings[nextMeeting][1], roomNo))
                roomsMeetingCnt[roomNo] += 1
            else:
                # clearing the rooms by fast-forwarding the end time
                tEndTime, roomNo = heapq.heappop(allocatedRoomQueue)
                # print(roomNo)
                # heapq.heappush(rooms, roomNo)
                nextMeetDuration = meetings[nextMeeting][1]-meetings[nextMeeting][0]
                heapq.heappush(allocatedRoomQueue, (max(tEndTime,nextMeetStartTime)+nextMeetDuration, roomNo))
                roomsMeetingCnt[roomNo] += 1
            nextMeeting += 1
        maxRoomNo = 0
        maxRoomCnt = 0
        for i in range(0, n):
            if roomsMeetingCnt[i] > maxRoomCnt:
                maxRoomNo = i
                maxRoomCnt = roomsMeetingCnt[i]
        print(roomsMeetingCnt)
        return maxRoomNo
        
