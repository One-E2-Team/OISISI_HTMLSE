# OISISI_HTMLSE
Second project from OISISI Subject (Fundamentals of Information Systems and Software Engineering); E2/RA-PRNiI, 5th semester - PYTHON.

[HTMLSE website](https://fmasterofu.github.io/OISISI_HTMLSE/)

In order to set up Test Dataset, Run as Administrator following PowerShell command (only on Windows, in Linux default execution policy in powershel is Unrestricted, however, given script won't work under Linux ¯\\_(ツ)_/¯)
```powershell
Set-ExecutionPolicy RemoteSigned
```
After that, every time you need the test set rebuild just run the [`get-dataset-test.ps1`](get-dataset-test.ps1) poweshell script.


This program has been developed and tested using Python interpreter version 3.7.5.

## Needed external python libraries (without their requirements):

- [Progressbar2](https://pypi.org/project/progressbar2) version 3.47.0 `pip install progresbar2`
- [NumPy](https://pypi.org/project/numpy/) version version 1.18.1  `pip install numpy`
- [Parglare](https://pypi.org/project/parglare/) version version 0.12.0  `pip install parglare`

or see [requirements.txt](requirements.txt)
