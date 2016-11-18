#!/usr/bin/env bash

rm -f jmeter.log log.jtl
jmeter -n -t httptest.jmx -l log.jtl
echo ""
echo ">>> Requests with error:"
cat log.jtl | grep -v "Request,200"