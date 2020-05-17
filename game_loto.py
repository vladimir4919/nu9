from prepare_loto import Bag,Person,Computer,Dropout

#выбираем кто играет:компьютер или человек
def choice_of_gamers(num_of_gamers):
    choice = None
    while choice not in ['c', 'p']:
        print(num_of_gamers, " геймер человек (person) или компьютер(c) ?")
        choice = input("(c/p): ")
    if choice == "c":
        return Computer()
    return Person()


print("Выбираем:сколько игроков участвует?")
count_of_gamers = int(input("Введите количество игроков: "))
gamers = []
for i in range(count_of_gamers):
    gamer = choice_of_gamers(i + 1)
    gamers.append(gamer)

bag = Bag()


while bag.samples:
    num = bag.select_sample()
    for i in range(count_of_gamers):
        if not isinstance(gamers[i],Dropout):
            print("Ход", i + 1, " геймера")
        if not gamers[i].act(num):
            gamers[i] = Dropout()
        if gamers[i].is_victory():
            print(i + 1, " игрок победил")
            break
