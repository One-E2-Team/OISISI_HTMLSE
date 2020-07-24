Remove-Item -Force -Confirm:$false .\test-skup.zip
Remove-Item -Recurse -Force -Confirm:$false .\test-skup
$url = "https://github.com/One-E2-Team/OISISI_HTMLSE/dataset/test-skup.zip"
$output = "$PSScriptRoot\test-skup.zip"
Invoke-WebRequest -Uri $url -OutFile $output
Expand-Archive $output
Remove-Item -Force -Confirm:$false .\test-skup.zip
