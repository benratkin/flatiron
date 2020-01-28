import os
import subprocess

base = '/home/ben/flatiron'
for directory in os.listdir(base):
    if directory.startswith('section_'):
        print(f'Removing from {directory}')
        for subdir in os.listdir(f'{base}/{directory}'):
            print(f'Removing from {subdir}')
            try:
                subprocess.run(f'rm -rf /home/ben/flatiron/{directory}/{subdir}/.git')
            except FileNotFoundError as e:
                print(e)
