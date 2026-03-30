class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = deque([])
        postfix = deque([])
        cur_pre = 0
        cur_post = 0
        res = 0

        for i in range(len(height)):
            prefix.append(cur_pre)
            cur_pre = max(cur_pre, height[i])
        
        for j in range(len(height)-1, -1, -1):
            postfix.appendleft(cur_post)
            cur_post = max(cur_post,height[j])
        
        for index, val in enumerate(height):
            cur = min(prefix[index], postfix[index])-val
            if cur>0:
                res+=cur
        
        return res