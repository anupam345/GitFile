

repo = Repo(local_link)
fixing_commit = "aff4d0aefcdb99726fd739abf3b9bb96df97b0f"
repo.git.checkout(fixing_commit)

show_data = repo.git.show("--shortstat", fixing_commit).splitlines()

commit = repo.commit(fixing_commit)

fix_date = show_data[3][8:32]

files = s.files
directoryList = []
fileNames = []

fileName = ""
for line in diff_data:

    if(line[0:10] == 'diff --git'):
        fileName = line[13:line.find(' b')]
        print(line[12:])
    if(line[0:3] == '@@ '):
        print(line)
        start = ' +'
        parentScopeStart = ' @@ '
        end = ' @@'
        s = line
        ps = (s[s.find(pss)+len(oss):])
        af = (s[s.find(start)+len(start):s.rfind(end)]).split(',')

        print('\x1b[1;31m'+"FN "+'\x1b[0m'+fileName)
        if("Project" == str(parentScope[:parentScope.find(': ')])):
            print('\x1b[1;31m'+""+'\x1b[0m')
        else:
            print('\x1b[1;31m'+"ES "+'\x1b[0m'+str(ps[:ps.find(': ')]))
        print('\x1b['+" "+'\x1b[0m'+"Line number " + affectedLines[0] + " to "+ str((int(affectedLines[0]))))
        
        
        lines = "-L"+af[0]

        blame_data = repo.git.blame(lines, fixing_commit, "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))

        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"Mo+'\x1b[0m'+mf)
        print("==============================================================")
        print()




        lines = "-L"+affectedLines[0]

        blame_data = repo.git.blame(lines, fixing_commit, "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"No para : "+'\x1b[0m'+mostFrequent)

        blame_data = repo.git.blame(lines, fixing_commit, "-w", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"-w : "+'\x1b[0m'+mostFrequent)
       
        blame_data = repo.git.blame(lines, fixing_commit, "-wM", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = dict(zip(unique, counts))
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+" -wM : "+'\x1b[0m'+mostFrequent)
        
        blame_data = repo.git.blame(lines, fixing_commit, "-wC", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = zip(unique, counts)
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+" -wC : "+'\x1b[0m'+mostFrequent)
       
        blame_data = repo.git.blame(lines, fixing_commit, "-wCC", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = (zip(unique, counts)
        mostFrequent = max(d, key=d.get)
        
        blame_data = repo.git.blame(lines, fixing_commit, "-wCCC", "--", fileName).splitlines()
        commits = []
        for l in blame_data:
            commits.append(l[0:8])
        unique, counts = np.unique(commits, return_counts=True)
        d = zip(unique, counts)
        mostFrequent = max(d, key=d.get)
        print('\x1b[1;31m'+"-wCCC : "+'\x1b[0m'+mostFrequent)
        



show_data = repo.git.show("--shortstat", mostFrequent).splitlines()
print('\x1b[1;31m'+"Commit Title:"+'\x1b[0m'+show_data[4])
print('\x1b[1;31m'+":"+'\x1b[0m'+show_data[6])



mostFrequent = max(d, key=d.get)
commit = repo.commit(mostFrequent)
s = commit.stats
for file in s.files:
    print(file)
print('\x1b[1;31m'+"AF:"+'\x1b[0m'+ str(s.total["files"]))


files = s.files
directoryList = []
for file in files.keys():
    directory = file[0:file.rfind('/')]

    if directory not in directoryList:
        directoryList.append(directory)

    



diff_data = repo.git.diff(mostFrequent + "^", mostFrequent).splitlines()
count = 0
for line in diff_data:
    if(not line[0:3] == '---'):
        if(line[0:1] == '-'):
            count=count+1
print('\x1b[1;31m'+"Deletions including blank lines:"+'\x1b[0m'+str(count))




diff_data = repo.git.diff(mostFrequent + "^", mostFrequent).splitlines()
count = 0
for line in diff_data:
    if(not line[0:3] == '+'):
        if(line[0:1] == '+'):
            count=count+1




diff_data = repo.git.diff("-w",mostFrequent + "^", mostFrequent).splitlines()
count = 0
comment_started = False
for line in diff_data:
    if(not line[0:3] == '---'):
        if(line.find('/*') != -1):
            comment_started = True
            continue
        elif(line.find('*/') != -1):
            comment_started = False
            continue
        if(comment_started==False):
            if(line[0:1] == '-' and not re.search(r'\s', line) is None):
                if(line.find('//') == -1):
)
                    count=count+1


diff_data = repo.git.diff("-w",mostFrequent + "^", mostFrequent).splitlines()
count = 0
comment_started = False
for line in diff_data:
    if(not line[0:3] == '+++'):
        if(line.find('/*') != -1):
            comment_started = True
            continue
        elif(line.find('*/') != -1):
            comment_started = False
            continue
)
        if(comment_started==False):
            if(line[0:1] == '+' and not re.search(r'\s', line) is None):
                if(line.find('//') == -1):
)
                    count=count+1

                
print('\x1b[1;31m'+"Insertions excluding blank lines and comments:"+'\x1b[0m'+str(count))

:


from datetime import datetime
from datetime import date)
i=0
for file in files: 
    i=i+1
    if(i==6):
        break
    print('\x1b[1;31m'+"File Name: "+'\x1b[0m'+file)
    log_data = repo.git.log(mostFrequent,file).splitlines()
    commit_number = 0
    date1 = datetime.now()
    date2 = datetime.now()
    for line in log_data:
        if(line[0:8] == "Date:   "):
            commit_number=commit_number+1
            if(commit_number ==1):
                date1 = datetime.strptime(line[8:32], '%a %b %d %H:%M:%S %Y')
                print('\x1b[1;31m'+"VCC Commit Date\Time: "+'\x1b[0m'+str(date1))
                date2 = datetime.strptime(line[8:32], '%a %b %d %H:%M:%S %Y')
                print('\x1b[1;31m'+"Fix Commit Date\Time: "+'\x1b[0m'+str(date2))
                break

    print('\x1b[1;31m'+"Time Difference: "+'\x1b[0m'+str(date2-date1))
    print("===")
