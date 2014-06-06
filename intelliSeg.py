#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-05-29 12:46:15
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 20:53:13
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
from __future__ import division
from hmm import viterbi
from mm import fmm,maxprob
from configs import config

if config.USE_CHARDETECT:
	import chardet 

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
	# print handler
	encoding = 'utf-8'
	# try:
	if config.USE_CHARDETECT:
		s_encoding = chardet.detect(sentence)['encoding']
		if s_encoding.lower() == 'utf-8':
			pass
		elif s_encoding.lower() in ['cp936','gbk','gb2312']:
			encoding = s_encoding
		else:
			raise EncodingError(s_encoding)
	ascii_sentence = sentence.decode(encoding)

	if not handler:
		segments = ['[not a valid segment handler.]']
	else:
		segments = handler(ascii_sentence)

	return segments
	# except EncodingError as e:
	# 	print e
	# except Exception as e:
	# 	print e 


def seg(inputcontent,handlers,is_file=False):
	handlers=list(handlers)
	if is_file:
		with open(inputcontent) as f:
			sentence = f.read()
			print chardet.detect(sentence)
	else:
		sentence=inputcontent
	segments = [segit(sentence,HANDLERS.get(handler,None)) for handler in handlers]

	if is_file:
		for h,segment in zip(handlers,segments):
			filename = '%s.%s.seg'%(inputcontent,h)
			with open(filename,'wb') as f:
				content = '/'.join(segment)
				content=content.encode('utf-8')
				f.write(content)
	else:
		for h,segment in zip(hanlders,segments):
			print '[%s]: %s'%(h,'/'.join(segment))

	return segments



if __name__ == '__main__':
	s='从你走进来的那一刹那我就知道你是一个错误'
	seg('./test/foo.txt', 'vfm',True)




	