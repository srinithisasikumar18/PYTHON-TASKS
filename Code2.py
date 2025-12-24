# candies=[4, 2, 1, 1, 2] 
# new_candies=[]
# extra_candies=int(input("enter: " ))
# output=[]
# for i in candies:
#     a=i+extra_candies
#     # print(a)
#     new_candies.append(a)
# print(new_candies)
# b=max(candies)
# for j in new_candies:
#     if j>=b:
#         output.append("true")
#     else:
#         output.append("false")
# print(output)


li = [1,3,4,6,4,2]
add_can = 2
li_sec = {}
for i in li:
    if i+add_can >= max(li):
        li_sec[i]= "True"
    # else:
    #     li_sec[i]="False"
print(li_sec)