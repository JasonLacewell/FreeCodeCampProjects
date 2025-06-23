** start of main.py **

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
        if isinstance(self, Square):
            self.set_side(width)
            

    def set_height(self, height):
        self.height = height
        if isinstance(self, Square):
            self.set_side(height)

    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.' 
        width_pic_string = f'*{"*":*>{self.width-1}}'
        width_pic_string += '\n'
        for h in range(self.height-2):
            width_pic_string += f'*{"*":*>{self.width - 1}}\n'
        width_pic_string += f'*{"*":*>{self.width-1}}\n'
        return width_pic_string

    def get_amount_inside(self, rect):
        if not isinstance(rect,(Rectangle, Square)):
            raise TypeError('Must be either a rectangle or a square!')
        if all([self.width >= rect.width, self.height >= rect.height]):
            return (self.width//rect.width)*(self.height//rect.height)
        return 0
        
    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side:int):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.width})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

** end of main.py **

