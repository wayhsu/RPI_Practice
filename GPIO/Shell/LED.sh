#! /bin/bash

echo 4 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio4/direction

cnt=0

while [ "$cnt" -lt 5 ]
do
    echo $cnt
	
    sleep 0.5
    echo 0 > /sys/class/gpio/gpio4/value
    
    sleep 0.5
    echo 1 > /sys/class/gpio/gpio4/value
	
	cnt=`expr $cnt + 1`
done
