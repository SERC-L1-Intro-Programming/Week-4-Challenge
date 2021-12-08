#!/bin/bash

CHALLENGEFILE=commacode.py

_check_file_exists () {
    # internal function to exit test if file missing
    # arguments
    # $1 feedback message
    if [ ! -f "$CHALLENGEFILE" ]; then
        echo "$CHALLENGEFILE missing."
        exit 1
    fi
}

"$@"
