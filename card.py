'''
Name: Eyosias Tesfaye
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card for a card game. Cards have a rank,
a suit, and an image. The card stores its position in a graphics window. It can be drawn and
undrawn in the graphics window.

Document Assistance (who and what or declare no assistance):
NO assitnace given or recieved


'''
from graphics2 import *
import time

class Card:
    # Add your methods above __eq__
    
    def __init__(self,image_name):
        '''
        Create a standard poker card
        
        Params:
        image_name(string): That image file name
        '''
        rank, suit = self.__extract_data_from_filename(image_name)
        
        self.image = Image(Point( 0, 0),image_name)
        self.rank = int(rank)
        self.suit = suit
        
    def __extract_data_from_filename(self,image_name):
        '''
        A private method that extracts the suit and rank from file name
        
        Params:
        image_name(string): That image file name
        
        return:
        A tuple containing the rank and suit
        '''
        
        string = image_name[6:]
        rank = string[:-5]
        suit = string[-5]
        
        return rank, suit
    
    def getRank(self):
        '''
        Returns the rank of the card
        
        return:
        The rank of the card 
        '''
        return self.rank
    
    def getSuit(self):
        '''
        Returns the suit of the card
        
        return:
        The suit of the card 
        '''
        return self.suit
    
    def getImage(self):
        '''
        Returns a graphical object which is the  image of the card
        
        return:
        The image of the card
        '''
        return self.image
    
    def draw(self,window):
        '''
        Draws the card on the window
        
        Params:
        window(Graphwin): The window where the card will be drawn from.
        '''
        self.image.draw(window)
        
    def undraw(self):
        '''
        Undraws the card Image
        '''
        self.image.undraw()
        
    def isRed(self):
        '''
        Checks if the card is red or black
        
        return:
        True if the card is red and false if it is black 

        '''
        return self.suit == "h" or self.suit == "d"
    
    def move(self, dx, dy):
        '''
        Moves the card
        
        Params:
        dx(int): The amount we want to horizontally move the card
        dy(int): The amount we want to vertically move the card
        '''
        self.image.move(dx, dy)
        
    def containsPoint(self, point):
        '''
        Checks if the point passed is in the card.
        
        Params:
        point(Point): A point in a window
        
        returns:
        True if the point is in the card false if its not
        '''
        half_width = self.image.getWidth() / 2
        half_height = self.image.getHeight() / 2
        
        center_x = self.image.getCenter().getX()
        center_y = self.image.getCenter().getY()
        
        x_1 = center_x - half_width
        x_2 = center_x + half_width
        y_1 = center_y - half_width
        y_2 = center_y + half_width
        
        is_x_valid = x_1 < point.getX() < x_2
        is_y_valid = y_1 < point.getY() < y_2
        
        return is_x_valid and is_y_valid
    
    def __str__(self):
        '''
        Creates a string representation of the card
        
        Returns:
        A string with each card rank, suit and center.
        '''
        return f"suit = {self.suit}, rank = {self.rank}, center = {self.image.getCenter()}"
    
    def __eq__(self, cardToCompare):
        '''
        Allows users of the Card class to compare two cards using ==
        
        Params:
        cardToCompare (Card): the Card to check for equality with this Card
        
        Returns:
        True if the two cards have the same rank and suit. Otherwise, False
        '''
        return self.suit == cardToCompare.suit and self.rank == cardToCompare.rank

def main():  
    window = GraphWin("Testing Card", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    print(card.getSuit())
    print(card.getImage())
    print(card.isRed())
    
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click only on the card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click only on the card should move it 200 pixels right and 100 pixels down
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 100)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Spades card
    fileName = 'cards/2s.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    print(card2.isRed())
    
    # move card2 to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        