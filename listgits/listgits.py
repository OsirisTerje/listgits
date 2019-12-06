import subprocess
import os
import argparse


def spaces(n):
    return ' '*(n-1)*3

def listgits(cwd,level,short,local,remotes,isSearch,gitoptions,results):
    level += 1
    spc = spaces(level)
    dirs = list(filter(lambda d:os.path.isdir(d) and not os.path.isdir('./.git'),os.listdir()))
    if len(dirs)==0:
        return
    root = os.getcwd()
    i=0
    for dir in dirs:
        os.chdir(dir)
        # print (str(i))
        # i += 1
        if os.path.isdir('./.git'):
            isOptions = len(gitoptions)>0
            git = ['git']
            if isOptions:
                git = git+ gitoptions
            else:
                git = git + ['remote','-v']   
            proc = subprocess.Popen(git,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout = proc.communicate()[0].decode("utf-8").split('\n')
            stderr = proc.communicate()[1].decode("utf-8").split('\n')
            if len(stdout[0])==0:
                if not remotes and not isSearch:
                    print (spc+'Folder '+root+'/'+dir+'  has local repo only')
                    print (' ')
                os.chdir(root)
                continue
            if local and len(stderr)>0 and not short:
                for line in stderr:
                    if len(line)>0:
                        print (line)      
            else:
                if not local or isOptions:  
                    fulldir = root +"/"+dir 
                    if not isSearch: 
                        print (spc+'Folder '+fulldir+'  ') 
                        for line in stdout:
                            if len(line)>0:
                                print (spc+line)
                        if isOptions:
                            print('----------')
                        else:
                            print ('  ')
                    results.append((fulldir,stdout))
        else:
            if not short and not isSearch:
                print('Folder only: '+ spc+root+'/'+dir)
                print (' ')
            listgits(root,level,short,local,remotes,isSearch,gitoptions,results)
        os.chdir(root)
         

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s",action="store_true",help="Output results in short form, ignoring non-git folders")
    parser.add_argument("--l",action="store_true",help="Show only local repos")
    parser.add_argument("--r",action="store_true",help="Show only repos with remotes")
    parser.add_argument("--f",default="",help="Find a local repo by adding a part of the remote url. All matching local repos will be displayed")
    parser.add_argument("--g",default="",help="Git options, passes the string of options in to git, and runs git with those instead of the default remote command")

    args = parser.parse_args()

    short = args.s
    local = args.l
    remotes = args.r
    search = args.f.lower()
    isSearch=len(search)>0
    if not short and (local or remotes):
        short=True
    if isSearch:
        short=True
        remotes=True
    results = []
    gitOptions= [] 
    if len(args.g)>0:
        gitOptions=args.g.split(' ')
        short=True


    # print('Short form: %s  Local: %s Remote: %s Find: %s  GitOptions: %s' % (short,local,remotes,search,gitOptions))    
    listgits('./',0,short,local,remotes,isSearch,gitOptions,results)
    if isSearch:
        matches = [(x,y) for x,y in results if [s for s in y if search in s.lower() ]]
        for match in matches:
            print ('Folder: '+match[0])
            for remote in match[1]:
                if len(remote)>0:
                    print ('Remote : '+remote)
            print ('   ')


if __name__ == "__main__":
      main()

