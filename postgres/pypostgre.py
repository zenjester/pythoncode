#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='test1' user='test' host='216.189.151.23' password='craven'")
    print "Yes a connection"
except:
    print "I am unable to connect to the database"
