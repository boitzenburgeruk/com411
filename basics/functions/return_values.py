def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight


def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight) / 2
    return avg_weight


def run():
    beep = int(input("What is the weight of Beep? ").lower())
    bop = int(input("What is the weight of Bop? ").lower())
    choice = str(input("What would you like to calculate (sum or average)? "))
    if choice == "sum":
        print("The sum of Beep and Bop's weight is", sum_weights(beep, bop))
    elif choice == "average":
        print("The average weight of Beep and Bop is", calc_avg_weight(beep, bop))


run()
