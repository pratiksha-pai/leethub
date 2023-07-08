import os
import codecs

problems = {
    "Arrays and Strings": [
        {"title": "Two Sum", "url": "https://leetcode.com/problems/two-sum/", "id": 1},
        {"title": "Container With Most Water", "url": "https://leetcode.com/problems/container-with-most-water/", "id": 11},
        {"title": "3Sum", "url": "https://leetcode.com/problems/3sum/", "id": 15},
        {"title": "Longest Substring Without Repeating Characters", "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "id": 3},
    ],
    # Add the rest of the problems here, following the same format
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