Push-Location $PSScriptRoot/..
Start-Process node -ArgumentList 'node_modules/http-server/bin/http-server'
Pop-Location
