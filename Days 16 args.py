# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i

#     print(sum)    



# addition(12,52,4,525,4,45,45,) 


# kwargs

def information(**kwargs):
    print("your information is\n\n ")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")


information(name = "Anuj",age = 23,designation = "DA")        



