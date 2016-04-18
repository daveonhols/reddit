NOW=`date +%Y%m%d-%H.%M.%S`

$PYEXE code/feeder.py > ./logs/$NOW"_feeder.log" 2>&1 &
