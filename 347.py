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


        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]:
                result.append(n)
            if len(result) == k:
                return result

    # O(n)
