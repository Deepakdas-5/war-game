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

    def _fetch(self):
        return self.player_card.pop(0)

    def _vangichoo_(self,a):
        self.player_card.extend(a)

    

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

game_on=True
round=0

while game_on:

    round+=1

    if (len(p1.player_card)==0):
        print("player one out of card player one lost")
        print("game over")
        game_on=False
        break
    elif (len(p2.player_card)==0):
        print("player 2 out of card player two lost")
        print("game over")
        game_on=False
        break

    else:
        player_one_fetched=[]
        player_one_fetched.append(p1._fetch())

        player_two_fetched=[]
        player_two_fetched.append(p2._fetch())

        war=True

        while war:
            if (player_one_fetched[-1].value)>(player_two_fetched[-1].value):
                p1._vangichoo_(player_one_fetched)
                p1._vangichoo_(player_two_fetched)
                war=False


            elif (player_one_fetched[-1].value)<(player_two_fetched[-1].value):
                p2._vangichoo_(player_one_fetched)
                p2._vangichoo_(player_two_fetched)
                war=False



            else:
                if (len(p1.player_card)<5):
                    print("p1 lost beacuase of less cards")
                    game_on=False
                    break

                elif (len(p2.player_card)<5):
                    print("p2 lost beacuse of less cards")
                    game_on=False
                    break

                else:
                    for i in range(5):
                        player_one_fetched.append(p1._fetch())
                        player_two_fetched.append(p2._fetch())

print(round)
            

                


                              
        





















        
        
