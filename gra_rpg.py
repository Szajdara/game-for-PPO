import sys
import random


if sys.stdout.encoding and sys.stdout.encoding.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# wszystko dla startu

def wyswietl_ekran_startowy():

    print("=" * 68)
    print("        [+] PRZETRWANIE W ZSK: DROGA DO DYREKCJI [+]")
    print("         Szkolna Gra Przygodowa RPG (Klasa 3B ZSK)")
    print("=" * 68)
    print("Wcielasz sie w odwaznego ucznia Zespolu Szkol Komunikacji w Poznaniu.")
    print("Nadszedl dzien ostatecznej klasyfikacji. Aby zdac do nastepnej klasy,")
    print("musisz przejsc przez 5 sal lekcyjnych i obronic sie przed nauczycielami,")
    print("a w ostatniej sali stanac twarza w twarz z sama DYRCIA!")
    print("-" * 68)
    print("ZASADY I STEROWANIE:")
    print(" * Wybieraj akcje wpisujac numer (np. 1, 2, 3) i wciskajac ENTER.")
    print(" * Twoje zdrowie (HP) to poziom Energii / Zdrowia Psychicznego.")
    print(" * Pokoje:")
    print("    - Pokoj 1: Wartaczyna")
    print("    - Pokoj 2: Jusia")
    print("    - Pokoj 3: Adaś")
    print("    - Pokoj 4: Agatka (Egzaminator)")
    print("    - Pokoj 5 (FINAL BOSS): Gabinet Dyrekcji - PANI DYREKTOR (DYRCIA)!")
    print(" * WARUNEK WYGRANEJ: Pokonanie Dyrci i zdobycie promocji z paskiem.")
    print(" * WARUNEK PRZEGRANEJ: Spadek Twojego HP do 0 (sierpniowa poprawka / kibel).")
    print(" * Na przerwach odwiedzaj sklepik, przeszukuj szafki (uwazaj na psikusy!)")
    print("   oraz pij energetyki (Monsterki), aby uzupelniac energie!")
    print("=" * 68)
    try:
        input("\nNacisnij [ENTER], aby przekroczyc prog szkoly...")
    except (EOFError, KeyboardInterrupt):
        print("\nDo widzenia!")
        sys.exit(0)
    print("\n")

# 2 funkcje pomocnicze i wejście

def pobierz_wybor(dozwolone_opcje):
    while True:
        try:
            wybor = input("\nTwoj wybor: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nUciekles ze szkoly na wagary. Koniec gry!")
            sys.exit(0)

        if wybor in dozwolone_opcje:
            return wybor
        opcje_tekst = ", ".join(dozwolone_opcje)
        print(f"Niepoprawny wybor! Wpisz jedna z dostepnych opcji: [{opcje_tekst}]")


def wyswietl_statystyki(uczen):
    print("\n" + "-" * 52)
    print(f" Uczen ZSK:            {uczen['imie']}")
    print(f" Energia / Zdrowie HP: {uczen['hp']} / {uczen['max_hp']}")
    print(f" Sila odpowiedzi:      {uczen['atak_min']} - {uczen['atak_max']}")
    print(f" Kasa na sklepik:      {uczen['kasa']} zl")
    print(f" Energetyki (Monster): {uczen['energetyki']} szt.")
    print(f" Ekwipunek:            {', '.join(uczen['ekwipunek'])}")
    print("-" * 52)


def wypij_energetyka(uczen):
    if uczen['energetyki'] <= 0:
        teksty_brak = [
            "\n[!] Twoj plecak jest pusty! Nie masz juz zadnego energetyka!",
            "\n[!] Szukasz po kieszeniach, ale znajdujesz tylko stare paragony!",
            "\n[!] Brak Monsterka w zapasie! Musisz odwiedzic szkolny sklepik!"
        ]
        print(random.choice(teksty_brak))
        return False

    if uczen['hp'] >= uczen['max_hp']:
        print("\n[!] Masz maksymalna energie! Szkoda marnowac drogiego Monstera na zapas.")
        return False

    przywrocenie = 35
    uczen['energetyki'] -= 1
    stare_hp = uczen['hp']
    uczen['hp'] = min(uczen['max_hp'], uczen['hp'] + przywrocenie)
    zysk = uczen['hp'] - stare_hp

    teksty_picia = [
        f"\n[+] Otworzyles puszke Monstera z glosnym sykiem! Chlodna kofeina przywraca Ci {zysk} HP! ({uczen['hp']}/{uczen['max_hp']})",
        f"\n[+] Wypiles duszkiem schlodzonego energetyka pod lawka! Zyskujesz {zysk} HP energii! ({uczen['hp']}/{uczen['max_hp']})",
        f"\n[+] Zastrzyk cukru i tauryny stawia Cie na nogi! Odzyskujesz {zysk} HP! ({uczen['hp']}/{uczen['max_hp']})"
    ]
    print(random.choice(teksty_picia))
    return True


