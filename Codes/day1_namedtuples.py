from collections import namedtuple
from random import choice

Card = namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
                                        
    def __len__(self):
        return len(self._cards)
        
    def __getitem__(self, position):
        return self._cards[position]
        
deck = FrenchDeck()

# Randomly pick a card
print(choice(deck))

# Print Aces only
print(deck[12::13])

# Check if card exists
print(Card('7', 'heart') in deck)
print(Card('7', 'hearts') in deck)