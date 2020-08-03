from time import time

class FuncTimer:
  def __init__(self, func):
      self.func = func
      self.time_count = 10

  def __call__(self, *args, **kwargs):
      avg = 0
      for i in range(self.time_count):
          t1 = time()
          self.func(*args, **kwargs)
          t2 = time()
          avg += t2-t1
      print('Average time execution of "{}" function is {:f} sec for {} times'.format(self.func.__name__, avg/self.time_count, self.time_count))
      return self.func(*args, **kwargs)


@FuncTimer
def fibonachi(poz):
    '''
    Returns pointed (poz) element of Fibonachi sequence
    '''
    i_0 = 0
    i_1 = 1
    cur_poz = 1
    while cur_poz <= poz:
        i_0, i_1 = i_1, i_0 + i_1
        cur_poz += 1
    return i_0

print(fib_none_recur(300))
