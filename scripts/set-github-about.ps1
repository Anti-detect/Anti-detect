# Updates GitHub repository About fields via REST API.
# Requires: $env:GITHUB_TOKEN with repo scope (classic PAT or fine-grained on this repo).
#
# Usage:
#   $env:GITHUB_TOKEN = "ghp_..."
#   .\scripts\set-github-about.ps1

$ErrorActionPreference = "Stop"

$owner = "Anti-detect"
$repo = "Anti-detect"
$token = $env:GITHUB_TOKEN

if (-not $token) {
    Write-Host "Set GITHUB_TOKEN first (repo scope)." -ForegroundColor Yellow
    Write-Host "Example: `$env:GITHUB_TOKEN = 'ghp_...'; .\scripts\set-github-about.ps1"
    exit 1
}

$metaPath = Join-Path $PSScriptRoot "..\.github\repo-metadata.json"
if (-not (Test-Path $metaPath)) {
    Write-Error "Missing $metaPath"
}
$meta = Get-Content $metaPath -Raw | ConvertFrom-Json

$body = @{
    description     = $meta.description
    homepage        = $meta.homepage
    has_wiki        = $meta.has_wiki
    has_discussions = $meta.has_discussions
} | ConvertTo-Json

$headers = @{
    Authorization = "Bearer $token"
    Accept        = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

Write-Host "Patching repository metadata..."
Invoke-RestMethod -Method Patch -Uri "https://api.github.com/repos/$owner/$repo" -Headers $headers -Body $body -ContentType "application/json"

$topicBody = @{ names = @($meta.topics) } | ConvertTo-Json
Write-Host "Applying $($meta.topics.Count) topics..."
Invoke-RestMethod -Method Put -Uri "https://api.github.com/repos/$owner/$repo/topics" -Headers $headers -Body $topicBody -ContentType "application/json"

Write-Host "Done. Verify at https://github.com/$owner/$repo" -ForegroundColor Green
