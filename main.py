age = int(input("Bitte gebe dein Alter ein: "))

if age < 18:
        print("ACHTUNG, DER NUTZER IST JÜNGER ALS 18!")
elif age == 18:
    print("der Nutzer ist exakt 18!")
else:
         print("Der Nutzer ist volljährig!")