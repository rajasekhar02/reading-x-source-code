def getQueryParams(url):
    listQueryParams = list(map(lambda x: x.split("="), url.split("?")[1].split("&")))
    dictParams = defaultdict(lambda: "")
    for eachItem in listQueryParams:
        dictParams[eachItem[0]] = eachItem[1]
    return dictParams
        
def alphaNumeric(string):
    for i in string:
        if not (ord('a') <= ord(i) <= ord("z") or (ord('0') <= ord(i) <= ord("9"))):
            return False
    return True

def alphaNumericRegex(string):
    return re.fullmatch("[a-z0-9]+", string) is not None

def getResponses(valid_auth_tokens, requests):
    # Write your code here
    answers = []
    setOfTokens = set(valid_auth_tokens)
    for eachRequest in requests:
        requestType = eachRequest[0]
        requestQueryParams = getQueryParams(eachRequest[1])
        if requestQueryParams["token"] not in setOfTokens:
            answers.append("INVALID")
            continue
        restParams = ",".join([f"{i},{requestQueryParams[i]}" for i in requestQueryParams if i not in ['token', 'csrf']])
        print((requestQueryParams["csrf"] == ""), (len(requestQueryParams["csrf"]) < 8), alphaNumericRegex(requestQueryParams["csrf"]))
        if requestType == "GET":
            answers.append(f"VALID,{restParams}")
        else:
            if requestQueryParams["csrf"] == "" or len(requestQueryParams["csrf"]) < 8 or not alphaNumericRegex(requestQueryParams["csrf"]):
                answers.append("INVALID")
                continue
            answers.append(f"VALID,{restParams}")
    return answers
