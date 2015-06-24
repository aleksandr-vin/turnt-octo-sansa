# Sample Web Cache Lab Setup

## The setup

`sample-client-loop.sh` <===> `squid` <---> `web`

## Description

1. The `sample-client-loop.sh` simply requests `web` through `squid` every 10 seconds.
2. The `web` returns an HTTP resource with `Cache-Control: no-cache, max-age=30`.
3. The `squid` caches the resource and revalidates it after 30 seconds of age.

## How to run it

If you want to try it yourself, just:

1. `git clone` it
2. Run `docker-compose up`
3. And start the client `sample-client-loop.sh`
