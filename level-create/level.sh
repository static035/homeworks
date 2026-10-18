#!/bin/bash
#PLEASE READ readme.txt IF YOU DONT KNOW HOW TO USE THIS
#GET the level number (defaults to 0 if none provided)
LEVEL_N=${1:-0}

#declaring variables
LEVEL_DIR="../homeworks/level${LEVEL_N}"
CLASSWORK="${LEVEL_DIR}/classwork"
HOMEWORK="${LEVEL_DIR}/homework"

#make directories for classwork (level gets created as well.)
mkdir -p "$CLASSWORK"
mkdir -p "$HOMEWORK"

#echo the outputs
echo "Successfully created structure for level ${LEVEL_N}✅"
echo "   📁 ${LEVEL_DIR}/"
echo "      ├── 📁 classwork/"
echo "      └── 📁 homework/"