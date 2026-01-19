# PowerShell script to add favicon meta tags to HTML files
# This script adds proper favicon tags to all HTML fil files that are missing them

$faviconTags = @"
  <!-- Favicon - Multiple sizes for Google Search & Browsers -->
  <!-- Google requires 192x192 or larger for search results -->
  <link rel="icon" type="image/png" sizes="192x192" href="images/favicon-192.png">
  <!-- Apple touch icon for iOS devices -->
  <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
  <!-- Standard favicon for browser tabs -->
  <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32.png">
  <!-- Legacy favicon for older browsers -->
  <link rel="shortcut icon" href="images/favicon.ico">
"@

$faviconTagsActivities = $faviconTags -replace 'href="images/', 'href="../images/'

# List of root HTML files
$rootFiles = @(
    "activities.html",
    "packs.html",
    "reviews.html",
    "contact.html",
    "about.html",
    "checkout.html",
    "blog.html",
    "blog-single.html"
)

# Process root files
foreach ($file in $rootFiles) {
    $filePath = "e:\Marragafay\$file"
    if (Test-Path $filePath) {
        $content = Get-Content -Path $filePath -Raw
        
        # Check if favicon tags already exist
        if ($content -notmatch 'favicon-192') {
            # Find </head> tag and insert before it
            $content = $content -replace '</head>', ($faviconTags + "`r`n</head>")
            Set-Content -Path $filePath -Value $content -NoNewline
            Write-Host "Added favicon tags to: $file" -ForegroundColor Green
        } else {
            Write-Host "Favicon tags already exist in: $file" -ForegroundColor Yellow
        }
    }
}

# Process activity detail pages
$activityFiles = Get-ChildItem -Path "e:\Marragafay\activities\" -Filter "*.html"
foreach ($file in $activityFiles) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Check if favicon tags already exist
    if ($content -notmatch 'favicon-192') {
        # Find </head> tag and insert before it
        $content = $content -replace '</head>', ($faviconTagsActivities + "`r`n</head>")
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "Added favicon tags to: activities\$($file.Name)" -ForegroundColor Green
    } else {
        Write-Host "Favicon tags already exist in: activities\$($file.Name)" -ForegroundColor Yellow
    }
}

# Process package detail pages
$packageFiles = Get-ChildItem -Path "e:\Marragafay\packages\" -Filter "*.html"
foreach ($file in $packageFiles) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Check if favicon tags already exist
    if ($content -notmatch 'favicon-192') {
        # Find </head> tag and insert before it
        $content = $content -replace '</head>', ($faviconTagsActivities + "`r`n</head>")
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "Added favicon tags to: packages\$($file.Name)" -ForegroundColor Green
    } else {
        Write-Host "Favicon tags already exist in: packages\$($file.Name)" -ForegroundColor Yellow
    }
}

Write-Host "`nCompleted! All HTML files have been updated with fav icon tags." -ForegroundColor Green
Write-Host "Remember to create the actual favicon files in the images folder." -ForegroundColor Cyan
