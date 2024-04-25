$exclude = @("venv", "RPAChallenge_UiPathReframeworkTemplate.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "RPAChallenge_UiPathReframeworkTemplate.zip" -Force