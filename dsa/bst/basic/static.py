def myfunc():
  myfunc.counter += 1
  print myfunc.counter

# attribute must be initialized
myfunc.counter = 12
myfunc()