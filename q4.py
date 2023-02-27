import collections

a = input()
nums = input()
# print(nums)
exit = collections.defaultdict(int)
ans = 0
nums = list(map(int, nums.strip().split()))
nums.sort(reverse=True)

for n in nums:
    if exit[n] < 1:
        ans += n
        exit[n] += 1
    else:
        for i in range(n-1, 0, -1):
            if exit[i] < 1:
                ans += i
                exit[i] += 1
                break
print(ans)
