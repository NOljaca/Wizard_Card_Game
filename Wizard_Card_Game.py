"""Python code for playing the card game “Wizard„ with 52 cards"""


__author__ = "Nikola_Oljaca"

from random import choice, shuffle


CARDS = ["Kreuz2", "Kreuz3", "Kreuz4", "Kreuz5", "Kreuz6", "Kreuz7", "Kreuz8", "Kreuz9",
         "KreuzX", "KreuzB", "KreuzD", "KreuzK", "KreuzA", "Pik2", "Pik3", "Pik4", "Pik5",
         "Pik6", "Pik7", "Pik8", "Pik9", "PikX", "PikB", "PikD", "PikK", "PikA", "Herz2",
         "Herz3", "Herz4", "Herz5", "Herz6", "Herz7", "Herz8", "Herz9", "HerzX", "HerzB",
         "HerzD", "HerzK", "HerzA", "Karo2", "Karo3", "Karo4", "Karo5", "Karo6", "Karo7",
         "Karo8", "Karo9", "KaroX", "KaroB", "KaroD", "KaroK", "KaroA"]

GAME_RULES = """
Rule_1 = The person who wins the most during the round wins that round. 
At the end of the game, whoever has won the most rounds wins.
In the event of a tie, whoever has the highest score is deemed the winner.
Rule_2 = Write the card you want to throw exactly as you see it on the screen.
Rule_3 = The trump card is scored higher than all the cards. 
Only 1 card can be discarded at a time.
See user manual for more. Good luck!!

Example of cards(highest to lowest):
⌠ ♣| KreuzA = Kreuz Ass
| A⌡

⌠ ♠| PikK = Pik König
| K⌡

⌠ ♥| HerzD = Herz Dame
| D⌡

⌠ ♦| KaroB = Karo Bube
| B⌡

⌠ ♦| KaroX = Karo 10(ten)
| X⌡
  
2-9 = Other numbers
"""


def create_cards():
    # weist den Karten eine Indexnummer zu und erstellt ein Dictionary
    """Function to shuffle predefined playing cards (52 pieces)

    Returns:
        Returns shuffled cards (in dictionary type)
    """
    shuffle(CARDS)
    cards_dic = dict()
    for index, card in enumerate(CARDS):
        cards_dic[index+1] = card
    return cards_dic


def deal_cards(player_num, roundd):
    # erstellt eine temporäre Liste mit so vielen Karten,
    # wie wir für jede Runde benötigen, und bildet ein Tupel
    """Deals enough cards to the players

    Arguments:
        player_num -- Total number of players
        roundd -- Number of rounds

    Returns:
        Returns temporary list (in tupple type) to be used during that round
    """
    cards = create_cards()
    temp = []
    for i in range(1, roundd*player_num+1):
        # um zu berechnen, wie viele Karten benötigt werden
        temp.append(cards.get(i))
    temp_deck = tuple(temp)
    return temp_deck


