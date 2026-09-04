class Solution:

    def twosum(self, arr, target):
        seen = {}

        for i in range(len(arr)):
            if(target - arr[i] in seen):
                return [seen[target - arr[i]], i]
            seen[arr[i]] = i
        return [-1, -1]

    
arr = [2, 7, 11, 15]
target = 18

s = Solution()
ans = s.twosum(arr, target)

print(ans)