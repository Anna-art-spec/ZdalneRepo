import os
import sys

print("Będzie to projekt zaliczeniowy")
file = open("help.txt", "r", encoding="utf-8")

def zakoczenie_programu():                                                                        #kończy program w wewnętrznej pętli
    haslo = input("naciśnij Enter aby zakończyć: ")
    if haslo == "":
        print("Koniec programu.")
    else:
        print(f"nieprawidłowy wybór klawisza")
def wyswietl_ponumerowane_pliki():                                                                 #wyświetla pliki funkcją ls
    lista = os.listdir()
    ponumerowane_pliki = [f"[{numer}] {plik}" for numer, plik in enumerate(lista, start=1)]

    # Wyświetla wszystkie ponumerowane pliki w jednej linii
    print(" ".join(ponumerowane_pliki))

def utworz_nowy_plik():                                                                             #tworzy nowy plik
    while True:
        nazwa_pliku = input("Wpisz nazwę nowego pliku i naciśnij Enter: ")

        if nazwa_pliku.strip():  # Sprawdza, czy nazwa pliku nie jest pusta
            try:
                with open(nazwa_pliku, 'w') as plik:
                    print(f"Plik o nazwie '{nazwa_pliku}' został utworzony.")
                break  # Przerywa pętlę, jeśli plik został utworzony poprawnie
            except Exception as e:
                print(f"Wystąpił błąd podczas tworzenia pliku: {e}")
        else:
            print("Nazwa pliku nie może być pusta. Spróbuj ponownie.")

def usun_plik(nazwa_pliku):                                                                        #usuwa plik
    try:
        os.remove(nazwa_pliku)
        print(f"Plik '{nazwa_pliku}' został usunięty.")
    except FileNotFoundError:
        print(f"Plik o nazwie '{nazwa_pliku}' nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd podczas usuwania pliku: {e}")


def utworz_katalog(nazwa_katalogu):                                                                  #tworzy katalog
    try:
        os.mkdir(nazwa_katalogu)
        print(f"Katalog o nazwie '{nazwa_katalogu}' został utworzony.")
    except FileExistsError:
        print(f"Katalog o nazwie '{nazwa_katalogu}' już istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd podczas tworzenia katalogu: {e}")

def usun_katalog(nazwa_katalogu):                                                                     #usuwa katalog
    try:
        os.rmdir(nazwa_katalogu)
        print(f"Katalog '{nazwa_katalogu}' został usunięty.")
    except FileNotFoundError:
        print(f"Katalog o nazwie '{nazwa_katalogu}' nie istnieje.")
    except OSError as e:
        print(f"Wystąpił błąd podczas usuwania katalogu '{nazwa_katalogu}': {e}")


def przejdz_do_katalogu():                                                                             #przejście do katalogu
    while True:
        nazwa_katalogu = input("Wpisz nazwę katalogu, do którego chcesz przejść: ")

        if nazwa_katalogu.strip():  # Sprawdza, czy nazwa katalogu nie jest pusta
            if os.path.isdir(nazwa_katalogu):  # Sprawdza, czy podana nazwa istnieje jako katalog
                os.chdir(nazwa_katalogu)  # Zmienia bieżący katalog na podany
                print(f"Przejście do katalogu '{nazwa_katalogu}' zostało zakończone.")
                break  # Przerywa pętlę, jeśli udało się przejść do katalogu
            else:
                print("Podany katalog nie istnieje. Spróbuj ponownie.")
        else:
            print("Nazwa katalogu nie może być pusta. Spróbuj ponownie.")

def wyswietl_zawartosc_pliku(nazwa_pliku):                                                              #wyświetla zawartość pliku
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            zawartosc = plik.read()
            print("Zawartość pliku:")
            print(zawartosc)
    except FileNotFoundError:
        print(f"Plik o nazwie '{nazwa_pliku}' nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd podczas wczytywania pliku: {e}")

def podsumowanie_ilosci_znakow(nazwa_pliku):                                                             #podaje ilość znaków
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            zawartosc = plik.read()
            ilosc_znakow = len(zawartosc)
            print(f"Podsumowanie ilości znaków w pliku '{nazwa_pliku}':")
            print(f"Ilość znaków: {ilosc_znakow}")
    except FileNotFoundError:
        print(f"Plik o nazwie '{nazwa_pliku}' nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd podczas wczytywania pliku: {e}")

