class Features:
    valid_colors = ["red", "green", "purple"]
    valid_shapes = ["oval", "diamond", "squiggle"]
    valid_numbers = [1, 2, 3]
    valid_textures  = ["solid", "striped", "open"]

   #todo: refactor this so that it doesn't have so much shared code
   # maybe need a factory or something
    def computeNumber(self, number1, number2):
        numbers = valid_numbers[:] # copy by value, not reference
        numbers.remove(number1)
        numbers.remove(number2)
        return numbers[0]

    def computeTexture(self, texture1, texture2):
        textures = valid_textures[:]
        textures.remove(texture1)
        textures.remove(texture2)
        return textures[0]


    def computeColor(self, color1, color2):
        colors = valid_colors[:]
        colors.remove(color1)
        colors.remove(color2)
        return colors[0]

    def computeShape(self, shape1, shape2):
        shapes = valid_shapes[:]
        shapes.remove(shape1)
        shapes.remove(shape2)
        return shapes[0]
