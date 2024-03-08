#!/bin/sh

FILENAME=$1
SIZE=$2

# Create a file of a size with random data
dd if=/dev/urandom of="$FILENAME" bs=1 count="$SIZE"
