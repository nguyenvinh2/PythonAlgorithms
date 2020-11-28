class Triangle():
    def __init__(self, base, height):
      self.base = base
      self.height = height
      self.area = base * height

    def info(self):
      print("Triangle Base: {}, Triangle Height: {}, Area: {}".format(self.base, self.height, self.area))