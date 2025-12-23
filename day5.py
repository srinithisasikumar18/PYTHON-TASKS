
# Longest Subarray with Equal 0's and 1's

nums = [1, 1, 0, 0, 1] 
new_nums=[] 
sum_=0
count_=0
li_sum=[]
for i in nums:
    if i==0:
        new_nums.append(-1)
    else:
        new_nums.append(i)
print(new_nums)
print(len(nums)-sum(new_nums))

# # nums = [0,1,0]
# # li=[]
# # one_count=0
# # zero_count=0
# # for i in nums:
# #     if i==1:
# #         one_count+=1
# #     else:
# #         zero_count+=1
# # li.append(one_count)
# # li.append(zero_count)
# # print(li)
# # sum=0
# # s=min(li)
# # print(s*2)


# li = [1,0,1,0,1,1,1]

# # one = li.count(1)
# # zero = li.count(0)
# print(min(li.count(1),li.count(0))*2)