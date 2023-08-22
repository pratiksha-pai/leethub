class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        from collections import Counter
        
        counter = Counter(hand)
        # print(counter)
        
        for key in sorted(counter):
            count = counter[key]
            
            if count > 0:
                for i in range(1, gs):
                    curr_key = key+i
                    if curr_key not in counter:
                        return False
                    if counter[curr_key] < count:
                        return False
                    counter[curr_key] -= count

                counter[key] = 0
        
        
        return True
        