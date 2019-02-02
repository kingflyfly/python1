def count(n):
    print("counting:")
    while n > 0:
        yield n
        n -= 1
for i in count(5):
    print(i)