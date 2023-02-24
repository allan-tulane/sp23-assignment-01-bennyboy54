"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x
    else:
      ra = foo(x-1)
      rb = foo(x-2)
      return ra + rb
    pass

def longest_run(mylist, key):
    counter = 0
  curr_longest_run = 0
  for i in mylist:
    if i == key:
      counter += 1
    if counter > curr_longest_run:
      curr_longest_run = counter
      counter = 0
  return curr_longest_run
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    class Result:
  """ done """

  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size  # run on left side of input
    self.right_size = right_size  # run on right side of input
    self.longest_size = longest_size  # longest run in input
    self.is_entire_range = is_entire_range  # True if the entire input matches the key

  def __repr__(self):
    return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def longest_run_recursive(mylist, key):
  def result(R_left, R_right):
    if R_right.is_entire_range == True and R_left.is_entire_range == True:
      total = R_right.longest_size + R_left.longest_size
      return Result(total, total, total, True)
    else:
      total = 0
      if R_left.is_entire_range == True:
        L = R_right.left_size + R_left.left_size
      else:
        L = R_left.left_size
      if R_right.is_entire_range == True:
        R = R_right.right_size + R_left.right_size
      else:
        R = R_right.right_size
      if R_left.right_size != 0 and R_right.left_size != 0:
        total = R_right.left_size + R_left.right_size
      total = max(total, R_right.longest_size, R_left.longest_size)
      return Result(L, R, total, False)

  def longest_run_recursive_helper(mylist, key):
    if len(mylist) == 1:
      if mylist[0] == key:
        positive_result = Result(1, 1, 1, True)
        return positive_result
      else:
        negative_result = Result(0, 0, 0, False)
        return negative_result
    else:
      return (result(longest_run_recursive_helper(mylist[0:(len(mylist)//2)], key), longest_run_recursive_helper(mylist[(len(mylist)//2):], key)))

  answer = longest_run_recursive_helper(mylist, key)
  return answer.longest_size
    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


