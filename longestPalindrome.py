import sys
def longestPalindrome(s):

    if len(s) <= 1:
        return s

    substrings = [s[i: j]
        for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    palindromes = {}
    for st in substrings:
        palindromes[st] = isPalindrome(st)
        # palindromes.append(self.isPalindrome(st))
    # print(substrings)
    # print(palindromes)
    r = ''
    for key in palindromes:
        if len(key) > len(r) and palindromes[key] == True:
            r = key
    return r

def isPalindrome(s):
    i = 0
    j = len(s)-1
    while(j >=i or j>=0 or i<len(s)):
        if s[j] !=s[i]:
            return False
        i = i+1
        j = j-1

    return True


if __name__=='__main__':
    print(longestPalindrome(sys.argv[1]))


    """
    :type s: str
    :rtype: str
    """
