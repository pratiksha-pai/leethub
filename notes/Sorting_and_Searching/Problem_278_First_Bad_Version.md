# First Bad Version

[Problem Link](https://leetcode.com/problems/first-bad-version/)

## Notes
- learn how to use binary search 
while start <= end:
    mid = (start + end) // 2
    if isBadVersion(mid):
        end = mid - 1
    else:
        start = mid + 1 

is this better than while start < end? and mid = (start + end + 1) // 2 ? why?

