# Quick local checks before push (docs hub).
# Usage: .\scripts\verify-docs.ps1

$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent

Write-Host "Checking legacy branding (README + docs only)..." -ForegroundColor Cyan
$mdFiles = @(
    (Join-Path $root "README.md")
) + (Get-ChildItem $root -Filter "README.*.md" | ForEach-Object { $_.FullName }) `
  + (Get-ChildItem (Join-Path $root "docs") -Filter "*.md" | ForEach-Object { $_.FullName })

$pattern = 'adblogin\.com|toolskiemtrieudo|t\.me/|ADBNEW50|SAVE50|business@adblogin'
$hits = $mdFiles | Select-String -Pattern $pattern
if ($hits) {
    $hits | ForEach-Object { Write-Host "$($_.Path):$($_.LineNumber) $($_.Line)" }
    throw "Legacy branding found."
}

Write-Host "Checking promo codes and UTM in all README locales..." -ForegroundColor Cyan
Get-ChildItem $root -Filter "README*.md" | ForEach-Object {
    $text = Get-Content $_.FullName -Raw
    if ($text -notmatch 'SAAS50' -or $text -notmatch 'MIN50' -or $text -notmatch 'utm_source=saas') {
        throw "$($_.Name) must include SAAS50, MIN50, and utm_source=saas."
    }
    Write-Host "OK $($_.Name)" -ForegroundColor Green
}

Write-Host "Checking multilogin-automation repo URLs..." -ForegroundColor Cyan
$urlPattern = 'https://github.com/multilogin-automation/[A-Za-z0-9_.-]+'
$allUrls = [System.Collections.Generic.HashSet[string]]::new()
foreach ($file in $mdFiles) {
    $text = Get-Content $file -Raw
    foreach ($m in [regex]::Matches($text, $urlPattern)) {
        [void]$allUrls.Add($m.Value)
    }
}
if ($allUrls.Count -eq 0) {
    throw "No multilogin-automation URLs found to verify."
}

foreach ($url in ($allUrls | Sort-Object)) {
    $resp = Invoke-WebRequest -Uri $url -Method Head -MaximumRedirection 5 -TimeoutSec 20 -UseBasicParsing
    Write-Host "OK $($resp.StatusCode) $url" -ForegroundColor Green
}

Write-Host "All local doc checks passed." -ForegroundColor Green
