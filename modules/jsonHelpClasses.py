#
# this is a module for python
### -- imports -- ###
            #-#-# I hope to import a json module
import json

### -- classes -- ###


### -- helper functions -- ###



if __name__ == '__main__':
    variable = dir(json)
    # test
    def do_not_run_(variable, boolVal = False):
        if type(variable) == type([]):
            if not boolVal:
                for i in variable:
                    print(i + " \n")
            else:
                for i in variable:
                    print(i)
    # test
    def do_not_run_2():
        print(len(variable))
    # columns: 3
    columnA = []
    columnB = []
    columnC = []
    #Set Variables:
    f = "the result/dynamic variable"
    stringOfSuccess = []
    f = {"a": 1, "b":0, "c":0}
    count = 0
    for i in variable:
    # for e, i in enumerate(variable):
        match f:
            case {"a": 1, "b": 0, "c": 0}:
                f["a"] = 0
                f["b"] = 1
                columnA.append(i)
                stringOfSuccess.append('successful run, A')
                count += 1
            case {"a": 0, "b": 1, "c": 0}:
                f["b"] = 0
                f["c"] = 1
                columnB.append(i)
                stringOfSuccess.append('successful run, B')
                count += 1
            case {"a": 0, "b": 0, "c": 1}:
                f["c"] = 0
                f["a"] = 1
                columnC.append(i)
                stringOfSuccess.append('successful run, C' + '\n')
                count += 1
    def do_not_run_3():
        variable = stringOfSuccess
        for i in variable:
            print(i)
    with open("modules/newTxtFile.txt", "w", encoding='utf-8') as tF:
        rangeOfColumns= len(columnA)
        if len(columnB) < rangeOfColumns:
            rangeOfColumns = len(columnB)
        if len(columnC) < rangeOfColumns:
            rangeOfColumns = len(columnC)
        rangeOFColumns_partA = rangeOfColumns
        for i in range(rangeOfColumns):
            print(columnA[i].rjust(30)+columnB[i].rjust(30)+columnC[i].rjust(30), file=tF)
        def run_For_Print(pre_part, x):
            for i in range(pre_part, x):
                print(columnA[i].rjust(30) + columnB[i].rjust(30), file=tF)
        
        if rangeOFColumns_partA < len(columnB):
            run_For_Print(rangeOFColumns_partA, len(columnB))
            rangeOFColumns_partB = len(columnB)
        else: 
            rangeOFColumns_partB = None
        if rangeOFColumns_partB:
            if rangeOFColumns_partB < len(columnA):
                run_For_Print(rangeOFColumns_partB, len(columnA))
    #test
    def do_not_run_4(variable):
        for i in variable:
            print(i)
    do_not_run_(columnB, True)
    #create Test for String Cases
