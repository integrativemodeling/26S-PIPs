[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.496173.svg)](https://doi.org/10.5281/zenodo.496173)

# 26S-PIPs

The modeling.py script demonstrates the use of [IMP](https://integrativemodeling.org)
and [PMI](https://github.com/salilab/pmi) in the modeling of the 26S proteasome - UBLCP1 complex, using chemical crosslinking and comparative modeling. 

The modeling protocol will work with a default build of IMP.

## List of files and directories:

- `modeling.py`  the main IMP/PMI script for modeling

- `inputs`
  - `h26s_flex_fix.pdb`  comparative model of the 26S proteasome structure
  - `ublcp1_t1_1.pdb`    comparative model of the UBLCP1 structure with its Ubl domain bound to T1 site
  - `ublcp1_t1_2.pdb`    comparative model of the UBLCP1 structure with its Ubl domain bound to T2 site
  - `sequences.fasta`    FASTA file with all the protein sequences
  - `topology.txt`       IMP/PMI topology input file
  - `xlinks.txt`         list of cross-links

- `output`               An example IMP/PMI output directory obtained by running the modeling.py script

## Running the IMP/PMI scripts for the 26S-UBLCP1 complex:

- `python modeling.py`


## Information

_Author(s)_: Peter Cimermancic, Charles Greenberg

_Date_: May 17th, 2016

_License_: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode).
This work is freely available under the terms of the Creative Commons
Attribution-ShareAlike 4.0 International License.

_Last known good IMP version_: [![build info](https://integrativemodeling.org/systems/?sysstat=21&branch=master)](https://integrativemodeling.org/systems/) [![build info](https://integrativemodeling.org/systems/?sysstat=21&branch=develop)](https://integrativemodeling.org/systems/)

_Publications_:
 - X. Wang, P. Cimermancic, C. Yu, E. Sakata, X. Guo, C. Greenberg,
   A. Schweitzer, A.S. Huszagh, Y. Yang, E.J. Novitsky, A. Leitner, P. Nanni,
   A. Kahraman, J. Dixon, S.D. Rychnovsky, R. Aebersold, W. Baumeister,
   A. Sali, L. Huang. [Molecular Details Underlying Dynamic Structures and
   Regulation of the Human 26S Proteasome](https://www.ncbi.nlm.nih.gov/pubmed/28292943), Mol Cell Proteomics, mcp.M116.065326 [Epub ahead of print], 2017
  
