# OISISI_Python
Drugi projekat iz predmeta OISISI (Osnovi informacionih sistema i softverskog inženjerstva) E2/RA-PRNiI, peti semestar - PYTHON.

[HTMLSE website](https://fmasterofu.github.io/OISISI_Python/)

In order to set up Test Dataset, Run as Administrator following PowerShell command (only on Windows, in Linux default execution policy in powershel is Unrestricted)
```powershell
Set-ExecutionPolicy RemoteSigned
```

After that, every time you need the test set rebuild just run the `get-dataset-test.ps1` poweshell script.


This program has been developed and tested using Python interpreter version 3.7.5.

## Needed external python libraries:

- [Progrssbar2](https://pypi.org/project/progressbar2) version 3.47.0 `pip install progresbar2`
- [NumPy](https://pypi.org/project/numpy/) version version 1.18.1  `pip install numpy`