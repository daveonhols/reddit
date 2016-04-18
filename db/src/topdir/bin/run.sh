NOW=`date +%Y%m%d-%H.%M.%S`

$QEXE code/tick.q -p 127.0.0.1:10000 > ./logs/$NOW"_ticker.log" 2>&1 &

$QEXE data -p 127.0.0.1:10002 > ./logs/$NOW"_history.log" 2>&1 &

$QEXE code/rdb.q -source ::10000 -p 127.0.0.1:10001 > ./logs/$NOW"_realtime.log" 2>&1 &
