import subprocess

# Load the required packages
with open('required_packages.txt') as f:
    required_packages = {line.strip().lower() for line in f}

# Load the installed packages
with open('installed_packages.txt') as f:
    installed_packages = {line.strip().lower() for line in f}

# Identify unnecessary packages
unnecessary_packages = installed_packages - required_packages

# Uninstall unnecessary packages
for package in unnecessary_packages:
    print(f"Uninstalling: {package}")  # Print for clarity
    result = subprocess.run(['pip', 'uninstall', package, '-y'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error uninstalling {package}: {result.stderr}")  # Print error if it occurs

