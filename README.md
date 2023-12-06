- [GxG: Shared Task on Cross-Genre Gender Prediction in Italian - a tutorial](#gxg-shared-task-on-cross-genre-gender-prediction-in-italian---a-tutorial)
  - [Repository originale:](#repository-originale)
  - [How to:](#how-to)
  - [Scripts](#scripts)
  - [Dati](#dati)
  - [Resources:](#resources)


# GxG: Shared Task on Cross-Genre Gender Prediction in Italian - a tutorial

Tutorial sviluppato nell'ambito del corso di Linguistica Applicata tenuto dalla dott.ssa [Silvia Ballarè](https://www.unibo.it/sitoweb/silvia.ballare), basato sul task [Gender-x-Genre](http://sites.google.com/view/gxg2018/) presentato a EVALITA 2018.

## Repository originale:
`https://github.com/malvinanissim/gxg`

## How to:
- Scaricare l'intero repository dal link https://github.com/LaboratorioSperimentale/gxg-tutorial/archive/refs/heads/master.zip
- Estrarre l'archivio
- Le slides sono contenute in un file `html` all'interno della cartella `notebook`

## Scripts
La cartella `scripts` contiene, numerati, dei file python esemplificativi per trasformare i file contenuti nella cartella `Data`, progressivamente, nelle rappresentazioni necessarie per la creazione del modello linguistico

_Importante:_ gli script sono stati sviluppati esclusivamente per fini dimostrativi, e non sono dunque da ritenersi efficienti o utilizzabili per l'analisi di dati su più larga scala

## Dati
- La cartella `Data` contiene i file rilasciati dagli organizzatori dei task
- La cartella `TransformedData` contiene generati tramite gli script sopra citati, in particolare:
  - `training.txt` e `test.txt` contengono il dataset da cui sono stati rimossi i tag xml
  - `training_post_re.txt` e `test_post_re.txt` contiene il dataset dopo l'esecuzione di sostituzioni tramite espressioni regolati
  - `training_parsed.txt` e `test_parsed.txt` contiene il testo analizzato con la libreria `spaCy`
  - `training_repr.txt` e `test_repr.txt` contiene alcune features linguistiche estratte dai documenti
- il file `vocabulary_one_hot.txt` contiene la lista completa del vocabolario dei file di training con `id` e frequenza


## Resources:
- website to learn and try out different regular expressions: https://regex101.com/
- Google colab: https://colab.google/



----


Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
