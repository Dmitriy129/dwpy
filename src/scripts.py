
from src.helpers import addGradeLabelToPR, addLabelToPRByGrade, getAllClients, getDictPRGradeInfo, getGradeByPR


def script1(mainConfig, runConfig):
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    pr = ghclient.getPRById(
        runConfig["github"]["repo"],
        runConfig["github"]["prId"])

    dictGitFio = gsclient.getDictKeyVal(
        mainConfig["googleSheet"]["headers"]["github"],
        mainConfig["googleSheet"]["headers"]["fio"])

    dictFioGradeInfo = mdclient.getDictFioGradeInfo(
        runConfig["moodle"]["courseId"],
        runConfig["moodle"]["quizId"])

    grade = getGradeByPR(dictFioGradeInfo, dictGitFio, pr)

    addLabelToPRByGrade(pr, grade, mainConfig["github"]["accessLabel"])


def script1Mock(mainConfig, runConfig, mockNumber):
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    pr = ghclient.getPRById(
        runConfig["github"]["repo"],
        runConfig["github"]["prId"])

    dictGitFio = gsclient.getDictKeyVal(
        mainConfig["googleSheet"]["headers"]["github"],
        mainConfig["googleSheet"]["headers"]["fio"])

    dictFioGradeInfo = mdclient._getDictFioGradeInfo(
        runConfig["moodle"]["courseId"],
        runConfig["moodle"]["quizId"],
        mockNumber)

    grade = getGradeByPR(dictFioGradeInfo, dictGitFio, pr)

    addLabelToPRByGrade(pr, grade, mainConfig["github"]["accessLabel"])


def script2(mainConfig, runConfig):
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    dictGitPR = ghclient.getDictGitPR(
        runConfig["github"]["repo"],
        runConfig["github"]["prRegex"])

    dictFioGit = gsclient.getDictFioGit(
        mainConfig["googleSheet"]["headers"]["fio"], mainConfig["googleSheet"]["headers"]["github"])

    dictFioGradeInfo = mdclient.getDictFioGradeInfo(
        runConfig["moodle"]["courseId"], runConfig["moodle"]["quizId"])

    # get link pr - grade
    dictPRGradeInfo = getDictPRGradeInfo(
        dictFioGradeInfo, dictFioGit, dictGitPR)

    # add grade labels to prs
    addGradeLabelToPR(dictPRGradeInfo, mainConfig["github"]["gradeLabel"])


def script2Mock(mainConfig, runConfig, mockNumber):
    ghclient, gsclient, mdclient = getAllClients(mainConfig)

    dictGitPR = ghclient.getDictGitPR(
        runConfig["github"]["repo"],
        runConfig["github"]["prRegex"])

    dictFioGit = gsclient.getDictFioGit(
        mainConfig["googleSheet"]["headers"]["fio"], mainConfig["googleSheet"]["headers"]["github"])

    dictFioGradeInfo = mdclient._getDictFioGradeInfo(
        runConfig["moodle"]["courseId"], runConfig["moodle"]["quizId"], mockNumber)

    dictPRGradeInfo = getDictPRGradeInfo(
        dictFioGradeInfo, dictFioGit, dictGitPR)

    addGradeLabelToPR(dictPRGradeInfo, mainConfig["github"]["gradeLabel"])
