from os import system, name
import random
from time import sleep

team1 = [] 
team2 = []


def waiting_exit():
    input_user = None
    while input_user != "":
        input_user = input("\n-|ENTER para salir|-")


def clear_screen():
    if name == 'nt':
        return system('cls')
 
    else:
        return system('clear')


def num_players_def(clear_screen):
    num_players = int(input("Ingrese la cantidad de jugadores (la cantidad tiene que ser divisible por 2): "))
    while num_players %2 != 0:
            clear_screen()
            num_players = int(input(f"Tu numero ({num_players}) NO es divisible por 2, intente nuevamente: \n"))
    return num_players


def players_names(clear_screen, num_players_def):
    users = []
    for nro in range (1, num_players_def+1):
        clear_screen()
        print(users)
        name = str(input(f"Ingrese el nombre del jugador nro {nro}: \n")).capitalize()
        users.append(name)
    return users


def print_team():
    clear_screen()
    print(f" EQUIPO 1 (CT): {team1}")
    print(f" EQUIPO 2 (TT): {team2}")
    sleep(1.5)


def raffle(print_team, users):
    while len(team1) != len(users)/2:
        random_user = random.choice(users)
        if random_user not in team1:
            print_team()
            team1.append(random_user)

    print_team()
    if len(team1) == len(users) / 2:
        for i in users:
            if i not in team1:
                team2.append(i)
                print_team()


def main():
    clear_screen()
    users = players_names(clear_screen, num_players_def(clear_screen))
    raffle(print_team, users)
    waiting_exit()


if __name__ == "__main__":
    main()
