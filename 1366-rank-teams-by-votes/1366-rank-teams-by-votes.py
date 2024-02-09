class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        mp = {team:[0] * n for team in votes[0]}
        
        for vote in votes:
            for i, team in enumerate(vote):
                mp[team][i] -= 1
        
        items = sorted(mp.items(), key= lambda x:(x[1], x[0]))
        
        return "".join(item[0] for item in items)