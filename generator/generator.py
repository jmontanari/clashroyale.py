#!/usr/bin/env python3
"""
Simple wrapper to run openapi-generator-cli with predefined arguments
"""

import subprocess
import sys


def generate_client(input_file, output_dir, package_name):
    """Run openapi-generator-cli with specified arguments"""

    cmd = [
        "openapi-generator-cli", "generate",
        "-i", input_file,
        "-g", "python",
        "--package-name", package_name,
        "--skip-validate-spec",
        "--global-property", "modelTests=false",
        "--global-property", "apiTests=false",
        "-o", output_dir,
        "--additional-properties", "packageVersion=1.0.0,projectName=clashroyale.py"
    ]

    print(f"Running: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True)
        print("✅ Client generated successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Generation failed with exit code {e.returncode}")
        return False
    except FileNotFoundError:
        print("❌ openapi-generator-cli not found. Install with:")
        print("npm install @openapitools/openapi-generator-cli -g")
        return False


def main():
    # Define your arguments here
    input_file = "swagger.yaml"
    output_dir = "../"
    package_name = "clashroyale"

    success = generate_client(input_file, output_dir, package_name)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()