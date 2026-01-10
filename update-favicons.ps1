# Favicon Update Script
# This script updates all HTML files to use the proper favicon

$files = @(
    "checkout.html",
    "packages/basic.html",
    "packages/comfort.html",
    "packages/luxe.html",
    "activities/buggy.html",
    "activities/camel-ride.html",
    "activities/dinner-show.html",
    "activities/hot-air-balloon.html",
    "activities/paragliding.html",
    "activities/quad-biking.html"
)

foreach ($file in $files) {
    $fullPath = Join-Path "e:\Marragafay" $file
    
    if (Test-Path $fullPath) {
        $content = Get-Content $fullPath -Raw
        
        # Determine if we're in a subdirectory
        $iconPath = if ($file.Contains("/")) { "/icon.png" } else { "/icon.png" }
        $appleIconPath = if ($file.Contains("/")) { "/apple-icon.png" } else { "/apple-icon.png" }
        
        # Replace old favicon references
        $content = $content -replace '<link rel="icon"[^>]*href="[^"]*main-logo\.jpg"[^>]*>', "<link rel=""icon"" type=""image/png"" href=""$iconPath"">"
        $content = $content -replace '<link rel="shortcut icon"[^>]*href="[^"]*main-logo\.jpg"[^>]*>', ''
        
        # Add apple touch icon if not present
        if ($content -notmatch 'apple-touch-icon') {
            $content = $content -replace '(<link rel="icon"[^>]*>)', "`$1`r`n  <link rel=""apple-touch-icon"" href=""$appleIconPath"">"
        }
        
        Set-Content $fullPath $content -NoNewline
        Write-Host "Updated: $file"
    }
}

Write-Host "Favicon update complete!"
