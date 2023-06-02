# Particle Physics & CMS References

## BibTeX style
The bibliography style file [`style_CMS_TDR.bst`](style_CMS_TDR.bst) for `BibTeX` is adopted from the official
CMS TDR style found here: https://gitlab.cern.ch/tdr/utils/-/blob/master/general/cms_unsrt.bst
One nice feature of this style is that it automatically makes the name of collaborations bold.

## Recommended & common references
Many recommended & common references for CMS are available in
- Higgs: https://gitlab.cern.ch/tdr/utils/-/blob/master/general/higgs.bib
- Generators: https://gitlab.cern.ch/tdr/utils/-/blob/master/general/gen.bib
- Generators: https://twiki.cern.ch/twiki/bin/viewauth/CMS/CitationsForGenerators
- Detector: https://twiki.cern.ch/twiki/bin/viewauth/CMS/Internal/PubDetector
- Statistics: https://twiki.cern.ch/twiki/bin/viewauth/CMS/StatisticsReferences
- Combine: https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part4/usefullinks/?#citations

Note some guidelines for references and citations in CMS publications are given here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/Internal/PubGuidelines#References

## More references
The `refs_*.bib` contain more cleaned-up references that may be useful for CMS members:
- [`refs_SM.bib`](refs_SM.bib): For the Standard Model (SM) of particle physics, including some historical papers.
- [`refs_Higgs.bib`](refs_Higgs.bib): For Higgs theory & discovery, ...
- [`refs_flavor.bib`](refs_flavor.bib): For flavor physics, including basic theory, lepton-flavor universality (LFU), lepton-flavor violating (LFV) decays, LFU, B anomalies, LQ models, ...
- [`refs_BSM.bib`](refs_BSM.bib): For some models beyond the SM, like dark matter (DM), SUSY (MSSM, 2HDM), vector-like quarks (VLQs), ...
- [`refs_LHC.bib`](refs_LHC.bib): For the accelerators, pp collisions, deep inelastic scattering (DIS), pp collisions, luminosities, ...
- [`refs_detector.bib`](refs_detector.bib): For the CMS detector, subdetectors, ...
- [`refs_objects.bib`](refs_objects.bib): For object reconstruction in general and in CMS: electrons, muons, taus, jets, MET, ...
- [`refs_samples.bib`](refs_samples.bib): For samples, MC generation, cross sections, tunes, ...
- [`refs_stats.bib`](refs_stats.bib): For statistical methods, ...
Note that some references are for CMS-internal use only (ANs), and cannot be used in theses.

You can load multiple `.bib` files in [`sections/references.tex`](../sections/references.tex) like this:
```
\bibliographystyle{bib/style_CMS_TDR}
\begin{flushleft}
  \bibliography{bib/refs_SM,bib/refs_LHC,bib/refs_detector,bib/refs_samples,bib/refs_stats}
\end{flushleft}
```

## Cleaning BibTeX files
To clean BibTeX files and spot potential issues, you can use
[this script](https://github.com/IzaakWN/CodeSnippets/blob/master/LaTeX/cleanBibTeX.py):
```python
cd bib/
curl https://raw.githubusercontent.com/IzaakWN/CodeSnippets/master/LaTeX/cleanBibTeX.py > cleanBibTeX.py
python cleanBibTeX.py refs.bib -o refs_clean.bib --backup --check
```
The checks are similar to this script from CMS TDR:
https://gitlab.cern.ch/tdr/utils/-/blob/master/general/cleanRefs.py