#!/bin/ksh

# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# See LICENSE.txt included in this distribution for the specific
# language governing permissions and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at LICENSE.txt.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END

set -x
NUMRUNNERS=4
MEMCACHED=/Users/ingenthr/src/memcached-dev/memcached/memcached


# start a number of memcached processes

function start_runners {
  for (( i=0; i<$NUMRUNNERS; i++)); do
    $MEMCACHED -m 64 -p 1131$i &
    runnerports[$i]=1131$i;
    if [[ $servers == "" ]]; then
      servers="localhost:1131$i"
    else 
      servers="$servers,localhost:1131$i"
    fi
    export MEMCACHED_SERVERS=$servers
  done
}

function kill_jobs {
  kill "$@" $(jobs -p)
}



function flush_runners {
  fc=${#runnerports[*]}
  i=0
  while [ $i -lt $fc ]; do
    echo flush_all | nc localhost ${runnerports[$i]} 
    (( i=i+1 ))
  done
}

function stats_runners {
  fc=${#runnerports[*]}
  i=0
  while [ $i -lt $fc ]; do
    echo stats | nc localhost ${runnerports[$i]} 
    (( i=i+1 ))
  done
}

function run_peclmemcache {
  php -c php/php.ini php/peclmemcache.php
}

# Main part of the run

start_runners
run_peclmemcache
flush_runners
kill_jobs
wait
