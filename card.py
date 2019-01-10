class Card:
    def __init__(self, color, shape, number, texture):
        self.color = color
        self.shape = shape
        self.number = number
        self.texture = texture

    def __str__(self):
        return self.color + ", " + self.shape + ", "  + str(self.number) + " and " + self.texture

