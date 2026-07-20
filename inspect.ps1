Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead('data/Dataset_BDH_Simulado.xlsx')
$entry = $zip.GetEntry('xl/worksheets/sheet2.xml')
$reader = New-Object System.IO.StreamReader($entry.Open())
$xml = [xml]$reader.ReadToEnd()
$xml.worksheet.sheetData.row | Select-Object -First 5 | ForEach-Object {
    Write-Output ('ROW {0}' -f $_.r)
    $_.c | ForEach-Object {
        $cell = $_
        $type = $cell.t
        $value = ''
        if ($cell.v) { $value = $cell.v.'#text' }
        if ($cell.is) { $value = $cell.is.t }
        Write-Output ("{0} {1} {2}" -f $cell.r, $type, $value)
    }
    Write-Output '---'
}
