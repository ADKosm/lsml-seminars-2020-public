#!/usr/bin/env bash

set -e

sudo fdisk -l
sudo parted /dev/sdc --script mklabel gpt mkpart primary ext4 0% 100%
sudo mkfs -t ext4 /dev/sdc1
sudo fdisk -l
sudo mkdir /data
sudo mount /dev/sdc1 /data
