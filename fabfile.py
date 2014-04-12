from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm


env.use_ssh_config = False
env.hosts = ["dev.magrabbit.com",]
env.user = "huymac"
env.password = ""
env.parallel = True
env.roledefs = {
    'db': ['db1', 'db2'],
    'web': ['web1', 'web2', 'web3'],
}

def hostname_check():
    run("hostname")

def command(cmd):
    run(cmd)

def sudo_command(cmd):
    sudo(cmd)

def install(package):
    sudo("apt-get -y install %s" % package)

def local_cmd():
    local("echo fabtest >> test.log")

@parallel
def pcmd(cmd):
    run(cmd)

@roles('db')
def migrate():
    # Database stuff here.
    pass

@roles('web')
def update():
    # Code updates here.
    pass

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

def deploy2():
    execute(migrate)
    execute(update)

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

@parallel
def runs_in_parallel():
    pass

def runs_serially():
    pass

@parallel(pool_size=5)
def heavy_task():
    # lots of heavy local lifting or lots of IO here
    print "TEST"

    
    