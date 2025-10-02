Create ssh tunnelling:
```bash
ssh -L 1443:acd-ops01.fnal.gov:443 acdaq@acd-gw05.fnal.gov
```
In firefox, go to [https://localhost:1443](https://localhost:1443). 
- Then click `acdaq` to connect.
