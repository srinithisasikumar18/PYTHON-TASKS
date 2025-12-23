import random
def otp(n):
    # n=int(input("Enter the Number of times OTP to be Occured: "))
    otp_li=[]
    for i in range(1,n+1):
        otp=random.randint(1000,9999)
        otp_li.append(otp)
    print("OPT's:",otp_li)
    print("Non repeated OTP's",list(set(otp_li)))
otp(10)

# n=int(input("Enter the Number of times OTP to be Occured: "))
# otp_li=[]
# for i in range(1,n+1):
#     otp=random.randint(1000,9999)
#     otp_li.append(otp)
# print("OPT's:",otp_li)
# print("Non repeated OTP's",list(set(otp_li)))




# first_count=0
# for j in otp_li:
#     first_count+=1
# print(first_count)

# for s in otp_li:
#     if otp_li.count(s)>1:
#         otp_li.remove(s)
# print(otp_li)

# second_count=0
# for m in otp_li:
#     second_count+=1
# print(second_count)
