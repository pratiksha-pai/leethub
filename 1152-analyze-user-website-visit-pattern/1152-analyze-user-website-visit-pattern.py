class Solution:
    def mostVisitedPattern(self, usernames: List[str], timestamps: List[int], websites_list: List[str]) -> List[str]:
        
        website_for_user = defaultdict(list)
        for _, username, website in sorted(zip(timestamps, usernames, websites_list), key=lambda x: x[0]):
            website_for_user[username].append(website)
        
        patterns = defaultdict(set)
        for username, websites in website_for_user.items():
            combs = set(combinations(websites, 3))
            for comb in combs:
                patterns[tuple(comb)].add(username)
        
        max_pattern, max_len = (), 0
        for pattern, users in patterns.items():
            if len(users) > max_len or len(users) == max_len and pattern < max_pattern:
                max_pattern, max_len = pattern, len(users)
        
        return list(max_pattern)