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
        self.identifier = identifier

    def __str__(self):
        return self.identifier


class Hand:
    def __init__(self, cards: list[Card]) -> None:
        self.cards: list[Card] = cards

    def __has_x_of_y_size_tuple(self, x, y, values=None, values_to_exclude: list | None = None):
        """
        Returns if the user has e.g. "2" of a pair of size "2".
        """
        if not values:
            values = sorted([card.value for card in self.cards])

        if not values_to_exclude:
            values_to_exclude = []

        count_dict = {}
        for val in values:
            if val in count_dict:
                count_dict[val] += 1
            else:
                count_dict[val] = 1

        def pair_filter(key):
            return count_dict[key] == y

        # filter for pairs of size y
        filtered = list(filter(pair_filter, count_dict))

        highest = None
        if filtered:
            highest = max([i for i in filtered if i not in values_to_exclude])

        return len(filtered) == x, highest

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
        return self.__has_x_of_y_size_tuple(1, 2)

    def has_two_pair(self) -> tuple[bool, int | None]:
        return self.__has_x_of_y_size_tuple(2, 2)

    def has_three_of_a_kind(self) -> tuple[bool, int | None]:
        return self.__has_x_of_y_size_tuple(1, 3)

    def has_four_of_a_kind(self) -> tuple[bool, int | None]:
        return self.__has_x_of_y_size_tuple(1, 4)

    def has_full_house(self):
        has_pair, has_pair_with = self.__has_x_of_y_size_tuple(1, 2)
        has_three, has_three_with = False, None
        if has_pair:
            has_three, has_three_with = self.__has_x_of_y_size_tuple(1, 3, values_to_exclude=[has_pair_with])

        has_full_house_with = None
        has_full_house = has_pair and has_three
        if has_full_house:
            has_full_house_with = has_three_with

        return has_full_house, has_full_house_with

    def get_highest_card(self, to_exclude: list[int] = None) -> int:
        if not to_exclude:
            to_exclude = []
        return max([card.value for card in self.cards if card.value not in to_exclude])

    def get_hand_ranking(self) -> tuple[str, int | None]:
        if self.has_royal_flush():
            return "royal flush", None

        elif self.has_straight_flush()[0]:
            return "straight flush", self.has_straight_flush()[1]

        elif self.has_four_of_a_kind()[0]:
            return "four of a kind", self.has_four_of_a_kind()[1]

        # full house
        elif self.has_full_house()[0]:
            return "full house", self.has_full_house()[1]

        # flush
        elif self.has_flush()[0]:
            return "flush", self.has_flush()[1]

        # straight
        elif self.has_straight()[0]:
            return "straight", self.has_straight()[1]

        # three of a kind
        elif self.has_three_of_a_kind()[0]:
            return "three of a kind", self.has_three_of_a_kind()[1]

        # 2 pairs
        elif self.has_two_pair()[0]:
            return "two pair", self.has_two_pair()[1]

        # pair
        elif self.has_pair()[0]:
            return "pair", self.has_pair()[1]

        # high card
        else:
            return "high card", self.get_highest_card()

    @classmethod
    def load_hand_from_string(cls, hand_str: str):
        cards = [Card(i) for i in hand_str.split()]
        return Hand(cards=cards)


class Round:
    def __init__(self, hand_1: Hand, hand_2: Hand):
        self.hand_1 = hand_1
        self.hand_2 = hand_2
        self.__hand_rankings = {
            "royal flush": 1,
            "straight flush": 2,
            "four of a kind": 3,
            "full house": 4,
            "flush": 5,
            "straight": 6,
            "three of a kind": 7,
            "two pair": 8,
            "pair": 9,
            "high card": 10
        }

    def compare_highest_cards(self):
        winner_determined = False
        checked_values = []
        while not winner_determined:
            hand_1_highest = self.hand_1.get_highest_card(to_exclude=checked_values)
            hand_2_highest = self.hand_2.get_highest_card(to_exclude=checked_values)
            if hand_1_highest not in checked_values:
                checked_values.append(hand_1_highest)
            if hand_2_highest not in checked_values:
                checked_values.append(hand_2_highest)
            if hand_1_highest > hand_2_highest:
                return 1
            elif hand_2_highest > hand_1_highest:
                return 2
            if len(checked_values) >= len(
                    set([card.value for card in self.hand_1.cards]) | set([card.value for card in self.hand_2.cards])):
                return 0

    def calculate_winner(self) -> int:
        hand_1_result, hand_1_result_with = self.hand_1.get_hand_ranking()
        hand_1_ranking = self.__hand_rankings[hand_1_result]
        hand_2_result, hand_2_result_with = self.hand_2.get_hand_ranking()
        hand_2_ranking = self.__hand_rankings[hand_2_result]

        # rankings are 1st 2nd etc
        if hand_1_ranking < hand_2_ranking:
            return 1
        elif hand_1_ranking > hand_2_ranking:
            return 2
        elif hand_1_result_with > hand_2_result_with:
            return 1
        elif hand_1_result_with < hand_2_result_with:
            return 2
        else:
            return self.compare_highest_cards()


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


def get_all_poker_hands(filename="poker.txt"):
    all_rounds: list[Round] = []
    with open(filename) as f:
        rounds = [i.split() for i in f.readlines()]
        for round in rounds:
            first_5: list[str] = round[:5]
            assert len(first_5) == 5
            last_5: list[str] = round[5:]
            assert len(last_5) == 5
            card_list_1 = [Card(i) for i in first_5]
            card_list_2 = [Card(i) for i in last_5]
            hand_1 = Hand(card_list_1)
            hand_2 = Hand(card_list_2)
            round = Round(hand_1, hand_2)
            all_rounds.append(round)

    return all_rounds


if __name__ == "__main__":
    all_rounds = get_all_poker_hands()
    count = 0
    for round in all_rounds:
        winner = round.calculate_winner()
        if winner == 1:
            count += 1

    print(count)
