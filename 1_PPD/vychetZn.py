
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
