# Projekt: Elections Scraper
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde]([https://pages.github.com/](https://github.com/paget82/Projekt-Elections-Scraper/blob/main/vysledky_prostejov.csv)).

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložene v souboru `requirements.txt`. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
```
$ pip3 -- version                   # overim verzi manazeru
$ pip3 install -r requirements.txt  # nainstalujeme knihovny
```

## Spuštění projektu
Spuštění souboru `main.py` v rámci přík. řádku požaduje dva povinné argumenty.
```
python main.py <odkaz-uzemniho celku> <vysledny-soubor>
```
Následně se vám stáhnou výsledky jako soubor s příponou `.csv`.

## Ukázka projektu
Výsledky hlasování pro okres 
Prostějov:

 1. argument: ` https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103 `

 2. argument:  `vysledky_prostejov.csv `


Spuštění programu:
```
main.py  'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' vysledky_prostejov.csv
```
Průbeh stahování:
```
DOWNLOADING DATA FROM SELECTED URL: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
SAVING TO FILE: vysledky_prostejov.csv
FINISHED
```
Částečný výstup:
```
code, location, registered, envelopes, valid,...
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
...
```
