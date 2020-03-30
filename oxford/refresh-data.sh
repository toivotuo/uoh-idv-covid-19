#!/bin/sh

# Fetch the latest source data.

FILENAME="OxCGRT_Download_latest_data.xlsx"

echo "Fetching 'oxford' data with curl"

cd data
curl https://www.bsg.ox.ac.uk/sites/default/files/${FILENAME} > $FILENAME
