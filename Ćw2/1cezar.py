def szyfr_cezara(s, klucz):
    zaszyfrowany_tekst = ""
    for char in s:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            zaszyfrowany_tekst += chr((ord(char) - start + klucz) % 26 + start)
        else:
            zaszyfrowany_tekst += char
    return zaszyfrowany_tekst

def odszyfruj_cezara(s, klucz):
    return szyfr_cezara(s, -klucz)

tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = int(input("Podaj klucz (liczba): "))

zaszyfrowany = szyfr_cezara(tekst, klucz)
print(f"Zaszyfrowany tekst: {zaszyfrowany}")

odszyfrowany = odszyfruj_cezara(zaszyfrowany, klucz)
print(f"Odszyfrowany tekst: {odszyfrowany}")
