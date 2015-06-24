#!/usr/bin/env bash

while true ; do
    date --rfc-3339='seconds'
    curl -v --proxy localhost:3128 http://web:5000/
    echo "\n\n\n"
    echo waiting for 10 sec...
    sleep 10
    echo "\n\n\n"
done
