# OISISI_HTMLSE
Second project from OISISI Subject (Fundamentals of Information Systems and Software Engineering); E2/RA-PRNiI, 5th semester - PYTHON.

[HTMLSE website](https://one-e2-team.github.io/OISISI_HTMLSE/)

In order to set up Test Dataset, Run as Administrator following PowerShell command (only on Windows, in Linux default execution policy in powershel is Unrestricted, however, given script won't work under Linux ¯\\_(ツ)_/¯)
```powershell
Set-ExecutionPolicy RemoteSigned
```
After that, every time you need the test set rebuild just run the [`get-dataset-test.ps1`](get-dataset-test.ps1) poweshell script.


This program has been developed and tested using Python interpreter version 3.7.5.

## Needed external python libraries (without their requirements):

- [Progressbar2](https://pypi.org/project/progressbar2) version 3.47.0 (current)  `pip install progresbar2`
- [NumPy](https://pypi.org/project/numpy/) version 1.18.1 (current)  `pip install numpy`
- [Parglare](https://pypi.org/project/parglare/) version 0.12.0 (current)  `pip install parglare`

or see [requirements.txt](requirements.txt)

### Algorithm

The ranking algorithm (as well as all functions in project) are explained in documentation comments within the code.
For Ranking alorithm, as entry point to the explanation, use `get_ranks` method in module `irank` in `search` package.
