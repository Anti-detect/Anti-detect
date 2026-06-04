# Quick local checks before push (docs hub).
# Usage: .\scripts\verify-docs.ps1

$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent

Write-Host "Checking legacy branding (README + docs only)..." -ForegroundColor Cyan
$mdFiles = @(
    (Join-Path $root "README.md")
) + (Get-ChildItem $root -Filter "README.*.md" | ForEach-Object { $_.FullName }) `
  + (Get-ChildItem (Join-Path $root "docs") -Filter "*.md" | ForEach-Object { $_.FullName })

$pattern = 'adblogin\.com|toolskiemtrieudo|ADBNEW50|SAVE50|business@adblogin'
$hits = $mdFiles | Select-String -Pattern $pattern
if ($hits) {
    $hits | ForEach-Object { Write-Host "$($_.Path):$($_.LineNumber) $($_.Line)" }
    throw "Legacy branding found."
}

Write-Host "Checking promo codes in README.md..." -ForegroundColor Cyan
$readme = Get-Content (Join-Path $root "README.md") -Raw
if ($readme -notmatch 'SAAS50' -or $readme -notmatch 'MIN50') {
    throw "README.md must include SAAS50 and MIN50."
}

Write-Host "Checking multilogin-automation repo URLs..." -ForegroundColor Cyan
$urlPattern = 'https://github.com/multilogin-automation/[A-Za-z0-9_.-]+'
$allUrls = $mdFiles | Select-String -Pattern $urlPattern -AllMatches |
    ForEach-Object { $_.Matches } | ForEach-Object { $_.Value } | Sort-Object -Unique

foreach ($url in $allUrls) {
    $resp = Invoke-WebRequest -Uri $url -Method Head -MaximumRedirection 5 -TimeoutSec 20 -UseBasicParsing
    Write-Host "OK $($resp.StatusCode) $url" -ForegroundColor Green
}

Write-Host "All local doc checks passed." -ForegroundColor Green
