import random
import os


Word_List = []
try:
    wordfile = open("words.txt", "r")

    Word_List = wordfile.read()
    Word_List = Word_List.split()
    wordfile.close()
except:
    print("Ups! I can't find 'words.txt', sorry :(")
    exit()


while True:
    randList = []
    randword = (Word_List[random.randint(0,len(Word_List)-1)])
    randList = [s for s in randword]
    health = 3
    print(randList)
    print('''  _______
   |    |   ''')
    print('   |         ')
    print('   |         ')
    print('   |         ')
    print('   |         ')
    print('   |         ')
    print('   |         ')
    print('___|___      ')

    game_inp = input("Hey! I choose a word. Do you wanna find it? ( To continue type y or to exit type q ) : ")
    if game_inp == "y" or game_inp == "Y":
        print("Okay our word has ({}) character so type a character to guess word :o".format(len(randword)))
        hidden_typer = []
        for i in range(len(randword)):
            hidden_typer.append("_")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if health <= 0:
                print("Sorry bro, he is gone\n\n\n")
                print('''  _______
   |    |   ''')
                print('   |    O    ')
                print('   |    |    ')
                print('   |  \- -/  ')
                print('   |    |    ')
                print('   |   / \\  ')
                print('   |  /   \\ ')
                print('___|___      ')

                input("Press enter to continue")
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            if "_" not in hidden_typer:
                print("You winnnn dude, you saved the guy from hanging :D")
                break
            else:
                for i in range(len(hidden_typer)):
                    print(hidden_typer[i], end = "")
                print("")
                get_ch = str(input("Type character(A - Z): "))
                get_ch = get_ch.upper()
                if get_ch in randList:
                    for i in range(len(randword)):
                        if get_ch == randList[i]:
                            hidden_typer[i] = get_ch

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    health -= 1
                    print("Upss this character, i couldn't find it in my word :O You are loosing your health {}/3".format(health))
                    if health < 3:
                        print('''  _______
   |    |   ''')
                        print('   |    O    ')
                        print('   |    |    ')
                    if health < 2:
                        print('   |  \- -/  ')
                        print('   |    |    ')
                    if health < 1 and health == 0:
                        print('   |   / \\  ')
                        print('   |  /   \\ ')
                        print('___|___      ')

                    input("Press enter to continue")

    elif game_inp == "q" or game_inp == "Q":
        print("Good bye :)")
        exit()
    else:
        print("Undefined variable")