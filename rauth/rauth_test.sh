#!/bin/sh

echo user1 with correct password
curl -X POST --data "username=testdomain\\testuser01&password=password1" http://127.0.0.1:8000/rauth/
echo

echo
echo user1 with wrong password
curl -X POST --data "username=testdomain\\testuser01&password=wrong" http://127.0.0.1:8000/rauth/
echo

echo
echo user2 with correct password
curl -X POST --data "username=testdomain\\testuser02&password=password2" http://127.0.0.1:8000/rauth/
echo

echo
echo user2 with wrong password
curl -X POST --data "username=testdomain\\testuser02&password=wrong" http://127.0.0.1:8000/rauth/
echo

echo
echo user3 with correct password
curl -X POST --data "username=testdomain\\testuser03&password=password3" http://127.0.0.1:8000/rauth/
echo

echo
echo user3 with wrong password
curl -X POST --data "username=testdomain\\testuser03&password=wrong" http://127.0.0.1:8000/rauth/
echo

echo
echo
