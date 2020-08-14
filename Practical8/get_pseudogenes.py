# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:49:14 2020

@author: skysblues
"""
xlen = 0
line2 = ''
import re
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
fout = open('pseudogenes.fa','w')
for line in xfile:
    if line.startswith ('>'):
        line0 = str(line)
        line1 = re.findall('gene:[^ ]+? ', line0)
        line1_1 = str (line1) + '\n'
        fout.write (line1_1)
        line2 = 'genelengh:'+ str(len(line)) + '\n'
        fout.write (line2)
    else:
        xlen = xlen + len(line)
fout.close()