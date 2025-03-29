import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {e.cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Error Output:\n{e.stderr}")

def main():
    with open('requirements.txt') as f:
        packages = [line.strip() for line in f if line.strip()]
    for package in packages:
        command = ["pip", "install", package]
        print(f"Installing: {package}")
        run_command(command)

if __name__ == "__main__":
    main()
