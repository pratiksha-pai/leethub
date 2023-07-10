import os
import codecs

problems = {
    "Arrays and Strings": [
        {"title": "Two Sum", "url": "https://leetcode.com/problems/two-sum/", "id": 1},
        {"title": "Container With Most Water", "url": "https://leetcode.com/problems/container-with-most-water/", "id": 11},
        {"title": "3Sum", "url": "https://leetcode.com/problems/3sum/", "id": 15},
        {"title": "Longest Substring Without Repeating Characters", "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "id": 3},
    ],
    "Linked Lists": [
        {"title": "Add Two Numbers", "url": "https://leetcode.com/problems/add-two-numbers/", "id": 2},
        {"title": "Reverse Linked List", "url": "https://leetcode.com/problems/reverse-linked-list/", "id": 206},
        {"title": "Linked List Cycle", "url": "https://leetcode.com/problems/linked-list-cycle/", "id": 141},
    ],
    "Trees": [
        {"title": "Maximum Depth of Binary Tree", "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/", "id": 104},
        {"title": "Validate Binary Search Tree", "url": "https://leetcode.com/problems/validate-binary-search-tree/", "id": 98},
        {"title": "Binary Tree Inorder Traversal", "url": "https://leetcode.com/problems/binary-tree-inorder-traversal/", "id": 94},
    ],
    "Stacks and Queues": [
        {"title": "Valid Parentheses", "url": "https://leetcode.com/problems/valid-parentheses/", "id": 20},
        {"title": "Implement Queue using Stacks", "url": "https://leetcode.com/problems/implement-queue-using-stacks/", "id": 232},
        {"title": "Implement Stack using Queues", "url": "https://leetcode.com/problems/implement-stack-using-queues/", "id": 225},
    ],
    "Graphs": [
        {"title": "Clone Graph", "url": "https://leetcode.com/problems/clone-graph/", "id": 133},
        {"title": "Number of Islands", "url": "https://leetcode.com/problems/number-of-islands/", "id": 200},
        {"title": "Course Schedule", "url": "https://leetcode.com/problems/course-schedule/", "id": 207},
    ],
    "Sorting and Searching": [
        {"title": "Merge Sorted Array", "url": "https://leetcode.com/problems/merge-sorted-array/", "id": 88},
        {"title": "First Bad Version", "url": "https://leetcode.com/problems/first-bad-version/", "id": 278},
        {"title": "Find Peak Element", "url": "https://leetcode.com/problems/find-peak-element/", "id": 162},
    ],
    "Dynamic Programming": [
        {"title": "Climbing Stairs", "url": "https://leetcode.com/problems/climbing-stairs/", "id": 70},
        {"title": "Coin Change", "url": "https://leetcode.com/problems/coin-change/", "id": 322},
        {"title": "Longest Increasing Subsequence", "url": "https://leetcode.com/problems/longest-increasing-subsequence/", "id": 300},
    ],
    "Design Problems": [
        {"title": "LRU Cache", "url": "https://leetcode.com/problems/lru-cache/", "id": 146},
        {"title": "Implement Trie (Prefix Tree)", "url": "https://leetcode.com/problems/implement-trie-prefix-tree/", "id": 208},
        {"title": "Design Add and Search Words Data Structure", "url": "https://leetcode.com/problems/design-add-and-search-words-data-structure/", "id": 211},
    ],
}

for category, problem_list in problems.items():
    category_dir = category.replace(" ", "_")  # replace spaces with underscores
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)  # create directory if it doesn't exist

    for problem in problem_list:
        # Use problem id and title for unique filename
        filename = f"{category_dir}/Problem_{problem['id']}_{problem['title'].replace(' ', '_')}.md"

        with codecs.open(filename, 'w', 'utf-8') as f:
            f.write(f"# {problem['title']}\n")
            f.write(f"\n[Problem Link]({problem['url']})\n")
            f.write("\n## Notes\n")