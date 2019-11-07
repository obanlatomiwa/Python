def threatdetector (textMessages):
    for txt in textMessages:

        l=len(txt)
        ans = 0
        sym = txt [-3:]

        for i in range(0, l-5):
            for j in range(i+3, l-2):
                subStr = txt [i:j]
                if subStr. isalnum( ) and subStr== subStr [::-1] / and len (subStr) >=3 :
                    ans+= len(subStr)

        if ans==0:
            print (sym, 'Ignore')

        elif ans < 11:
            print (sym, 'Feasible')

        elif ans < 41:
            print (sym, 'Probable')

        elif ans < 150:
            print( sym, 'Ignore')

