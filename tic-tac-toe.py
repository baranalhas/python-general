import os

matrix_table = ["1","2","3","4","5","6","7","8","9"]
win_list = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
player1_turn = True

def show_table():
    print(f"""
          {matrix_table[0]} | {matrix_table[1]} | {matrix_table[2]}
         ___________
          
          {matrix_table[3]} | {matrix_table[4]} | {matrix_table[5]}
         __________
          
          {matrix_table[6]} | {matrix_table[7]} | {matrix_table[8]}
          """)
def check_win():
    global matrix_table
    global player1_turn

    for i in win_list:
        if (matrix_table[i[0]] == matrix_table[i[1]] == matrix_table[i[2]] == "X"):
            show_table()
            print("Player 1(X) kazandı!!")
            matrix_table = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            input("")
            os.system('cls' if os.name == 'nt' else 'clear')
            player1_turn = True
        elif (matrix_table[i[0]] == matrix_table[i[1]] == matrix_table[i[2]] == "O"):
            show_table()
            print("Player 2(O) kazandı!!")
            matrix_table = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            input("")
            player1_turn = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            z = 0
            for q in range (0,9):
                if matrix_table[q] == "X" or matrix_table[q] == "O":
                    z +=1
            if z == 9:
                show_table()
                print("Oyun berabere bitti :)")
                matrix_table = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                player1_turn = True
                input("")
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
def select_box():
    global player1_turn
    global matrix_table
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Çıkmak için seçiminizi q olarak yapabilirsiniz")
    while True:
        check_win()
        show_table()
        get_var = input("işaretlemek istediğiniz kutuyu seçin: ")
        if get_var == "q" or get_var == "Q":
            exit()
        if not get_var.isnumeric():
            print("Sadece sayısal değerler(1-9)")
            continue
        get_var = int(get_var)
        get_var = get_var - 1
        if get_var not in range(0,9):
            print("Üzgünüm böyle bir kutu yok")
            continue
        if matrix_table[get_var] == "X" or matrix_table[get_var] == "O":
            print("Üzgünüm bu kutu dolu, lütfen tekrar dene!")
            continue
        if player1_turn:
            matrix_table[get_var] = "X"
            player1_turn = False
        else:
            matrix_table[get_var] = "O"
            player1_turn = True
        os.system('cls' if os.name == 'nt' else 'clear')

while True:
    select_box()