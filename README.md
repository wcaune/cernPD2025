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

## Setup VNC server for ProtoDUNE-VD event display
In the first time we login, it may ask us to set a password for connection.
### initial VNC password 
```bash
kinit -f -7d username@FNAL.GOV
ssh -AKXY username@dunegpvm15.fnal.gov
source ~/setup2025VNC.sh
exit
```
Once exit this login, open a new terminal window and in the `$HOME/.ssh/config` or `$HOME/.ssh/ssh_config`, and paste the following:
```bash
Host dunegpvm??
  HostName %h.fnal.gov
  User username
  ForwardAgent yes
  ForwardX11 yes
  ForwardX11Trusted yes
  GSSAPIAuthentication yes
  GSSAPIDelegateCredentials yes
  LocalForward 5901 localhost:XXXXX
```
Then exit the window.
### Build the VNC session
In a new window, do
```bash
ssh -Y dunegpvm09
source ~/setup2025VNC.sh
dunesl7
export UPS_OVERRIDE="-H Linux64bit+3.10-2.17"
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
source ~/setup2025VNC.sh
exit
```
Now we should in `dunegpvm09` and out of sl7 container. Use `vncserver -list` to check if we setup the VNC session as we want.
### Local connection to VNC session
In a local terminal, do
```bash
open vnc://localhost:5901
```
Do not logout the AL9 from the upper right corner, but close connection in the upper left APP `Quit Screen Sharing`. 

And in `dunegpvm09`, use `kill -9` to end the VNC session.

