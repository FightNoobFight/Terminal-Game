import random
import time
Players_health = 100
Player_Attack = random.randint(3,5)
Additional_Attack_Boost = Player_Attack + 10
Potion = 10
Boss_health = 200
Boss_attack = random.randint(4,7)
Boss_minor_Attack = random.randint(2,4)
Boss_PowerfulAttack = random.randint(8,10)
Moves = ["attack", "block", "heal", "boost"]
boss_healed = False


Announcement = print("Welcome player to the adventure of your imagination! \n In this game mode, you will travel through the dark dungeon, trying to find your way out! \n However, this isn't your ordinary dungeon, you may encounter something in the abyss.")
Name = input("How would you like to be refer to as? ")


while True:
    Choices_1 = input("Now, how shall you continue this journey? There's two gateway, which one would you choose? The right or left? ").lower()

    if Choices_1 == "right" or Choices_1 == "left":
        break
    else:
        print("It seems you have typed in the wrong command. Try spelling ""right"" or ""left"" correctly")


if Choices_1 == "left":
        print(f"{Name} has chosen the gateway of left, he's now encounter yet another gateway, only this time he's standing to a single gateway.")
        print(f"...... {Name} decided to continue walking on the path. The light as now appeared, he's finally at the entrance.")
        print(f"Congratulations, {Name} you have picked the right choice and now you're safe from whatever what've lured there.")
        print("THE END")
        exit()

    



if Choices_1 == "right":
    print(f"Oh no! {Name} you have fallen into this massive giant hole! You're now hearing this weird sound. Oh no! You have woken up the monster!")
    print(f"You are now frigtening, but there's no where to run! The only way of escaping is entering that gateway behind the boss! However, there's an issue. The boss is blocking the gateway and now you're stuck. What will happen {Name}? ")
      
    Character_move = input("What's your first action? Attack? or Run? ").lower()

    while True:
        if Character_move == "attack" or Character_move == "run":
            break
        else:
            print("Wrong command. Try again with either 'attack' or 'run.")
            Character_move = input("What's your first action? Attack? or Run? ").lower()

        

    Survival_Chances = random.randint(0,1)

    if Character_move == "run":
        print(f"WARNING! There's only 50% chances you'll survive if you decided to run.")
        time.sleep(2)
                
        print(f"You have decided you run, maybe the possibility of survivng could happen without ever fighting the boss! Now let's see if you made it")
        if Survival_Chances == 1:
            print(f"It seems {Name} manage to get out of there. You're now full sprinting while hearing the boss's cries. You see a very dim bright light across the dungeon. Congratulations! You are now out of the dungeon, and into the free world!")
            print("THE END")
        else:
            print(f"Unfortunately, it seems the boss managed to grab you. You're not stuck in the boss grasp, clingy with your life! But now, it seems the boss crushed you, perishing your entire body with that crush.")
            print("THE END")
    elif Character_move == Moves[0].lower():
        print(f"{Name} decided to become a man on that day and strike the boss! It seems he had felt the strike")
        Boss_health -= Player_Attack
        print(f"The Boss health: {Boss_health}")
        print(f"Nice, it seems the boss has felt. However it's now upset! The boss is heading and planning on attacking you!")
        time.sleep(2)
        Players_health -= Boss_attack
        print(f"{Name}'s current health: {Players_health}")
        while True:
            Command = input("Would you like to continue the attack? say: (attack, block, or heal, or boost?) ").lower()
            if Command == Moves[0].lower():
                print(f"{Name} has decided to attack again!")
                Boss_health -= Player_Attack
                print(f"Boss also decided to attack aswell!")
                Players_health -= Boss_attack
            elif Command == Moves[1].lower():
                print(f"Player has succesfully block the boss upcoming attack!")
            elif Command == Moves[2].lower():
                print(f"{Name} decided to heal! ")
                Players_health += Potion
                print(f"However, it seems the boss decided to do a quick sneak attack!")
                Players_health -= Boss_minor_Attack
            elif Command == Moves[3].lower():
                print(f"{Name} has given himself a power boost to strike the boss! ")
                Boss_health -= Additional_Attack_Boost
                print(f"However, it seems the boss retaliate from that offensive! ")
                Players_health -= Boss_PowerfulAttack
            else:
                print(f"Wrong command. {Name}")

            if Boss_health <= 95 and not boss_healed:
                print(f"It seems the Boss is aware of his current situation, so he decided to heal!")
                heal_amount = random.randint(10, 15)
                Boss_health += heal_amount
                print(f"The Boss has healed for {heal_amount} HP!")
                boss_healed = True
                
            
            print(f"Boss's current health: {Boss_health}")
            print(f"{Name}'s current health: {Players_health}")




            if (Players_health <= 0):
                print(f"Unfortunately {Name}, it seems you have failed to defeat the boss...")
            elif (Boss_health <= 0):
                print(f"Congratulations! You have defeated the boss! You can now enter through the gateway that needs to your freedom.")
                print("THE END")


            
    

    



