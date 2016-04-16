NOW=`date +%Y%m%d-%H.%M.%S`

/c/q/w32/q.exe code/tick.q -p 10000 > ./logs/$NOW"_ticker.log" 2>&1 &

/c/q/w32/q.exe data -p 10002 > ./logs/$NOW"_history.log" 2>&1 &

/c/q/w32/q.exe code/rdb.q -source ::10000 -p 10001 > ./logs/$NOW"_realtime.log" 2>&1 &