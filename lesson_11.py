#kontakt:matejbaco95@gmail.com
def fibonacci(kolik):
    if kolik < 1:
        return 0
    if kolik == 2:
        return [0,1]
    
    vysledek = [0,1]
    for i in range(kolik - 2):
        dalsi_cislo = vysledek[-1] + vysledek[-2]
        vysledek.append(dalsi_cislo)
    return vysledek
"""
while True:
    vstup = int(input("Zadejte kolik cisel chcete vypsat"))
    print(fibonacci(vstup))
"""      
def smile(seznam):
    seznam1=[]
    for i in seznam:
        if i not in seznam1:
            seznam1.append(i)
    return seznam1
print(smile([1,1,2,3,3,4,5,5,6,7,7,8,9]))