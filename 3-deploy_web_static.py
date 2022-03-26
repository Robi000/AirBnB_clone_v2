#!/usr/bin/python3
from fabric.api import *
"""this will pack webstatic ready for deploy 
    """
packing = __import__('1-pack_web_static').do_pack
to_server = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['ubuntu@35.229.89.215', 'ubuntu@3.235.60.220']

fcheck = 0


def checker():
    global fcheck
    fcheck += 1
    print("check no: {}".format(fcheck))


def deploy():
    path = packing()
    checker()  # check no: 1  must be printed
    if path is not False:
        checker()  # check no: 2
        if not to_server(path):
            print("------ return flase here ---------")
            return False
        print("------ return true here ---------")
        return True
