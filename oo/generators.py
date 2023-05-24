def create_cubs(n):
    for x in range(n):
        yield x**3

for x in create_cubs(10):
    print(x)
