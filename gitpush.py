import subprocess

commitmessage = input("Enter commit message : ")
branchname = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE)
branchname = branchname.stdout.decode().strip()

addcmd = ['git', 'add', '.']
commitcmd = ['git', 'commit', '-m', commitmessage]
pushcmd = ['git', 'push', 'origin', branchname]

commands = [addcmd, commitcmd, pushcmd]

def executecommands(commands):
    for cmd in commands:
        subprocess.run(cmd)

executecommands(commands)