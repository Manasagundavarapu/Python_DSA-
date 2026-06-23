class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ansList = []

        def findSubsets(ind, ds):
            ansList.append(ds[:])

            for i in range(ind, len(nums)):

                if i != ind and nums[i] == nums[i - 1]:
                    continue

                ds.append(nums[i])
                findSubsets(i + 1, ds)
                ds.pop()

        findSubsets(0, [])

        return ansList
