#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-07 15:30:54
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-07 17:26:16
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

import sys
sys.path.append('..')
from hmm import viterbi
from configs import config
import maxprob
import fmm

def seg(sentence):
	segments = viterbi.seg(sentence)
	# print ('/-'.join(segments)).encode('cp936')
	trie = config.trie
	word_freq = config.word_freq
	for segment in segments:
		if len(segment) < 3:
			continue
		p=trie
		s=0
		while s<len(segment):
			if segment[s] not in p:
				p[segment[s]]={}
				word_freq[segment] = -0.1
			p=p[segment[s]]
			s+=1
		p['']=''
		


	return maxprob.seg(sentence)




if __name__ == '__main__':
	s=u'我很喜欢左小祖咒这个歌手'
	print ('/+'.join(maxprob.seg(s))).encode('cp936')
	print ('/%'.join(fmm.seg(s))).encode('cp936')
	print ('/*'.join(seg(s))).encode('cp936')







	