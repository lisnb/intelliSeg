#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-05-29 12:46:15
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 23:49:18
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
from __future__ import division
from hmm import viterbi
from mm import fmm,maxprob
from configs import config

if config.USE_CHARDETECT:
	import chardet_ 

HANDLERS={
			'f':fmm.seg,
			'm':maxprob.seg,
			'v':viterbi.seg	
	}


class EncodingError(Exception):
	def __init__(self,value):
		self.value = value 
	def __str__(self):
		return 'Unhandlable Encoding: %s\n'%self.value


# def handle_encoding(sentence):



def segit(sentence,handler):
	if not handler:
		segments = ['[not a valid segment handler.]']
		return segments
	# print handler
	encoding = 'utf-8'
	# try:
	if config.USE_CHARDETECT:
		s_encoding = chardet_.detect(sentence)['encoding']
		if s_encoding.lower() == 'utf-8':
			pass
		elif s_encoding.lower() in ['cp936','gbk','gb2312','ascii']:
			encoding = s_encoding

		else:
			raise EncodingError(s_encoding)
	# else:
	# 	if config.ISWINDOWS:
	# 		encoding='gb2312'
	segments=[]
	ascii_sentence = sentence if encoding=='ascii' else sentence.decode(encoding) 
	validsentence = config.re_chinese.split(ascii_sentence)

	for vs in validsentence:
		if config.re_chinese.match(vs):
			# print vs
			segments.extend(handler(vs))
		else:
			puncs = config.re_punc.split(vs)
			for pe in puncs:
				if pe.strip()!='':
					segments.append(pe)


	return segments
	# except EncodingError as e:
	# 	print e
	# except Exception as e:
	# 	print e 


def seg(inputcontent,handlers='fvm',is_file=False):
	handlers=list(handlers)
	if is_file:
		with open(inputcontent) as f:
			sentence = f.read()
			# print chardet.detect(sentence)
	else:
		sentence=inputcontent
	segments = [segit(sentence,HANDLERS.get(handler,None)) for handler in handlers]

	if is_file:
		for h,segment in zip(handlers,segments):
			filename = '%s.%s.seg.%s'%(inputcontent,h,'txt' if config.ISWINDOWS else '')
			with open(filename,'wb') as f:
				content = '/'.join(segment)
				content=content.encode('utf-8')
				f.write(content)
	else:
		for h,segment in zip(handlers,segments):
			print '[%s]: %s\n'%(h,'/'.join(segment))

	return segments

usage="""

usage: intelliSeg.py  -i <inputcontent> [-s <segmentmethod>] [-f <isfile>]

detail:
	
	-h 	help infomation
	-s 	choose the methed(s) to cut :
			f:	Forward Maximum Matching 
			m:	Maximum Probability Path 
			v:	HMM & Viterbi ('B','M','E','S')
		you can combine them when you want to compare the results:
			eg: -s fm 
			>> return the results of both methods
		if you don't specify, default:
			fmv
		if you input something else, it will return a hint
			eg: -s p "hello world"
				>> [p]:[not a valid segment handler.]
	-i 	the content you want to cut.
		it can be both a sentence and a path to the file containing 
		the sentence 
		you are supposed to surround the content with quotes when it 
		cantains space. 
			eg: valid: "hello world"
				invalid: hello world 
		if a sentence is provided, the result will be output directly
			eg: -i "hello world" -s fm 
				>>[f]: hello/world
				>>[m]: hello/world
		if a file path is provided, there will be some other files 
		added to the directory
			eg:	-i "/foo/biz.txt" -f -s fv
				>> 	the file "/foo/biz.txt_f.seg" 
					and "/foo/biz_v.seg"
					will be created, the content 
					is the same as output
		if it is run on a Windows OS, there will be a '.txt' too 
		in case you want to open it with notepad .
	-f 	specify -f means the input is a file. if it is just a single 
		sentence, ignore it.

"""

if __name__ == '__main__':
	import sys,getopt
	opts,args = getopt.getopt(sys.argv[1:], 'hi:s:f')
	handlers='fvm'
	isfile=False
	inputcontent=''
	if len(opts) is 0:
		print usage
	for op,v in opts:
		if op == '-h':
			print usage
		elif op == '-s':
			handlers=v
		elif op == '-f':
			isfile = True
		elif op == '-i':
			inputcontent=v
	if not inputcontent:
		print 'You should provide a content at least. with -h to check the usage.'
		exit(1)


	seg(inputcontent, handlers,isfile)

	# print handlers,isfile,inputcontent


		




	