"""Exporta datos desde el archivo Excel de datos reales a JSON para el dashboard.

Uso:
    python export_data_json.py

Requiere:
    pandas, openpyxl
"""
import json
from pathlib import Path
import pandas as pd

INPUT_PATH = Path(__file__).resolve().parents[2] / 'data' / 'datos_reales_psm.xlsx'
OUTPUT_PATH = Path(__file__).resolve().parent / 'datos_reales_psm.json'


def load_excel_data(path: Path) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name=0, engine='openpyxl')


def export_to_json(df: pd.DataFrame, output_path: Path) -> None:
    records = df.to_dict(orient='records')
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def main() -> None:
    df = load_excel_data(INPUT_PATH)
    export_to_json(df, OUTPUT_PATH)
    print(f'Exported {len(df)} rows to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()
