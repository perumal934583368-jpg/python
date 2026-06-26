"""l=[1,2,3,4,5]
print(l)
l.clear()
print(l)
l=[1,2,3,4,5]
print()
print(l.copy())"""
"""l=[1,2,3,4,5]
print(l)
l.append(6)
print(l)
print(l.count(5))
l.extend([7,8,9,10])
print(l)"""
#( 2 largest number)
"""n1=int(input("enter first largest number:"))
n2=int(input("enter second largest number:"))
n3=int(input("enter third largest number:"))
numbers=[n1,n2,n3]
numbers.sort()
print("second largest number:",numbers[-2])"""
"""(highest value)
l=[]
n=int(input("enter length:"))
for i in range(n):
    elements=int(input("enter your elements:"))
    l.append(elements)
print(l)
highest=l[0]
for j in l:
    if j>highest:
     highest=j
print("high value",highest)"""
("2 highest value")
"""l=[]
n=int(input("enter length:"))
for i in range(n):
    elements=int(input("enter elements:"))
    l.append(elements)
print(l)
highest=l[0]
second=l[0]
for i in l:
    if i>highest:
        highest=i
for j in l:
    if j>second and j!=highest:
        second=j
print("highest value:",highest)
print("second highest value:",second)"""
l=[]
n=int(input("enter length:"))
for i in range(n):
    elements =int(input("enter elements:"))
    l.append(elements)
print(l)
highest=l[0]
smallest=l[0]
for i in l:
    if i>highest:
        highest=i
for j in l:
    if j<smallest:
        smallest=j
print("highest value:",highest)
print("smallest value:",smallest)


    




