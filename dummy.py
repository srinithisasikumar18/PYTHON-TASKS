# # iuoooooooooiu0
# employees=[
#     {'eid':101,'ename':'raju','gender':'M'},
#     {'eid':102,'ename':'soniya','gender':'F'},
#     {'eid':103,'ename':'priyanka','gender':'F'},
#     {'eid':104,'ename':'modi','gender':'M'},
# ]
# for emp in employees:
#     # emp.update({"gender"}{"M":"male","F":"female"})
#     # print(emp["ename"],emp["gender"])
#     emp.update[]

emp=[
    {'eid':101,'ename':'raju','gender':'M'},
    {'eid':102,'ename':'soniya','gender':'F'},
    {'eid':103,'ename':'priyanka','gender':'F'},
    {'eid':104,'ename':'modi','gender':'M'},
]
for em in emp:
    if em['gender']=="M":
        em['gender']="Male"
    if em['gender']=="F":
        em['gender']="Female"

    print(em["ename"],"=",em["gender"])