#!/usr/bin/python
import os
import subprocess
import time

def runCmds(cmds):
    p = subprocess.Popen(
            '/bin/bash',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    for c in cmds:
        yield c
        p.stdin.write(c + os.linesep)
    p.stdin.close()
    for line in iter(p.stdout.readline, ""):
        yield line
    p.stdout.close()
    rc = p.wait()
    if rc:
        raise subprocess.CalledProcessError(rc, cmds)

def GenerateCheckoutCmds(external):
    return [
            "mkdir -p externals/%s" % external['name'],
            "cd externals/%s" % external['name'],
            "git init",
            "git remote add origin %s" % external['url'],
            "git fetch --depth=1 origin %s" % external['commit'],
            "git reset --hard FETCH_HEAD"
            ]

if __name__ == "__main__":
    externals = [
            {
                'name' : 'googletest',
                'url' : 'https://github.com/google/googletest.git',
                'commit' : 'release-1.8.0',
                },
            {
                'name' : 'logger',
                'url' : 'git@github.com:grifcj/cmake-logger',
                'commit' : 'master'
                },
            ]

    for e in externals:
        path = 'externals/%s' % e['name']
        if not os.path.exists(path):
            print("Checkout external %s" % e['name'])
            for line in runCmds(GenerateCheckoutCmds(e)):
                print('   ' + line)

