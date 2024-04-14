from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.git.models import GitRepositoryCreateOptions
import pprint, os

class DevOpsClient:
    def __init__(self):
        # Fill in with your personal access token and org URL
        personal_access_token = os.getenv('FK_DEVOPS_PAT')
        organization_url = os.getenv('DEVOPS_ORG_URL')

        # Create a connection to the org
        credentials = BasicAuthentication('', personal_access_token)
        self.connection = Connection(base_url=organization_url, creds=credentials)

        # Get a client (the "core" client provides access to projects, teams, etc)
        self.core_client = self.connection.clients.get_core_client()

    def list_projects(self):
        # Get the first page of projects
        get_projects_response = self.core_client.get_projects()
        for project in get_projects_response:
            pprint.pprint(project.name)

    def get_project(self, project_name):
        # Get the first page of projects
        get_projects_response = self.core_client.get_projects()
        for project in get_projects_response:
            if project.name == project_name:
                return project.id
        return None

    def list_repos(self, project_id):
        # Get a git client
        git_client = self.connection.clients.get_git_client()

        # Get the repositories in the project
        repos = git_client.get_repositories(project_id)
        for repo in repos:
            pprint.pprint(repo.name)

    def get_repo(self, project_id, repo_name):
        # Get a git client
        git_client = self.connection.clients.get_git_client()

        # Get the repositories in the project
        repos = git_client.get_repositories(project_id)
        for repo in repos:
            if repo.name == repo_name:
                return repo.id
        return None

    def create_repo(self, project_id, repo_name):
        # Get a git client
        git_client = self.connection.clients.get_git_client()

        create_options = GitRepositoryCreateOptions(name=repo_name)
        # Create the repository
        new_repo = git_client.create_repository(create_options, project=project_id)
        return new_repo
    


#repo = get_repo(get_project('Dataplattform'), 'setup-test')
#new_repo = create_repo(get_project('Dataplattform'), 'wikitest2')
#print(new_repo.id)