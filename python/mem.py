#!/usr/bin/env python

from threading import Thread
import sys
sys.path.append("python-memcached-1.44")


#{{{ Workers
class Workers(Thread):
	def __init__(self, c, times, gs):
		Thread.__init__(self)

		self.c = c
		self.times = times
		self.gs = gs
		self.completiontime = 0
		self.name = c

	def run(self):
		import memcache
		from hashlib import md5
		from time import time

		startTime = time()
		for i in range(self.times):
			m = memcache.Client(['localhost:11310'])

			hashval = md5(str(self.c) + str(i)).hexdigest()
			if self.gs == 'set':
				m.set(hashval, hashval)
			else:
				m.get(hashval)

			m.disconnect_all()

		endTime = time()
		self.completiontime = endTime - startTime
#}}} Workers


#chars = 'a,b,c,d,e,f,g,h,i,j'.split(',')
threads = []
for char in range(int(sys.argv[2])):
	print char

	gs = 'get'
	if sys.argv[1] == 'set':
		gs = 'set'

	t = Workers(char, 10000, gs)
	threads.append(t)
	t.start()


for t in threads:
	t.join()
	print 'Got ', t.name, t.gs, t.completiontime

# vim: fdm=marker:
