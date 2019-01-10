class Features:

   #todo: refactor this so that it doesn't have so much shared code
   # maybe need a factory or something
    @staticmethod
    def computeNumber(number1, number2):
        numbers = [1, 2, 3]
        numbers.remove(number1)
        numbers.remove(number2)
        return numbers[0]

    @staticmethod
    def computeTexture(texture1, texture2):
        textures  = ["solid", "striped", "open"]
        textures.remove(texture1)
        textures.remove(texture2)
        return textures[0]


    @staticmethod
    def computeColor(color1, color2):
        colors = ["red", "green", "purple"]
        colors.remove(color1)
        colors.remove(color2)
        return colors[0]

    @staticmethod
    def computeShape(shape1, shape2):
        shapes = ["oval", "diamond", "squiggle"]
        shapes.remove(shape1)
        shapes.remove(shape2)
        return shapes[0]
