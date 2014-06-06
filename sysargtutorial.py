#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 22:23:23
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 22:24:56
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""





if __name__ == '__main__':
	import sys,getopt
	opts,args = getopt.getopt(sys.argv[1:], 'hi:s:f')
	for op,v in opts:
		print op,v,type(v)







	