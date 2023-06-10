import math


class progressBar:
  def __init__(self, currentProgress=0):
    self.currentProgress = currentProgress

  def reset(self):
    self.currentProgress = 0

  def showProgress(self):
    print("\r [{0}] {1}%".format('#'*(self.currentProgress//5), self.currentProgress), end='`')
    if self.currentProgress == 100:
      self.reset()
    else:
      self.currentProgress = self.currentProgress + 1
      
class testingProgress(progressBar:

  def showProgress(self):
    print("\r [{0}] {1}%".format('#'*(self.currentProgress//50), math.floor(self.currentProgress/10)), end='`')
    if self.currentProgress == 1000:
      self.reset()
    else:
      self.currentProgress = self.currentProgress + 1 
