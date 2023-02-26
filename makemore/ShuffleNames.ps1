$total = (Get-Content -Path C:\Users\andre\ScratchNeuralNet\makemore\names.txt).Count
$count = 0
Get-Content -Path C:\Users\andre\ScratchNeuralNet\makemore\names.txt | Sort-Object {Get-Random} | ForEach-Object {
    $count++
    Write-Progress -Activity "Shuffling names" -PercentComplete (($count / $total) * 100) -Status "Line $count of $total"
    $_
} | Set-Content -Path C:\Users\andre\ScratchNeuralNet\makemore\names_shuffled.txt
