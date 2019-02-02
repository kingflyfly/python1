def fibonacci():
  a=b=1
  yield a 
  yield b 
  while True: 
    a,b = b,a+b 
    yield b
c = fibonacci()
print(c.__next__())
print(c.__next__())
print(c.__next__())