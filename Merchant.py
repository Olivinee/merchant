import time
gold = 100
carrot = 20
apple = 30
carrotCount = 5
appleCount = 5
choice = ""

def printMenu():
    print("                        ")
    print("--------MERCHANT--------")
    print("                        ")
    print("------------------------")
    print("Your current gold is",gold)
    print("a - Open sell menu")
    print("b - Open buy menu")
    print("c - Open grow menu")
    print("d - Open inventory")
    print("e - Exit game")
    print("------------------------")
    print("                        ")
    choice = input("Choose an option: ")
    if choice == 'a':
        sellMenu()
    elif choice == 'b':
        buyMenu()
    elif choice == 'c':
        growMenu()
    elif choice == 'd':
        inventoryMenu()
    elif choice == 'e':
        exitGame()
    else:
        print("ERROR")
        time.sleep(2)
        printMenu()


def sellMenu():
    global gold
    print("                        ")
    print("------------------------")
    print("a - Sell carrot.....+20G")
    print("b - Sell apple......+30G")
    print("c - Cancel              ")
    print("------------------------")
    print("                        ")
    choice = input("Choose an option: ")
    if choice == 'a':
        sellCarrot()
    elif choice == 'b':
        sellApple()
    elif choice == 'c':
        printMenu()
    else:
        print("ERROR")


def buyMenu():
    global gold
    print("                        ")
    print("------------------------")
    print("a - Buy carrot......-20G")
    print("b - Buy apple.......-30G")
    print("c - Cancel              ")
    print("------------------------")
    print("                        ")
    choice = input("Choose an option: ")
    if choice == 'a':
        buyCarrot()
    elif choice == 'b':
        buyApple()
    elif choice == 'c':
        printMenu()
    else:
        print("ERROR")
        time.sleep(5)
        printMenu()

def inventoryMenu():
    global carrotCount
    global appleCount
    global gold
    print("                        ")
    print("------------------------")
    print("Carrots - ",carrotCount)
    print("Apples  - ",appleCount)
    print("Gold    - ",gold)
    print("------------------------")
        
    if carrotCount < 0:
        carrotCount = 0
        print("                        ")
        print("------------------------")
        print("Carrots can't be < 0!   ")
        print("------------------------")

    if appleCount < 0:
        appleCount = 0
        print("                        ")
        print("------------------------")
        print("Apples can't be < 0!    ")
        print("------------------------")

    cheatmenu = input(" ")
    if cheatmenu == 'wasd':
        cheatMenu()

    time.sleep(5)
    printMenu()


def sellCarrot():
    global gold
    global carrotCount
    print("                        ")
    print("------------------------")
    print("Selling carrot..........")
    print("------------------------")
    print("                        ")
    carrotCount = carrotCount - 1
    time.sleep(5)
    print("------------------------")
    print("Carrot sold!            ")
    print("You have",carrotCount,"carrots!")
    print("Your gold is now",gold+carrot)
    print("------------------------")
    gold = gold + carrot

    if gold > 10000:
        gold = 9999
        print("                        ")
        print("------------------------")
        print("Gold is capped at 9999! ")
        print("------------------------")

    time.sleep(5)
    printMenu()

def buyCarrot():
    global gold
    global carrotCount
    if gold < 19:
        print("                        ")
        print("------------------------")
        print("Not enough gold!        ")
        print("------------------------")
        print("                        ")
        time.sleep(2)
        printMenu()

    elif gold > 19:
        print("                        ")
        print("------------------------")
        print("Buying carrot...........")
        print("------------------------")
        print("                        ")
        carrotCount = carrotCount + 1
        time.sleep(2)
        print("                        ")
        print("------------------------")
        print("Carrot bought!          ")
        print("You have",carrotCount,"carrots!")
        print("Your gold is now",gold - carrot)
        print("------------------------")
        print("                        ")
        gold = gold - carrot
        time.sleep(2)
        printMenu()

        if gold > 10000:
            gold = 9999
            print("                        ")
            print("------------------------")
            print("Gold is capped at 9999! ")
            print("------------------------")

    else:
        print("ERROR")

def buyApple():
    global gold
    global appleCount
    if gold < 20:
        print("                        ")
        print("------------------------")
        print("Not enough gold!        ")
        print("------------------------")
        print("                        ")
        time.sleep(2)
        printMenu()

    elif gold > 29:
        print("                        ")
        print("------------------------")
        print("Buying apple............")
        print("------------------------")
        print("                        ")
        appleCount = appleCount + 1
        time.sleep(2)
        print("                        ")
        print("------------------------")
        print("Apple bought!          ")
        print("You have",appleCount,"apples!")
        print("Your gold is now",gold - apple)
        print("------------------------")
        print("                        ")
        gold = gold - apple
        time.sleep(2)
        printMenu()

        if gold > 10000:
            gold = 9999
            print("                        ")
            print("------------------------")
            print("Gold is capped at 9999! ")
            print("------------------------")

    else:
        print("ERROR")

def sellApple():
    global gold
    global appleCount
    print("                        ")
    print("------------------------")
    print("Selling apple...........")
    print("------------------------")
    print("                        ")
    appleCount = appleCount - 1
    time.sleep(5)
    print("------------------------")
    print("Apple sold!            ")
    print("You have",appleCount,"carrots!")
    print("Your gold is now",gold+apple)
    print("------------------------")
    gold = gold + apple

    if gold > 10000:
        gold = 9999
        print("                        ")
        print("------------------------")
        print("Gold is capped at 9999! ")
        print("------------------------")

    time.sleep(5)


def exitGame():
    print("------------------------")
    print("Thanks for playing!")
    print("Created by Olivine ")
    print("------------------------")
    time.sleep(2)
    exit
    
def cheatMenu():
    global gold
    global appleCount
    global apple
    global carrotCount
    global carrot
    print("                        ")
    print("-------CHEAT MENU-------")
    print("                        ")
    print("------------------------")
    print("Your current gold is",gold)
    print("a - Change gold amount  ")
    print("b - Change apple amount ")
    print("c - Change carrot amount")
    print("d - Cancel")
    CheatChoice = input("Choose an option: ")

    if CheatChoice == 'a':
        ChangeGold()
    if CheatChoice == 'b':
        ChangeApple()
    if CheatChoice == 'c':
        ChangeCarrot()
    if CheatChoice == 'd':
        printMenu()
    else:
        print("ERROR")

    time.sleep(5)

printMenu()
