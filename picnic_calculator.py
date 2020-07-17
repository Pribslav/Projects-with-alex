def party(ch, cr, p):
    if int(ch) >= 3 * int(p):
        if int(cr) >= 1 * int(p):
            print("that's enough for a party \n grab a blanket!")
        else:
            print("That's not enough for a party *sadface*")
    else:
        print("That's not enough for a party *sadface*")

people = input("How many people be coming?")
cheese = input("How much cheese do you have?")
crackers = input("How many boxes of crackers do you have?")

party(cheese, crackers, people)
