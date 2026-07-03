#without arqument
"""def demo():
    print("in a function")
    print("in a function")
    print("in a function")
demo()"""
"""def demo():
    return "hello world"
print(demo())"""
#with arqument
#without return
"""def add(a,b):
    print(a+b)
add(20,30)"""
#with return
"""def sub(a,b):
    return(a-b)
print(sub(10,20))"""
#default arqument
"""def details(name="anu",age=23):
    print("name",name)
    print("age",age)
details"""
#with return
"""def details(name="anu",age=23):
    return "name:",name,"age:",age
print(details())"""
#with return second method
"""def details(name="anu",age=23):
    s=f"name:{name}\n age:{age}"
    return s
print(details("varsha",23))"""
#key word value arqument
#with out return
"""def values(*a):
    print(*a)
values(f"anu",20,"salem","height",5.68)"""
#with return
"""def values(*a):
    return a
print(values("anu",20,"salem"))"""
#2.key word value arbitary
"""def details(**a):
    print(a)
details(name="anu",age=23,address="salem")"""
"""def details (**a):
    for i,j,in a.items():
     print(i,":",j)
details(name="anu",age=21,address="salem",gender="female")"""
#with return
"""def details(**a):
    return a
print(details(name="anu",age=23,address="salem",))"""




















