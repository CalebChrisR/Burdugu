from os import system
from os import name as OS_NAME
from time import sleep


def clear_screen():
    # for windows
    if OS_NAME == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def draw_body():
    cells = [(row, column) for row in range (32) for column in range(64)]
    print(cells)

def main() :
    # Clearing the Screen
    clear_screen()    
    draw_body()



if __name__ == "__main__" :
    main()