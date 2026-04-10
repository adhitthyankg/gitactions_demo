import subprocess

cmd = input("Enter command: ")
subprocess.call(cmd, shell=True)
