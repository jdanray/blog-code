#!/bin/bash

# backup your files to your USB drive

# find the USB drive's mountpoint
USB_DEV_NAME="sdb1"
USB_MOUNTDIR="/media/daniel"
USB_MOUNTPT="$(lsblk | grep ${USB_DEV_NAME} | grep -o ${USB_MOUNTDIR}.*)"

# identify and concatenate the backup files
FILES_LOC="/home/daniel/backup/files.txt"
CAT_FILES="$(tr '\n' ' ' < ${FILES_LOC})"

# archive and compress the files
BACKUP_FILE="backup$(date -I).tar.gz"
tar -czf ${BACKUP_FILE} ${CAT_FILES}

# copy the tarball to the USB drive
rsync -a ${BACKUP_FILE} ${USB_MOUNTPT}
