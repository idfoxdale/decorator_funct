import os
import shutil
import re
from datetime import datetime

def rename_files():
    current_dir = os.getcwd()
    
    for filename in os.listdir(current_dir):
        if "image" in filename and "(" in filename and ")" in filename:
            original_file = os.path.join(current_dir, filename)
            
            # Get file creation date
            creation_time = os.path.getctime(original_file)
            creation_date = datetime.utcfromtimestamp(creation_time).strftime('%d%m%Y%H%M%S')
            
            # Remove "(" and ")"
            new_filename = re.sub(r'[\(\)]', '', filename)
            
            # Insert creation date after "image"
            new_filename = new_filename.replace("image", f"image{creation_date}")
            
            # Rename file
            new_file = os.path.join(current_dir, new_filename)
            shutil.move(original_file, new_file)
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    rename_files()
