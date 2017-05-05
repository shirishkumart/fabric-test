from fabric.api import local

def test():
    local("cd /home/devops/fabscript/fabric-test && touch file1 file2 file3" )
    local("cd /home/devops/fabscript/fabric-test && git add . && git commit -m 'test 123 '" )
    local("cd /home/devops/fabscript/fabric-test && git push origin master ")
