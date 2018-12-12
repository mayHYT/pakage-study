import _pickle

age =24

with open(r'test.txt', 'wb') as f:
    _pickle.dump(age, f)
