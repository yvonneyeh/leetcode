# 347. Top K Frequent Elements

"""
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution:


    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:

        # Time: O(NlogN)
        # Space: O(N)
        #
        # Build a frequency dictionary - invert the sign of the frequency (-ve frequency serves as priority key for the heap later)
        # Push all (item, -ve freq) pairs into heap
        # Pop k items from heap and append to a result list
        # return list

        if not nums:
        	return []

        if len(nums) == 1:
        	 return nums[0]

        # first find freq - freq dict
        d = {}
        for num in nums:
        	if num in d:
        		d[num] -= 1 # reverse the sign on the freq for the heap's sake
        	else:
        		d[num] = -1

        h = []
        from heapq import heappush, heappop
        for key in d:
        	heappush(h, (d[key], key))

        res = []
        count = 0
        while count < k:
        	frq, item = heappop(h)
        	res.append(item)
        	count += 1
        return res


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    # keep track of count of each num in dictionary
    # using a list with len = k + 1, keep track of count of nums with each count
    # iterate through list backwards to find most frequent count of num

        counts = {}
        frequency = [[] for i in range(len(nums)+1)]
        result = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            frequency[count].append(num)


        for i in range(len(frequency)-1, 0, -1): # last index, to zero, descending order
            for n in frequency[i]:
                result.append(n)
            if len(result) == k:
                return result

    # O(n)
