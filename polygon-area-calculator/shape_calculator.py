class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    if self.width != self.height:
      self.shape = "Rectangle"
    else:
      self.shape = "Square"

  def __str__(self):
    obj_string = self.shape + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return obj_string

  def set_width(self, width):
    temp_width = self.width
    self.width = width
    self.get_shape()
    return print("Width changed from", temp_width, "to", width)

  def set_height(self, height):
    temp_height = self.height
    self.height = height
    self.get_shape()
    return print("Height changed from", temp_height, "to", height)

  def get_area(self):
    area = self.width * self.height
    print("Area of " + str(self.shape) + ": " + str(area))
    return area

  def get_perimeter(self):
    perimeter = 2*(self.width + self.height)
    print("Perimeter of " + str(self.shape) + ": " + str(perimeter))
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    temp_calc_format = f'{(diagonal):.2f}'
    print("Diagonal of " + str(self.shape) + ": " + str(temp_calc_format))
    return temp_calc_format

  def get_shape(self):
    if self.width != self.height:
      self.shape = "Rectangle"
    else:
      self.shape = "Square"
  
  def get_picture(self): 

    if self.height > 50:
      return "Too big for picture"
    
    else:
      print("Picture:\n")
      for i in range(self.height):
        print("*/"*self.width)

  def get_amount_inside(self, obj):
    print("Number of times a " + obj.shape + " can fit into a " + self.shape + "\n")
    # Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

    #Print obj data
    print(obj)
    obj_area = obj.get_area()
    obj_peri = obj.get_perimeter()
    obj.get_picture()

    #Print self data
    print(self)
    self_area = self.get_area()
    self_peri = self.get_perimeter()
    self.get_picture()

    # print(obj.width)
    # print(self.width)

    if obj.width > self.width or obj.height > self.height:
      message = "The " + obj.shape + " cannot fit into the " + self.shape + "\n"
      return message

    else:
      num_width_iterations = 0
      if self_area % obj_area == 0 and self_peri == obj_peri:
        num_width_iterations = 1

      elif self_area % obj_area == 0:
        num_width_iterations = int(self_area/obj_area)

      else:
        width_diff = self.width
        chk_width_diff = width_diff
        height_diff = self.height
        width_cnt = 0
        height_cnt = 0
        while True:

          if chk_width_diff >= obj.width:
            chk_width_diff -= obj.width
            width_diff -= obj.width
            width_cnt += 1

          elif height_diff >= obj.height:
              height_diff -= obj.height
              height_cnt += 1

          else:
            num_width_iterations = height_cnt * width_cnt
            break

      response = "The " + obj.shape + " can fit into the " + self.shape + " " + str(num_width_iterations) + " times\n"
      return response

class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    self.width = side
    self.height = side
    self.shape = "Square"

  def __str__(self):
    obj_str = "Square(side=" + str(self.side) + ")"
    return obj_str

  def set_side(self, side):
    temp_side = self.side
    self.side = side
    self.width = side
    self.height = side
    return print("Side changed from", temp_side, "to", side)