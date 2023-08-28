class chelovek:
    def __init__(self, fname, fsurname, fage):
        self.__name = fname
        self.__surname = fsurname
        self.__age = fage

    def TakeName(self):
        return self.__name

    def TakeSurname(self):
        return self.__surname

    def TakeAge(self):
        return self.__age


cheloveki = []
human1 = chelovek("Kamal", "Badalzade", 15)
human2 = chelovek("Omar", "Isayev", 15)
human3 = chelovek("Chingiz", "Dzhalilov", 15)

cheloveki.append(human1.TakeName())
cheloveki.append(human2.TakeName())
cheloveki.append(human3.TakeName())

name = input("enter name: ")


for i in cheloveki:
    if name == i:
        print("its in the list!")
        break
    else:
        print("it is not in the list!")