def compare_cards(trump, cards):
    """Compares given cards

    Arguments:
        trump -- Randomly picked trump
        cards -- List of cards to compare

    Returns:
        Returns the index of the card which has the highest value
    """
    temp = []
    colors = {"Kreuz": 4, "Pik": 3, "Herz": 2, "Karo": 1}
    numbers = {"A": 14, "K": 13, "D": 12, "B": 11, "X": 10, "9": 9,
               "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    for index, card in enumerate(cards):
        if card[:-1] == trump:
            temp.append(
                1000 + 50*numbers[cards[index][-1]] + colors[cards[index][:-1]])
        else:
            temp.append(50*numbers[cards[index][-1]] +
                        colors[cards[index][:-1]])
    return temp.index(max(temp))


def set_trump():
    """Picks a random trump

    Returns:
        Returns randomly picked trump
    """
    return choice(["Karo", "Herz", "Pik", "Kreuz"])


def change_player(row, player_num):
    # mathematische Gleichung, um jedes Mal den Überblick über die Spielerrunde zu behalten
    """Player switching function

    Arguments:
        row -- Current row information
        player_num -- Total number of players

    Returns:
        Returns new row information
    """
    row = (row) % player_num + 1
    return row


def card_select(cards, player_type):
    """Player/Robot selects a card from own cards

    Arguments:
        cards -- Cards that can be played
        player_type -- Type of player (player or bot)

    Returns:
        Returns the selected card
    """
    print(cards)
    if player_type == "player":
        while True:
         # Es fragt erneut, ob eine Karte ausgewählt ist, die nicht unter den Karten ist.
            decision = str(input("Please select a card: "))
            if decision in cards:
                return decision
            else:
                continue
    elif player_type == "bot":
        decision = choice(cards)
        return decision


def game_end(players_lst):
    """End of game points list and winner announcement

    Arguments:
        players_lst -- List of current players with points
    """
    # Es wird festgestellt, wer die maximal erzielte Punktzahl besitzt,
    # das heist der Gewinner wird ermittelt.
    temp = []
    for i in players_lst:
        temp.append(i[1])
    max_point = max(temp)
    print("\n", "="*17, sep="")
    for i in players_lst:
        print(*i, sep=": ", end=" ")
        if i[1] == max_point:
            print("WINNER", end=" ")
        print()
    print("="*17)
    input("Game is over. Please press Enter to exit...")


def main_loop(player_num, robot):
    """Function that provides the general operation of the game

    Arguments:
        player_num -- Total number of players
        robot -- Total number of bots
    """
    players_lst = []
    for i in range(1, player_num-robot+1):
        players_lst.append([f"Player{i}", 0])
    if robot >= 1:
        for i in range(1, robot+1):
            players_lst.append([f"Robot{i}", 0])
    row = 1
    max_round = 52//player_num
    roundd = 1
    sub_round = 1
    new_tup = deal_cards(player_num, roundd)
    new_lst = list(new_tup)
    while max_round >= roundd:
        trump = set_trump()
        print(f"Trump: [{trump}] Round: [{roundd}/{sub_round}]")
        game_pltz = []
        for i in range(player_num):
            temp_deck = new_lst[(row-1)*(roundd-sub_round+1):row*(roundd-sub_round+1)]
            print()
            print(f"{players_lst[row-1][0]} is playing now")
            if players_lst[row-1][0][:-1] == "Player":
                game_pltz.append(card_select(temp_deck, "player"))
            elif players_lst[row-1][0][:-1] == "Robot":
                game_pltz.append(card_select(temp_deck, "bot"))
            print("\nRevealed cards:", *game_pltz, sep=" ")
            row = change_player(row, player_num)
        best_card = compare_cards(trump, game_pltz)
        # Zeigt die abgelegte Karte mit der höchsten Punktzahl an
        # Herauszufinden, wem die größte Karte gehört.
        # es wird auf diese Weise erkannt,
        # weil das Spiel jedes Mal nach einer bestimmten Reihenfolge abläuft
        if best_card+row > player_num:
            players_lst[best_card+row-player_num-1][1] += 1
        else:
            players_lst[best_card+row-1][1] += 1
        print(f"Best card: {game_pltz[best_card]}")
        for i in game_pltz:
            new_lst.remove(i)
            # löscht abgelegte Karten von eigenen Karten
        row = change_player(row, player_num)
        if sub_round == roundd:
            decision = input("Press (Q/q) to end the game or Enter to skip: ")
            if decision == "Q" or decision == "q":
                game_end(players_lst)
                exit(0)
            else:
                sub_round = 1
                roundd += 1
        else:
            sub_round += 1

        if sub_round == 1:
            new_tup = deal_cards(player_num, roundd)
            new_lst = list(new_tup)

    game_end(players_lst)


if __name__ == "__main__":
    print("__Testfälle__")
    # Es ist nicht möglich alle funktionen zu testen, da voneinander abhängige funktionen
    print(create_cards(), "\n")
    print(create_cards(), "\n")
    print(create_cards(), "\n")
    print(compare_cards(trump= "Herz", cards= ["Herz2", "Karo2"]), "\n") # Index der Gewinnkarte
    print(compare_cards(trump= "Karo", cards= ["KreuzA", "Pik6", "Pik3", "Karo2"]), "\n")
    print(compare_cards(trump= "Pik", cards= ["KreuzA", "Pik2", "Herz2", "Karo2"]), "\n")
    # Alle Karten, die in dieser Runde ausgeteilt werden
    print(deal_cards(player_num= 4, roundd= 2), "\n")
    print(deal_cards(player_num= 3, roundd= 5), "\n")
    print(deal_cards(player_num= 2, roundd= 1), "\n")
    print(set_trump(), "\n")
    print(set_trump(), "\n")
    print(set_trump(), "\n")
    print(change_player(1,1), "\n")
    print(change_player(3,2), "\n")
    print(change_player(1,4), "\n")
    print(card_select(cards=["KreuzA", "Pik6", "Pik3"], player_type= "bot"), "\n")
    print(card_select(cards=["Herz2", "Karo2"], player_type= "bot"), "\n")
    print(card_select(cards=["KaroA"], player_type= "bot"), "\n")
    input("Test is over. Press Enter to continue....")
    print(GAME_RULES)
    while True:
        # um mögliche Fehler zu vermeiden
        try:
            number_of_player = int(
                input("Please enter the number of players(2-5): "))
            bot_player = int(
                input(f"How many of the {number_of_player} players are robots?: "))
        except ValueError:
            print("Please enter number only!")
            continue
        if number_of_player < 2 or number_of_player > 5:
            print("Please enter the number of players between 2-5")
            continue
        if bot_player > number_of_player or bot_player < 0:
            print(
                f"Please enter the number of robots between 0 and {number_of_player}")
            continue
        main_loop(number_of_player, bot_player)