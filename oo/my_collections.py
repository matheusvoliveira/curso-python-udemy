from collections import Counter
from collections import namedtuple

mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]

print(Counter(mylist))



mylist = ['a', 'a', 10,10,10]
print(Counter(mylist))

sentence = 'how many times does each word show yo up in this sentence with a word'
print(Counter(sentence.split()))

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
# namedTuple é como se fosse uma classe porem é uma tupla
sammy = Dog(5, 'Husky', 'Sam')

print(sammy)

