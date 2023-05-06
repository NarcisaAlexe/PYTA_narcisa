# Partea 2 - Operatori, condiționale

# Exerciții - studiu în workshopul de weekend

# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

# IF-ul este un conditional. Practic ne ajuta sa executam cod in functie de anumite conditii.
# Intr-un if avem prima data definita ramura if. Aceasta se executa doar daca conditia de la if
# se evalueaza ca fiind adevarata.
# Daca conditia de la if nu e adevarata/ e false, atunci se va executa ramura else, daca aceasta exista.
# Putem sa mai avem si elif, care ne ajuta sa punem mai multe conditii.

# 2. Verifică și afișează dacă x este număr natural sau nu.
# x = int(input("X="))
# if x >0:
#     print("x este nr natural")
# else:
#     print("x nu este nr natural")


# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# x = int(input("X="))
# if x >0:
#     print("x este nr pozitiv")
# elif x<0:
#     print("x este negativ")
# else:
#     print("x este neutru")


# 4. Verifică și afișează dacă x este între -2 și 13.
# x = int(input("X="))
# if x -2<=x <=13:
#     print("x este in interval")
# else:
#     print("x nu este in interval")


# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# x = int(input("X="))
# y = int(input("y="))
# if x-y <5:
#     print("diferenta e mai mica decat 5")
# else:
#     print("diferenta este mai mare ca 5")


# 6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
# x = 28
# if not(5 <= x <= 27):
#     print('x nu este intre 5 si 27')
# else:
#     print('x este intre 5 si 27')


# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# x = 12
# y = 15
# if x == y:
#     print('sunt egale')
# elif x > y:
#     print('x mai mare decat y')
# else:
#     print('y este mai mare decat x')


# 8.
# x, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

# x = int(input("X="))
# y = int(input("y="))
# z = int(input("z="))
# if x==y==z:
#     print("echilateral")
# elif x==y or x==z or y==z:
#     print("isoscel")
# else:
#     print("oarecare")


# 9. Citește o literă de la tastatură.
#     Verifică și afișează dacă este vocală sau nu.
# x  = input("Litera")
# if x in ['a', 'e', 'i', 'o', 'u']:
#     print("este vocala")
# else:
#     print("e consoana")


# 10.Transformă și printează notele din sistem românesc în  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

# x = int(input("nota="))
# if x >= 9:
#     x = 'A'
# elif x >= 8:
#     x = 'B'
# elif x >= 7:
#     x = 'C'
# elif x >= 6:
#     x = 'D'
# elif x >= 4:
#     x = 'E'
# else:
#     x = 'F'
# print(x)


# 11.Verifică dacă x are minim 4 cifre (x e int).
# x = int(input('Introdu un numar: '))
# x = str(x)
# if len(x) >= 4:
#     print('Numarul introdus este format din minim 4 cifre.')
# else:
#     print('Numarul introdus are mai putin de 4 cifre.')
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)


# 12.Verifică dacă x are exact 6 cifre.
# solutia urmatoare nu este valabila pt nr negative
# x = int(input('Introdu un numar: '))
# # x = str(x)
# if len(x) == 6:
#     print('Numar introdus este format din 6 cifre.')
# elif len(x) < 6:
#     print('Numarul introdus este format din mai putin de 6 cifre.')
# else:
#     print('Numarul introdus este format din mai mult de 6 cifre.')


# 13.Verifică dacă x este număr par sau impar (x e int).

# x = int(input("x:"))
# if x % 2 ==0:
#     print("par")
# else:
#     print("impar")


# 14.      x, y, z (int)
# Afișează care este cel mai mare dintre ele?

# x = int(input("X="))
# y = int(input("y="))
# z = int(input("z="))
# max = 0
# if x >y and x>z:
#     print("x e cel mai mare")
#     max = x
# elif y> x and y>z:
#     print("y e cel mai mare")
# elif z>x and z>y:
#     print("z este cel mai mare")
# elif x == y == z:
#     print("nr sunt egale")
# else:
#     print("doua sunt egale")


# 15.
# x, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citește de la tastatură un int x
# Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

# x = int(input("X="))
# stringus = 'Coral is either the stupidest animal or the smartest rock'
# print(stringus[:-x])

# 17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
# stringus = 'Coral is either the stupidest animal or the smartest rock'
# str2 = stringus[:5]+stringus[-5:]
# print(stringus[:-5])
# print(str2)

# 18. Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# output: 'Coral is either the stupidest animal or the smartest'

# stringus = 'Coral is either the stupidest animal or the smartest rock'
# str2 = stringus.index('rock')
# print(stringus[:str2])

# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

# 20.  Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

# 21. Având stringul '0123456789'
# Afișează doar numerele pare
# Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)