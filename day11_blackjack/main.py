def start_game():
    game_over = False

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    import random
    def deal_card():
        card = random.choice(cards)
        return card


    user_cards = []
    for _ in range(2):
        user_cards.append(deal_card())

    computer_cards = []
    for _ in range(2):
        computer_cards.append(deal_card())


    while not game_over:
        def calculate_score(cards):
            return sum(cards)

            if sum(user_cards) == 21 or sum(computer_cards) == 21:
                return 0
            for i in user_cards:
                if i == 11:
                    user_ace = True
            for i in computer_cards:
                if i == 11:
                    computer_ace = True

            if sum(user_cards) > 21 and user_ace:
                user_cards.remove(11)
                user_cards.append(1)
                return user_cards

            if sum(computer_cards) > 21 and computer_ace:
                computer_cards.remove(11)
                computer_cards.append(1)
                return computer_cards

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"The user's cards, {user_cards} and score {user_score}")
        print(f"The computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            if input("Would you like to draw another card, yes or no? ") == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    def compare(user_score, computer_score):
        if user_score == computer_score:
            print("It's a draw!")
        elif user_score == 0:
            print("You win!")
        elif computer_score == 0:
            print("You lose!")
        elif user_score > 21:
            print("You lose!")
        elif computer_score > 21:
            print("You win!")
        else:
            if user_score > computer_score:
                print("You win!")
            elif computer_score > user_score:
                print("You lose!")

    compare(user_score, computer_score)
    print(f"The computer's cards were {computer_cards}")


while input("Do you want to play a game of Blackjack, yes or no? ") == "yes":
    print("\n" * 10)
    start_game()
