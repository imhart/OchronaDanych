import string
from collections import Counter


czestotliwosci_polskie = {'a': 0.097, 'b': 0.022, 'c': 0.035, 'd': 0.034, 'e': 0.089, 'f': 0.022,
                         'g': 0.020, 'h': 0.029, 'i': 0.076, 'j': 0.014, 'k': 0.035, 'l': 0.043,
                         'm': 0.029, 'n': 0.070, 'o': 0.068, 'p': 0.027, 'r': 0.061, 's': 0.049,
                         't': 0.037, 'u': 0.025, 'w': 0.042, 'z': 0.027}

def szyfr_cezara(tekst, klucz):
    zaszyfrowany_tekst = ""
    for char in tekst:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            zaszyfrowany_tekst += chr((ord(char) - start + klucz) % 26 + start)
        else:
            zaszyfrowany_tekst += char
    return zaszyfrowany_tekst


def oblicz_czestotliwosci(tekst):
    tekst = tekst.lower()
    czestotliwosci = Counter(c for c in tekst if c in string.ascii_lowercase)
    total = sum(czestotliwosci.values())
    for key in czestotliwosci:
        czestotliwosci[key] /= total
    return czestotliwosci


def lam_szyfr_cezara(tekst_zaszyfrowany, liczba_wynikow=10):
    czestotliwosci_zaszyfrowane = oblicz_czestotliwosci(tekst_zaszyfrowany)

    wyniki = []
    for przesuniecie in range(26):
        tekst = szyfr_cezara(tekst_zaszyfrowany, -przesuniecie)
        czestotliwosci_odszyfrowane = oblicz_czestotliwosci(tekst)
        
        roznica = sum((czestotliwosci_zaszyfrowane.get(letter, 0) - czestotliwosci_polskie.get(letter, 0))**2
                      for letter in string.ascii_lowercase)
        
        wyniki.append((roznica, tekst, przesuniecie))
    
    wyniki.sort(key=lambda x: x[0])
    
    for i in range(min(liczba_wynikow, len(wyniki))):
        print(f"Wynik {i+1} (klucz {wyniki[i][2]}): {wyniki[i][1]}")

tekst = input("Podaj tekst do złamania: ")
liczba_wynikow = int(input("Podaj liczbę wyników do wyświetlenia (max 10): "))

lam_szyfr_cezara(tekst, liczba_wynikow)
