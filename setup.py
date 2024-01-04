import os
import shutil
import zipfile

# List of directories to be created in the current directory
directories = [
    "docs",
    "img",
    "templates",
    "src",
    "data",
    "bibliography",
    "scripts",
    "logs",
    "backups",
    "misc"
]

# Function to create the directories in the current directory
def create_directories_in_current(dirs):
    for dir in dirs:
        path = os.path.join(os.getcwd(), dir)
        os.makedirs(path, exist_ok=True)

# Function to integrate the Sullivan Business Report template
def integrate_template(template_dir):
    source_template_dir = "sullivan_template"  # Directory where you placed the template files

    if os.path.exists(source_template_dir):
        # Create the template directory if it doesn't exist
        os.makedirs(template_dir, exist_ok=True)

        # Copy the template files to the template directory
        for root, dirs, files in os.walk(source_template_dir):
            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(template_dir, os.path.relpath(src_file, source_template_dir))
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(src_file, dest_file)
    else:
        print("The Sullivan Business Report template directory does not exist. Please place the template files in a directory named 'sullivan_template'.")

if __name__ == "__main__":
    create_directories_in_current(directories)
    template_dir = os.path.join(os.getcwd(), "templates")
    integrate_template(template_dir)
