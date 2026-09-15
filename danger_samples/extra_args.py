import subprocess

subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE, cwd="/tmp")
