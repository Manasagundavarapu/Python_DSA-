class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        j=0

        for ele in pushed:
            stack.append(ele)

            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return len(stack)==0
