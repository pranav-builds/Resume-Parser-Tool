# main.py

import os
from utils.organizer import organize_by_date
from utils.parser import extract_info_from_pdf
import pandas as pd
from tabulate import tabulate
from rich.console import Console

console = Console()

INPUT_FOLDER = 'resumes'
ORG_FOLDER = 'organized/by_date'
OUTPUT_FILE = 'output/extracted_data.xlsx'

def main():
    # Step 1: Organize files
    console.rule("[bold cyan]PDF Organizer")
    organize_by_date(INPUT_FOLDER, ORG_FOLDER)
    console.print("[green]PDFs organized by modified date.")

    # Step 2: Parse files
    console.rule("[bold cyan]Parsing Resumes")
    extracted_data = []

    for root, _, files in os.walk(ORG_FOLDER):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                info = extract_info_from_pdf(file_path)
                extracted_data.append(info)

    # Step 3: Output
    df = pd.DataFrame(extracted_data)
    df.to_excel(OUTPUT_FILE, index=False)

    # Print to console as table
    console.print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    console.print(f"\n[bold green]✅ All done! Extracted data saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
