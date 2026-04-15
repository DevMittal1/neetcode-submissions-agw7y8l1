class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        arr = [[] for i in range(len(nums)+1)]
        for i, j in dict1.items():
            arr[j].append(i)
        last_arr = []
        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                last_arr.append(n)
                if len(last_arr)==k:
                    return last_arr
        