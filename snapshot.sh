#!/bin/bash

# Variables
BACKUP_TARGET_DIR="/home/wei/demo/backup"
BACKUP_SOURCE_DIR="/home/csgoserver/csgo5v5/serverfiles/csgo"

# Copy files
cp ${BACKUP_SOURCE_DIR}/*dem ${BACKUP_TARGET_DIR} || { echo "No .dem files to copy"; exit 1; }

# Change directory to BACKUP_TARGET_DIR
cd ${BACKUP_TARGET_DIR}

# Classify files by date and compress
for file in *dem; do
    # Extract date
    date=${file:8:10}

    # If tar.gz file with the same date exists, extract it
    if [ -f ${date}.tar.gz ]; then
        tar -zxvf ${date}.tar.gz && rm -rf ${date}.tar.gz
    fi

    # Make directory if it doesn't exist
    mkdir -p $date

    # Move file to its date directory and remove the original file
    mv $file $date && rm -rf $file

    # Compress date directory into a tar.gz file and remove the date directory
    tar zcvf ${date}.tar.gz $date && rm -rf $date
done
