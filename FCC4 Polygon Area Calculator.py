class Rectangle:
    def __init__(self, width, height):
        width = int(width)
        self.width = width
        height = int(height)
        self.height = height
    def set_width(self, width):
        self.width = int(width)
        return self.width
    def set_height(self, height):
        self.height = int(height)
        return self.height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        a = 2 * self.width
        b = 2 * self.height
        return a+b
    def get_diagonal(self):
        c = self.width ** 2
        d = self.height ** 2
        diag = (c+d) ** .5
        return diag
    def get_picture(self):
        string = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                string += '*' * self.width
                string += '\n'
            return string
        else:
            return 'Too big for picture.'
    def get_amount_inside(self, some):
        s_area = some.get_area()
        f_area = self.get_area()
        times = f_area // s_area
        return times
    def __str__(self):
        n_str = ''
        n_str += f'Rectangle(width={self.width}, height={self.height})'
        return n_str


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        width, height = int(side), int(side)
        self.width = width
        self.height = height
    def set_side(self, side):
        self.side = side
        self.set_width(side)
        self.set_height(side)
    def set_width(self, width):
        self.width = int(width)
        self.side = self.width
        self.height = self.side
        return self.width
    def set_height(self, height):
        self.height = int(height)
        self.side = self.height
        self.width = self.side
        return self.height
    def get_area(self):
        return Rectangle.get_area(self)
    def get_perimeter(self):
        return Rectangle.get_perimeter(self)
    def get_diagonal(self):
        return Rectangle.get_diagonal(self)
    def get_picture(self):
        if self.width and self.height <= 50:
            return Rectangle.get_picture(self)
        else:
            return 'Too big for picture.'
    def __str__(self):
        n_str = ''
        n_str += f'Square(side={self.side})'
        return n_str

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect.get_picture())
sq = Square(15)
print(sq.get_picture())
sq.set_width(51)
print(sq.side, sq.width, sq.height)
print(sq.get_picture())

