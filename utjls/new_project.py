import subprocess, os, sys, requests, json
from utjls.devops import DevOpsClient


d = DevOpsClient()

def setup_new_project(project, name):
    os.chdir(os.path.expanduser('~/projects'))
    
    subprocess.run(["poetry", "new", name], check=True)

    # Change to the new directory
    os.chdir(name)

    # Initialize a new git repository
    subprocess.run(["git", "init"], check=True)

    # Rename the branch from master to main
    subprocess.run(["git", "branch", "-m", "master", "main"], check=True)
    
    # Get the project id and create a new repository in Azure DevOps
    project_id = d.get_project(project)
    new_repo = d.create_repo(project_id, name)

    # Add the remote origin
    subprocess.run(["git", "remote", "add", "origin", new_repo.remote_url], check=True)

    # Add all files to the git repository
    subprocess.run(["git", "add", "."], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "init project"], check=True)

    # Push the changes to the remote repository
    subprocess.run(["git", "push", "-u", "origin", "--all"], check=True)

# Usage
# Check if the user asked for help
if '-h' in sys.argv or '--help' in sys.argv:
    print("Usage: python3 new_project.py <project_name> <repo_name>")
    print("(or'newproject <project_name> <repo_name>' if .dotfiles is installed)")
    print("<project_name>: The name of the project")
    print("<repo_name>: The name of the repository")
    sys.exit()
    

# Check if the correct number of arguments were passed
if len(sys.argv) != 3:
    print("Usage: python3 new_project.py <project> <name>")
else:
    # Call the function with the command-line arguments
    setup_new_project(sys.argv[1], sys.argv[2])