:


for file in files:   
    print('\x1b[1;31m'+"File Name: "+'\x1b[0m'+file)
    log_data = repo.git.log(mostFrequent,"--pretty=\"format:%H%M%S\"", "--",file).splitlines()
    print('\x1b[1;31m'+"Number of Revisions including renaming: "+'\x1b[0m'+str(len(log_data)))
    print("====")



for file in files:   
    print('\x1b[1;31m'+"File Name: "+'\x1b[0m'+file)
    print('\x1b[1;31m'+"Contributors of the file: "+'\x1b[0m')
    log_data = repo.git.log(mostFrequent,"--pretty=format:%an", "--follow", "--",file).splitlines()

    x = np.array(log_data) 
    uniqueNames = np.unique(x)
    for name in uniqueNames:
        print(name) 
    print()

commit_authors = repo.git.shortlog("-sne", "--all").splitlines()

author_commits = []

for commit_author in commit_authors:
    commit, author = commit_author.split("\t")
    author_commits.append([int(commit), author])
    print('\x1b[1;34m'+"Author: \x1b[1;31m'"+author)
    print('\x1b[1;34m'+"Number of commits: \x1b[1;31m'"+commit)

devs_above_450 = 0
devs_below_450 = 0
for item in author_commits:
    if(item[0]>=450):
        devs_above_450 = devs_above_450+1
    else:
        devs_below_450 = devs_below_450+1
exp_level="new"
if(devs_above_450>devs_below_450):
    exp_level = "experienced"
    
print('\x1b[1;34m'+"According to the number of commits of the developers, we can see the majority of the developers are "+exp_level+"."+'\x1b[0m')
print('\x1b[1;34m'+"The number of developers with at least 450 commits is "+str(devs_above_450)+"."+'\x1b[0m')
print('\x1b[1;34m'+"The number of developers with less than 450 commits is "+str(devs_below_450)+"."+'\x1b[0m')


# # 

# In[ ]:




