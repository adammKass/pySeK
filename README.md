# pySeK - Python Segmenter pre slovenský jazyk

**pySeK** je jednoduchá command-line aplikácia pre segmentáciu textu na vety pre slovenský jazyk. 

Segmentácia viet je založená na pravidlách na pravidlách. Pravidlá využívajú regulárne výrazy. Aplikácia obsahuje pravidlá iba pre **slovenský jazyk**.

## Inštalácia

1. Inštalácia cez **pip**
```
pip install git+https://github.com/adammKass/pySeK
```
2. Stiahnutie navnovšej verzie cez lištu Releases

## Použitie

```
Usage: Segmenter segment [OPTIONS] SOURCE GOAL

  Segmentuje text zo súboru SOURCE do novovytvoreného súboru GOAL.
  SOURCE je cesta k zdrojovému textovému súboru.
  GOAL je cesta k cielovému textovému súboru.

Options:
  --help  Show this message and exit.
```
Príklad

```
C:\Users\User\pySek> Segmenter segment C:\cesta_k_zdroju\zdroj.txt C:\cesta_k_cielu\ciel.txt   
```
Príklad zdrojového textového súboru

```
Toto je prvá veta. toto je 2. veta. 3. veta.
```

Výsledok

```
Toto je prvá veta.
toto je 2. veta.
3. veta.
```

## Záverečná práca
Táto aplikácia vznikla ako praktická časť záverečnej bakálarskej práce **Segmentácia textu na vety pre slovenský jazyk** na Univerzite Konštantína Filozofa v Nitre.
