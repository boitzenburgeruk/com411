def run():
    lives = int(input("Please enter the number of lives: "))
    energy = int(input("Please enter the energy level: "))
    shield = int(input("Please enter the shield level: "))
    livesSign = "♥"
    energyAndShieldSign = "♦"
    
    print("\nHealth has been set\n")
    print("Lives: " + (livesSign*lives))
    print("Energy: " + (energyAndShieldSign*energy))
    print("Shield: " + (energyAndShieldSign*shield))
