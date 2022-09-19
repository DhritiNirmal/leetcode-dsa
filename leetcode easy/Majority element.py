"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

#brute force
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
              
              
#hashmap
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
      

#sorting
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
      
      
#divide and conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count_max = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == nums[0]:
                count+=1
                if count>count_max:
                    count_max = count
                    num_max = nums[i]
            else:
                nums[0] = nums[i]
                count =1 
        return num_max
      

#boyer moore voting algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
      

