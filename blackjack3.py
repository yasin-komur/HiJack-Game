import random
import tkinter


def load_images(card_images):  # Although this is not necessary we write a function to improve ourself
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"
    # for each suit retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        # second the face cards
        for card in face_cards:
            name = "cards/{}_{}.{}".format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


column = 0


def score_hand(hand):
    ace = False
    score = 0
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            card_value = 11
            ace = True
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_card(frame):
    global deck
    global column
    # pop the next card off the pop of the deck
    next_card = deck.pop(0)
    if len(deck) == 0:
        print("New deck's coming.")
        deck = list(cards)
        random.shuffle(deck)
    # add the image to a label and display label
    tkinter.Label(frame, image=next_card[1], relief="solid", border=5).grid(row=0, column=column)  # todo --> or pack="left" without using grid
    column += 1
    # return the cards face value
    return next_card


def deal_dealer():
    global dealer_win
    global player_win
    dealer_score = score_hand(dealer_hand)
    while 0 <= dealer_score < 17:  # todo --> dealer 17'den önce çekilemiyor oyundan.
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_win += 1
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
        player_win += 1
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
        dealer_win += 1
    else:
        result_text.set("Draw!")


def deal_player():
    global dealer_win
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_win += 1
    print(locals())


# Set up the screen and frames for the dealer and player
main_window = tkinter.Tk()
main_window.title("Blackjack")
main_window.geometry("640x480-8-200")
main_window["bg"] = "green"

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text, fg="#000000").grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief="groove", borderwidth=5, bg="green")
card_frame.grid(row=1, column=0, sticky="we", columnspan=3, rowspan=2)

# player_winning_times = tkinter.IntVar()
# dealer_winning_times = tkinter.IntVar()
player_win = 0
dealer_win = 0

player_win_int = tkinter.IntVar()
dealer_win_int = tkinter.IntVar()

player_win_int.set(player_win)
dealer_win_int.set(dealer_win)

# player_winning_label = tkinter.Label(main_window, bg="green", fg="white", textvar=player_win_int).grid(row=1, column=3)
# dealer_winning_label = tkinter.Label(main_window, bg="green", fg="white", textvar=dealer_win_int).grid(row=3, column=3)

tkinter.Label(card_frame, text="Dealer", bg="green", fg="white").grid(row=0, column=0)
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, textvariable=dealer_score_label, bg="green", foreground="white").grid(row=1, column=0)

# embedded frame to hold the card images for dealer
dealer_card_frame = tkinter.Frame(card_frame, bg="green")
dealer_card_frame.grid(row=0, column=1, rowspan=2, columnspan=2, sticky="ew")

tkinter.Label(card_frame, text="Player", bg="green", fg="white").grid(row=2, column=0)
player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, textvariable=player_score_label, bg="green", fg="#ffffff").grid(row=3, column=0)

# embedded frame to hold the card images for player
player_card_frame = tkinter.Frame(card_frame, bg="green")
player_card_frame.grid(row=2, column=1, rowspan=2, columnspan=2, sticky="we")  # todo: columnspan=2 ?

# Button frame
button_frame = tkinter.Frame(main_window, relief="groove", border=5)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer).grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text="Player", command=deal_player).grid(row=0, column=1)


def new_game():
    global player_win
    global player_winning_label
    global dealer_winning_label
    global player_win_int
    global dealer_win_int
    global player_card_frame
    global dealer_card_frame

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, rowspan=2, columnspan=2, sticky="we")  # todo: columnspan=2 ?

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, rowspan=2, columnspan=2, sticky="ew")

    result_text.set("")

    dealer_hand.clear()
    player_hand.clear()

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

    player_win_int = tkinter.IntVar()
    dealer_win_int = tkinter.IntVar()

    player_win_int.set(player_win)
    dealer_win_int.set(dealer_win)

    player_winning_label = tkinter.Label(main_window, bg="green", fg="white", textvar=player_win_int).grid(row=2, column=3)
    dealer_winning_label = tkinter.Label(main_window, bg="green", fg="white", textvar=dealer_win_int).grid(row=1, column=3, sticky="n")

    print(player_win)
    print(dealer_win)

    if dealer_win == 1:
        card_frame.destroy()
        tkinter.Label(main_window, text="DEALER WIN!").grid(row=1, column=0, columnspan=3)
        main_window.destroy()
    elif player_win == 1:
        card_frame.destroy()
        tkinter.Label(main_window, text="PLAYER WIN!").grid(row=1, column=0, columnspan=3)
        main_window.destroy()


new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game).grid(row=0, column=2)
# load cards
cards = []
load_images(cards)

deck = list(cards)
random.shuffle(deck)
print(deck)
print(cards)

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

main_window.mainloop()
