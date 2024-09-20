# 1. Vytvořte proměnnou, do které vložíte své jméno
jmeno = "Oleksandra"
# 2. Vytvořte proměnnou, do které vložíte své příjmení
prijmeni = "Maslova"
# 3. Vypište tyto dvě proměnné do konzole.
print("Jméno:", jmeno)
print("Příjmení:", prijmeni)
# 4. Vstup pro uživatele (věk)
while True:
    try:
        vek = int(input("Zadej svůj věk: "))
        break
    except ValueError:
        print("Zadej prosím celé číslo.")
# 5. Výpis délky jména a příjmení
print("Délka jména:", len(jmeno))
print("Délka příjmení:", len(prijmeni))
# 6. Vytvořte proměnnou, do které uložíte hodnotu 6.
cislo = 6
# 7. Vytvořte cyklus, který bude mít 5 opakování a při každém opakování se přičte hodnota 3.
for _ in range(5):
    cislo += 3
# 8. Vypište v konzoli výslednou hodnotu po 5 cyklech.
print("Výsledná hodnota:", cislo)
# 9. Vytvořte podmínku pro uživatele, který zadá věk
if isinstance(vek, int):
    print("Děkuji.")
else:
    print("Zadej jen celočíselnou hodnotu.")
# 10. Vytvořte proměnnou, do které uloží program náhodnou hodnotu od 1-10 a vypište ji do konzole. 
import random
nahodne_cislo = random.randint(1, 10)
print("Náhodné číslo:", nahodne_cislo)