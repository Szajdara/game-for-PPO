# Mini-projekt: Tekstowa gra RPG ("Przetrwanie w ZSK: Droga do Dyrekcji")

Projekt przygotowany zgodnie z wytycznymi na zajęcia z **Programowania Obiektowego** (prowadzący: **Bartosz Zaręba**, ZSK Poznań).

---

## 🏫 Fabuła i koncepcja gry
Gra to turowa przygoda RPG osadzona w realiach **Zespołu Szkół Komunikacji (ZSK w Poznaniu)**:
* **Główny bohater:** Uczeń ZSK (klasa 3B), który staje przed wyzwaniem zaliczenia roku szkolnego.
* **Pokoje / sale lekcyjne (wrogowie):**
  1. **Sala 104:** *Nauczyciel od Historii* (atakuje datami bitew, dynastią Piastów i Unią w Krewie)
  2. **Sala 210:** *Nauczycielka od Chemii* (atakuje bilansowaniem redoksów, stechiometrią i hybrydyzacją)
  3. **Sala 305:** *Nauczyciel od Matematyki* (atakuje deltą, granicami ciągów i funkcją homograficzną)
  4. **Sala 12:** *Nauczyciel Informatyki / Egzaminator* (atakuje wskaźnikami, SQL, podsieciami Cisco i egzaminem INF.04)
  5. **Gabinet Dyrekcji (FINAL BOSS):** *Pani Dyrektor (DYRCIA)* (wzywa rodziców, grozi naganą dyrektora i decyduje o promocji do następnej klasy!)
* **Mechaniki i nowości:**
  * **Odpowiedź przy tablicy:** Zwykła odpowiedź lub ryzykowne lanie wody (szansa na krytyka lub wtopę) z wieloma różnorodnymi tekstami.
  * **Leczenie:** Dyskretny łyk puszki Monstera pod ławką.
  * **Szkolny sklepik:**
    * *Energetyk / Monster:* kosztuje 20 zł.
    * *Ciepła Bluza ZSK (+20 Max HP):* do kupienia **tylko raz** (potem status `[WYPRZEDANE]`).
    * *Zestaw Cienkopisów (+4 do ataku):* do kupienia **tylko raz** (potem status `[WYPRZEDANE]`).
  * **Szafki na korytarzu:** Możliwość znalezienia kasy, zapasowych puszek Monstera, ściąg maturalnych **lub trafienia na psikus** (spleśniała kanapka z września, przycięcie palców drzwiczkami, spadający worek z trampkami po w-fie – strata HP!).
  * **Bogate dialogi:** Znacznie rozbudowana pula tekstów ataków, powitań nauczycieli, reakcji belfrów oraz odzywek Pani ze sklepiku.

---

## ✅ Spełnienie wymagań formalnych projektu

| Wymaganie formalne | Realizacja w kodzie |
|---|---|
| **Tutorial / ekran startowy** | Funkcja `wyswietl_ekran_startowy()` przedstawia zasady, sterowanie klawiaturą, opis sal oraz warunki ukończenia gry. |
| **Logika gry (wygrana / przegrana)** | **Wygrana:** Pokonanie Dyrci w gabinecie (zdanie roku ze świadectwem z paskiem).<br>**Przegrana:** Spadek HP do 0 (brak energii/psychiki, wezwanie rodziców i poprawka w sierpniu). |
| **Interaktywność i pętla gry** | Pętla `main()` i `gra()` z bezpieczną funkcją `pobierz_wybor()`, która weryfikuje wejście użytkownika i zapobiega błędom programu. |
| **Instrukcje warunkowe** | `if`, `elif`, `else` w walce przy tablicy, weryfikacji zakupów jednorazowych, losowaniu zdarzeń w szafkach oraz decyzjach w czasie przerw. |
| **Pętle** | `while` (główna pętla, pętla komnat/sal, pętla walki, sklepik, restart) oraz `for` (iteracje po elementach i opcjach). |
| **Tablice (listy)** | Listy w Pythonie: baza nauczycieli (`lista_nauczycieli`), bogate listy dialogów i ataków (`teksty_ataku`, `teksty_sukces`, `teksty_porazka` itp.), ekwipunek ucznia (`uczen['ekwipunek']`). |
| **Funkcje** | Pełna modularyzacja (`wyswietl_ekran_startowy`, `walka_z_nauczycielem`, `wypij_energetyka`, `wydarzenie_szafka`, `wydarzenie_sklepik`, `stworz_ucznia`, `gra`, `main`). |

---

## 🚀 Uruchomienie gry

W terminalu wpisz:
```bash
python gra_rpg.py
```

---

## 📧 Wysłanie projektu

Plik gotowy do przesłania na adres **`bartosz.zareba@zsk.poznan.pl`**:
📄 **`gra_rpg.txt`**
