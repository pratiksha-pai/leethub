# Container With Most Water

[Problem Link](https://leetcode.com/problems/container-with-most-water/)

## Notes
- approach of keeping track of max_from_left and max_from_right is wrong, ex [1 2 4 3],here 2,3 and distance between them is 2 is better than 2,4 and distance between them is 1
- the correct approach is to keep track of the max_area
- the max_area is the min of the two heights * the distance between them
- even storing the max_from_left and max_from_right indexes does not work since i can montonically increasing and then monotonically decreasing, you are now essentially storing n values (both arrays) and for loop becomes O(n^2)
- better way is to start from both ends and move the pointer that has the smaller height
- why do we not need to consider all starts and all ends? the n2 solution is not required. consider the areas betweem two pillars, these hold some weight (LLM!!!? no) and max_area is like a composite of all these areas, but consecutively, so max area is where these individual areas are max. its like max_area is pulled towards these places and they are kinda (?) simulated when we move the pointers away from smaller height - i dont know what im ssaying
- 46% after soooooo long, need a better solution

## NEED TO REVIEW