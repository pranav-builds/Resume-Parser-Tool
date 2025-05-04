# utils/organizer.py

import os
import shutil
from datetime import datetime

def organize_by_date(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith('.pdf'):
            file_path = os.path.join(input_folder, file)
            date_str = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')
            target_dir = os.path.join(output_folder, date_str)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(target_dir, file))

def organize_by_name(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith('.pdf'):
            name = file.split('_')[0]  # Assuming resumes named like "John_Doe_Resume.pdf"
            target_dir = os.path.join(output_folder, name)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(os.path.join(input_folder, file), os.path.join(target_dir, file))
