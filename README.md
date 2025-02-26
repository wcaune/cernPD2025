# cernPD2025

## Setup ProtoDUNE software
Once I activate sl7 container, do the following.
```bash
export UPS_OVERRIDE="-H Linux64bit+3.10-2.17"
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
setup dunesw v10_03_01d02 -q e26:prof
```


## Geant4 stage with GeGeDe GDML file
The V5 ProtoDUNE-VD geometry GDML file was constructed using GeGeDe (General Geometry Description), a Python-based software.
In `gen.fcl` file, we add:
```bash
services.AuxDetGeometry.GDML: "protodunevd_v5_refactored.gdml"
services.AuxDetGeometry.Name: "protodunevd_v5"

services.Geometry.GDML: "protodunevd_v5_refactored.gdml"
services.Geometry.Name: "protodunevd_v5"
services.Geometry.ROOT: "protodunevd_v5_refactored.gdml"

```

Then in `g4.fcl`, the next step after generator, we add:
```bash
services.AuxDetGeometry.GDML: "protodunevd_v5_refactored.gdml"
services.AuxDetGeometry.Name: "protodunevd_v5"

services.Geometry.GDML: "protodunevd_v5_refactored.gdml"
services.Geometry.Name: "protodunevd_v5"
services.Geometry.ROOT: "protodunevd_v5_refactored.gdml"

services.LArG4Detector.gdmlFileName_: "protodunevd_v5_refactored.gdml"
```
