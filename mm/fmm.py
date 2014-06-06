#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 17:09:01
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 23:33:32
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
import sys
sys.path.append('..')
from configs import config

def seg(sentence):
	# print sentence
	trie = config.trie
	s,e=0,0
	segments=[]
	p=trie
	while e< len(sentence):
		# print sentence[e].encode('cp936')
		if sentence[e] in p:
			p = p[sentence[e]]
			e+=1
		else:
			
			if e is s:
				e+=1
			segments.append(sentence[s:e])
			s=e
			p=trie
	if e>s:
		segments.append(sentence[s:])
	return segments


if __name__ == '__main__':
	s='用我们的无私与真诚去感动世界'
	ss=s.decode('utf-8')
	print ('/'.join(seg(ss))).encode('cp936')







	