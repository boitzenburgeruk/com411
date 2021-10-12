def run():
    hear = str(input("What did I hear? ").lower())
    see = str(input("What did I see? ").lower())

    if hear == "grrr" and see == "two red eyes":
        print("There is a scary creature! I should get out of here!")
    else:
        print("I am a little scared... But I will continue!")