import json




if __name__ == '__main__':
    #test print:
    # print(dir(json))
    variable = dir(json)
    lenVariable = len(variable)
    floorVariable = lenVariable//10
    moduloVariable = lenVariable % 10
    if moduloVariable > 0:
        columns = floorVariable + 1
    else:
        columns = floorVariable
    objectMain = {}
    for i in range(columns):
        objectMain[i] = []
    #test print:
    # print(objectMain)
    for i in range(3):
        # if i == 0:
        #     f = (i+1) * 10
        # else:
        #     f = i * 10
        # fStart = f - 10
        # fEnd = f - 10 + 10
        #    ^ trying a diff method:
        if i == 0:
            fStart = 0
        elif i > 0:
            fStart = i * 10
        fEnd = fStart + 10
        if i == floorVariable and moduloVariable > 0:
            fEnd = lenVariable
        for ii in variable[fStart:fEnd]:
            objectMain[i] = objectMain[i] + [ii]
    for i in objectMain:
        print("\n" + str(i), ":", str(objectMain[i]))
    
    #TEST
    count = 0
    printOut = []
    dictionary = {}
    innerCount = 0
    for i in variable:
        count += 1
        printOut.append(i)
        if count == 10:
            dictionary[str(innerCount)] = printOut
            printOut = []
            count = 0
            innerCount += 1
    if len(printOut) > 0 :
        dictionary[str(innerCount)] = printOut
    print("\n")
    for i in dictionary:
        print(i, ":", dictionary[i], "test", "\n")