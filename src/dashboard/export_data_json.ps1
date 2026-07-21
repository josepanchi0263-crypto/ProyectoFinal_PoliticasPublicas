Add-Type -AssemblyName System.IO.Compression.FileSystem

$inputPath = (Resolve-Path '..\..\data\Dataset_BDH_Simulado.xlsx').Path
$outputPath = Join-Path (Get-Location) 'datos_reales_psm_raw.json'

$zip = [System.IO.Compression.ZipFile]::OpenRead($inputPath)
$entry = $zip.GetEntry('xl/worksheets/sheet2.xml')
$reader = New-Object System.IO.StreamReader($entry.Open())
$xml = [xml]$reader.ReadToEnd()
$reader.Close()

function Get-CellValue($cell) {
    if ($cell.v) { return $cell.v.'#text' }
    if ($cell.is) { return $cell.is.t }
    return ''
}

$rows = @()
$headers = @{}

foreach ($row in $xml.worksheet.sheetData.row) {
    $rowIndex = [int]$row.r
    $mapped = @{}
    foreach ($cell in $row.c) {
        $col = ($cell.r -replace '\d+$', '')
        $mapped[$col] = Get-CellValue $cell
    }

    if ($rowIndex -eq 1) {
        foreach ($entry in $mapped.GetEnumerator()) {
            $headers[$entry.Key] = $entry.Value
        }
        continue
    }

    if ($mapped.Count -eq 0) { continue }

    $record = @{}
    foreach ($col in $headers.Keys) {
        $header = $headers[$col]
        $value = if ($mapped.ContainsKey($col)) { $mapped[$col] } else { '' }
        switch -regex ($header) {
            '^(ID_Hogar|Jefe_Mujer|Anios_Escolaridad|Num_Hijos|Area_Rural|Puntaje_Registro_Social|Recibe_BDH|Ingreso_Per_Capita_USD)$' {
                if ($value -eq '') { $record[$header] = $null } else { $record[$header] = [double]$value }
            }
            default {
                $record[$header] = $value
            }
        }
    }
    $rows += [pscustomobject]$record
}

$json = $rows | ConvertTo-Json -Depth 5
Set-Content -Path $outputPath -Value $json -Encoding UTF8
Write-Output "Exported $($rows.Count) records to $outputPath"
