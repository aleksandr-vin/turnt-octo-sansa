#!/usr/bin/env bash

while true ; do
    date --rfc-3339='seconds'
    curl -v --max-time 5 --proxy localhost:3128 http://web:5000/ #-H 'If-None-Match: 123qwe321'
    printf "\n\n\n"
    echo waiting for 10 sec...
    sleep 10
    printf "\n\n\n"
done
