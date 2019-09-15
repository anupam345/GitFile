#!/usr/bin/env python
# coding: utf-8

# 
# 

# # Load libraries

# In[1]:


import numpy as np
import pandas as pd
import os
import re
from datetime import datetime
# Specify git executable file for GitPython in Jupyter Notebook (In IDE, it can still work without this line.)
#os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = "C:\Program Files\Git\cmd\git.exe"

import git
from git import RemoteProgress

from git import Repo
import matplotlib.pyplot as plt
import seaborn as sns


class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(self._cur_line)



local_link = "~/Excercise2/hibernate-validator/"
repo = Repo(local_link)
fixing_commit = "fd4eaed7fb930db6a5e4c03742b4b3adcfecc90e"
affected_file = "engine/src/main/java/org/hibernate/validator/internal/cfg/context/CascadableConstraintMappingContextImplBase.java"

 #a git show -s --format=%B fd4eaed7fb930db6a5e4c03742b4b3adcfecc90e

print "1 \n"
show_data = repo.git.show("-s","--format=%B",fixing_commit).splitlines();
for line in show_data:
    print(line)

#b git diff-tree --no-commit-id --name-only -r fd4eaed7fb930db6a5e4c03742b4b3adcfecc90
print "2 \n"
os.system("git diff-tree --no-commit-id --name-only -r fd4eaed7fb930db6a5e4c03742b4b3adcfecc90")

total_files = repo.git.show("--stat",fixing_commit).splitlines()
print("Total Files Affected")
total_files=total_files[10:]
for line in total_files:
    print(line)


#c
print "3 \n"


os.system("git diff --dirstat=files HEAD~1 fd4eaed7fb930db6a5e4c03742b4b3adcfecc90e | sed 's/^[ 0-9.]\+% //g'|wc -l")


#d
print "4 \n"
os.system("git show --numstat --oneline   fd4eaed7fb930db6a5e4c03742b4b3adcfecc90e |tail -n +2|awk '{print $2;}' > output.txt;awk -F '|' ' {sum += $1} END {print sum}' output.txt;rm output.txt")

total_line_del = repo.git.show("--shortstat",fixing_commit).splitlines()
total_line_del.reverse()
total_line_del = total_line_del[0].split(',')
print("Total Number of lines of codes Deleted(including blank spaces):"+total_line_del[2])

#e
print "5 \n"
#zos.system("git show --numstat --oneline   fd4eaed7fb930db6a5e4c03742b4b3adcfecc90e |tail -n +2|awk '{print $1;}' > output.txt;awk -F '|' ' {sum += $1} END {print sum}' output.txt;rm output.txt")
show_del_line = repo.git.show("-U0","--pretty=""",fixing_commit).splitlines()
tot_del = 0
for line in show_del_line:
    if re.search("^\-",line):
        l = line.split(" ")
        if(len(l) > 1):
            if(len(l[0]) == 1):
                if(l[1][:1] != '*' or l[1][:1] != '/'):
                    tot_del +=1

#f
print "6 \n"
show_del_line = repo.git.show("-U0","--pretty=""",fixing_commit).splitlines()
tot_del = 0
for line in show_del_line:
    if re.search("^\-",line):
        l = line.split(" ")
        if(len(l) > 1):
            if(len(l[0]) == 1):
                if(l[1][:1] != '*' or l[1][:1] != '/'):
                    tot_del +=1
                    
                    
                    
print("Total lines Deleted (Excluding comments and blank line)="+str(tot_del))

#g

print "7 \n"

show_add_line = repo.git.show("-U0","--pretty=""",fixing_commit).splitlines()
tot_add = 0
for line in show_add_line:
    if re.search("^\+",line):
        l = line.split(" ")
        if(len(l) > 1):
            if(len(l[0]) == 1):
                if(l[1][:1] != '*' or l[1][:1] != '/'):
                    tot_add +=1
                    
                    
                    
print("Total lines Added (Excluding comments and blank line)="+str(tot_add))


#h
print "8\n"

day_diff = repo.git.log("-2","--format=%cd",fixing_commit,"--",affected_file).splitlines()
#print(day_diff)
d1 = datetime.strptime(day_diff[0],"%a %b %d %X %Y %z")
#print(date)
d2 = datetime.strptime(day_diff[1],"%a %b %d %X %Y %z")
#print(dated)
daydifference=(abs(d1-d2).days)
print("Days between the current fixing commit and the previous commit of each affected file:"+str(daydifference))


#i
print "9 \n"
show_times = repo.git.log("--follow","--format=%cd",fixing_commit,"--",affected_file).splitlines()
print(len(show_times))

#j 
print "10 \n"
show_name = repo.git.log("--follow","--format=%an",fixing_commit,"--",affected_file).splitlines()
deve=set(show_name)
print(deve)

print "11 \n"
#k


deve_commits = repo.git.shortlog("-ns","--all","--no-merges",fixing_commit,"--",affected_file).splitlines()
for line in deve_commits:
    print(line)










