#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 20:57:37
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 22:23:03
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

import re
from configs import config
import chardet

def foo():
	# sentence='小编总结一下：考前上厕所，考中别抄袭，考完别对题，报考大学需abcd efg 谨慎，看看留言里那些拼命劝人不要考自己大学的小伙伴就知道了'
	# sentence=sentence.decode('utf-8')
	# blocks = config.re_chinese.split(sentence)
	# for b in blocks:
	# 	print b.encode('cp936')
	s='12345678'
	s=s.decode('utf-8')
	for b in config.re_chinese.split(s):
		if config.re_chinese.match(b):
			print b.encode('cp936')
		else :
			tmp = config.re_punc.split(b)
			for bb in tmp:
				if bb.strip() != '':
					print bb.encode('cp936')

def bar():
	s='where is the love'
	print chardet.detect(s)
	print s.encode('cp936')
if __name__ == '__main__':
	import sys,getopt
	opts,args = getopt.getopt(sys.argv[1:], 'hs:f')
	for op,v in opts:
		print op,v
	







	