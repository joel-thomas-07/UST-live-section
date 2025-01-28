import string
from random import sample
five_letters = ''.join(sample(string.ascii_letters, 5))

print("Five randomly sampled letters:")
print(five_letters)