# 3 walka

def walka_z_nauczycielem(uczen, nauczyciel):
    print("\n" + "/!\\ " * 15)
    print(f"DZWONEK NA LEKCJE! Przed Toba: {nauczyciel['nazwa']}!")
    print(f"Statystyki nauczyciela: {nauczyciel['hp']} HP | Sila pytan: {nauczyciel['atak_min']}-{nauczyciel['atak_max']}")
    powitanie = random.choice(nauczyciel['teksty_powitalne'])
    print(f'Nauczyciel wita Cie slowami: "{powitanie}"')
    print("/!\\ " * 15)

    # Petla turowej walki przy tablicy
    while nauczyciel['hp'] > 0 and uczen['hp'] > 0:
        print(f"\n--- SYTUACJA PRZY TABLICY ---")
        print(f"Twoja Energia (HP): {uczen['hp']}/{uczen['max_hp']}  |  Cierpliwosc Nauczyciela: {nauczyciel['hp']} HP")
        print("Co robisz?")
        print("1. Zwykla odpowiedz z podrecznika")
        print("2. Ryzykowne lanie wody (szansa na krytyka lub wtope)")
        print(f"3. Dyskretny lyk Monstera pod lawka (posiadasz: {uczen['energetyki']})")
        print("4. Prosba o wyjscie do toalety (ucieczka z lekcji)")

        wybor = pobierz_wybor(["1", "2", "3", "4"])

        # Akcja 1: Zwykla odpowiedz
        if wybor == "1":
            obrazenia = random.randint(uczen['atak_min'], uczen['atak_max'])
            nauczyciel['hp'] -= obrazenia
            teksty_zwykle = [
                f"\n-> Recytujesz z pamieci wyuczona formule z podrecznika! Nauczyciel traci {obrazenia} pkt cierpliwosci!",
                f"\n-> Pewnym glosem cytujesz definicje z wczorajszych notatek! Zadajesz {obrazenia} pkt obrazen!",
                f"\n-> Rzucasz wyuczonymi faktami prosto w tablice! Nauczyciel traci {obrazenia} pkt cierpliwosci!",
                f"\n-> Rysujesz poprawny schemat na tablicy pod czujnym okiem belfra (-{obrazenia} HP)!",
                f"\n-> Spokojnie i precyzyjnie odpowiadasz na podchwytliwe pytanie belfera za {obrazenia} pkt!"
            ]
            print(random.choice(teksty_zwykle))

        # Akcja 2: Lanie wody
        elif wybor == "2":
            udane = random.choice([True, True, False])  # 66% szans
            if udane:
                obrazenia = int(random.randint(uczen['atak_min'], uczen['atak_max']) * 1.65)
                nauczyciel['hp'] -= obrazenia
                teksty_sukces = [
                    f"\n-> GENIALNA IMPROWIZACJA! Zaginasz belfra teoria z Wikipedii i Reddita za potezne {obrazenia} pkt!",
                    f"\n-> MOWCA ROKU! Opowiadasz tak kwieciscie, ze nauczyciel sam zwatpil w podrecznik (-{obrazenia} HP)!",
                    f"\n-> BLEF STULECIA! Polaczyles trzy losowe trudne slowa i stworzyles nowa teorie (-{obrazenia} HP)!",
                    f"\n-> Plyniesz z tematem jak natchniony! Cala klasa zbiera szczeki z podlogi! (-{obrazenia} HP)!",
                    f"\n-> Nauczyciel kiwa z uznaniem glowa, myslac ze czytales literature akademicka! (-{obrazenia} HP)!"
                ]
                print(random.choice(teksty_sukces))
            else:
                teksty_porazka = [
                    "\n-> Pomyliles pojecia! Nauczyciel tylko z politowaniem pokrecil glowa... (0 pkt)!",
                    "\n-> Zaczesz opowiadac o grach wideo zamiast o temacie lekcji! Totalna kompromitacja (0 pkt)!",
                    "\n-> Nauczyciel przerywa: 'Co pan za bzdury opowiada?! Siadaj pan, dwoja wisi w powietrzu!' (0 pkt)!",
                    "\n-> Zaplatales sie we wlasnych myslach i zamilkles w niezrecznej ciszy... (0 pkt)!",
                    "\n-> Nauczyciel pyta z politowaniem: 'Czy pan w ogole wie, na jakiej jest lekcji?!' (0 pkt)!"
                ]
                print(random.choice(teksty_porazka))

        # Akcja 3: Leczenie
        elif wybor == "3":
            sukces = wypij_energetyka(uczen)
            if not sukces:
                continue  # Nie traci tury jesli nie ma napoju

        # Akcja 4: Ucieczka do toalety
        elif wybor == "4":
            if nauczyciel.get('czy_boss', False):
                teksty_boss_ucieczka = [
                    "\n[!] Z gabinetu Dyrci nie ma ucieczki! Dyrcia patrzy na Ciebie lodowatym wzrokiem!",
                    "\n[!] Proba ucieczki przed Dyrcia? Drzwi sa zamkniete, musisz dokonczyc rozmowe!",
                    "\n[!] 'Dokad to, mlody czlowieku? Jeszcze z panem nie skonczylam!' - mowi stanowczo Dyrcia."
                ]
                print(random.choice(teksty_boss_ucieczka))
            else:
                szansa = random.random()
                if szansa < 0.5:
                    teksty_udana_ucieczka = [
                        "\n[+] Nauczyciel machnal reka: 'Idz pan, i nie wracaj do dzwonka!' Unikasz jedynki!",
                        "\n[+] 'Szybko, bo zaczynamy nowy temat!' - uciekasz do toalety i przeczekujesz lekcje!",
                        "\n[+] Wybiegasz z sali pod pretekstem krwotoku z nosa! Udalo sie uniknac pytania!"
                    ]
                    print(random.choice(teksty_udana_ucieczka))
                    return True
                else:
                    teksty_nieudana_ucieczka = [
                        '\n[-] Nauczyciel mowi: "Siadaj pan na miejsce, dzwonek jest dla mnie, a nie dla pana!"',
                        '\n[-] "Toaleta byla na przerwie! Teraz odpowiadamy przy tablicy!" - nici z ucieczki!',
                        '\n[-] "Nigdzie pan nie pojdzie, dopoki nie uslysze poprawnej odpowiedzi!"'
                    ]
                    print(random.choice(teksty_nieudana_ucieczka))

        # Sprawdzenie czy nauczyciel zostal pokonany (przedmiot zaliczony)
        if nauczyciel['hp'] <= 0:
            teksty_wygrana = [
                f"\n[+] BRAWO! Nauczyciel ma dosc i stawia Ci 5 w Librusie! Zaliczyles przedmiot u: {nauczyciel['nazwa']}!",
                f"\n[+] Nauczyciel kaze Ci siadac: 'No dobrze, zaskoczyl mnie pan'. Przedmiot zaliczony!",
                f"\n[+] Nauczyciel zrezygnowany macha reka: 'Dosc na dzisiaj, wpisuje bardzo dobry!' Sukces!"
            ]
            print(random.choice(teksty_wygrana))
            uczen['zaliczonych_przedmiotow'] += 1
            nagroda = random.randint(nauczyciel['nagroda_kasa_min'], nauczyciel['nagroda_kasa_max'])
            uczen['kasa'] += nagroda
            print(f'Znajdujesz w kieszeni {nagroda} zl na przerwe! (Stan konta: {uczen["kasa"]} zl)')

            # Szansa na znalezienie energetyka w lawce
            if random.random() < 0.45:
                uczen['energetyki'] += 1
                print("[+] Ktos w lawce obok zostawil zamknieta puszke Monstera! Zgarniasz ja do plecaka.")

            return True

        # Tura nauczyciela - atak kartkowka lub trudnym pytaniem
        atak_los = random.choice(nauczyciel['teksty_ataku'])
        obrazenia_nauczyciela = random.randint(nauczyciel['atak_min'], nauczyciel['atak_max'])
        uczen['hp'] -= obrazenia_nauczyciela
        print(f"<- {nauczyciel['nazwa']} {atak_los} Tracisz {obrazenia_nauczyciela} HP!")

        if uczen['hp'] <= 0:
            return False

    return uczen['hp'] > 0


