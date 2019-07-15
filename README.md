# brainrf1
code and wikis for brain rf1 project

Usage: [fw-heudiconv](https://github.com/PennBBL/fw-heudiconv) and [Flywheel CLI](https://docs.flywheel.io/hc/en-us/articles/360008285193-CLI-Usage-Examples)

fw-heudiconv wiki: https://github.com/PennBBL/fw-heudiconv/wiki

## Table of Contents
/heuristics  
-- contain set of heuristics currently in use for project  
  
/operation:  
use corresponding heuristic for matching visit  

## Heuristic guide:  
brainrf1_heuristic_baseline.py -> baseline visit  
brainrf1_heuristic_[CONDITION].py -> tms visits (use heuristic corresponding to visit condition)  
brainrf1_heuristic_task -> task visit  
  
for heuristics in use prior to change in scan protocol, reference archive folder  
