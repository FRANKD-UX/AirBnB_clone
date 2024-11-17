#!/usr/bin/env bash
# Script to run pycodestyle --first on all Python files from the project's root

SCRIPT_DIR=$(dirname "$(realpath "$0")")

echo "Running pycodestyle --first on Python files from $SCRIPT_DIR..."
find "$SCRIPT_DIR" -type f -name "*.py" ! -path "*/__pycache__/*" -exec pycodestyle --first {} +

if [ $? -eq 0 ]; then
	    echo "No pycodestyle issues found!"
    else
	        echo "Pycodestyle check complete. Please address the above issues."
fi
