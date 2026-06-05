# Quick local checks before push (docs hub).
# Usage: .\scripts\verify-docs.ps1

$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent

Write-Host "Checking legacy branding..." -ForegroundColor Cyan
$mdFiles = @(
    (Join-Path $root "README.md")
    (Join-Path $root "CONTRIBUTING.md")
    (Join-Path $root "SECURITY.md")
    (Join-Path $root "SUPPORT.md")
) + (Get-ChildItem $root -Filter "README.*.md" | ForEach-Object { $_.FullName }) `
  + (Get-ChildItem (Join-Path $root "docs") -Recurse -Filter "*.md" | ForEach-Object { $_.FullName }) `
  + (Get-ChildItem (Join-Path $root "sdk") -Recurse -Filter "*.md" -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName })

$legacy = 'adblogin\.com|toolskiemtrieudo|t\.me/|ADBNEW50|SAVE50|business@adblogin'
$extKit = 'multilogin-automation'

$hits = $mdFiles | Select-String -Pattern $legacy
if ($hits) {
    $hits | ForEach-Object { Write-Host "$($_.Path):$($_.LineNumber) $($_.Line)" }
    throw "Legacy branding found."
}

$ext = $mdFiles | Select-String -Pattern $extKit
if ($ext) {
    $ext | ForEach-Object { Write-Host "$($_.Path):$($_.LineNumber) $($_.Line)" }
    throw "External kit org references found. Keep content in this repo."
}

Write-Host "Checking promo codes and UTM in README locales..." -ForegroundColor Cyan
Get-ChildItem $root -Filter "README*.md" | ForEach-Object {
    $text = Get-Content $_.FullName -Raw
    if ($text -notmatch 'SAAS50' -or $text -notmatch 'MIN50' -or $text -notmatch 'utm_source=saas') {
        throw "$($_.Name) must include SAAS50, MIN50, and utm_source=saas."
    }
    Write-Host "OK $($_.Name)" -ForegroundColor Green
}

Write-Host "Checking affiliate footer in docs/ and sdk/ markdown..." -ForegroundColor Cyan
$affTargets = (Get-ChildItem (Join-Path $root "docs") -Recurse -Filter "*.md" | ForEach-Object { $_.FullName }) `
  + (Get-ChildItem (Join-Path $root "sdk") -Recurse -Filter "*.md" -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName })
$skipAff = @('pricing-footer.md', 'pricing-cta.md')
foreach ($path in $affTargets) {
    $name = Split-Path $path -Leaf
    if ($skipAff -contains $name) { continue }
    $text = Get-Content $path -Raw
    if ($text -notmatch 'SAAS50' -or $text -notmatch 'MIN50' -or $text -notmatch 'multilogin\.com/pricing') {
        throw "$(Split-Path $path -Leaf) must include SAAS50, MIN50, and multilogin.com/pricing."
    }
    Write-Host "OK $(Split-Path $path -Leaf)" -ForegroundColor Green
}

Write-Host "Running spec integrity check..." -ForegroundColor Cyan
python (Join-Path $root "scripts\check-spec-integrity.py")

Write-Host "All local doc checks passed." -ForegroundColor Green
