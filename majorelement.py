class Solution:
    def majorityElement(self, nums):
        # 1st pass: find candidates
        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # 2nd pass: verify candidates
        result = []
        for c in (cand1, cand2):
            if c is not None and nums.count(c) > len(nums) // 3:
                result.append(c)

        return result
