# python code to get the
# smallest multiple of N
# with binary digits only
def multiple(A):
  flag = False
  i = 1
  while(flag != True):
    result = A * i

    # method returns smallest
    # multiple which has
    # binary digits
    allowed_chars = set('01')
    validationString = str(result)
    if set(validationString).issubset(allowed_chars):
      flag = True;
      break;
    else:
      i = i + 1

  return validationString

# Driver code
n = 12
print(multiple(n))
