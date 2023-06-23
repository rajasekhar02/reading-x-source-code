seq1 = [1,23,4,5]
seq2 = [1,2,3,4]

def do_something_with(*argv):
    print([*argv])

for items in zip(seq1,seq2):
  do_something_with(*items)