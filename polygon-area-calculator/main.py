# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
# from unittest import main

#Rectangle class invoked with arguments (width, height)
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.get_picture()
rect.set_width(3)
rect.set_height(10)
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect)
rect.get_picture()

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.get_picture()
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
sq.get_picture()

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(2)
rect.set_height(2)
sq.set_side(2)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(2)
rect.set_height(2)
sq.set_side(4)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(2)
rect.set_height(4)
sq.set_side(5)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(1)
rect.set_height(4)
sq.set_side(5)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(1)
rect.set_height(4)
sq.set_side(8)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(3)
rect.set_height(5)
sq.set_side(8)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(5)
rect.set_height(4)
sq.set_side(8)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(2)
rect.set_height(9)
sq.set_side(9)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))

rect.set_width(4)
rect.set_height(2)
sq.set_side(9)

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))


# Run unit tests automatically
# main(module='test_module', exit=False)