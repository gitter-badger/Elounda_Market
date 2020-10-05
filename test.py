#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import os
import subprocess

folder_to_delete = 'build'
file = 'Discovery.spec'
file_to_delete = f'{folder_to_delete}/{file}'

folder_command = ['rmdir', folder_to_delete]
file_command = ['rm', file_to_delete]
base_dir = ['cd', os.path.abspath(os.getcwd())]

subprocess.run(base_dir)

subprocess.run(file_command)
subprocess.run(folder_command)

