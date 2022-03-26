#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tabnanny import check
from fabric.api import *
import os

# fcheck = 0

# def check():
#     global fcheck
#     fcheck = fcheck + 1
#     print("checker no:", fcheck)
"""this will pack webstatic ready for deploy 
    """
env.hosts = ['35.229.89.215', '3.235.60.220']
check = ''


def do_deploy(archive_path=None):
    """here we will deploy all conteents of archived path 

    Args:
        archive_path (string): _description_
        file_name (string): _description_
        release_name (string): _description_
    """

    if not os.path.exists(archive_path):

        # check()  # 1fcheck

        return False
    release_name = archive_path[-29:-4]

    # -> /mnt/c/repositeris/AirBnB_clone_v2/versions/web_static_20220326102222.tgz == web_static_20220326102222

    file_name = archive_path[-29:]

    # -> /mnt/c/repositeris/AirBnB_clone_v2/versions/web_static_20220326102222.tgz == web_static_20220326102222.tgz

    tmp_file_handler(archive_path, file_name, release_name)
    if check == 'scusses':
        # print('---------return true------------')
        return True
    else:
        # print('----------- not scuss-------')
        return False


def tmp_file_handler(archive_path, file_name, release_name):
    """here we will make sure put and remove temp files

    Args:
        archive_path (string): _description_
        file_name (string): _description_
        release_name (string): _description_
    """

    global check
    put(archive_path, '/tmp')
    x = 0
    if not server_work(file_name, release_name):
        return
    run('sudo rm -f /tmp/{}'.format(file_name))
    check = 'scusses'
    if x == 1:
        return True
    else:
        return False


def server_work(file_name, release_name):
    """here all server !done 

    Args:
        file_name (string): _description_
        release_name (string): _description_

    Returns:
        boolian: true if succided and false if not 
    """

    # tmp_file_location

    tfl = '/tmp/' + file_name

    # destination_forlder

    df = '/data/web_static/releases/{}'.format(release_name)

    # to be soft linkd

    tbsl = \
        '/data/web_static/releases/{}/web_static'.format(release_name)
    try:
        run('sudo mkdir -p /data/web_static/releases/{}'.format(release_name))
        run('sudo tar zxvf {} -C {}'.format(tfl, df))
        run('sudo mkdir -p /data/web_static')
        run('sudo rm -f /data/web_static/current')
        run('sudo ln -sf {} /data/web_static/current'.format(tbsl))
        return True
    except:
        return False
