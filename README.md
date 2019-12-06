# listgits
Python command line program for listing all git repositories under a folder root

Usage:

```
python listgits
```

Options :

* --h: Show the possible options
* --s: Short form, not showing non-git folders
* --l: Show only local repos, which do not have any remotes (includes --s)
* --r: Show only repos that have remotes (includes --s)
* --f somestring: Find a local repo by adding a part of the remote url. All matching local repos will be displayed
* --g commands: Git options, passes the string of options in to git, and runs git with those instead of the default remote command


Read this [blogpost](http://hermit.no/how-to-list-git-repositores-under-a-common-folder-root/) for more information on how to use it.


