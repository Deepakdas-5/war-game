import random
SUIT=("SPADE","HEART","DIAMOND","CLUB")
RANK=["TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","JACK","QUEEN","KING","ACE"]
VALUES={"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,"NINE":9,"TEN":10,"JACK":11,"QUEEN":12,"KING":13,"ACE":14}

class card():

    def __init__(self,suit,rank):

        self.suit=suit
        self.rank=rank
        self.value=VALUES[rank]


    def __str__(self):
        print(VALUES[self.rank])
        return f"{self.rank} of {self.suit}"
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class deck():

    def __init__(self):

        self.total_cards=[]
        for suit in SUIT:
            for rank in RANK:

                self.total_cards.append(card(suit,rank))

    def _card_(self):
        return self.total_cards

    def shuffle(self):

        random.shuffle(self.total_cards)

    def deal_one(self):
        return self.total_cards.pop()

        
class player():

    def __init__(self,name):
        self.name=name
        self.player_card=[]


    def player_cards(self,deck):

        for i in range(26):

           self.player_card.append(deck.deal_one())

    def __repr__(self):
        return f"player {self.name} : {self.player_card}"
           
            
d=deck()
d.shuffle()
p1=player("one")
p1.player_cards(d)
print(p1)
p2=player("two")
p2.player_cards(d)
print(p2)




















        
        
