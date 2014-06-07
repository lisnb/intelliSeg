#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 19:16:07
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-07 15:47:36
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
from __future__ import division 
import sys
sys.path.append('..')
from configs import config


def dag_(sentence):
	trie = config.trie
	s,e=0,0
	token_index={}
	c=trie

	while e<len(sentence):
		if sentence[e] in c:
			c=c[sentence[e]]
			e+=1
		else:
			if e not in token_index:
				token_index[e]=[]
			token_index[e].append(s)
			s+=1
			e=s
			c=trie
	for i in range(len(sentence)):
		if i not in token_index:
			token_index[i]=[i]
	print token_index
	return token_index

def dag(sentence):
	trie = config.trie

	s,e=0,0
	token_index={}
	current_tree=trie
	
	while  e < len(sentence) :
		current_char=sentence[e]
		if current_char in current_tree:
			current_tree=current_tree[current_char]
			if '' in current_tree:
				if e not in token_index:
					token_index[e]=[]
				token_index[e].append(s)
			e+=1
		else:
			s+=1
			e=s
			current_tree=trie
	for i in range(len(sentence)):
		if i not in token_index:
			token_index[i]=[i]
	# print token_index
	return token_index

def max_line(sentence,token_index):
	word_freq = config.word_freq
	smooth = config.smooth
	lines={}
	i=len(sentence)-1
	lines[i+1]=(0.0,i+1)
	while i>=0:
		cans=[(word_freq.get(sentence[x:i+1],smooth)/(3*(i+1-x) if i+1 != x else 0.5)+lines[i+1][0],x) for x in token_index[i]]
		m=max(cans)
		lines[i]=m
		i-=1
	lines.pop(len(sentence))
	return lines

def seg_(sentence):
	token_index=dag_(sentence)
	# print token_index
	lines=max_line(sentence, token_index)
	# print lines
	segments=[]
	s,e=0,0
	i=len(sentence)-1
	while i>=0:
		segments.append(sentence[lines[i][1]:i+1])
		i=lines[i][1]-1
	segments.reverse()

	return segments

def seg(sentence):
	token_index=dag(sentence)
	# print token_index
	lines=max_line(sentence, token_index)
	# print lines
	segments=[]
	s,e=0,0
	i=len(sentence)-1
	while i>=0:
		segments.append(sentence[lines[i][1]:i+1])
		i=lines[i][1]-1
	segments.reverse()

	return segments



if __name__ == '__main__':
	s='汉语自动分词基本算法'
	ss=s.decode('utf-8')

	print ('/'.join(seg(ss))).encode('cp936')
	# print ('/'.join(seg_(ss))).encode('cp936')






	