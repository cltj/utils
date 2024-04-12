import subprocess, os, sys, requests, json

# def create_devops_repo(project, token):
#     url = f"https://felleskjopet.visualstudio.com/{project}/_apis/git/repositories?api-version=6.0"
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {token}'
#     }
#     data = {
#         'project': {
#             'name': project
#         }
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     if response.status_code == 201:
#         print(f"Repository {name} created successfully.")
#         return response.json()['sshUrl']
#     else:
#         print(f"Failed to create repository. Status code: {response.status_code}, error: {response.text}")
#         return None

def setup_new_project(project, url, devops):
    os.chdir(os.path.expanduser('~/projects'))
    
    subprocess.run(["poetry", "new", project], check=True)

    # Change to the new directory
    subprocess.run(["cd", project], check=True, shell=True)

    # Initialize a new git repository
    subprocess.run(["git", "init"], check=True)

    # Rename the branch
    if devops is "y" or "Y":
        subprocess.run(["git", "branch", "-m", "master", "main"], check=True)

    # Add the remote origin
    subprocess.run(["git", "remote", "add", "origin", url], check=True)

    # Add all files to the git repository
    subprocess.run(["git", "add", "."], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "init project"], check=True)

    # Push the changes to the remote repository
    subprocess.run(["git", "push", "-u", "origin", "--all"], check=True)

# Usage
# Check if the user asked for help
if '-h' in sys.argv or '--help' in sys.argv:
    print("Usage: python3 new_project.py <project_name> <url>")
    print("<name>: The name of the new project")
    print("<url>: The URL of the remote repository")
    sys.exit()
    
# Usage
organization = input("Enter the name of the organization: ")
project = input("Enter the name of the project: ")
token = input("Enter your personal access token (default is to get token from your .env file) (y/n): ")
devops = input("Do you want to create your repo on Azure Devops (if no github is default): (y/n) ")

# Check if the correct number of arguments were passed
if len(sys.argv) != 4:
    print("Usage: python3 new_project.py <name> <new_name> <url>")
else:
    # Call the function with the command-line arguments
    setup_new_project(sys.argv[1], sys.argv[2], sys.argv[3])
