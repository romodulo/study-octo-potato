import json

def file_properties():
    #
    # {}
    pass

def run_app(fileObject, dictionary):
    #
    #
    fileObject = None
    #
    #
    # will hard
    # code a
    # dictionary in
    # codebase
    # instead
    #
    #
    #
    dictionary = {0: None, 1: None, 2:None}
    #
    #
    #
    return fileObject, dictionary

    



# prints dir(json)
def test():
    for i in dir(json):
        print(i)
def test2(x):
    fileObject = json.loads(x)
    print(fileObject, "REMEMBER TO REMOVE Print Statement from Function Definition... Note: PRINT Statement in def test2")
    return fileObject



if __name__ == '__main__':
    #
    file_properties()
    #
    #
    # runs app
    fileObject = "unInitialized" #un-initialized before function run
    dictionary = None
    fileObject, dictionary = run_app(fileObject, dictionary)
    #
    #
    print(fileObject)
    print('seperator:')
    print(dictionary)
    #
    #
    # my goal is run json items in script
    fileObject = json.dumps(dictionary)
    print('seperator:')
    print('seperator:')
    print(fileObject)
    #def 'test2' here:
    print('#2 test here:')
    loadDict = test2(fileObject)
    print('seperator')
    print('seperator')
    print('seperator')
    print(loadDict)
    # test:
    print(list(loadDict))
    for i in list(loadDict):
        loadDict[int(i)] = loadDict.pop(i, 'defaultKey') #I still do not know how to use pop's method when it comes to its second argument (e.g. <"defaultKey">) tldr: I do not know how to use pop's second argument in this case (, the value that I used here is <"defaultKey">)
    #below test will not be removed
    #to show how I tested and where
    #I placed my test.
    # tldr: I don't want to lose
    #>the placement of this test
    #to better understand its
    #functionality if
    #necessary
    def test4(): #this was a good test
        #for ex. i <key in DictObject>
        #if i <key in Dict> = '0'
        i = '0' #75a
        loadDict[int(i)] = loadDict.pop(i, 'defaultKey') #75b
        print('The Value of Dict:' + str(loadDict)) #75c
        #the last 3 lines work: notations are 75a 75b 75c
    print('seperator')
    print('seperator')
    print('seperator')
    print('seperator')
    print(loadDict)