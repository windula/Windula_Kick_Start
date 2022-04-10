T = int(input())                # no. of test cases
for word in range(0,T):
    N = int(input())            # length of the string
    S = list(input())           # string
    out = []
    for letter in range(0,N):            # loop from first letter in string
        total = 1                       # total letters in increasing substring
        while S[letter - 1] < S[letter]:              # first letter is before second letter in alphabet
            total = total + 1
            letter = letter - 1
        out.append(total)               # append output to a list
    print("Case #{}: {}".format(word + 1,' '.join(map(str,out))))