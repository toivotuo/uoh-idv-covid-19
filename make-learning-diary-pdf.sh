#!/bin/sh

# Make a PDF copy of a learning diary.

if [ "$#" != "1" ]
then
  echo "Usage: $0 <diary-number>" >&2
  exit 1
fi

BASE="learning-diary-${1}"

pandoc -f gfm -o ${BASE}.pdf --variable urlcolor=cyan ${BASE}.md
