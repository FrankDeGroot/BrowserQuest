Push-Location $PSScriptRoot/..
Start-Process node -ArgumentList '--inspect-brk', 'server/js/main.js'
Pop-Location
