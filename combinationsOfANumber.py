digits = "23"

digitMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def combinations(digits):
    result = []
    combination = ""
    dfs(digits, digitMap, result, combination, 0)
    print(result)

def dfs(digits, digitMap, result, combination, index):

    print("dfs called with index {}, combination {}".format(index, combination))

    if index == len(digits):
        result.append(combination)
        return
    
    digit = digits[index]
    lettersForDigit = digitMap[int(digit)]

    for i in lettersForDigit:
        combination += i
        dfs(digits, digitMap, result, combination, index+1)
        # print("combintation before removing " + combination)
        combination = combination[:-1]


combinations(digits)





