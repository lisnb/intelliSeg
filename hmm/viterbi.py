#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 14:50:38
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 19:14:02
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
from prob_emit import emit,smooth
from prob_trans import trans 
from prob_start import start 
from prob_condition import condition,hmm_states

smooth_min =-3.14e100

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] +emit_p[y].get(obs[0],smooth_min)
        path[y] = [y]
 
    # Run Viterbi for t > 0
    for t in range(1,len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max([(V[t-1][y0] + trans_p[y0][y] +emit_p[y].get(obs[t],smooth_min), y0) for y0 in condition[y]])
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
 
    # print_dptable(V)
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in ('E','S')])
    return (prob, path[state]) 


def seg(sentence):
	segments=[]
	prob,path = viterbi(sentence, hmm_states, start, trans, emit)
	s,e=0,0
	print path
	while e<len(sentence):
		if path[e] == 'B':
			s=e
			e+=1
		elif path[e]=='E':
			segments.append(sentence[s:e+1])
			e+=1
			s=e
		elif path[e]=='S':
			segments.append(sentence[e])
			e+=1
			s=e
		else:
			e+=1
	if e>s:
		segments.append(sentence[s:])
	# print ('/'.join(segments)).encode('cp936')
	return segments


if __name__ == '__main__':
	# print min([min(emit[x].values()) for x in emit ])
	s='我很喜欢周杰伦这个歌手'

	ss=s.decode('utf-8')
	seg(ss)







	