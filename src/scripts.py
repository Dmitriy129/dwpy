
import os
from src.helpers import addGradeLabelToPR, addLabelToPRByGrade, getAllClients, getDictPRGradeInfo, getGradeByPR


def chackParamsScript2():

    if "GITHUB_REPO" not in os.environ:
        print("incorrect param GITHUB_REPO")
        exit()
    if "GITHUB_PR_REGEX" not in os.environ:
        print("incorrect param GITHUB_PR_REGEX")
        exit()
    if "COURSE_ID" not in os.environ:
        print("incorrect param COURSE_ID")
        exit()
    if "CM_ID" not in os.environ:
        print("incorrect param CM_ID")
        exit()


def script1(mainConfig):
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    pr = ghclient.getPRById(
        os.environ['GITHUB_REPO'],
        int(os.environ['GITHUB_PR_ID'])
    )

    dictGitFio = gsclient.getDictKeyVal(
        mainConfig["googleSheet"]["headers"]["github"],
        mainConfig["googleSheet"]["headers"]["fio"]
    )

    dictFioGradeInfo = mdclient.getDictFioGradeInfo(
        int(os.environ['COURSE_ID']),
        int(os.environ['CM_ID'])
    )

    grade = getGradeByPR(dictFioGradeInfo, dictGitFio, pr)

    addLabelToPRByGrade(pr, grade, mainConfig["github"]["accessLabel"])


def script1Mock(mainConfig, mockNumber):
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    pr = ghclient.getPRById(
        os.environ['GITHUB_REPO'],
        int(os.environ['GITHUB_PR_ID'])
    )

    dictGitFio = gsclient.getDictKeyVal(
        mainConfig["googleSheet"]["headers"]["github"],
        mainConfig["googleSheet"]["headers"]["fio"]
    )

    dictFioGradeInfo = mdclient._getDictFioGradeInfo(
        int(os.environ['COURSE_ID']),
        int(os.environ['CM_ID']),
        mockNumber
    )

    grade = getGradeByPR(
        dictFioGradeInfo,
        dictGitFio,
        pr
    )

    addLabelToPRByGrade(pr, grade, mainConfig["github"]["accessLabel"])


def script2(mainConfig):
    chackParamsScript2()
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    dictGitPR = ghclient.getDictGitPR(
        os.environ['GITHUB_REPO'],
        os.environ['GITHUB_PR_REGEX']
    )

    dictFioGit = gsclient.getDictFioGit(
        mainConfig["googleSheet"]["headers"]["fio"],
        mainConfig["googleSheet"]["headers"]["github"]
    )

    dictFioGradeInfo = mdclient.getDictFioGradeInfo(
        int(os.environ['COURSE_ID']),
        int(os.environ['CM_ID']),
    )

    # get link pr - grade
    dictPRGradeInfo = getDictPRGradeInfo(
        dictFioGradeInfo,
        dictFioGit,
        dictGitPR
    )

    # add grade labels to prs
    addGradeLabelToPR(dictPRGradeInfo, mainConfig["github"]["gradeLabel"])


def script2Mock(mainConfig,  mockNumber):
    chackParamsScript2()
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    dictGitPR = ghclient.getDictGitPR(
        os.environ['GITHUB_REPO'],
        os.environ['GITHUB_PR_REGEX']
    )

    dictFioGit = gsclient.getDictFioGit(
        mainConfig["googleSheet"]["headers"]["fio"],
        mainConfig["googleSheet"]["headers"]["github"],
    )

    dictFioGradeInfo = mdclient._getDictFioGradeInfo(
        int(os.environ['COURSE_ID']),
        int(os.environ['CM_ID']),
        mockNumber
    )

    dictPRGradeInfo = getDictPRGradeInfo(
        dictFioGradeInfo,
        dictFioGit,
        dictGitPR
    )

    addGradeLabelToPR(dictPRGradeInfo, mainConfig["github"]["gradeLabel"])
