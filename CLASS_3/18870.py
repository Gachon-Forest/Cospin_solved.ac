n=int(input())
nums=list(map(int,input().split()))
sort_nums=sorted(set(nums))
num_dict={num:i for i, num in enumerate(sort_nums)}
compressed_nums=[num_dict[num] for num in nums]
print(*compressed_nums)