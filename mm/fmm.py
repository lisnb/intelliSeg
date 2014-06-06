#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 17:09:01
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 19:14:20
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
import sys
sys.path.append('..')
from configs import config

def seg(sentence):
	trie = config.trie
	s,e=0,0
	segments=[]
	p=trie
	while e< len(sentence):
		if sentence[e] in p:
			p = p[sentence[e]]
			e+=1
		else:
			segments.append(sentence[s:e])
			s=e
			p=trie
	if e>s:
		segments.append(sentence[s:])
	return segments


if __name__ == '__main__':
	s='我很喜欢周杰伦这个歌手'
	ss=s.decode('utf-8')
	print ('/'.join(seg(ss))).encode('cp936')







	