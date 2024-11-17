#!/bin/bash

# Function to fix indentation issues
fix_indentation() {
    local file="$1"
    echo "Fixing indentation in $file..."

    # Use sed to replace tabs with 4 spaces (if using spaces for indentation)
    sed -i 's/^\t/    /g' "$file"

    # Convert all tabs to spaces (if using spaces for indentation)
    expand -t 4 "$file" > temp_file && mv temp_file "$file"

    # Run autopep8 to fix other indentation issues
    autopep8 --in-place "$file"
}

# Iterate over all Python files in the current directory and subdirectories
find . -name "*.py" | while read -r file; do
    fix_indentation "$file"
done

echo "Indentation fixing complete."

