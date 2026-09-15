import subprocess

cmd = "ls -la"
subprocess.Popen(shell=True, args=cmd)
