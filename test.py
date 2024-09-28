import subprocess

commitmessage = input("Enter commit message : ")
branchname = input("Enter branch name (default: main) : ",)
if branchname == "":
    branchname = "main"

if branchname != "main":
    if subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode().strip() == branchname:
        subprocess.run(['git', 'checkout', '-b', branchname])
        print(f"Switched to a new branch '{branchname}'")

addcmd = ['git', 'add', '.']
commitcmd = ['git', 'commit', '-m', commitmessage]
pushcmd = ['git', 'push', 'origin', branchname]

commands = [addcmd, commitcmd, pushcmd]

def executecommands(commands):
    for cmd in commands:
        subprocess.run(cmd)

executecommands(commands)