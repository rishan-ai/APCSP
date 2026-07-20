import random
def roll_dice(num_dice):
    return sorted([random.randint(1, 6) for _ in range(num_dice)], reverse=True)
def calculate_round(attacker_dice, defender_dice):
    attacker_rolls = roll_dice(attacker_dice)
    defender_rolls = roll_dice(defender_dice)
    attacker_losses = 0    
    defender_losses = 0
    for a, d in zip(attacker_rolls, defender_rolls):
        if a > d:
            defender_losses += 1        
        else:
            attacker_losses += 1
    return attacker_losses, defender_losses, attacker_rolls, defender_rolls
def simulate_battle(attacker_count, defender_count):
    rounds = []
    attacker_count -= 1
    while attacker_count > 0 and defender_count > 0:
        attacker_dice = min(attacker_count, 3) 
        defender_dice = min(defender_count, 2)  
        attacker_losses, defender_losses, attacker_rolls, defender_rolls = calculate_round(attacker_dice, defender_dice)
        attacker_count -= attacker_losses
        defender_count -= defender_losses
        rounds.append({
            "attacker_losses": attacker_losses,
            "defender_losses": defender_losses,
            "remaining_attackers": attacker_count,
            "remaining_defenders": defender_count,
            "attacker_rolls": attacker_rolls,
            "defender_rolls": defender_rolls
        })
    return rounds
def main():
    attacker_count = int(input("Enter the number of attacking armies: "))
    defender_count = int(input("Enter the number of defending armies: "))
    rounds = simulate_battle(attacker_count, defender_count)
    print("\nBattle Results:")
    for i, round_result in enumerate(rounds):
        print(f"Round {i + 1}:")        
        print(f"Dice Rolls: " , round_result['attacker_rolls'] , round_result['defender_rolls'])
        print(f"  Attacker Losses: {round_result['attacker_losses']}")
        print(f"  Defender Losses: {round_result['defender_losses']}")
        print(f"  Remaining Attackers: {round_result['remaining_attackers']}")
        print(f"  Remaining Defenders: {round_result['remaining_defenders']}\n")
    if rounds:
        final_attacker = rounds[-1]['remaining_attackers']
        final_defender = rounds[-1]['remaining_defenders']
        if final_attacker > 0:
            print("Attackers win!")
        elif final_defender > 0:
            print("Defenders win!")
        else:
            print("It's a tie!")
choice = input("Would you like to simulate the battle or the odds(Choose 'odds' or 'battle')")
if choice == "battle":
  main()
elif choice == "odds":
    attakers = int(input("How many attackers are there?"))
    defenders = int(input("How many defenders are there?"))
    attakers_wins = 0
    defenders_wins = 0
    for i in range(10000):
        attacker_count = attakers
        defender_count = defenders
        rounds = simulate_battle(attacker_count, defender_count)
        if rounds:
            final_attacker = rounds[-1]['remaining_attackers']
            final_defender = rounds[-1]['remaining_defenders']
            if final_attacker > 0:
                attakers_wins += 1
            elif final_defender > 0:
                defenders_wins += 1
    print("The odds of the attackers winning is", attakers_wins/10000*100, "%")
    print("The odds of the defenders winning is",defenders_wins/10000*100, "%")
else:
    while choice != "battle" or choice != "odds":
        print("Invalid choice. Please enter 'battle' or 'odds'.")
        choice = input("Would You like to simulate the battle outcome or the odds(Choose 'odds' or 'battle')")w