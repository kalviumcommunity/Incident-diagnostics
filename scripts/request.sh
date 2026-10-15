#!/bin/sh
set -eu
. ./network/resolve.env
curl --noproxy '*' --fail --show-error --silent --max-time 5 --resolve "$HOSTNAME:18084:127.0.0.1" "http://notes.test:18084/health"
