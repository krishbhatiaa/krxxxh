import random

print("Hello and welcome to group 6's Casino Blackjack")
starting_balance = int(input("Enter your starting balance: $"))
balance = starting_balance

while balance > 0:
    print(f"Your current balance is: ${balance}")
    bet = int(input("Place your bet: $"))
    if bet > balance:
        print("Insufficient balance. Please place a valid bet.")
        continue

    balance -= bet
    print("Dealing cards...")
    input("Press <ENTER> to begin.")
    
    # Initialize card names and values
    Ace = 11
    Jack, Queen, King = 10, 10, 10
    
    # Generate initial cards for player and dealer
    player_hand = [random.randint(1, 13) for _ in range(2)]
    dealer_hand = [random.randint(1, 13) for _ in range(2)]
    
    # Function to calculate the total value of a hand
    def calculate_total(hand):
        total = sum(Ace if card == 1 else min(card, 10) for card in hand)
        # Adjust for Aces if total exceeds 21
        while total > 21 and 1 in hand:
            total -= 10
            hand.remove(1)
        return total

    # Display player's initial hand and total
    print("Your hand is:", player_hand)
    print("The total of your hand is:", calculate_total(player_hand))

    # Player's turn
    while True:
        decision = input("Do you want to HIT or STAND? ").lower()
        if decision.startswith('hit') or decision.startswith('h'):
            player_hand.append(random.randint(1, 13))
            player_total = calculate_total(player_hand)
            print("Your hand is:", player_hand)
            print("The total of your hand is:", player_total)

            if player_total > 21:
                print("You bust! Dealer wins.")
                break
        elif decision.startswith('stand') or decision.startswith('s'):
            break

    # Dealer's turn
    dealer_total = calculate_total(dealer_hand)
    while dealer_total < 17:
        dealer_hand.append(random.randint(1, 13))
        dealer_total = calculate_total(dealer_hand)

    print("Dealer's hand is:", dealer_hand)
    print("The total of dealer's hand is:", dealer_total)

    # Determine the winner
    player_total = calculate_total(player_hand)
    if dealer_total > 21 or (21 >= player_total > dealer_total):
        print("Congratulations! You beat the dealer!")
        balance += bet * 2
    elif player_total == dealer_total:
        print("It's a tie! You get your bet back.")
        balance += bet
    else:
        print("Too bad, the dealer beat you!")

    # Ask if the player wants to continue or exit
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Game over! You've either run out of money or chosen to exit.")
