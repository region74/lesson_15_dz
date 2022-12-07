import random

a = [1, 3, 4, 5, 6, 7, '3', '#', '#', '#']
# random.shuffle(a)
print(a)
c = 3
b = a.index(c)
print(b)

count = 0
for item in a:
    if str(item).isdigit():
        count += 1

print(count)
b=a[0:2]+a[2:4]
print(b)
