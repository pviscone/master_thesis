# UZH MNF Title Page

The faculty of natural sciences (MNF) has strict guidelines for the tile page and provides a template in MS Word.
Please see https://www.mnf.uzh.ch/en/studium/phd/checkliste-fuer-doktorierende.html.

For a Master thesis in the Physics Institute, an official UZH template with a different title page can also be found
[here](https://www.physik.uzh.ch/en/study/Counselling-and-forms/formulare.htm).


## Files

MS Word template:
- `titlepage_UZH_MNF2011.doc`: as provided by MNF with instructions & comments
- `titlepage_UZH_PhD.doc`: with instructions & comments removed
- [`titlepage_UZH_PhD.pdf`](titlepage_UZH_PhD.pdf): PDF version of the above template
- [`titlepage_UZH_PhD_red.pdf`](titlepage_UZH_PhD_red.pdf): PDF version of the above template in red for comparison

LaTeX template:
- [`titlepage.tex`](titlepage.tex): loaded by `thesis.tex` via `\include{titlepage/titlepage}`
- [`titlepage_test.tex`](titlepage_test.tex): standalone file for testing
- [`titlepage_test.pdf`](titlepage_test.pdf): output from the above file
- [`titlepage_test_overlay.pdf`](titlepage_test_overlay.pdf): comparison with `titlepage_UZH_PhD_red.pdf` using overlay

Please do not change any of the spacing in the LaTeX template like `\break`, `\vspace`, `\\`, white spaces, etc.
Leave `%` at the end of a text line without a space after the last word to avoid a spurious space that offsets the centered text.

<p align="center" vertical-align: middle>
  <img src="titlepage_test.png" alt="Title page following UZH MNF guidelines" width="500"/>
</p>

## MNF Guidelines

Rules for capitalization in titles
- Capitalize nouns, pronouns, verbs (including conjugated forms of to be), adjectives, and adverbs.
- Lowercase definite and indefinite articles (a, an, the).
- Lowercase all prepositions when used strictly as prepositions.
- Capitalize prepositions when used as adverbs or adjectives: "Straighten Up and Fly Right".
- Lowercase usage of "to" in all situations – whether as a preposition or as part of an infinitive.
- Capitalize the second part of a hyphenated compound: "Research-Based Teaching and Learning".

For example:
```
A Search for Dark Matter in Association with Top Quarks with the CMS Experiment%

A Search for New Exotic Particles with Jets in Proton-Proton Collisions at the CMS Experiment%

Collider Physics Measurements in High Jet Multiplicity Final States%
```

If you have a Swiss citizenship, name your place of citizenship, e.g.,
- `von Genf GE`
- `von Uster ZH`
- `von Z\"urich ZH`
- ...

If you are not a Swiss citizen, name the country of your official nationality, e.g.,
- `aus Genf GE`
- `aus Uster ZH`
- `aus Z\"urich ZH`
- `aus \"Agypten`
- `aus Belgien`
- `aus Brasilien`
- `aus Deutschland`
- `aus Frankreich`
- `aus Italien`
- `aus Iran`
- `aus den Niederlanden`
- `aus Russland`
- `aus der Ukraine`
- `aus dem Vereinigten K\"onigreich`
- `aus den Vereinigten Staaten von Amerika`
- `aus der V.R. China`
- ...
