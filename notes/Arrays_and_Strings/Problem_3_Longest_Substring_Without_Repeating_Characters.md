# Longest Substring Without Repeating Characters

[Problem Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Notes
- this approach is called sliding window
- track the start, ex abba 
- _len start with 0 not 1, ex ""
- we need a _len and max_len, because we need to track the stream of continous non repeating chars
- max_len cannot handle this stream because _len has to reset to curr_index - start when it sees a repeating char
- i am getting 60% faster than other python3 submissions why?

## NEED TO REVIEW