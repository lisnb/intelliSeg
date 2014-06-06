#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-06-06 23:03:54
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-06-06 23:39:35
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
from configs.config import ISWINDOWS
import intelliSeg





if __name__ == '__main__':
	s="""
以下内容将被分词：\n\n“小编总结一下：考前上厕所，考中别抄袭，(don\' cheat in the exam）,考完别对题，报考大学需谨慎，看看留言里那些拼命劝人不要考自己大学的小伙伴就知道了…”
	
同时，位于test目录下的 Mr.Zong.txt 中的内容也将被分词，并生成文件。
	"""

	if ISWINDOWS:
		print s.decode('utf-8').encode('gbk')
	else:
		print s

	intelliSeg.seg(s)
	intelliSeg.seg('./test/Mr.Zong.txt',is_file=True)







	