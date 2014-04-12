from fabric.api import local

def prepare_deploy():
    local("git add . && git commit -m 'Test'")
    local("git push")