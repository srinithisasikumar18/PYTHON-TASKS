accounts=[[1,2,3],
        [3, 2, 1]] 
sum_=[]
for i in accounts:
    sum_.append(sum(i))
richest_wealth=max(sum_)
print("Customer Wealth",richest_wealth)



def richest_wealth(li):
    _max=0
    _sum=[]
    for i in li:
        _sum.append(sum(i))
        wealth=max(_sum)
    return wealth
li1=[
    [ 2, 1,33],
    [1,2,3,4]
]
li2=[
 [1, 5],
 [7, 3],
 [3, 5]
] 
print("Customer Wealth",richest_wealth(li1))
print("Customer Wealth",richest_wealth(li2))


