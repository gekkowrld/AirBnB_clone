#!/usr/bin/env bash

# Collect all Python files in the current directory and its siblings
STYLE_FILES=$(find . -name "*.py")

# First change tabs (if available) to spaces
echo "Converting tabs to spaces..."
find . -name '*.py' ! -type d -exec bash -c 'expand -t 4 "$0" > /tmp/e && mv /tmp/e "$0"' {} \;

# Check if the tools are available
if command -v black &> /dev/null; then
    echo "Running black..."
    black $STYLE_FILES
else
    echo "Consider installing black"
fi

if command -v isort &> /dev/null; then
    echo "Running isort..."
    isort $STYLE_FILES
else
    echo "Consider installing isort"
fi

if command -v pycodestyle &> /dev/null; then
    echo "Running pycodestyle..."
    pycodestyle $STYLE_FILES
else
    echo "Consider installing pycodestyle"
fi
