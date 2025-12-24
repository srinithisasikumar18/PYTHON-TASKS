
# # Day-3-----Multi-User Shopping Cart Billing


# num=int(input("enter the no of customers: "))
# cart=[]
# for i in range(1,num+1):
#       customer=[]
#       while (True):
#          items=int(input(f"enter the cart items of {i} customer: "))
#          if items==0:
#             break
#          (customer.append(items))
#       cart.append(customer)
# totals = []
# for customer in cart:
#       totals.append(sum(customer))
# #    # return
# # def dis(totals,discount)
# #       final_lis=[]
#       for total in totals: 
#          if total >= 5000:
#             return (total-(total/100)*discount)
#          elif total > 1000:
#             return (total-(total/100)*discount)
#          elif total > 500:
#             return (total-(total/100)*discount)
#          else:
#             return totals
# dis(totals,20)

      


num=int(input("enter the no of customers: "))
cart=[]
for i in range(1,num+1):
    customer=[]
    while True:
        items=int(input(f"enter the cart items of {i} customer: "))
        if items==0:
            break
        customer.append(items)
    cart.append(customer)

totals=[]
for customer in cart:
    totals.append(sum(customer))

discount=20
final_lis=[]

for total in totals:
    if total>=5000:
        final_lis.append(total-(total/100)*discount)
    elif total>1000:
        final_lis.append(total-(total/100)*discount)
    elif total>500:
        final_lis.append(total-(total/100)*discount)
    else:
        final_lis.append(total)
   
print(final_lis)




n=[[100,400,127],
[450,600],
[127,128,57,600],[0,1,6/900],[2500,2500]
]
output=[]
for i in n:
    total=sum(i)
    if total>0 and total<500:
        output.append(total)
    elif total>500 and total<1000:
        discount=total/100*5
        total_price=total-discount
        output.append(total_price)
    elif total>1000 and total<5000:
        discount1=total/100*15
        total_price=total-discount1
        output.append(total_price)
    elif total>=5000:
        discount2=total/100*20
        total_price=total-discount2
        output.append(total_price)
    else:
        print("none")
print(output)

