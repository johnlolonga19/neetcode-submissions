class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]
        answer = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                answer += left_max - height[left]
                left += 1

            else:
                right_max = max(right_max, height[right])
                answer += right_max - height[right]
                right -= 1

        return answer

        
        