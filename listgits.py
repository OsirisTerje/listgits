import subprocess
import os
import argparse


def spaces(n):
    return ' '*(n-1)*3

def listgits(cwd,level,s,local,remotes):
    level += 1
    spc = spaces(level)
    dirs = list(filter(lambda d:os.path.isdir(d) and not os.path.isdir('./.git'),os.listdir()))
    if len(dirs)==0:
        return
    root = os.getcwd()
    for dir in dirs:
        os.chdir(dir)
        if os.path.isdir('./.git'):
            proc = subprocess.Popen(['git','remote','-v'],stdout=subprocess.PIPE)
            stdout = proc.communicate()[0].decode("utf-8").split('\n')
            if len(stdout[0])==0:
                if not remotes:
                    print (spc+'Folder '+root+'/'+dir+'  has local repo only')
            else:
                if not local:    
                    print (spc+'Folder '+root+'/'+dir+'  ') 
                    for line in stdout:
                        print (spc+line)
        else:
            if not s:
                print('Folder only: '+ spc+root)
            listgits(root,level,s,local,remotes)
        os.chdir(root)

parser = argparse.ArgumentParser()
parser.add_argument("--s",action="store_true",help="Output results in short form, ignoring non-git folders")
parser.add_argument("--l",action="store_true",help="Show only local repos")
parser.add_argument("--r",action="store_true",help="Show only repos with remotes")

args = parser.parse_args()

short = args.s
local = args.l
remotes = args.r
if not short and (local or remotes):
    short=True


listgits('./',0,short,local,remotes)

