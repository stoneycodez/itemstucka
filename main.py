spisok = ["Tamerlan", "Selim", "Fazil"]

for i in spisok:
    if i == "Selim":
        spisok.remove("Selim")
        spisok.remove("Fazil")
        spisok.append("Nihat")
        spisok.append("Fazil")

print(spisok)
