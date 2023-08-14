# Создайте функцию генератор чисел Фибоначчи

def fibo_generator(num):
    x, y = 0, 1
    for i in range(num):
        yield y
        x, y = y, x + y
       
num = 10
print(list(fibo_generator(num)))



# def fibo_generator():
#     x, y = 0, 1
#     while True:
#         yield y
#         x, y = y, x + y
    

# num = fibo_generator()
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))



