class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand): #hand in format "2S AH 2H AS AC"
        self.hand = hand
        self.suit = hand[1]+hand[4]+hand[7]+hand[10]+hand[13]
        self.cards = hand[0]+hand[3]+hand[6]+hand[9]+hand[12]
        self.straight = False
        self.flush = False
        self. play = ''

    def jugada(self):
        self.straight = False
        self.flush = False
        cards = {}
        self.play = ''
        self.cards
        for card in self.cards:

        if ''.join(sorted(self.cards)) in "23456789AJKQT" or \
            ''.join(sorted(self.cards)) in "2345A" or \
            ''.join(sorted(self.cards)) in "9JQKT" or \
            ''.join(sorted(self.cards)) in "89JQT" or \
            ''.join(sorted(self.cards)) in "789QT" or \
            ''.join(sorted(self.cards)) in "6789T": #straight
            self.straight = True
        if self.suit == 'SSSSS' or self.suit == 'HHHHH' or self.suit == 'CCCCC'\
            or self.suit == 'DDDDD':
            self.flush = True
        for i in self.cards:
            if i not in cards.keys():
                cards[i] = 1
            else:
                cards[i] += 1
        for key in cards:
            if cards[key] == 4:
                self.play = 'Four of a kind'
            if cards[key] == 3:
                if self.play == 'Two of a kind':
                    self.play = 'Full house'
                else:
                    self.play = 'Three of a kind'
            if cards[key] == 2:
                if self.play == 'Three of a kind':
                    self.play = 'Full house'
                else:
                    self.play = 'Two of a kind'


    def compare_with(self, other):
        pass
