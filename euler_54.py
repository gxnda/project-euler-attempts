

class Card:
    def __init__(self, identifier: str):
        """
        Identifier is a 2 char string from poker.txt, like "5H"
        """
        value: str = identifier[0]
        match value:
            case "T":
                value = "10"
            case "J":
                value = "11"
            case "Q":
                value = "12"
            case "K":
                value = "13"
            case "A":
                value = "14"  # In the description, an Ace is not described as low.

        self.value: int = int(value)
        self.suit: str = identifier[1]
        self.identifer = identifier

    def __str__(self):
        return self.identifer


class Hand:
    def __init__(self, cards: list[Card], owner: int) -> None:
        self.cards: list[Card] = cards
        self.owner: int = owner

    def has_flush(self) -> tuple[bool, int]:
        suits = [card.suit for card in self.cards]
        highest_value = max(card.value for card in self.cards)

        all_same_suit = False
        if len(set(suits)) == 1:
            all_same_suit = True

        return all_same_suit, highest_value

    def has_royal_flush(self) -> bool:

        all_same_suit = self.has_flush()

        values = [card.value for card in self.cards]
        if all_same_suit and sorted(values) == sorted([10, 11, 12, 13, 14]):
            return True
        else:
            return False

    def has_straight(self) -> tuple[bool, int | None]:
        values = sorted([card.value for card in self.cards])
        straight_cards = [values[0], values[0] + 1, values[0] + 2, values[0] + 3, values[0] + 4]
        return values == straight_cards, (values[-1] if values == straight_cards else None)

    def has_straight_flush(self) -> tuple[bool, int | None]:
        has_straight, has_straight_with = self.has_straight()
        return self.has_flush() and has_straight, has_straight_with

    def has_pair(self) -> tuple[bool, int | None]:
        """Finds the highest pair in the hand"""
        values = sorted([card.value for card in self.cards])
        count_dict = {}
        for val in values:
            if val in count_dict:
                count_dict[val] += 1
            else:
                count_dict[val] = 1

        for key in list(count_dict.keys())[::-1]:
            if count_dict[key] >= 2:
                return True, key

    def has_three_of_a_kind(self) -> tuple[bool, int | None]:
        values = sorted([card.value for card in self.cards])
        count_dict = {}
        for val in values:
            if val in count_dict:
                count_dict[val] += 1
            else:
                count_dict[val] = 1

        for key in list(count_dict.keys())[::-1]:
            if count_dict[key] >= 3:
                return True, key

    def has_four_of_a_kind(self) -> tuple[bool, int | None]:
        values = sorted([card.value for card in self.cards])
        count_dict = {}
        for val in values:
            if val in count_dict:
                count_dict[val] += 1
            else:
                count_dict[val] = 1

        for key in list(count_dict.keys())[::-1]:
            if count_dict[key] >= 4:
                return True, key
    
    def get_highest_card(self) -> int:
        return max([card.value for card in self.cards])

    def get_hand_ranking(self):
        if self.has_royal_flush():
            return "royal flush"
        
        elif self.has_straight_flush():
            return "straight flush", self.has_straight_flush()[1]
        
        elif self.has_four_of_a_kind():
            return "four of a kind", self.has_four_of_a_kind()[1]
        
        # full house
        elif self.has_full_house():
            pass
        
        # flush
        elif self.has_flush():
            return "flush", self.has_flush()[1]
        
        # straight
        elif self.has_straight():
            return "straight", self.has_straight()[1]
        
        # three of a kind
        elif self.has_three_of_a_kind():
            return "three of a kind", self.has_three_of_a_kind()[1]
        
        # 2 pairs
        elif self.has_two_pair():
            pass
        
        # pair
        elif self.has_pair():
            pass
        
        # high card
        else:
            return "high card", self.get_highest_card()

    def has_two_pair(self):
        pass

    def has_full_house(self):
        pass


def euler_54():
    """
    Poker Hands

    Problem 54

    In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

        High Card: Highest value card.
        One Pair: Two cards of the same value.
        Two Pairs: Two different pairs.
        Three of a Kind: Three cards of the same value.
        Straight: All cards are consecutive values.
        Flush: All cards of the same suit.
        Full House: Three of a kind and a pair.
        Four of a Kind: Four cards of the same value.
        Straight Flush: All cards are consecutive values of same suit.
        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair
     of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players
     have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest
     cards tie then the next highest cards are compared, and so on.

    Consider the following five hands dealt to two players:
    Hand	 	Player 1	 	Player 2	 	Winner
    1	 	5H 5C 6S 7S KD
    Pair of Fives
            2C 3S 8S 8D TD
    Pair of Eights
            Player 2
    2	 	5D 8C 9S JS AC
    Highest card Ace
            2C 5C 7D 8S QH
    Highest card Queen
            Player 1
    3	 	2D 9C AS AH AC
    Three Aces
            3D 6D 7D TD QD
    Flush with Diamonds
            Player 2
    4	 	4D 6S 9H QH QC
    Pair of Queens
    Highest card Nine
            3D 6D 7H QD QS
    Pair of Queens
    Highest card Seven
            Player 1
    5	 	2H 2D 4C 4D 4S
    Full House
    With Three Fours
            3C 3D 3S 9S 9D
    Full House
    with Three Threes
            Player 1

    The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten
    cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
    You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no
    specific order, and in each hand there is a clear winner.

    How many hands does Player 1 win?

    """
    pass


if __name__ == "__main__":
    # c1, c2, c3, c4, c5 = Card("JD"), Card("TD"), Card("QD"), Card("KD"), Card("AD")
    # hand = Hand(cards=[c1, c2, c3, c4, c5], owner=1)
    # print(hand.has_flush())
    # print(hand.has_royal_flush())
    pass
