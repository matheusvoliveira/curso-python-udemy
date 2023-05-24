def create_cubs(n):
    for x in range(n):
        yield x**3 #yield ele é capaz de output um valor sem gastar valor na memoria, não precisa estar dentro de uma lista

for x in create_cubs(10):
    print(x)





def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)



def get_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+c
