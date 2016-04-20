#!/bin/bash
NOW=`date +%Y%m%d-%H.%M.%S`

$PYEXE code/feeder.py 10020 > ./logs/$NOW"_feeder.log" 2>&1 &
