#!/bin/bash

let LIMIT=20
let N=1
while [ $N -le $LIMIT ]; do
	echo "$N -> $(python div4.py $N)"
	let N=N+1
done
