suit=("SPADE","HEART","DIAMOND","CLUB")
RANK=["TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","JACK","QUEEN","KING","ACE"]
VALUES={"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,"NINE":9,"TEN":10,"JACK":11,"QUEEN":12,"KING":13,"ACE":14}

class card():

    def __init__(self,suit,rank):

        self.suit=suit
        self.rank=rank
        self.value=VALUES[rank]


    def _str_(self):
        print(VALUES[self.rank])
        return f"{self.rank} of {self.suit}"


    

ob1=card("SPADE","THREE")
print(ob1._str_())
