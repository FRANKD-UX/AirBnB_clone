#!/bin/bash

# Recursively find all files and make them executable
find . -type f -exec chmod +x {} \;
