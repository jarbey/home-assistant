#!/bin/bash

send_key() {
	echo "SEND $1 $2"
	irsend SEND_ONCE $1 $2
	echo "FIN $1 $2"

	echo "Pause $3"
	sleep $3
}

send_key AVR-1509 "KEY_POWER KEY_VCR" 0
send_key TV BTN_0 15
send_key TV KEY_DISPLAYTOGGLE 2
send_key TV KEY_TV 5
send_key TV KEY_DISPLAYTOGGLE 2

for i in {1..3}
do
	send_key TV BTN_DPAD_UP 0.5
done

send_key TV KEY_OK 0
