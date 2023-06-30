import sys
import string
import timeit
import hashlib
import pickle
import random
import collections
import heapq
import math

# -------------------------------------------------------------------------------------------
# Usage of zip function
seq1 = [1,23,4,5]
seq2 = [1,2,3,4]

def do_something_with(*argv):
    print([*argv])

for items in zip(seq1,seq2):
  do_something_with(*items)

# -------------------------------------------------------------------------------------------
# all Characters in one place
print("string.ascii_letters")
print(string.ascii_letters)
print("string.ascii_lowercase")
print(string.ascii_lowercase)
print("string.ascii_uppercase")
print(string.ascii_uppercase)
print("string.digits")
print(string.digits)
print("string.hexdigits")
print(string.hexdigits)
print("string.octdigits")
print(string.octdigits)
print("string.printable")
print(string.printable)
print("string.punctuation")
print(string.punctuation)
print("string.whitespace")
print(string.whitespace)

# Using Slicing Operator in strings to reverse, split, and substring
phrase='Mary had a little Lamb'

# slicing operator has a ternary form [i:j:k], where k=1 is the step
print(phrase,phrase[::2],phrase[1::2],sep='\n')

# Reverse and split the string
print(phrase[::1], phrase[::-1], sep='|')

 # Same as phrase[-1::-2], phrase[-2::-2]
print(phrase[::-2], phrase[-2::-2], sep='\n')

# Beware of large and slow ints
maxVal = sys.maxsize
print(maxVal)

# all integer arithmetic operations produce precise integer results, but floating-point operations are approximate.
# So use floating-points for speed
print(10 ** 100 * 10 ** 100) # Integer, precise
print(10. ** 100 * 10. ** 100) # Floating-point, approximate
print(timeit.timeit('10**100 * 10**100'))
print(timeit.timeit('10.**100 * 10.**100'))

# -------------------------------------------------------------------------------------------

# Function Tips

# Always return something

# Return Consistently
#  -> If we assume that a valid result is as common as a failure, we choose a sentinel with the same type as the valid result but whose value is never valid.
#  -> If we can’t choose a proper sentinel or we’re assured that failures are rare, we let the function signal them by raising an exception.
# yield don't return
"""
  A generator is an object that, when asked, lazily produces one item at a time. From a caller’s perspective, 
  it looks like a function with internal memory that remembers where it stopped after returning the previous result 
  and resumes from the next line; seemingly impossible.
  
  Generator functions remember their internal state between calls and can produce long (possibly infinite) iterables on demand, one item at a time. The latter is important if we process large amounts of data but have limited memory.
"""
def fortune_teller(attempts=2):
  for _ in range(attempts):
    yield bool(random.randint(0, 1)) 
  return 'Do not call me again!'

oracle = fortune_teller(2) # The generator created 
print(next(oracle))
# call it again
print(next(oracle))
# the generator raises a StopIteration that we can handle
# But by providing the fallback value and doesn’t raise the exception.
print(next(oracle,True))

# -------------------------------------------------------------------------------------------
# cache it

source = 'https://lj-dev.livejournal.com/653177.html' 
hash = hashlib.sha256(source.encode())
filename = hash.hexdigest()
print(hash, filename)

cache = f'cache/{filename}.p' 
try:
  with open(cache, 'rb') as infile:
      # Has been pickled before! Simply unpickle 
      object = pickle.load(infile)
except FileNotFoundError:
    # Download and pickle
    object = 'https://lj-dev.livejournal.com/653177.html' 
    with open(cache, 'wb') as outfile:
      pickle.dump(outfile, object) 
except:
    # Things happen...
    pass
  
# Tips on Sorting
# if our list is large, sort it in place with list.sort(). If our list is moderately sized or needs to preserve the original order, call sorted() and retrieve a sorted copy.

# Importing based on conditions
# try:
#     import cPickle as pickle
# except ImportError: 
#     import pickle

# Formatted Strings
name = 'Mary'
print('Hello, ' + str(name) + ', how is your lamb?')
print(f'Hello, {name}, how is your lamb?')
# -------------------------------------------------------------------------------------------
# Math
math.hypot(10,10) # arguments should be x1-x2 and y1-y2
math.dist([10,12],[21,12]) # arguments should be list with size 2
# works for python > 3.11.*
n = 10
k = 3
math.comb(n,k) 
math.perm(n,k)
# -------------------------------------------------------------------------------------------
# Data Structures

## List
lisItems = [1,2,3]
lisItems.reverse()
lisItems.append(10)
lisItems.pop()

### Stack
stack = []
stack.append(10)
stack.pop()

## deque
queue = collections.deque()
queue.append(10) # append from back
queue.popLeft()  # dequeues from front

## Heap
minHeap = [1,2,3,4]
heapq.heapify(minHeap)
heapq.heappush(minHeap, 10)
heapq.hea

## defaultdict 
counter = collections.defaultdict(int)
counterMapInitList = collections.defaultdict(list)
counterMapInitCustomDataItem = collections.defaultdict(lambda: [[],[]])

## Counters
letter_counts = collections.Counter('Mary had a little lamb') 
letter_counts.update('Python is high-level language')
"""
most_common - get the n items which are most common according to the order they were present in the string
Eg:
Counter('Python is high-level language').most_common()
O/P: [('h', 3), (' ', 3), ('g', 3), ('l', 3), ('e', 3), ('n', 2), ('i', 2), ('a', 2), ('P', 1), ('y', 1), ('t', 1), ('o', 1), ('s', 1), ('-', 1), ('v', 1), ('u', 1)]
But 
Counter('Python is high-level language').most_common(3)
O/P: [('h', 3), (' ', 3), ('g', 3)]
"""
print(letter_counts.most_common(3))