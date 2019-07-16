#!/usr/bin/env bash

loadtest -k http://g6.fuse.tikal.io/cart -m GET --rps 150 -n 3000
