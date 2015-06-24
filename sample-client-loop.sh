#!/usr/bin/env bash

while true ; do
    echo waiting for 10 sec...
    sleep 10 && curl -v --proxy localhost:3128 http://web:5000/
done
