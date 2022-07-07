#!/bin/bash

curl --silent https://ipinfo.io/json | head -n 2 | tail -n 1 | sed "s/.*\ \"//" | sed "s/\".*//"
