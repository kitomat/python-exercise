a =int(input("what is the number one: "))
b =int(input("what is the number two: "))
operator=(input("zadejte operatora: "))
if operator=="+":
    soucet=a+b
    print(soucet)
elif operator=="-":
    rozdil=a-b
    print(rozdil)
elif operator=="*":
    soucin=a*b
    print(soucin)
elif operator=="/":
    podil=a/b
    print(podil)
elif operator=="//":
    vysledek=a//b
    print(vysledek)    
elif operator=="%":
    procenta=a%b
    print(procenta)
else:
    print("neznam dalsiho operatora")
    