# 4 przerwy sklepik i szafki

def wydarzenie_szafka(uczen):
    """
    Znaleziona uchylona szafka na korytarzu ZSK.
    Mozna znalezc kase, monsterki, sciage ALBO trafic na psikus i stracic HP!
    """
    teksty_korytarz = [
        "[?] Na korytarzu widzisz uchylona szafke szkolna z naklejka ZSK!",
        "[?] Przy szatni stoi niedomknieta szafka, z ktorej wystaje jakas kartka!",
        "[?] Ktos zapomnial zamknac klodki w szafce numer 73 na drugim pietrze!"
    ]
    print("\n" + "~" * 52)
    print(random.choice(teksty_korytarz))
    print("1. Przeszukaj szafke (uwazaj, w srodku moze byc pulapka!)")
    print("2. Zignoruj i idz dalej pod sale")

    wybor = pobierz_wybor(["1", "2"])
    if wybor == "1":
        # Losowanie zdarzenia: kasa, monsterki, sciaga LUB psikus ze strata HP!
        rodzaj_znaleziska = random.choice(["kasa", "monster", "sciaga", "psikus_kanapka", "psikus_palce", "psikus_worek"])

        if rodzaj_znaleziska == "kasa":
            znaleziona_kasa = random.randint(18, 38)
            uczen['kasa'] += znaleziona_kasa
            print(f"[+] Na dolnej polce lezaly drobne zgubione przez pierwszaka! Znalazles {znaleziona_kasa} zl.")

        elif rodzaj_znaleziska == "monster":
            ilosc = random.choice([1, 2])
            uczen['energetyki'] += ilosc
            if ilosc == 1:
                print("[+] W szafce lezala pelna, schlodzona puszka Monstera! Dodano do plecaka.")
            else:
                print("[+] Niewiarygodny fart! W szafce ktos zostawil az 2 puszki Monstera!")

        elif rodzaj_znaleziska == "sciaga":
            nowy_przedmiot = "Sciaga z Pytaniami Maturalnymi"
            if nowy_przedmiot not in uczen['ekwipunek']:
                uczen['ekwipunek'].append(nowy_przedmiot)
                uczen['atak_min'] += 5
                uczen['atak_max'] += 7
                print(f"[+] ZLOTE ZNALEZISKO! W szafce lezala: {nowy_przedmiot}!")
                print(f"Twoja sila odpowiedzi rosnie do {uczen['atak_min']}-{uczen['atak_max']}!")
            else:
                uczen['kasa'] += 25
                print("[+] Znalazles dodatkowa sakiewke z 25 zl w bocznej kieszonce!")


        elif rodzaj_znaleziska == "psikus_kanapka":
            obrazenia = random.randint(10, 15)
            uczen['hp'] = max(1, uczen['hp'] - obrazenia)
            print("\n[-] PSIKUS! Ze srodka bucha potworny smrod splesnialej kanapki z pasztetem z wrzesnia!")
            print(f"Mdłości i szok tlenowy odbieraja Ci {obrazenia} HP! (Aktualny stan HP: {uczen['hp']}/{uczen['max_hp']})")

        elif rodzaj_znaleziska == "psikus_palce":
            obrazenia = random.randint(8, 14)
            uczen['hp'] = max(1, uczen['hp'] - obrazenia)
            print("\n[-] PSIKUS! Zardzewiale drzwiczki nagle odbijaja i z impetem przycinaja Ci palce! AUUU!")
            print(f"Pulsujacy bol dloni zabiera Ci {obrazenia} HP! (Aktualny stan HP: {uczen['hp']}/{uczen['max_hp']})")

        elif rodzaj_znaleziska == "psikus_worek":
            obrazenia = random.randint(11, 16)
            uczen['hp'] = max(1, uczen['hp'] - obrazenia)
            print("\n[-] PSIKUS! Z gornej polki spada na Twoja glowe zakurzony, wilgotny worek z trampkami po w-fie!")
            print(f"Smrod i uderzenie trampkiem odbieraja Ci {obrazenia} HP! (Aktualny stan HP: {uczen['hp']}/{uczen['max_hp']})")

    else:
        teksty_rezygnacji = [
            "Postanowiles nie ryzykowac uwagi w dzienniku i poszedles dalej.",
            "Wolisz nie tykac cudzych szafek - w ZSK rozne rzeczy w nich leza.",
            "Omijasz szafke lukiem i ruszasz prosto pod sale lekcyjna."
        ]
        print(random.choice(teksty_rezygnacji))


