from nose.tools import *
import puppet_smoke

def setup():
  print "SETUP!"

def teardown():
  print "TEAR DOWN!"

def test_basic():
  print "I RAN!"
