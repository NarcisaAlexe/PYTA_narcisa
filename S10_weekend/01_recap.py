"""
1.
- Instantiaza un un browser de Chrome.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra
"""

"""
2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
Incearca mai multe variante posibile.
"""

"""
3. Identifica elementul ce contine textul "Login Page"
si verifica, folosind un assert, ca acest element are textul asteptat
"""

"""
4. Identifica input-urile username si password,
introdu valori valide, si da click pe butonul login
"""

"""
5. Verifica, folosind un assert ca ai ajuns pe pagina
https://the-internet.herokuapp.com/secure
"""

"""
6. Da click pe butonul logout
"""

"""
7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
"""

"""
8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este [parola]"
"""