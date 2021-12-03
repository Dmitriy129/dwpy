def getDictPRGradeInfo(dictFioGradeInfo, dictFioGit, dictGitPR):
    dicPrGradeInfo = {}
    for fioLong in dictFioGit:
        if not fioLong:
            continue
        git = dictFioGit[fioLong]
        arrFioLong = fioLong.split(" ")
        fioShort = " ".join([arrFioLong[1], arrFioLong[0]])
        if fioShort in dictFioGradeInfo and git in dictGitPR:
            grade = dictFioGradeInfo[fioShort]
            pr = dictGitPR[git]
            dicPrGradeInfo[pr] = grade
    return dicPrGradeInfo
