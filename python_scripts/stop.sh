#!/bin/bash

send_key() {
        echo "SEND $1 $2"
        irsend SEND_ONCE $1 $2
        echo "FIN $1 $2"

        echo "Pause $3"
        sleep $3
}

send_key TV BTN_0 0
send_key AVR-1509 Off 0
