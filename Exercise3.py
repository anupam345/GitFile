#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import os


import git
import re
# from git import RemoteProgress

from git import Repo
import matplotlib.pyplot as plt


local_link = "~/repo/spring-amqp"

repo = Repo(local_link)
fixing_commit = "3b605cdd"
repo.git.checkout(fixing_commit)

show_data = repo.git.show("--shortstat", fixing_commit).splitlines()

commit = repo.commit(fixing_commit)
s = commit.stats


files = s.files
directoryList = []
fileNames = []
for file in files.keys():
    fileNames.append(file)
    print(""+"File Name: "+'[0m'+file)
    print(''+"Insertions: "+'\'+str(files[file]['insertions']))
    print(''+"Deletions: "+''+str(files[file]['deletions']))
    print(''+"Total: "+'\x1b[0m'+str(files[file]['lines']))



# In[82]:


diff_data = repo.git.diff("-U0",fixing_commit + "^", fixing_commit).splitlines()
# print(diff_data)
fileName = ""
for line in diff_data:
#   print(line)
    if(line[0:10] == 'diff --git'):
        fileName = line[13:line.find(' b')]
        print(line[12:])
    if(line[0:3] == '@@ '):
        print(line)
        start = ' +'
        parentScopeStart = ' @@ '
        end = ' @@'
        s = line
        ps = (s[s.find(parentScopeStart)+len(parentScopeStart):])
        aL = (s[s.find(start)+len(start):s.rfind(end)]).split(',')
        blame_data = repo.git.blame(lines, fixing_commit, "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        uq, c = np.unique(commits, return_counts=True)
       
        mf = max(d, key=d.get)
        print('\x1b[1;31m'+"Most frequent commit : "+'\x1b[0m'+mostFrequent)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        


# 

# In[83]:



        l = "-L"+affectedLines[0]+",+"+affectedLines[1]

       bd = repo.git.blame(lines, fixing_commit, "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        u, c = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"No parameter : "+'\x1b[0m'+mostFrequent)
        ##################################
        bd = repo.git.blame(lines, fixing_commit, "-w", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        u, c = np.unique(commits, return_counts=True)
     
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"With -w : "+'\x1b[0m'+mostFrequent)
        ##################################
        blame_data = repo.git.blame(lines, fixing_commit, "-wM", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"With -wM : "+'\x1b[0m'+mf)
        ##################################
        blame_data = repo.git.blame(lines, fixing_commit, "-wC", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))
        mf = max(d, key=d.get)
        print('\x1b[1;31m'+"With -wC : "+'\x1b[0m'+mf)
        bd = repo.git.blame(lines, fixing_commit, "-wCC", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"With -wCC : "+'\x1b[0m'+mostFrequent)
        ##################################
        bd = repo.git.blame(lines, fixing_commit, "-wCCC", "--", fileName).splitlines()
        print('\x1b[1;31m'+"With -wCCC : "+'\x1b[0m'+mostFrequent)
        





