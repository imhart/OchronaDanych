def szyfr_vigenere(tekst, klucz):
    zaszyfrowany_tekst = ""
    klucz = (klucz * (len(tekst) // len(klucz))) + klucz[:len(tekst) % len(klucz)]  # Dopasowanie długości klucza do tekstu
    for i in range(len(tekst)):
        t = tekst[i]
        k = klucz[i]

        if t.isalpha():
            start = 65 if t.isupper() else 97
            zaszyfrowany_tekst += chr((ord(t) - start + ord(k.upper()) - 65) % 26 + start)
        else:
            zaszyfrowany_tekst += t

    return zaszyfrowany_tekst

def odszyfruj_vigenere(tekst, klucz):
    odszyfrowany_tekst = ""
    klucz = (klucz * (len(tekst) // len(klucz))) + klucz[:len(tekst) % len(klucz)]
    for i in range(len(tekst)):
        t = tekst[i]
        k = klucz[i]

        if t.isalpha():
            start = 65 if t.isupper() else 97
            odszyfrowany_tekst += chr((ord(t) - start - (ord(k.upper()) - 65)) % 26 + start)
        else:
            odszyfrowany_tekst += t

    return odszyfrowany_tekst

tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = input("Podaj klucz: ")

zaszyfrowany = szyfr_vigenere(tekst, klucz)
print(f"Zaszyfrowany tekst: {zaszyfrowany}")

odszyfrowany = odszyfruj_vigenere(zaszyfrowany, klucz)
print(f"Odszyfrowany tekst: {odszyfrowany}")
