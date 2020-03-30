#!/bin/sh

# Refresh data from all of the sources.

# FIXME: Missing "jhu" datasource refresh.

(cd ./oxford && ./refresh-data.sh)
