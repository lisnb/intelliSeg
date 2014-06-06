#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 17:10:51
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 18:55:16
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
from __future__ import division 
import math
import sys

sys.path .append('..')

from dicts import SogouLabTrie
from dicts import SogouLabFreq


trie = SogouLabTrie.SougouLabDicTrie
word_freq = SogouLabFreq.SogouLabDicFreq
smooth = SogouLabFreq.freq_smooth



def initialize(dictpath='../dicts/SogouLabDic.word.freq.dic'):
	global trie,word_freq,smooth
	with open(dictpath,'rb') as f:
		words = f.read()
	words=words.decode('utf-8')
	tmp=[x.split('\t') for x in  words.split('\n')]
	freq=[float(x[1]) for x in tmp]
	freq_sum=sum(freq)
	smooth=math.log(min(freq)/freq_sum)
	print smooth
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






	