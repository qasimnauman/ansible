import subprocess

commitmessage = input("Enter commit message: ")
branchname = input("Enter branch name (default: main): ")

if branchname == "":
    branchname = "main"

current_branch = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode().strip()

if branchname != current_branch:
    result = subprocess.run(['git', 'checkout', branchname], stdout=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Branch '{branchname}' does not exist. Creating a new branch.")
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

print(f"Changes have been committed and pushed to branch: {branchname}")