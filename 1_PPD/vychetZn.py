
def ExtendedEuclid(a, b):
  if (b == 0):
    return (a, 1, 0)
  dd, xx, yy = ExtendedEuclid(b, a % b)
  d, x, y = dd, yy, xx - (a//b) * yy
  return (d, x, y)

class Zn:
  def __init__(self, n, elem = 0):
    assert((n > 0) & (0 <= elem < n))
    self.n = n
    self.elem = elem
    
  def getN(self):
    return self.n

  def getElem(self):
    return self.elem
  
  def __str__(self):
    return "Vychet po modulu {0}, predstavitel {1}".format(self.n, self.elem)
  
  def __add__(self, other):
    assert(self.n == other.getN())
    ans = self.elem + other.getElem()
    return Zn(self.n, ans % self.n)
    
  def __mul__(self, other):
    assert(self.n == other.getN())
    ans = self.elem * other.getElem()
    return Zn(self.n, ans % self.n)
    
  def __truediv__(self, other):
    assert(self.n == other.getN())
    """
      Return 0 for impossible division.
    """
    # self / other = x -> other.elem * x = self.elem (mod self.n)
    # other * x + self.n * c = self = w * gcd(other, self.n)
    # other * x1 + self.n * y1 = gcd(other, self.n)
    d, x1, y1 = ExtendedEuclid(other.elem, self.n)
    #assert(self.elem % d == 0)
    w = self.elem // d
    return w * x1
  
  def inRing(self, num):
    return num % self.n == self.elem
    
 
    
    
  
if __name__ == "__main__":
  print("Vychet Zn")
  
  a = Zn(5, 2)
  b = Zn(5, 1)
  c = Zn(a.getN(), 4)  #c = Zn(5, 8) #  c = Zn(6, 1)
  print(a)
  print(a + b + b + b)
  print(a + c)

  print(a * c)
  
  print(a.inRing(10), a.inRing(12))
  
  one8 = Zn(8, 1)
  two8 = Zn(8, 2)
  three8 = Zn(8, 3)
  
  ans = two8 / three8
  print('Z8: 2 / 3 =', ans)
  ans = one8 / two8
  print('Z8: 1 / 2 =', ans)
  
