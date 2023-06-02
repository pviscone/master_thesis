# Particle Physics & CMS Figures
Some basic figures related to the SM, LHC, and CMS.
Some of the figures uploaded in this repo may be outdated by the time you need them.
Please use the sources below to look for updated plots.

## CMS results

### General guidelines
CMS guidelines for figures can be found here:
- https://twiki.cern.ch/twiki/bin/view/CMS/Internal/FigGuidelines
- https://twiki.cern.ch/twiki/bin/view/CMS/Internal/Publications
- https://twiki.cern.ch/twiki/bin/view/CMS/PhysicsApprovals

A standalone `python` module to get the official CMS style in ROOT plots can be found here:
[`CMSStyle.py`](https://github.com/cms-tau-pog/TauFW/blob/master/Plotter/python/plot/CMSStyle.py).

### Unapproved results
Please note the rules for plots with CMS data, simulation, results in PhD theses:
https://twiki.cern.ch/twiki/bin/view/CMS/PhysicsApprovals#Thesis_endorsement

### Published plots
You can retrieve the original file of most CMS plots that have been published
in a PAS or paper with CADI line `XXX-YY-NNN` either from CMS Public Pages, or directly from GitLab:
- PAS notes: http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/XXX-YY-NNN/index.html
- Paper: http://cms-results.web.cern.ch/cms-results/public-results/publications/XXX-YY-NNN/ (also linked from "Comments" on the arXiv page)
- PAS notes: https://gitlab.cern.ch/tdr/notes/XXX-YY-NNN
- Papers: https://gitlab.cern.ch/tdr/papers/XXX-YY-NNN

More recent reports on technical designs, upgrades, etc. can be found in https://gitlab.cern.ch/tdr/reports/

## Standard Model & beyond
- TikZ figures: https://tikz.net/category/physics/particle-physics/
- Particle physics timeline & energy scales: https://tikz.net/timeline/, https://particleadventure.org/other/history/index.html, [`intro/SM_timeline.pdf`](intro/SM_timeline.pdf)
- SM table: https://commons.wikimedia.org/wiki/File:Standard_Model_of_Elementary_Particles.svg, PDF version: [`intro/SM_particles_Wiki_edited.pdf`](intro/SM_particles_Wiki_edited.pdf), PDF of TikZ version: [`intro/SM_particles.pdf`](intro/SM_particles.pdf)
- SM particle timeline: https://tikz.net/timeline/, inspired by https://particleadventure.org/other/history/index.html
- Graphical representation of representations and quantum numbers under the SM gauge symmetry group: [`intro/SM_isospin_weak.pdf`](intro/SM_isospin_weak.pdf)
- NNPDF31 PDF plots: https://arxiv.org/abs/1706.00428, [`intro/pdf_NNPDF3.1_NNLO.pdf`](intro/pdf_NNPDF3.1_NNLO.pdf)
- CMS physics results & cross sections: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsCombined

## Feynman diagrams
- For instructions, see https://www.overleaf.com/learn/latex/Feynman_diagrams
- For more information and a gallery of examples, see https://wiki.physik.uzh.ch/cms/latex:feynman
- Some examples are included in [`feynman/`](feynman), including diagrams in equations ([`feynman/hierarchy_problem.tex`](feynman/hierarchy_problem.tex))

Note that it is possible to compile Feynman diagrams using the `feynmp` package together
with your thesis, but it can get quite messy as it creates extra files.
It's more convenient to create diagrams as standalone PDFs, and load them as a normal figure with `\includegraphics`.
In that way, it is also easy to reuse the same diagrams in other documents or presentations.

## Flavor physics
- Averages of B hadron decays (e.g. R(D) and R(D*)): https://hflav-eos.web.cern.ch/hflav-eos/semi/
- Summary of flavor anomalies: https://www.nikhef.nl/~pkoppenb/anomalies.html

## Higgs
- CMS Higgs results & plots: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsHIG
- LHC Higgs plots (cross sections, branching fractions): https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CrossSections, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGCrossSectionsFigures

## EXO summary plots
- CMS EXO public results: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SummaryPlotsEXO13TeV
- CMS physics results: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsCombined
- ATLAS EXO public results: https://twiki.cern.ch/twiki/bin/view/AtlasPublic/ExoticsPublicResults#Summary_Plots

## LHC & luminosities
- CMS instantaneous & integrated luminosities: https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults

## CMS detector
- TikZ figures: https://tikz.net/tag/cms/
- CMS 3D: https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/ShowDocument?docid=11514, https://twiki.cern.ch/twiki/bin/view/CMSPublic/SketchUpCMS
- CMS slice with different types of particles interacting with the subdetectors: https://cds.cern.ch/record/2628641/, https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/ListBy?authorid=226, [`detector/CMS_detector_PID_edit.pdf`](detector/CMS_detector_PID_edit.pdf)

## CMS subdetectors
- CMS pixel paper: https://arxiv.org/abs/2012.14304, https://gitlab.cern.ch/tdr/reports/pixuptdr
- CMS tracker sketch: https://twiki.cern.ch/twiki/bin/view/CMSPublic/DPGResultsTRK
- CMS tracking performance: https://twiki.cern.ch/twiki/bin/view/CMSPublic/TrackingPOGPerformance2017MC

## Tau reconstruction & identification
- TikZ figures: https://tikz.net/tag/tau/
- CMS tau reconstruction with the HPS algorithm (TAU-16-003): https://arxiv.org/abs/1809.02816, http://cds.cern.ch/record/2196972, http://cms-results.web.cern.ch/cms-results/public-results/publications/TAU-16-003
- CMS tau identification with the DeepTau algorithm (TAU-20-001): https://arxiv.org/abs/2201.08458, https://gitlab.cern.ch/tdr/papers/TAU-20-001, http://cms-results.web.cern.ch/cms-results/public-results/publications/TAU-20-001
- Lifetime vs. mass plot: [`objects/SM_particles_masses.pdf`](objects/SM_particles_masses.pdf), https://arxiv.org/abs/1810.12602

## Flow charts & sideband diagrams
Some examples of diagrams explaining the definition of variables, event selections, sidebands, control regions (such as for the ABCD method), etc. are in [`selections/`](selection).
