# Automating file operations
import os
import shutil
from datetime import datetime

def organize_downloads():
    """Sort files in Downloads folder by type into subfolders."""
    download_dir = os.path.expanduser("~/Downloads")
    
    # Create folders if they don't exist
    categories = ["Documents", "Images", "Videos", "Other"]
    for category in categories:
        folder = os.path.join(download_dir, category)
        if not os.path.exists(folder):
            os.mkdir(folder)
    
    # Extensions for each category
    extensions = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Images": [".jpg", ".png", ".gif"],
        "Videos": [".mp4", ".mov", ".avi"]
    }
    
    # Move files to appropriate folders
    for filename in os.listdir(download_dir):
        if os.path.isfile(os.path.join(download_dir, filename)):
            # Determine destination folder
            destination = "Other"  # Default
            file_ext = os.path.splitext(filename)[1].lower()
            
            for category, exts in extensions.items():
                if file_ext in exts:
                    destination = category
                    break
            
            # Move the file
            shutil.move(
                os.path.join(download_dir, filename),
                os.path.join(download_dir, destination, filename)
            )
    
    print(f"Organized downloads at {datetime.now()}")

# Can be scheduled to run daily
organize_downloads()
