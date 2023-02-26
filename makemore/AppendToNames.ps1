# 2052781 records!!
#Get-Content -Path C:\Users\andre\Downloads\names\*.txt
#Get-Content -Path C:\Users\andre\Downloads\names\*.txt | Select-String ',' | ForEach-Object { $_.Line.Split(',')[0].ToLower() }
#Get-Content -Path C:\Users\andre\Downloads\names\*.txt | ForEach-Object { $_.Split(',')[0].ToLower() }
#Get-Content -Path C:\Users\andre\Downloads\names\*.txt | ForEach-Object { $_.Split(',')[0].ToLower() } | Add-Content -Path C:\Users\andre\Documents\names.txt
$count = 0
$total = (Get-ChildItem -Path C:\Users\andre\Downloads\names\*.txt).Count
Get-ChildItem -Path C:\Users\andre\Downloads\names\*.txt | ForEach-Object {
    $count++
    $percent = [Math]::Min(($count / $total) * 100, 100)
    Write-Progress -Activity "Appending to file" -PercentComplete $percent -Status "File $count of $total"
    Get-Content -Path $_.FullName | ForEach-Object {
        $_.Split(',')[0].ToLower()
    }
} | Add-Content -Path C:\Users\andre\ScratchNeuralNet\makemore\names-copy.txt






