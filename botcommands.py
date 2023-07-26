import users
import wordlist


def search(word):
    word = word.upper()
    searchList = []
    foundList = []
    returnList = []
    i = 0
    count = 0
    searchList = list(wordlist.LIST.keys())
    while i < len(searchList):
        if searchList[i].find(word) != -1:
            searchList[i] = wordlist.CONVERT[searchList[i]]
            foundList.append(searchList[i])
            returnList = ", ".join(foundList)
            i = i + 1
            count = count + 1
        else:
            i = i + 1
    return count, returnList


def deptsearch(dept):
    dept = dept.upper()
    deptList = []
    foundDeptList = []
    returnDeptList = []
    j = 0
    fdept = 0
    deptList = list(users.DEPARTMENTS.values())
    while j < len(deptList):
        deptListUpper = deptList[j].upper()
        if deptListUpper.find(dept) != -1:
            foundDeptList.append(deptList[j])
            returnDeptList = ", ".join(foundDeptList)
            j = j + 1
            fdept = fdept + 1
        else:
            j = j + 1
    return fdept, returnDeptList