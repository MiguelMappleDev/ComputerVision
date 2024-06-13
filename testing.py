# python 3.11.1.64 bits

import subprocess
import importlib.util

def validatelibraries(library):
    pass

def main():
    print(f"Validating Libraries")
    cmd = "python --version"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f"Python version {result.stdout}")
    # commiting changes


if __name__ == "__main__":
    main()