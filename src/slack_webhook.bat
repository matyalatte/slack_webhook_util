@echo off

set url="url here"

curl -X POST --data-urlencode "payload={\"text\": \"%1\"}" %url%
echo;