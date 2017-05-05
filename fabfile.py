from fabric.api import local

def test():
    local("./manage.py")

   # local("cd /home/devops/fabscript/fabric-test && touch file1 file2 file3" )
def commit():
    local("cd /home/devops/fabscript/fabric-test && git add . && git commit -m 'adding script'" )
def push():
    local("cd /home/devops/fabscript/fabric-test && git push origin master ")
def pull():
    local(" git pull")

def depoly():
    print "Executing manage script."
    print "----------------------------"
    test()
    print "Commiting got code locally."
    print "------------------------------"
    commit()
    print "Pushing local git repository to Github."
    print "---------------------------------------------"
    push()
    print "Pull from repository"
    pull()
