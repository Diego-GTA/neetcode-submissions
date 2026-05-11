class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = sorted(enumerate(nums), key=lambda x: x[1])
        lp, rp = 0, len(n) - 1
        while lp < rp:
            sum = n[lp][1] + n[rp][1]
            if sum == target:
                return sorted([n[lp][0] , n[rp][0]])
            elif sum > target:
                rp -= 1
            else:
                lp += 1