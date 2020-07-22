"""
--- developed by Onur Sumakoglu on 05.07.2020 ---
"""
#!/usr/bin/env python

import os
import sys
import glob
from pathlib import Path


from hashlib import md5


def save(version_name):

    files = list(Path('.').rglob('*.txt'))


    version_file = open(f'backup/versions/{version_name}', 'w')

    for file_name in files:

        content = open(file_name).read()

        md5_hash = md5(content.encode('utf-8')).hexdigest()

        open(f'backup/contents/{md5_hash}', 'w').write(content)

        version_file.write(
            md5_hash + ',' + str(file_name) + '\n')


def backup(version_name):

    version_content = open(f'backup/versions/{version_name}')

    for line in version_content:
        _hash, file_name= line.strip().split(',')

        content = open(f'backup/contents/{_hash}').read()

        if "\\" in file_name:

            folder = file_name.rsplit("\\", 1)[0]

            if not os.path.isdir(folder):

                os.mkdir(folder)

        open(file_name, 'w').write(content)


def modified_status(version_name):

    version = open(f'backup/versions/{version_name}')

    for line in version:
        _hash, filePath = line.strip().split(',')

        if os.path.isfile(filePath):

            content = open(filePath).read()

            md5_hash = md5(content.encode('utf-8')).hexdigest()

            if _hash != md5_hash:
                print(f"{filePath} is modified.")

        else:
            print(f"{filePath} is deleted")


def new_status(version_name):

    files = list(Path('.').rglob('*.txt'))
    version = open(f"backup/versions/{version_name}").read()

    for filePath in files:

        if str(filePath) not in version:
            print(f"New file added. {filePath}")



if sys.argv[1] == 'start':
    os.mkdir('backup')
    os.mkdir('backup/contents')
    os.mkdir('backup/versions')


elif sys.argv[1] == 'save':
    if len(sys.argv) != 3:
        print('The save command requires a version name.')
    else:
        save(version_name = sys.argv[2])

elif sys.argv[1] == 'versions':
    versiyon_names = glob.glob("backup/versions/*")
    for version_name in version_names:
        print(version_name.split('/')[-1])

elif sys.argv[1] == 'backup':
    if len(sys.argv) != 3:
        print('The backup command requires a version name.')
    else:
        backup(version_name = sys.argv[2])

elif sys.argv[1] == 'status':
    if len(sys.argv) != 3:
        print('The status command requires a version name.')
    else:
        version_name = sys.argv[2]

        modified_status(version_name)

        new_status(version_name)

"""
--- developed by Onur Sumakoglu on 05.07.2020 ---
"""
