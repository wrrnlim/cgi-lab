#!/usr/bin/env python3
import os
import json

print("Content-Type:text/html")
print()

print("<p>QUERY_STRING =", os.environ["QUERY_STRING"], "</p>")
print("<p>HTTP_USER_AGENT =", os.environ["HTTP_USER_AGENT"], "</p>")
