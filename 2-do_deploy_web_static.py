#!/usr/bin/python3
"""Distributes an archive to my web servers"""

import os
from fabric.api import run, put, env
from datetime import datetime

# env.use_ssh_config = True
# env.ssh_config_path = '~/.ssh/school'
env.hosts = ['44.200.74.219', '3.239.76.41']
# Set the username
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to my web servers
    Args:
        archive_path (str): The path to the archived static files.
    Return: True if ok, False if else
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        # uploading file on remote server
        put(archive_path, "/tmp/")
        # creating folder on remote
        run("sudo mkdir -p {}".format(folder_path))
        # uncompress file within /temp to the folder
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        # remove compressed file in /tmp
        run("sudo rm -rf /tmp/{}".format(file_name))
        # Move all from web_static to new folder
        run("sudo mv {}web_static/* {}".format(folder_path, folder_path))
        # Delete web_static folder
        run("sudo rm -rf {}web_static".format(folder_path))
        # Delete the symbolic link /data/web_static/current
        run("sudo rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('You done it bro, deployed successfully !!!')
        success = True
    except Exception:
        success = False
    return success