def zmien_nazwe_pliku(stara_nazwa, nowa_nazwa):                                                          #zmienia nazwę pliku
    try:
        os.rename(stara_nazwa, nowa_nazwa)
        print(f"Nazwa pliku zmieniona z '{stara_nazwa}' na '{nowa_nazwa}'.")
    except FileNotFoundError:
        print(f"Plik o nazwie '{stara_nazwa}' nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zmiany nazwy pliku: {e}")

def wyszukaj_w_pliku(nazwa_pliku, szukany_tekst):                                                        #wyszukuje tekst w pliku
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            znaleziono = False
            for numer_linii, linia in enumerate(plik, start=1):
                if szukany_tekst in linia:
                    znaleziono = True
                    print(f"Znaleziono wiersz w pliku '{nazwa_pliku}', linijka {numer_linii}:")
                    print(linia.rstrip())  # Usunięcie znaku nowej linii z końca linii
            if not znaleziono:
                print(f"Nie znaleziono tekstu '{szukany_tekst}' w pliku '{nazwa_pliku}'.")
    except FileNotFoundError:
        print(f"Plik o nazwie '{nazwa_pliku}' nie istnieje.")
        return


while True:
    def main():
        while True:
            # Pobiera bieżącą ścieżkę dostępu
            sciezka = os.getcwd()

            # Wyświetla ścieżkę dostępu
            print(f"Aktualna ścieżka dostępu: {sciezka}")

            # Wprowadza komendę od użytkownika
            komenda = input("wpisz komendę z listy: ")

            if komenda == 'help':
                for line in file:
                    print(line.rstrip())
                file.seek(0)
                print(file.read())
                file.close()
                zakoczenie_programu()
                break

            if komenda.lower() == 'ls':
                wyswietl_ponumerowane_pliki()
                zakoczenie_programu()
                break

            if komenda == 'cr':
                utworz_nowy_plik()
                zakoczenie_programu()
                break

            if komenda == "delcr":
                nazwa_pliku = input("Podaj nazwę pliku do usunięcia: ")
                usun_plik(nazwa_pliku)
                zakoczenie_programu()
                break

            if komenda == 'cd':
                przejdz_do_katalogu()
                zakoczenie_programu()
                break

            if komenda == 'powrót':
                os.chdir("..")
                zakoczenie_programu()
                break

            if komenda == 'mkdir':
                nazwa_katalogu = input("Podaj nazwę katalogu, który chcesz utworzyć i naciśnij Enter: ")
                utworz_katalog(nazwa_katalogu)
                zakoczenie_programu()
                break

            if komenda == 'delmkdir':
                nazwa_katalogu = input("Podaj nazwę katalogu do usunięcia: ")
                usun_katalog(nazwa_katalogu)
                zakoczenie_programu()
                break

            if komenda == 'o':
                nazwa_pliku = input("Wpisz nazwę pliku, którego zawartość chcesz wyświetlić i naciśnij Enter: ")
                wyswietl_zawartosc_pliku(nazwa_pliku)
                zakoczenie_programu()
                break

            if komenda == 'stat':
                nazwa_pliku = input("Podaj nazwę pliku, którego ilość znaków chcesz podsumować: ")
                podsumowanie_ilosci_znakow(nazwa_pliku)
                zakoczenie_programu()
                break

            if komenda == 'rename':
                stara_nazwa = input("Podaj nazwę istniejącego pliku, którego nazwę chcesz zmienić: ")
                nowa_nazwa = input("Podaj nową nazwę pliku: ")
                zmien_nazwe_pliku(stara_nazwa, nowa_nazwa)
                zakoczenie_programu()
                break

            if komenda == 'find':
                nazwa_pliku = input("Podaj nazwę pliku: ")

                # Sprawdź, czy plik istnieje
                try:
                    with open(nazwa_pliku, 'r'):
                        pass
                except FileNotFoundError:
                    print(f"Plik o nazwie '{nazwa_pliku}' nie istnieje.")
                    break

                szukany_tekst = input("Podaj szukany tekst: ")

                wyszukaj_w_pliku(nazwa_pliku, szukany_tekst)
                zakoczenie_programu()
                break

            # Sprawdź czy użytkownik chce wyjść
            if komenda == "quit" or "exit":
                print("Koniec programu.")
                sys.exit()


            # Wykonuje komendę
            os.system(komenda)

    if __name__ == "__main__":
        main()
