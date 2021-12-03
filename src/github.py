

from github import Github as GH
import re


class GithubClient:
    def __init__(self, accessToken):
        self.accessToken = accessToken
        self.client = GH(accessToken)

    def getDictGitPR(self, repoName, prRegex):
        repo = self.client.get_repo(repoName)
        allPulls = repo.get_pulls()
        pullsDictionare = {}
        for pull in allPulls:
            if(re.search(prRegex, pull.title) != None):
                pullsDictionare[pull.user.login] = pull
        return pullsDictionare

   
