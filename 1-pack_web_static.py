#!/usr/bin/python3
""" script for tar """


from fabric.api import local
from datetime import datetime


def do_pack():
    """generate tgz"""
    archive = datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p versions")
    temp = "versions/web_static_{}.tgz".format(archive)
    placeholder = local("sudo tar -cvzf {} web_static".format(temp))

    if placeholder.succeeded:
        return archive
    else:
        return none


if __name__ == "__main__":
    do_pack()
