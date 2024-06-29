import random
cislo = random.randint(1,10)










import time
x = 0
while x < 10:
    print(x)
    x += 1

    if x % 5 == 0:
        print("x je delitelny 5")
    print("po cyklu")
python = int(input)
python = "ahoj svete"
print("zacatek")
while python < 3:
    print(python)
    python += "ahoj python"
    
#reseni:
cislo_opakovani = 0
pocet_opakovani = int(input())
while cislo_opakovani < pocet_opakovani:
    print("ahoj svete")
    cislo_opakovani += 1

progres = int(input())
while progres > 0:
    print(progres)
    progres -= 1
    time.sleep(1)
if progres == 0:
    print("BOOM")    
