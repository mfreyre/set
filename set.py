from board import Board
from card import Card
from features import Features

class Set:
    def set_up(self):
        self.draw_pile = self.initate_draw_pile()
        self.board = Board()

    def initiate_draw_pile(self):
        return range(0, 81)

    def find_set(self, board):
        #create a pair for every set on the board
        #compute the third for each pair
        #check if the third is in the board
        print "Implement me"


    def compute_third(self, card1, card2):
        card3 = Card()
        if card1.color == card2.color:
            card3.color = card1.color
        else:
            card3.color = Features.computeColor(card1.color, card2.color)

        if card1.shape == card2.shape:
            card3.shape = card1.shape
        else:
            card3.shape = Features.computeShape(card1.shape, card2.shape)

        if card1.number == card2.number:
            card3.number = card1.number
        else:
            card3.number = Features.computeNumber(card1.number, card2.number)

        if card1.texture == card2.texture:
            card3.texture = card1.texture
        else:
            card3.texture = Features.computeTexture(card1.texture, card2.texture)


