#!/bin/bash

COUNTER=1
let LIMIT=10
while [ $COUNTER -le $LIMIT ]; do
	let N=4*$COUNTER
	echo $N
	python div4.py $N
	let COUNTER=COUNTER+1
done
