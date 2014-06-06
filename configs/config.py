#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 17:10:51
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 21:33:48
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
from __future__ import division 
import math
import sys
import re
import string 
sys.path .append('..')
from dicts import SogouLabTrie
from dicts import SogouLabFreq



DICT_PATH = '../dicts/SogouLabDic.word.freq.dic'

USE_CHARDETECT = True



trie = SogouLabTrie.SougouLabDicTrie
word_freq = SogouLabFreq.SogouLabDicFreq
smooth = SogouLabFreq.freq_smooth


re_chinese= re.compile(ur"([\u4E00-\u9FA5]+)")
re_punc = re.compile(r'%s'%u'[%s\s？《》【】{}（）~“”‘’，。、]+'%string.punctuation)
re_space = re.compile(ur'[\s]+')


def initialize(dictpath=DICT_PATH):
	global trie,word_freq,smooth
	with open(dictpath,'rb') as f:
		words = f.read()
	words=words.decode('utf-8')
	tmp=[x.split('\t') for x in  words.split('\n')]
	freq=[float(x[1]) for x in tmp]
	freq_sum=sum(freq)
	smooth=math.log(min(freq)/freq_sum)
	# print smooth
	words=[x[0] for x in tmp]
	for i in range(len(words)):
		word=words[i]
		word_freq[word]=math.log(freq[i]/freq_sum)
		p=trie
		for c in word:
			if c not in p:
				p[c]={}
			p=p[c]
		p['']=''





if __name__ == '__main__':
	initialize()






	