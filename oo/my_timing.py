import pdb
from time import time
# mostra o tempo que a função demora pra executar
from timeit import timeit
#timeit é parecido com time
start_time = time()
def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))

func_two(1000000)

end_time = time()
func_two(10)

elapsed_time = end_time - start_time
# print(elapsed_time)


stm = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit(stm, setup, number=10000))

pdb.set_trace()