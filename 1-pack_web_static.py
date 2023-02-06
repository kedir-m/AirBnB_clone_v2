#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static
folder using function do_pack()"""

from fabric.operations import local
from datetime import datetime


def do_pack():
    """Function that compresses content
    and generates the tgz archive file"""
    date_time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date_time)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(path))
    if result.failed:
        return None
    return path
