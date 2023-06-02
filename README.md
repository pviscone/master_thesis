# Thesis template for UZH CMS

This repository contains a LaTeX template for a PhD thesis in the CMS group of the University of Zurich (UZH),
plus some useful materials to get started quickly.
For a Master thesis in the Physics Institute, an official UZH template can also be found
[here](https://www.physik.uzh.ch/en/study/Counselling-and-forms/formulare.htm).
More information for PhD students of the faculty of natural sciences (MNF) can be found
[here](https://www.mnf.uzh.ch/en/studium/phd/checkliste-fuer-doktorierende.html).

The main file is [`thesis.tex`](thesis.tex), which loads the chapters from [`sections/`](sections/).
If you use TeXShop, you can include `%!TEX root = ../thesis.tex` at the top of each file to compile this file.

Some examples of chapters based on my own thesis are already given in [`sections/chap*.tex`](sections),
and can be completely removed for your thesis, or used as a rough starting point for writing.
Have a look at [`thesis.pdf`](thesis.pdf) to see how this template looks.

## Title page
The MNF has strict guidelines for the tile page and provides a template in MS Word.
Please find the template here: https://www.mnf.uzh.ch/en/studium/phd/checkliste-fuer-doktorierende.html.
A LaTeX version of this template can be found in [`titlepage/`](titlepage).

<p align="center" vertical-align: middle>
  <img src="titlepage/titlepage_test.png" alt="Title page following UZH MNF guidelines" width="500"/>
</p>

## Settings
The preamble with settings like page layout are set in [`settings/preamble.tex`](settings/preamble.tex).
Note that the document class is `scrreprt` from the KOMA-script bundle.

Some of the common macros and particle pennames in CMS TDR are mimicked in
[`settings/macros_CMS_TDR.tex`](settings/macros_CMS_TDR.tex).
Note that for particle names "unslanted" Greek letters are used.
This is just my personal preference to separate them from variables, which are in italics.

Other common macros for general typesetting of symbols specific to your thesis
are loaded from [`settings/macros_user.tex`](settings/macros_user.tex).

## Figures
Some basic figures related to the SM, LHC, and CMS plus sources and can be found in [`fig/`](fig).

Please note the rules for PhD theses using plots with CMS results using data or simulation:
https://twiki.cern.ch/twiki/bin/view/CMS/PhysicsApprovals#Thesis_endorsement

## References
A bibliography style file for `BibTeX` that is adopted from the official CMS TDR style can be found in [`bib/`](bib),
as well as a bunch of BibTeX files with useful references.

## Copy to Overleaf
Overleaf offers a good editor, and allows you to make a private & secure back up of your thesis.
Using your affiliation with UZH or CERN, you can create a professional Overleaf account
to access all the features like `git`.

### Using a share link
This GitHub repo is synced to [this Overleaf project](https://www.overleaf.com/read/mspvhdpynsjb).
If you open the previous share link, the read-only project will be added to your
["My Projects"](https://www.overleaf.com/project) page.
You can then make a copy that you can edit yourself by clicking the copy button under "Actions".

### Using `git`
Alternatively, you can clone this GitHub repo locally, and push it to Overleaf yourself.
1. Create a new "Blank Project" from the ["My Projects"](https://www.overleaf.com/project) page
on Overleaf.
2. Find the `git` repo link of your project from the menu under "Git".
3. Clone this repo
```
git clone git@github.com:IzaakWN/PhDThesisTemplateUZHCMS.git thesis
```
4. Push it to Overleaf following
[these instructions](https://www.overleaf.com/learn/how-to/Using_Git_and_GitHub):
```
cd thesis
git remote add overleaf https://git.overleaf.com/...
git checkout master
git pull overleaf master --allow-unrelated-histories
git revert --mainline 1 HEAD
git push overleaf master
```
