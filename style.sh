#!/usr/bin/env bash

# Collect all Python files in the current directory and its siblings
STYLE_FILES=$(find . -name "*.py")

# First change tabs (if available) to spaces
echo "Converting tabs to spaces..."
find . -wholename '*.py' ! -type d -exec bash -c 'expand -t 4 "$0" > /tmp/e && mv /tmp/e "$0"' {} \;

for STYLE_FILE in $STYLE_FILES; do
    # Check if the tools are available
    if command -v black &> /dev/null; then
        echo "Running black..."
        black -l 78 "$STYLE_FILE"
    else
        echo -e "Consider installing black\npip install black"
    fi

    if command -v isort &> /dev/null; then
        echo "Running isort..."
        isort "$STYLE_FILE"
    else
        echo -e "Consider installing isort\npip install isort"
    fi

    if command -v pycodestyle &> /dev/null; then
        echo "Running pycodestyle..."
        pycodestyle "$STYLE_FILE"
    else
        echo -e "Consider installing pycodestyle\npip install pycodestyle"
    fi
done

