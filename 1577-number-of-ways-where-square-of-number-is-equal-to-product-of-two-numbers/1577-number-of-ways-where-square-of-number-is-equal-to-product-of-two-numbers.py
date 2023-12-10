class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        from collections import defaultdict
        
        squares_nums1 = defaultdict()
        squares_nums2 = defaultdict()
        products_nums1 = defaultdict()
        products_nums2 = defaultdict()
        
        count = 0 
        for i in range(len(nums1)):
            idx =  nums1[i] ** 2
            if idx in squares_nums1:
                squares_nums1[idx] += 1
            else:
                squares_nums1[idx] = 1
        
        for i in range(len(nums2)):
            idx = nums2[i] ** 2
            if idx in squares_nums2:
                squares_nums2[idx] += 1
            else:
                squares_nums2[idx] = 1
        
        for i in range(len(nums1)):
            for j in range(i):
                idx = nums1[i] * nums1[j]
                if idx in products_nums1:
                    products_nums1[idx] += 1
                else:
                    products_nums1[idx] = 1
        
        for i in range(len(nums2)):
            for j in range(i):
                idx = nums2[i] * nums2[j]
                if idx in products_nums2:
                    products_nums2[idx] += 1
                else:
                    products_nums2[idx] = 1
        
        
        for k, v in squares_nums1.items():
            if k in products_nums2:
                count += squares_nums1[k] * products_nums2[k]
        
        for k, v in squares_nums2.items():
            if k in products_nums1:
                count += squares_nums2[k] * products_nums1[k]
        
        
        return count