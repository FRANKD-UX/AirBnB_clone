#!/bin/bash

# Check if autopep8 is installed
if ! command -v autopep8 &> /dev/null
then
	    echo "autopep8 could not be found. Please install it using pip:"
	        echo "pip install autopep8"
		    exit 1
fi

# Log start of formatting
echo "Starting code formatting with autopep8..."

# Run autopep8 with the specified options
autopep8 --max-line-length 75 --in-place --recursive .

# Log completion
echo "Code formatting completed successfully."
