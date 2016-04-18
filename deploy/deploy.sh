#!/bin/bash
echo "deploying $1"
app=$(basename `pwd`)
echo $app

if [ ! -d /apps/$app/$1 ]; then
	mkdir -p /apps/$app/$1
fi

if [ -f /apps/$app/$1/bin/stop.sh ]; then
	cd /apps/$app/$1/
	./bin/stop.sh
	cd -
fi


cp -r $1/src/topdir/* /apps/$app/$1/

dos2unix /apps/$app/$1/bin/*

chmod u+x /apps/$app/$1/bin/*

if [ ! -d /apps/$app/$1/logs ]; then
	mkdir /apps/$app/$1/logs
fi

if [ ! -d /apps/$app/$1/data ]; then
        mkdir /apps/$app/$1/data
fi

if [ ! -d /apps/$app/$1/tplog ]; then
        mkdir /apps/$app/$1/tplog
fi

cd /apps/$app/$1
./bin/run.sh
cd -


