class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ele=1
        for i in range(len(nums)):
            if(count==0):
                count=1
                ele=nums[i]
            elif(nums[i]==ele):
                count+=1
            else:
                count-=1
        cnt=0
        for i in range(0,len(nums)):
            if nums[i]==ele:
                cnt+=1
        if(cnt>len(nums)//2):
            return ele
        return -1
