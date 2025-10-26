# Projekt-Elections-Scraper
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete zde.

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložene v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
$ pip3 -- version                   # overim verzi manazeru
$ pip3 install -r requirements.txt  #nainstalujeme knihovny


## Spuštění projektu
Spuštění souboru election-scraper.py v rámci přík. řádku požaduje dva povinné argumenty.

python election-scraper <odkaz-uzemniho celku> <vysledny-soubor>
Následně se vám stáhnou výsledky jako soubor s příponou .csv.

## Ukázka projektu
Výsledky hlasování pro okres Prostějov:
1.argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2.argument: vysledky_prostejov.csv

Spuštění programu:
python election-scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'

Průbeh stahování:
STAHUJI DATA Z VYBRANÉHO URL: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
UKLADAM DO SOUBORU: vysledky_prostejov.csv
UKONCUJI election-scraper

Částečný výstup:
code, location, registered, envelopes, valid,...
