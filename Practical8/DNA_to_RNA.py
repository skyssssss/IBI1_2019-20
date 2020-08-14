# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:19:04 2020

@author: skysblues
"""
seq2 = ('')
seq = ('ATGCGACTACGATCGAGGGCCAT')
for i in range(len(seq)):
    if seq[i] == 'A':
        seq2 = seq2 + 'A'
    if seq[i] == 'C':
        seq2 = seq2 + 'C'
    if seq[i] == 'T':
        seq2 = seq2 + 'U'
    if seq[i] == 'G':
        seq2 = seq2 + 'G'
    
print (seq2)
