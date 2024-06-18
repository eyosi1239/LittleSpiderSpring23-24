'''
Name: Eyosias Teafaye
CSC 201
Programming Project 4--Deck Class

The Deck class represents a stadard deck of playing cards with or without two jokers.
The card files for the graphic of each card are in a folder named cards. Each card
file is named with its rank and a letter for its suit. For example, the 4 of hearts
is in the file 4h.gif while the jack of clubs is in the file 11c.gif. Aces will have
rank 1 and kings rank 13. 

Document Assistance (who and what or declare no assistance):

No assitance given or recieved

'''
from card import Card
import random

class Deck:
    ACE_LOW = 1
    KING_HIGH = 13
    
    def __init__(self, useJokers = False):
        '''
        Creates a standard poker deck with or without jokers
        
        Params:
        useJokers (bool): True means that two jokers will be included in
        the deck. The default is no jokers.
        '''
        self.cardList = []
        for rank in range(Deck.ACE_LOW, Deck.KING_HIGH + 1):
            for suit in 'chsd':
                fileName = 'cards/'+ str(rank) + suit + '.gif'
                self.cardList.append(Card(fileName))
        if useJokers:
            self.cardList.append(Card('cards/0j.gif'))
            self.cardList.append(Card('cards/0j.gif'))
        self.currentIndex = 0
        self.shuffle()
    
    def getFullDeckSize(self):
            
        '''
        Returns the number of cards in the deck when it is full
        
        Returns:
            the number of cards in the deck when it is full
        '''
        return len(self.cardList)
    
    def shuffle(self):
        '''
        Shuffles the cards in the deck
        '''
        self.currentIndex = 0
        random.shuffle(self.cardList)
        
    def dealCard(self):
        '''
        Deals one card from the deck
        
        Returns:
            the card dealt from the deck
        '''
        dealt_card = self.cardList[self.currentIndex]
        self.currentIndex = self.currentIndex + 1
         
        return dealt_card 
                                                 
    def isEmpty(self):
        '''
        Determines if all of the cards have been dealt
        
        Returns:
            True when all of the cards have been dealt from the deck
        '''
        return self.currentIndex == len(self.cardList)
    
    def getNumCardsLeft(self):
        '''
        Determines the number of cards still left in the deck to deal
        
        Returns:
            The number of cards still in the deck to deal
        '''
        return len(self.cardList[self.currentIndex:])
    
    def moveToDealNext(self, cardToMove):
        
        '''
        Moves the card received as a parameter to the top of the deck
        and returns True. If the card has already been dealt, do not move
        the card and return False
        
        Params:
        cardToMove (Card): the card to move to the top of the deck if it
        hasn't yet been dealt
        
        Returns:
            True if the card was moved to the top of the deck. If not moved,
            returns False
        '''
        if cardToMove in self.cardList[self.currentIndex:]:
            self.cardList.remove(cardToMove)
            self.cardList.insert(self.currentIndex, cardToMove)
            return True
        
        else:
            return False
    
    def __str__(self):
        '''
        Creates a string representation of the deck
        
        Returns:
        A string with each card in the deck on a separate line
        '''
        result = ''
        for card in self.cardList:
            result = result + str(card) + '\n'
        return result


# Test code for the Deck class.
def main():
    random.seed(651)  # Don't change the seed 
    deck = Deck()
    print('Print entire shuffled deck.')
    print(deck)
    print('Full deck size:', deck.getFullDeckSize())
    
    didItMove = deck.moveToDealNext(Card('cards/1s.gif'))
    print('\nPrint deck again. Ace of spades should be first card')
    print('didItMove should be True: ', didItMove)
    print(deck)
    
    print('\nDeal first 5 cards')
    for i in range(5):
        card = deck.dealCard()
        print(card)
    
    print('\nNum cards left to deal:', deck.getNumCardsLeft())
    print('Is deck empty?', deck.isEmpty());
    
    print('\nDeal remaining cards without printing them.')
    for i in range(47):
        card = deck.dealCard()
    
    print('\nNum cards left to deal:', deck.getNumCardsLeft())
    print('Is deck empty?', deck.isEmpty());
    print()
    
    print('\nReshuffle the cards and print again.')
    deck.shuffle()
    print(deck)
    
    print('\nDeal first 5 cards')
    for i in range(5):
        card = deck.dealCard()
        print(card)
    
    cardAlreadyDealt = deck.cardList[2]
    print(f'\nCard already dealt is {cardAlreadyDealt}')
    didItMove = deck.moveToDealNext(cardAlreadyDealt)
    print(f"didItMove should be False: {didItMove}")
    if deck.cardList.index(cardAlreadyDealt) != 2:
        print("This card shouldn't have moved!")
        
    cardStillToDeal = deck.cardList[9]
    print(f'\nCard still to deal {cardStillToDeal}')
    didItMove = deck.moveToDealNext(cardStillToDeal)
    print(f'didItMove should be True: {didItMove}')
    if deck.cardList.index(cardStillToDeal) == 5:
        print(f'{cardStillToDeal} moved to be the next card to deal.')
    
    print('\nDeal a card')
    cardDealt = deck.dealCard()
    print(cardDealt)
        
    
if __name__ == '__main__':
    main()