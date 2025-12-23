# --------------------
# def arr():
#    num=int(input("enter the no of customers: "))
#    cart=[]
#    for i in range(1,num+1):
#       customer=[]
#       le=int(input(f"enter the lenght for {i} customer: "))
#       for j in range(le):
#          items=int(input("enter the cart items: "))
#          customer.append(items)
#       cart.append(customer)
#    for i in cart:
#       print(sum(i))
#    return cart
# print(arr())


def arr():
   num=int(input("enter the no of customers: "))
   cart=[]
   for i in range(1,num+1):
      customer=[]
      while (True):
         items=int(input(f"enter the cart items of {i} customer: "))
         if items==0:
            break
         (customer.append(items))
      cart.append(customer)
   totals = []
   for customer in cart:
      totals.append(sum(customer))
   # return
   def dis(totals,discount):
      final_lis=[]
      for total in totals: 
         if total >= 5000:
            return (total-(total/100)*discount)
         elif total > 1000:
            return (total-(total/100)*discount)
         elif total > 500:
            return (total-(total/100)*discount)
         else:
            return totals
   dis(totals,20)
print(arr())
      
# def arr():
#     num = int(input("enter the no of customers: "))
#     cart = []

#     for i in range(1, num+1):
#         customer = []
#         while True:
#             items = int(input(f"enter the cart items of {i} customer (0 to stop): "))
#             if items == 0:
#                 break
#             customer.append(items)
#         cart.append(customer)

#     totals = []
#     for customer in cart:
#         totals.append(sum(customer))

#     # discount function
#     def dis(total):
#         if total >= 5000:
#             return total - (total * 20 / 100)
#         elif total > 1000:
#             return total - (total * 15 / 100)
#         elif total > 500:
#             return total - (total * 10 / 100)
#         else:
#             return total

#     # Apply discount for each customer
#     final_amounts = []
#     for total in totals:
#         final_amounts.append(dis(total))

#     return final_amounts


# print(arr())

# def arr():
#     num = int(input("Enter the number of customers: "))
#     cart = []

#     for i in range(1, num + 1):
#         customer = []
#         print(f"\nEnter items of Customer {i} (0 to stop):")
#         while True:
#             item = int(input("Enter item price: "))
#             if item == 0:
#                 break
#             customer.append(item)

#         cart.append(customer)

#     # Individual totals for every customer



# print(arr())


# def append_items_price(User: int, size: int) -> list:
#     li = []
#     print(f"_____________________Enter {User} user items price : ______________________")
#     i = 0
#     while i < size:
#         li.append(int(input(f"Enter {i + 1} Item price : ")))
#         i += 1
#     return li


# def make_dis(total: int, dis: int) -> float:
#     return total - (total * dis / 100)


# de*f log(li: list) -> float:
#     temp_sum = sum(li)
#     if temp_sum >= 5000:
#         return make_dis(temp_sum, 20)
#     elif temp_sum > 1000:
#         return make_dis(temp_sum, 15)
#     elif temp_sum > 500:
#         return make_dis(temp_sum, 5)
#     else:
#         return temp_sum


# # ---------- START ----------
# num_users = int(input("Enter number of users : "))

# items_size = []
# i = 1
# while i <= num_users:
#     size = int(input(f"Enter the Cart items Size of User_{i} : "))

#     # ✅ EXIT CONDITION
#     if size == 0:
#         print("Cart size is 0. Exiting program...")
#         exit()

#     items_size.append(size)
#     i += 1


# total_users_cart_list = []
# user = 1
# while user <= len(items_size):
#     cart = append_items_price(User=user, size=items_size[user - 1])
#     total_users_cart_list.append(cart)
#     user += 1


# final_cart_after_discount = []
# i = 0
# while i < len(total_users_cart_list):
#     final_cart_after_discount.append(log(total_users_cart_list[i]))
#     i += 1


# print("____________________Total Bill Amount_______________________")
# i = 0
# while i < len(final_cart_after_discount):
#     print(f"{i + 1} User total price : {final_cart_after_discount[i]} RS")
#     i += 1         




# def append_items_price(User:int,size:int)->list:
#     li = []
#     print(f"_____________________Enter {User} user  items price : ______________________")
#     for _ in range(size):
#         li.append(int(input(f"Enter {_ + 1} Item price : ")))
#     return li

# def make_dis(total:int,dis:int)->float:
#     temp_dis_value = total*(dis/100)
#     return total - temp_dis_value

# def log(li:list)->float:
#     temp_sum = sum(li)
#     if temp_sum >= 5000:
#         final_total = make_dis(total=temp_sum,dis=20)
#     elif temp_sum > 1000:
#         final_total = make_dis(total=temp_sum,dis=15)
#     elif temp_sum > 500:
#         final_total = make_dis(total=temp_sum,dis=5)
#     else:
#         final_total = temp_sum
#     return final_total
    

# #start here
# num_Users = int(input("Enter number of users : "))

# items_size = []
# for i in range(1,num_Users+1):
#     temp = int(input(f"Enter the Cart items Size of User_{i} : "))
#     items_size.append(temp)

# total_users_cart_list = []
# for user,size in enumerate(items_size):
#     temp = append_items_price(User=user+1,size=size)
#     total_users_cart_list.append(temp)

# final_cart_after_discount = []

# for user_cart in total_users_cart_list:
#     temp = log(li=user_cart)
#     final_cart_after_discount.append(temp)

# print("____________________Total Bill Amount_______________________")
# for user,total_price in enumerate(final_cart_after_discount):
#     print(f"{user+1} User total price : {total_price} RS")

# # print(final_cart_after_discount)

























   

# # def append_items_price(User:int,size:int)->list:
# #     li = []
# #     print(f"_Enter {User} user  items price : ______________________")
# #     for _ in range(size):
# #         li.append(int(input(f"Enter {_ + 1} Item price : ")))
# #     return li

# # def make_dis(total:int,dis:int)->float:
# #     temp_dis_value = total*(dis/100)
# #     return total - temp_dis_value

# # def log(li:list)->float:
# #     temp_sum = sum(li)
# #     if temp_sum >= 5000:
# #         final_total = make_dis(total=temp_sum,dis=20)
# #     elif temp_sum > 1000:
# #         final_total = make_dis(total=temp_sum,dis=15)
# #     elif temp_sum > 500:
# #         final_total = make_dis(total=temp_sum,dis=5)
# #     else:
# #         final_total = temp_sum
# #     return final_total
    

# # #start here
# # num_Users = int(input("Enter number of users : "))

# # items_size = []
# # i = 1
# # while i <= num_Users:
# #     size = int(input(f"Enter the Cart items Size of User_{i} : "))
# #     if size == 0:
# #         print("Cart size is 0. Exiting program...")
# #     i += 1  
# #     items_size.append(size)
    

# # total_users_cart_list = []

# # for user,size in enumerate(items_size):
# #     temp = append_items_price(User=user+1,size=size)
# #     total_users_cart_list.append(temp)

# # final_cart_after_discount = []

# # for user_cart in total_users_cart_list:
# #     temp = log(li=user_cart)
# #     final_cart_after_discount.append(temp)

# # print("_Total Bill Amount")
# # for user,total_price in enumerate(final_cart_after_discount):
# #     print(f"{user+1} User total price : {total_price} RS")

# # print(final_cart_after_discount)