def wydarzenie_sklepik(uczen):

    teksty_powitanie_sklepik = [
        '"Co tam podac, mlody czlowieku? Inflacja nie wybiera, ale Monster przed sprawdzianem to koniecznosc!"',
        '"Witaj w sklepiku! Ceny poszly w gore, ale na energii w ZSK sie nie oszczedza!"',
        '"Widze zmeczenie w oczach! Kawa, Monster czy cieple wyposazenie na korytarze?"',
        '"Dzien dobry! Bierz zapasy szybko, bo za piec minut dzwoni na lekcje!"'
    ]
    print("\n" + "$" * 52)
    print("Wchodzisz do szkolnego sklepiku. Za lada stoi mila Pani ze sklepiku.")
    print(random.choice(teksty_powitanie_sklepik))

    CENA_ENERGETYKA = 20
    CENA_BLUZY = 35
    CENA_CIENKOPISOW = 30

    while True:
        posiada_bluze = "Ciepla Bluza ZSK" in uczen['ekwipunek']
        posiada_cienkopisy = "Zestaw Profesjonalnych Cienkopisow" in uczen['ekwipunek']

        print(f"\nTwoje fundusze: {uczen['kasa']} zl | Energetyki w plecaku: {uczen['energetyki']} szt.")
        print(f"1. Kup Energetyka / Monstera (Koszt: {CENA_ENERGETYKA} zl)")

        if posiada_bluze:
            print("2. Ciepla Bluza ZSK [WYPRZEDANE - Juz posiadasz ten przedmiot!]")
        else:
            print(f"2. Kup Ciepla Bluze ZSK (+20 Max HP, Koszt: {CENA_BLUZY} zl - dostepna tylko raz)")

        if posiada_cienkopisy:
            print("3. Zestaw Profesjonalnych Cienkopisow [WYPRZEDANE - Juz posiadasz ten przedmiot!]")
        else:
            print(f"3. Kup Zestaw Profesjonalnych Cienkopisow (+4 do ataku, Koszt: {CENA_CIENKOPISOW} zl - tylko raz)")

        print("4. Zakoncz zakupy i wracaj na korytarz")

        wybor = pobierz_wybor(["1", "2", "3", "4"])

        # Opcja 1: Energetyk
        if wybor == "1":
            if uczen['kasa'] >= CENA_ENERGETYKA:
                uczen['kasa'] -= CENA_ENERGETYKA
                uczen['energetyki'] += 1
                teksty_kupno_napoju = [
                    "[+] Kupiles zimnego Monstera! Pani ze sklepiku podaje Ci puszke z lodowki.",
                    "[+] Puszka energetyka wedruje do Twojego plecaka! Twoj portfel nieco zeszczuplal.",
                    "[+] Zakupiono Monstera! Ostatnia puszka z polki jest Twoja."
                ]
                print(random.choice(teksty_kupno_napoju))
            else:
                print(f"[-] Masz za malo kasy! Monster podrozal i kosztuje teraz {CENA_ENERGETYKA} zl.")

        # Opcja 2: Ciepla Bluza ZSK
        elif wybor == "2":
            if posiada_bluze:
                print("[-] Kupiles juz Ciepla Bluze ZSK! W wiecej niz jedna i tak sie nie zmiescisz.")
            elif uczen['kasa'] >= CENA_BLUZY:
                uczen['kasa'] -= CENA_BLUZY
                uczen['max_hp'] += 20
                uczen['hp'] += 20
                uczen['ekwipunek'].append("Ciepla Bluza ZSK")
                print(f"[+] ZAKUPIONO KULTOWA BLUZE ZSK! Jest ciepla i dodaje prestizu!")
                print(f"Twoje maksymalne HP wzrasta trwale o +20! (Aktualny stan: {uczen['hp']}/{uczen['max_hp']})")
            else:
                print(f"[-] Brakuje Ci pieniedzy na bluze! Kosztuje ona {CENA_BLUZY} zl.")

        # Opcja 3: Cienkopisy
        elif wybor == "3":
            if posiada_cienkopisy:
                print("[-] Masz juz ten zestaw cienkopisow! Drugi komplet jest Ci zbedny.")
            elif uczen['kasa'] >= CENA_CIENKOPISOW:
                uczen['kasa'] -= CENA_CIENKOPISOW
                uczen['atak_min'] += 4
                uczen['atak_max'] += 4
                uczen['ekwipunek'].append("Zestaw Profesjonalnych Cienkopisow")
                print("[+] Kupiles Zestaw Cienkopisow! Notatki w zeszycie wygladaja teraz jak dzielo sztuki!")
                print(f"Twoja sila odpowiedzi rosnie! Nowy zakres ataku: {uczen['atak_min']}-{uczen['atak_max']}.")
            else:
                print(f"[-] Nie stac Cie na te cienkopisy! Potrzebujesz {CENA_CIENKOPISOW} zl.")

        # Opcja 4: Wyjscie ze sklepiku
        elif wybor == "4":
            teksty_pozegnanie = [
                '"Powodzenia na lekcji, trzymam kciuki!"',
                '"Ucz sie pilnie, do zobaczenia na nastepnej przerwie!"',
                '"Dziekuje za zakupy i nie spoznij sie na dzwonek!"'
            ]
            print(random.choice(teksty_pozegnanie))
            break


