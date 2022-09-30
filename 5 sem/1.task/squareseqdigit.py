def kol(n):
  l = 0
  while n >= 1:
    n = n / 10
    l = l + 1
  return(l)

def squareSequenceDigit(n):
  i = 0
  s = 0
  while i < n:
    s = s + 1
    S = s*s
    i = i + kol(S)
  if n == i:
    S = S % 10
    return(S)
  else:
    i = i - n
    S = S / (10**i) % 10
    return(int(S))
    
    
    
    
if __name__ == "__main__":
    squareSequenceDigit(1)
    squareSequenceDigit(2)
    squareSequenceDigit(7)
    squareSequenceDigit(12)
    squareSequenceDigit(17)
    squareSequenceDigit(27)
