uziv_jmeno="Coding_Giants"
heslo1="python_program"
jmeno=input("enter your user name")
heslo2=input("enter your password")
if uziv_jmeno==jmeno and heslo1==heslo2:
    print("succes")
if uziv_jmeno!=jmeno and heslo1!=heslo2:
    print("incorrect") 
else:
    if uziv_jmeno == heslo1:
        print("incorrect password")
    if heslo1 == uziv_jmeno:
        print("incorrect user name")           