# glowna struktura

def stworz_ucznia():
    try:
        imie = input("Podaj imie lub ksywe ucznia ZSK: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nDo widzenia!")
        sys.exit(0)

    if not imie:
        imie = "Uczen 3B"

    poczatkowy_ekwipunek = ["Legitymacja Szkolna ZSK", "Zeszyt w kratke", "Ostatni dlugopis"]

    uczen = {
        'imie': imie,
        'hp': 100,
        'max_hp': 100,
        'atak_min': 10,
        'atak_max': 18,
        'kasa': 35,
        'energetyki': 2,
        'ekwipunek': poczatkowy_ekwipunek,
        'zaliczonych_przedmiotow': 0
    }
    return uczen


def gra():

    wyswietl_ekran_startowy()
    uczen = stworz_ucznia()

    lista_nauczycieli = [
        {
            "sala": "Sala 104 - Pracownia Historyczna",
            "nazwa": "Nauczyciel od Historii",
            "hp": 38,
            "atak_min": 6,
            "atak_max": 11,
            "nagroda_kasa_min": 14,
            "nagroda_kasa_max": 24,
            "teksty_powitalne": [
                "Wyciagamy karteczki! Pytanie pierwsze: wymien dokladna date Bitwy pod Cedynia!",
                "Dzien dobry. Dzisiaj sprawdzimy, kto naprawde uwazal, a kto spal w ostatniej lawce!",
                "Kto nie zna historii, ten jest skazany na jej powtarzanie w sierpniu! Do tablicy!"
            ],
            "teksty_ataku": [
                "pyta o drzewo genealogiczne Piastow i rozbicie dzielnicowe!",
                "robi niezapowiedziana kartkowke z trzech ostatnich stuleci!",
                "mowi: 'Alez to bylo w podreczniku na stronie 214, znowu brak przygotowania!'",
                "kaze wymienic wszystkich wladcow elekcyjnych w kolejnosci chronologicznej!",
                "pyta o skutki zawarcia Unii w Krewie i pokoju w Toruniu!",
                "krzyczy: 'Prosze wskazac na mapie dokladny przebieg granic I Rzeczypospolitej!'"
            ]
        },
        {
            "sala": "Sala 210 - Laboratorium Chemiczne",
            "nazwa": "Nauczycielka od Chemii",
            "hp": 48,
            "atak_min": 8,
            "atak_max": 14,
            "nagroda_kasa_min": 18,
            "nagroda_kasa_max": 28,
            "teksty_powitalne": [
                "Prosze podejsc do tablicy i zbilansowac reakcje redoks w srodowisku kwasnym!",
                "Zakladamy fartuchy i okulary. Jeden blad ze stechiometrii i lufka w dzienniku!",
                "Mam nadzieje, ze uklad okresowy macie w malym palcu, bo zaraz zaczynamy odpytywanie!"
            ],
            "teksty_ataku": [
                "sprawdza zadanie domowe ze stechiometrii gazow w warunkach normalnych!",
                "pyta o wzor polstrukturalny 2,2,4-trimetylopentanu!",
                "grozi wyslaniem do tablicy na cala 45-minutowa lekcje!",
                "rzuca podchwytliwym pytaniem o hybrydyzacje orbitali atomowych w zwiazkach wegla!",
                "mowi chlodno: 'Na laboratoriach to by pan juz caly sprzet potlukl!'",
                "kaze podac stala dysocjacji kwasu siarkowodorowego z pamieci!"
            ]
        },
        {
            "sala": "Sala 305 - Sala Matematyczna",
            "nazwa": "Nauczyciel od Matematyki",
            "hp": 55,
            "atak_min": 9,
            "atak_max": 16,
            "nagroda_kasa_min": 22,
            "nagroda_kasa_max": 35,
            "teksty_powitalne": [
                "Kto nie policzy delty z pamieci, ten nie ma co marzyc o zdaniu do nastepnej klasy!",
                "Matematyka to krolowa nauk. Siadac, otwierac zbiory zadan na stronie 150!",
                "Dzisiaj zadania z gwiazdka. Zobaczymy, kto mysli, a kto tylko przepisuje z Photomatha!"
            ],
            "teksty_ataku": [
                "zadaje zadanie z parametrem m i trzema wartosciami bezwzglednymi!",
                "kaze udowodnic tozsamosc trygonometryczna bez tablic maturalnych!",
                "mowi: 'Matematyka to krolowa nauk, a u Ciebie widze czarna dziure!'",
                "rzuca zadaniem: 'Oblicz granice ciagu przy dążeniu n do nieskonczonosci!'",
                "krzyczy: 'Dzielenie przez zero?! Za drzwi, ochlonac na korytarzu!'",
                "kaze narysowac wykres funkcji homograficznej bez uzycia linijki!"
            ]
        },
        {
            "sala": "Sala 12 - Pracownia Sieciowa i Programowania",
            "nazwa": "Nauczyciel Informatyki (Egzaminator)",
            "hp": 65,
            "atak_min": 11,
            "atak_max": 19,
            "nagroda_kasa_min": 28,
            "nagroda_kasa_max": 45,
            "teksty_powitalne": [
                "Wskaz blad pamieci segfault w petli while oraz napisz zapytanie SQL w 30 sekund!",
                "Logujemy sie na stanowiska. Dzisiaj symulacja panstwowego egzaminu zawodowego INF.04!",
                "U mnie na maszynie kod dziala, u was zaraz sprawdzimy standardy czystego kodu!"
            ],
            "teksty_ataku": [
                "pyta o maski podsieci VLSM i trasowanie pakietow w routerach Cisco!",
                "kaze napisac zlaczenie trzech tabel LEFT JOIN w SQL bez bledu skladni!",
                "sprawdza wycieki pamieci i wskazniki NULL w jezyku C++!",
                "mowi: 'Kod nie kompiluje sie na serwerze testowym. Zero punktow z zadania!'",
                "pyta o roznice miedzy stosem a sterta o godzinie 8 rano!",
                "kaze recznie przeliczyc liczbe szesnastkowa na kod dwojkowy w pamieci!"
            ]
        }
    ]

    calkowita_liczba_pokoi = 5
    aktualny_pokoj = 1

    # Petla glowna przechodzenia przez pokoje szkolne
    while aktualny_pokoj <= calkowita_liczba_pokoi:
        print("\n" + "=" * 58)
        print(f"            POKOJ {aktualny_pokoj} Z {calkowita_liczba_pokoi}")
        print("=" * 58)

        wyswietl_statystyki(uczen)

        # Ostatni pokoj (5): Finałowy Boss
        if aktualny_pokoj == calkowita_liczba_pokoi:
            print("\nWchodzisz po schodach na sam szczyt... Pukasz do wielkich debowych drzwi.")
            print("To Gabinet Dyrekcji! Za biurkiem siedzi najwazniejsza osoba w calej szkole...")
            boss = {
                "nazwa": "PANI DYREKTOR (DYRCIA) [FINAL BOSS]",
                "hp": 115,
                "atak_min": 14,
                "atak_max": 24,
                "nagroda_kasa_min": 120,
                "nagroda_kasa_max": 220,
                "teksty_powitalne": [
                    "Zapraszam do gabinetu. Przejrzalam Twoja frekwencje i oceny. Porozmawiajmy o Twojej przyszlosci w ZSK!",
                    "Proszę usiasc. Raport z rady pedagogicznej lezy na moim biurku. Czy ma pan cos na swoja obrone?",
                    "W ZSK wymagamy pelnego zaangazowania. Dzis zadecyduje sie, czy zobaczymy sie we wrzesniu!"
                ],
                "teksty_ataku": [
                    "wyciaga z debowego biurka oficjalne wezwanie rodzicow do szkoly!",
                    "grozi wpisaniem nagany dyrektora z wilczym biletem do akt szkoly!",
                    "zadaje mrozace krew w zylach pytanie: 'A gdzie pana usprawiedliwienia z piatkow?!'",
                    "zaglada w dziennik elektroniczny Librus i kreci z dezaprobata glowa!",
                    "mowi chlodnym glosem: 'W sierpniu jest piekna pogoda na egzamin komisyjny!'",
                    "sprawdza regulaminowy stroj i pyta o brak identyfikatora szkolnego!"
                ],
                "czy_boss": True
            }
            wynik = walka_z_nauczycielem(uczen, boss)


            if wynik:
                # warunek wygranej

                print("\n" + "*" * 68)
                print("       *** GRATULACJE! ZDALES ROK W ZSK! ***")
                print(f"Uczen {uczen['imie']} przekonal Dyrcie i obronil swoje oceny!")
                print("Dyrcia z uznaniem wrecza Ci swiadectwo z czerwonym paskiem!")
                print("Cala szkola bije brawo, a Ty z usmiechem wyruszasz na upragnione wakacje!")
                print("*" * 68)
                print("TWOJE OSIAGNIECIA W ROKU SZKOLNYM:")
                print(f" - Zaliczone przedmioty:   {uczen['zaliczonych_przedmiotow']}")
                print(f" - Zaoszczedzona kasa:     {uczen['kasa']} zl")
                print(f" - Pozostala energia HP:   {uczen['hp']} / {uczen['max_hp']}")
                print(f" - Zdobyty ekwipunek:      {', '.join(uczen['ekwipunek'])}")
                print("*" * 68)
                return
            else:
                break 

        nauczyciel = lista_nauczycieli[aktualny_pokoj - 1]
        print(f"\n[+] Wchodzisz do sali: {nauczyciel['sala']}")
        wynik_lekcji = walka_z_nauczycielem(uczen, nauczyciel)

        if not wynik_lekcji:
            break


        teksty_przerwa_korytarz = [
            "DZWONEK NA PRZERWE! Korytarze zapelniaja sie uczniami powtarzajacymi notatki.",
            "DZWONEK NA DLUGĄ PRZERWE! Z dolu unosi sie zapach tostow i kawy ze sklepiku.",
            "DZWONEK! Masz chwile wytchnienia przed wejsciem do kolejnej sali."
        ]
        print("\n" + "#" * 58)
        print(random.choice(teksty_przerwa_korytarz))
        print("Co chcesz zrobic w czasie wolnym?")
        print("1. Idz prosto pod nastepna sale lekcyjna")
        print("2. Odwiedz szkolny sklepik (napoje i ulepszenia)")
        print("3. Sprawdz losowa szafke na korytarzu (szansa na skarb lub psikus)")
        print("4. Wypij energetyka z plecaka")

        wybor_przerwy = pobierz_wybor(["1", "2", "3", "4"])
        if wybor_przerwy == "2":
            wydarzenie_sklepik(uczen)
        elif wybor_przerwy == "3":
            wydarzenie_szafka(uczen)
        elif wybor_przerwy == "4":
            wypij_energetyka(uczen)

        aktualny_pokoj += 1

    #warnek przegranej
    print("\n" + "#" * 68)
    print("                     GAME OVER!")
    print(f"Niestety, {uczen['imie']} nie wytrzymal presji w ZSK...")
    print(f"Twoja energia spadla do 0 w pokoju numer {aktualny_pokoj}.")
    print("Czeka Cie wezwanie rodzicow, nagana i egzamin poprawkowy w sierpniu!")
    print("Sprobuj ponownie z lepszym zapasem energetykow i sciag!")
    print("#" * 68)


# główna petla z opcją restartu

def main():
    """Petla restartu - pozwala rozpoczac nowy rok szkolny bez resetu Pythona."""
    while True:
        gra()
        print("\nCzy chcesz rozpoczac kolejny rok szkolny w ZSK?")
        print("1. Tak, nowa rozgrywka")
        print("2. Nie, wychodze ze szkoly")
        wybor = pobierz_wybor(["1", "2"])
        if wybor == "2":
            print("\nDo zobaczenia w ZSK! Dziekujemy za gre!")
            break
        print("\n" * 2)


if __name__ == "__main__":
    main()
