#!/bin/bash
# This script is used to import custom strategies into vnpy_ctastrategy module.
# Change the destination path to your own vnpy_ctastrategy installation path.
# Make the script executable by running "chmod +x import_strategies.sh"
# Then do 'bash import_strategies.sh' to import your custom strategies.

# Set the destination path to the strategies folder of vnpy_ctastrategy module.
# Change the path below to your own vnpy_ctastrategy installation path.
DEST_PATH=/home/shell007/anaconda3/envs/ve/lib/python3.9/site-packages/vnpy_ctastrategy/strategies

# Copy your custom strategy file to the destination folder.
cp my_strategy.py $DEST_PATH