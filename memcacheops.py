#!/usr/bin/env python2.5

"""

 CDDL HEADER START

 The contents of this file are subject to the terms of the
 Common Development and Distribution License (the "License").
 You may not use this file except in compliance with the License.

 See LICENSE.txt included in this distribution for the specific
 language governing permissions and limitations under the License.

 When distributing Covered Code, include this CDDL HEADER in each
 file and include the License file at LICENSE.txt.
 If applicable, add the following below this CDDL HEADER, with the
 fields enclosed by brackets "[]" replaced with your own identifying
 information: Portions Copyright [yyyy] [name of copyright owner]

 CDDL HEADER END

"""

"""

 Portions Copyright 2009 Matt Ingenthron
  Matt Ingenthron <ingenthr@cep.net>

"""

import sys
sys.path.append("python-memcached-1.44")

import memcache
import time
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# TODO: namespace all operation keys so they don't impact real apps

time.sleep(1)
print "Set and get with found"
mc.set("setop", "a set value")
mc.set("setop", "a new value")
mc.get("setop")
mc.delete("setop")
# TODO: verify those did the right thing

time.sleep(1)
print "Get not found"
mc.get("nothere")
mc.delete("nothere")

time.sleep(1)
print "Add op, then add op existing"
mc.add("addop", "an added value")
mc.add("addop", "shouldn't add")

time.sleep(1)
print "Replace op"
mc.set("replaceop", "new value")
mc.replace("replaceop", "replaced with this value")

time.sleep(1)
print "Set and incr/decr"
mc.set("anumber", "100")
mc.incr("anumber")
mc.decr("anumber")
mc.decr("anumber")
mc.decr("anumber")
mc.decr("anumber")
mc.decr("anumber")
mc.decr("anumber")
mc.decr("anumber")

# TODO: delete all of the objects

"""
 TODO: add a performance test: 
       500 iterations, 1 set and 9 gets per object 1kB objects
       50 iterations, 1 set and 49 gets, 1MByte objects
       report average operation time, with microsecond precision
       small object tests should be under 1ms, large under 3ms
"""
