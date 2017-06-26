docker run --rm -itv "$(Resolve-Path ..\..):/bq" -p 8000:8000 -p 8080:8080 --name browserquest browserquest sh
