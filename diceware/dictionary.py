import os

class Dictionary():
  '''
  Dictionary to hold a list of words and generate random passwords.
  It overloads the relevant operations, working with any iterables.
  '''
  def __init__(self, lines):
    self.words = [line.strip() for line in lines]
  
  def __iter__(self):
    return iter(self.words)
  
  def __getitem__(self, key):
    return self.words[key]
  
  def __add__(self, other):
    s = set(self)
    for word in other:
      s.add(word.strip())

    return Dictionary(sorted(s))
  
  def __radd__(self, other):
    return self + other
  
  def __sub__(self, other):
    s = {word.strip() for word in other}
    return Dictionary(word for word in self if word not in s)
  
  def __rsub__(self, other):
    s = set(self)
    return Dictionary(word.strip() for word in other if word.strip() not in s)
  
  def __and__(self, other):
    s0 = set(self)
    s1 = {word.strip() for word in other}
    return Dictionary(sorted(s0 & s1))
  
  def __rand__(self, other):
    return self & other
  
  def __or__(self, other):
    return self + other
  
  def __ror__(self, other):
    return self + other
  
  def get_random_words(self, count):
    if len(self.words) == 0:
      raise ValueError('Dictionary is empty')
    
    for _ in range(count):
      max_value = 0xffffffff - (0xffffffff % len(self.words)) - 1
      x = max_value + 1
      while x > max_value:
        bytes = os.urandom(4)
        x = int.from_bytes(bytes, byteorder='little', signed=False)
      
      yield self[x % len(self.words)]