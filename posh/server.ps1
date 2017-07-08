Push-Location $PSScriptRoot/..
Start-Process node -ArgumentList 'server/js/main.js'
Pop-Location
