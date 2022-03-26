#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from fabric.api import *


def do_pack():
    """this will pack file to tgz arcive

    Returns:
        file path: if it success
    """

    now = datetime.now()  # current date and time

    # web_static_<year><month><day><hour><minute><second>.tgz

    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')
    hour = now.strftime('%H')
    minn = now.strftime('%M')
    sec = now.strftime('%S')
    time = now.strftime('%H:%M:%S')
    date_time = now.strftime('%m/%d/%Y, %H:%M:%S')
    filename = 'web_static_' + year + month + day + hour + minn + sec \
        + '.tgz'
    local('mkdir -p versions')
    print('Packing web_static to versions/{}'.format(filename))
    local('tar -cvzf versions/{} web_static'.format(filename))
    try:
        dictt = os.getcwd()
        filename = 'versions/{}'.format(filename)
        full_path = dictt + '/' + filename
        print(full_path)
        data_byte = os.path.getsize(full_path)
        print('web_static packed: {} -> {}Bytes'.format(filename,
                                                        data_byte))
        return full_path
    except:
        return None
