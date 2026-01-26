a = 0
b = 1
lst = []
for _ in range(1, 11):
    a, b = b, a+b
    lst.append(a)
print(lst)