#!/bin/sh

# generate coverage report for all the files in the package app, even those not tested
coverage run --branch --source=app -m pytest
# generate an html report
coverage html
OS="$(uname)"

# Open the HTML coverage report with the default browser
if [ "$OS" = "Darwin" ]; then
    # macOS
    open ./htmlcov/index.html
elif [ "$OS" = "Linux" ]; then
    # Linux
    xdg-open ./htmlcov/index.html &
else
    echo "Unsupported OS: $OS"
fi
