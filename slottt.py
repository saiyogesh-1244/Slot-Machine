import random


symbols = ["🍒", "🍋", "🍇", "🍉", "⭐", "7️⃣"]


def spin():
    return [random.choice(symbols) for _ in range(3)]


def check_win(result, bet):
    if result[0] == result[1] == result[2]:
        return bet * 5  
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        return bet * 2  
    else:
        return 0  

def main():
    balance = 100  
    print("🎰 Welcome to the Python Slot Machine! 🎰")
    print("You start with $100")
    
    while balance > 0:
        print(f"\nYour balance: ${balance}")
        try:
            bet = int(input("Enter your bet (or 0 to quit): $"))
        except ValueError:
            print("❌ Invalid input, try again.")
            continue

        if bet == 0:
            print("👋 Thanks for playing! Goodbye!")
            break
        elif bet > balance:
            print("❌ You don't have enough balance!")
            continue
        elif bet < 0:
            print("❌ Bet must be positive!")
            continue

        
        result = spin()
        print("Spinning... 🎲")
        print(" | ".join(result))

        
        winnings = check_win(result, bet)
        balance += winnings - bet

        if winnings > 0:
            print(f"🎉 You won ${winnings}!")
        else:
            print("😢 You lost this round.")

    if balance == 0:
        print("💀 You are out of money! Game Over.")

if __name__ == "__main__":
    main()
