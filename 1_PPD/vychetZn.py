
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
    

if __name__ == "__main__":
  print("Vychet Zn")
  
  a = Zn(5, 2)
  print(a)
