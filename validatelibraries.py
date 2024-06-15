import subprocess
def validatelibraries(libs):
    print(f"Validating Libraries")
    cmd = "python --version"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f"Python version {result.stdout}")
    # Getting Started with Images
    libraries = libs

    for lib in libraries:
        try:
            exec(f"import {lib}")
            print(f"{lib} is installed.")
        
        except ImportError:
            print(f"{lib} is not installed.")
            subprocess.run(["pip", "install", lib])
