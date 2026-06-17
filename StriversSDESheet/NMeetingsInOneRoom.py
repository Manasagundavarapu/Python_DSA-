class Solution:
    def maxMeetings(self, start, end):
        n = len(start)

        meetings = []

        for i in range(n):
            meetings.append((end[i], start[i]))

        meetings.sort()

        cnt = 1
        lastEnd = meetings[0][0]

        for i in range(1, n):
            if meetings[i][1] > lastEnd:
                cnt += 1
                lastEnd = meetings[i][0]

        return cnt
