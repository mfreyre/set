from card import Card
from set import Set

def run():
    card1 = Card("purple", "oval", 2, "open")
    card2 = Card("red", "diamond", 2, "open")
    set = Set()
    card3 = set.compute_third(card1, card2)
    print card3

if __name__=="__main__":
    run()
