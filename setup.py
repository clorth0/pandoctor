import os

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

# Execute the function to create the directories
create_directories_in_current(directories)
