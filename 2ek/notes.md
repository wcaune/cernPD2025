## Input txt file
Normally in `job/TextFileGen.fcl`, change the text file you want to use.
```cpp
BEGIN_PROLOG

standard_textfilegen:
{
 module_type:   TextFileGen
 InputFileName: "dp.txt"
}

END_PROLOG

```
## Modified mass of the particle 
```bash
awk '{if (NR % 3 == 0) sub("0.000511", "0.493677"); print}' f.txt > f_modified.txt
```

## Calculate events by hands, exported in txt file.
```bash
split -l 3000 -d your_file.txt ek_
```
## Text File Gen
The first line contains two entries, the event number (which is ignored in ART/LArSoft) and the number of particles in the event. Each following line containes 15 entries to describe each particle. The entries are:

- status code (should be set to 1 for any particle to be tracked, others won't be tracked)
- the pdg code for the particle
- the entry of the first mother for this particle in the event, 0 means no mother
- the entry of the second mother for this particle in the event, 0 means no mother
- the entry of the first daughter for this particle in the event, 0 means no daughter
- the entry of the second daughter for this particle in the event, 0 means no daughter
- x component of the particle momentum
- y component of the particle momentum
- z component of the particle momentum
- energy of the particle
- mass of the particle
- x position of the particle initial position
- y position of the particle initial position
- z position of the particle initial position
- time of the particle production
- 
For example, if you want to simulate a single muon with a 5 GeV energy moving only in the z direction, the entry would be
```bash
0 1
1 13 0 0 0 0 0. 0. 1.0 5.0011 0.105 1.0 1.0 1.0 0.0
```
There are some assumptions that go into using this format that may not be obvious. The first is that only particles with status code = 1 are tracked in the LArSoft/Geant4 combination making the mother daughter relations somewhat irrelevant. That also means that you should let Geant4 handle any decays.

The units in LArSoft are cm for distances and ns for time.

