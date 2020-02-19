Remove-Item -Force -Confirm:$false .\test-skup.zip
Remove-Item -Recurse -Force -Confirm:$false .\test-skup
$url = "https://fmasterofu.github.io/OISISI_HTMLSE/dataset/test-skup.zip"
$output = "$PSScriptRoot\test-skup.zip"
Invoke-WebRequest -Uri $url -OutFile $output
Expand-Archive $output
Remove-Item -Force -Confirm:$false .\test-skup.zip