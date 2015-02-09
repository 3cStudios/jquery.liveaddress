"""
This script is used by SmartyStreets when deploying a new version of the jquery.liveaddress plugin.
"""


import os
import subprocess


def main():
    if "branch" not in os.environ:
        os.environ['branch'] = raw_input("Enter the major.minor version number: ")
    branch = os.environ['branch']
    print 'Current branch: \'{0}\''.format(branch)
    tags = call('git tag').split('\n')
    tags = [t for t in tags if t.startswith(branch)]
    next_revision = 0 if not tags else max(int(x.split('.')[-1]) for x in tags) + 1
    print 'Tagging repository at: \'{0}.{1}\''.format(branch, next_revision)
    call('git tag -a {0}.{1} -m ""'.format(branch, next_revision))


def call(command):
    print command
    output = subprocess.check_output(command.split())
    print output
    return output


SAMPLE_TAG_OUTPUT = """
1.6.9
1.7.0
1.7.1
1.7.10
1.7.11
1.7.12
1.7.13
1.7.14
1.7.15
1.7.16
1.7.17
1.7.18
1.7.19
1.7.2
1.7.20
1.7.3
1.7.4
1.7.5
1.7.6
1.7.7
1.7.8
1.7.9
"""


if __name__ == '__main__':
    main()
