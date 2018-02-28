#!/bin/sh

if [ -z $1 ]; then
	echo "ERROR: missing input file"
	exit 1
fi

INPUT=$1
SCANROUND=100

echo "INFO: scanning adddresses from $INPUT"

for all in $(cat $INPUT); do
	python probe.py $all &
	I=$(($I+1))
	if [ $I -eq $SCANROUND ]; then
		wait
		I=0
	fi
done
wait
