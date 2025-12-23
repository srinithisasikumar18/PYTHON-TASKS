cart=[[100,400,127],   
      [450,600],
      [0,1,3],
      [2500,2500],
      [127,128,57,600]]
total_price=[]
dis_price=[]
for i in cart:
    total_price.append(sum(i))
for i in total_price:
    if i<500:
        dis_price.append(i)
    if i>=500 and i<1000:
        dis_price.append(i-(i/100)*5)
    elif (i>=1000) and i<5000:
        dis_price.append(i-(i/100)*15)
    elif (i>=5000):
        dis_price.append(i-(i/100)*20)   
print(dis_price)



# total_price=[]
# discount_price=[]
# for total in cart:
#     total_price.append(sum(total))
# def dis(discount):
#     for i in total_price:
#         # print(i)
#         if i<500:
#             discount_price.append(i)
#         elif i>=500 and i<1000:
#             discount_price.append(i-((i/100)*discount))
#         elif i>=1000 and i<5000:
#             discount_price.append(i-((i/100)*discount))
#         elif i>=5000:
#             discount_price.append(i-((i/100)*discount))
#     print(discount_price)
# (dis(5))
# (dis(10))
# (dis(15))


# cart=[[100,400,127],   
#       [450,600],
#       [0,1,3],
#       [2500,2500],
#       [127,128,57,600]]
# total_price=[]
# dis_price=[]

# def dic(discount):
#     for i in cart:
#         total=print(sum(i))
#         if total>500 and total<1000:
#             return dis_price.append(total-(total/100)*discount)
#         elif total>1000 and total<5000:
#             return dis_price.append(total-(total/100)*discount)
#         return dis_price
# print(dic(5))


# cart=[[100,400,127],   
#       [450,600],
#       [0,1,3],
#       [2500,2500],
#       [127,128,57,600]]
# for i in  cart:
#     total=0
#     for j in i:
#       total+=j
#       print(total)



li=[]
n=int(input("enter total customers: "))
for i in range(1,n+1):
    cus=[]
    le=(int(input(f"enter the length of {i}  customer: ")))
    for j in range(le):
            
      items=int(input(f"enter the {i} items prices: "))
      cus.append(items)
      li.append(cus)
print(li)  