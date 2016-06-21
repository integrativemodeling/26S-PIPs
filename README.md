# 26S-PIPs

The modeling.py script demonstrates the use of IMP and PMI in the modeling of the 26S proteasome - UBLCP1 complex, using chemical crosslinking and comperative modeling. 

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

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://integrativemodeling.org/systems/?sysstat=6&branch=master)](http://integrativemodeling.org/systems/) [![build info](https://integrativemodeling.org/systems/?sysstat=6&branch=develop)](http://integrativemodeling.org/systems/)

  
