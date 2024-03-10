#!/usr/bin/env bash

# Collect all Python files in the current directory and its siblings
STYLE_FILES=
if [ "$#" -ge 1 ]; then
	INPUT="$1"
	# Check if the input is a file
	if [ -f "$INPUT" ]; then
		STYLE_FILES=$INPUT
	else
		# Check for the py files in the directory instead
		STYLE_FILES=$(find "$INPUT" -name "*.py")
	fi
else
	STYLE_FILES=$(find . -name "*.py")
fi

# First change tabs (if available) to spaces
echo "Converting tabs to spaces..."
find . -wholename '*.py' ! -type d -exec bash -c 'expand -t 4 "$0" > /tmp/e && mv /tmp/e "$0"' {} \;

for STYLE_FILE in $STYLE_FILES; do
	# Check if the first line is the shebang line
	if ! head -n 1 "$STYLE_FILE" | grep -q "#!/usr/bin/python3"; then
		if [[ $(stat -c%s "$STYLE_FILE") -gt 0 ]]; then
			echo "Adding shebang line to $STYLE_FILE..."
			sed -i '1i#!/usr/bin/python3' "$STYLE_FILE"
		fi
	fi

	# Check if the tools are available
	if command -v black &>/dev/null; then
		echo "Running black..."
		black -l 78 "$STYLE_FILE"
	else
		echo -e "Consider installing black\npip install black"
	fi

	if command -v isort &>/dev/null; then
		echo "Running isort..."
		isort "$STYLE_FILE"
	else
		echo -e "Consider installing isort\npip install isort"
	fi

	if command -v pycodestyle &>/dev/null; then
		echo "Running pycodestyle..."
		pycodestyle "$STYLE_FILE"
	else
		echo -e "Consider installing pycodestyle\npip install pycodestyle"
	fi

	if command -v pylint &>/dev/null; then
		echo "Running Pylint for documentation checks on $STYLE_FILE..."
		pylint --rc-file=.slrc "$STYLE_FILE"
	else
		echo -e "Consider installing pylint\npip install pylint"
	fi
	# Make the(all?) files executable
	if [ ! -x "$STYLE_FILE" ]; then
		chmod +x "$STYLE_FILE"
	fi
done
