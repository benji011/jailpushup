#  _____ _____    ______ _____  ___   _____ _____   ___  ______________ _____   _    _   _    _
# |  __ \  _  |   | ___ \  ___|/ _ \ /  ___|_   _|  |  \/  |  _  |  _  \  ___  | |  | | | |  | |
# | |  \/ | | |   | |_/ / |__ / /_\ \\ `--.  | |    | .  . | | | | | | | |__   | |  | | | |  | |
# | | __| | | |   | ___ \  __||  _  | `--. \ | |    | |\/| | | | | | | |  __|  | |  | | | |  | |
# | |_\ \ \_/ /   | |_/ / |___| | | |/\__/ / | |    | |  | \ \_/ / |/ /| |___  |_|  |_| |_|  |_|
# \____/\___/     \____/\____/\_| |_/\____/  \_/    \_|  |_/\___/|___/ \____/  (_|  |_) (_|  |_)
#
# i could write this much simpler, but what fun would that be?
import operator
import random

# initialize all the cards in the deck
royal_set   = { 'King': 14, 'Queen': 13, 'Jack': 12, 'Ace': 11 }
numbers_set = { 'Ten': 10, 'Nine': 9, 'Eight': 8, 'Seven': 7, 'Six': 6, 'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2 }

# all the sets in a deck of cards
ace       = []
clubs     = []
spades    = []
diamonds  = []

# 52 cards in total
deck = {"ace": ace, "clubs": clubs, "spades": spades, "diamonds": diamonds}

# merge the royal set with numbers. No reason why i did this, i thought it just looked cool to seperate
# the special high cards from numbers.
def merge_dicts(src_dic, t_dict):
    dict_copy = src_dic.copy()
    dict_copy.update(t_dict)
    return sorted(dict_copy.items(), key=operator.itemgetter(1))

# create the deck of cards per set.
# should have 52 cards in total now.
def create_deck():
    sorted_dict = merge_dicts(royal_set, numbers_set)
    #  put the deck together
    ace.append(sorted_dict)
    clubs.append(sorted_dict)
    spades.append(sorted_dict)
    diamonds.append(sorted_dict)
    return deck

# count the deck of cards to make sure we have all 52 cards
def count_deck():
    rn_count = 0
    for key, value in deck.items():
        rn_count = rn_count + 1
        for v in value:
            reps = v[random.randint(0, len(v)-1)]
            print key, " ----- set [", rn_count, "] --------- ", v[random.randint(0, len(v)-1)], "\n"
            # moar = raw_input("add more reps? [y/N]")
            # if moar == 'y' or 'Y':
			# 	# fix this later
            #     print reps + v[random.randint(0, 3)]
            # while moar != 'n' or 'N':
            #     print "keep going?"

create_deck()
count_deck()
