class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    pic = ""
    line = ""
    for _ in range(self.width):
      line += "*"
    for i in range(self.height):
      pic += line + "\n"
    return pic

  def get_amount_inside(self, shape):
    times = 0
    for i in range(0, self.height, shape.height):
      for j in range(0, self.width, shape.width):
        if (i + shape.height <= self.height and j + shape.width <= self.width):
          times += 1
    return times

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
    
class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    super().__init__(side, side)

  def set_width(self, width):
    self.side = width
    if self.width != width:
      self.width = width
      self.set_height(width)

  def set_height(self, height):
    self.side = height
    if self.height != height:
      self.height = height
      self.set_width(height)
  
  def set_side(self, side):
    self.side = side
    self.set_height(side)
    
  def __str__(self):
    return f'Square(side={self.side})'
