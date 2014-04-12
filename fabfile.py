from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['localhost']
env.use_ssh_config = False

def test():
    with settings(warn_only=True):
        result = local('echo $PATH', capture=True)
        
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def deploy():
    code_dir = '/Users/macanhhuy/TestProject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            print "ok"
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")

def commit():
    local("git add . && git commit -m 'Test'")

def push():
    local("git push")

def info():
	print("Executing on %(host)s as %(user)s" % env)

def task1():
    run('ls')

def task2():
    run('whoami')

def prepare_deploy():
    commit()
    push()
    
    