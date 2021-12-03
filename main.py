"""
TODO:
0. configs
1. github
  1.1. auth
  1.2. create request: get repo + pull requests
  1.3. create request: add/del tag/text to pull request
2. moodle
  2.1. auth
  2.2. get cours grades
3. google sheets
  3.1. auth?
  3.2. get table (git-moodle links)
4. main
  3.1. moodle and github auth
  3.2. save responses (1.2,2.2)
  3.3. compare data from moodle and data from github
  3.4. put tags in pull requests (1.3)
5. logs
"""


import json

from src.github import GithubClient
from src.googleSheets import GoogleSheetClient
from src.moodle import MoodleClient
from src.utils import getDictPRGradeInfo

mainConfig = json.load(open('./configs/main.json'))
runConfig = json.load(open('./configs/run.json'))

# git - ok
ghclient = GithubClient(mainConfig["github"]["credentials"]["accessToken"])


dictGitPR = ghclient.getDictGitPR(
    runConfig["github"]["repo"],
    runConfig["github"]["prRegex"])

# google sheets - ok
gsclient = GoogleSheetClient(mainConfig["googleSheet"]["id"])
dictFioGit = gsclient.getDictFioGit(
    mainConfig["googleSheet"]["headers"]["fio"], mainConfig["googleSheet"]["headers"]["github"])

# moodle - ok
mdclient = MoodleClient(
    baseUrl=mainConfig["moodle"]["baseUrl"],
    token=mainConfig["moodle"]["credentials"]["token"])
dictFioGradeInfo = mdclient.getDictFioGradeInfo(
    runConfig["moodle"]["courseId"], runConfig["moodle"]["quizId"])


# get link pr - grade
dictPRGradeInfo = getDictPRGradeInfo(dictFioGradeInfo, dictFioGit, dictGitPR)

# add grade labels to prs
for pr in dictPRGradeInfo:
    grade = dictPRGradeInfo[pr]
    newLabelName = f'{mainConfig["github"]["label"]["template"]} {grade["raw"]}/{grade["max"]}'
    oldLabel = next(
        (l for l in pr.labels if mainConfig["github"]["label"]["template"] in l.name), None)
    if oldLabel:
        oldLabel.edit(name=oldLabel.name,
                      color=mainConfig["github"]["label"]["color"])
    else:
        pr.add_to_labels(newLabelName)
        newLabel = next(
            (l for l in pr.labels if mainConfig["github"]["label"]["template"] in l.name), None)
        if newLabel:
            newLabel.edit(name=newLabel.name,
                          color=mainConfig["github"]["label"]["color"])
print("end")
