import csv
import sys

# /Users/Emily/Documents/CodeProjects/python-practice/.venv/bin/python3 /Users/Emily/Documents/CodeProjects/python-practice/dna/dna.py /Users/Emily/Documents/CodeProjects/python-practice/dna/databases/small.csv /Users/Emily/Documents/CodeProjects/python-practice/dna/sequences/0.txt
# /Users/Emily/Documents/CodeProjects/python-practice/.venv/bin/python3 /Users/Emily/Documents/CodeProjects/python-practice/dna/dna.py /Users/Emily/Documents/CodeProjects/python-practice/dna/databases/large.csv /Users/Emily/Documents/CodeProjects/python-practice/dna/sequences/5.txt

def main(argv):
    length = len(argv)
    if length != 3:
        print(f"Incorrect number of args: {length}")
        return
    
    peopleFileName = argv[1]
    dnaFileName = argv[2]
    
    peopleData = readPeopleData(peopleFileName)
    keys = []
    for key in peopleData[0].keys():
        keys.append(key)
    keys.remove('name')
    
    dnaSeq = readDNAFile(dnaFileName)
    
    counts = countConsecutiveSequences(keys, dnaSeq)
    
    result = compareResults(peopleData, keys, counts)

    print(result)
    # -- end main --
    
def readPeopleData(fileName):
    data = csv.DictReader(open(fileName))
    list = []
    for row in data:
        list.append(row)
    return list

def readDNAFile(fileName):
    file = open(fileName).read()
    str = file
    return str

def countConsecutiveSequences(keys, dnaSeq):
    count = {}
    seqLen = len(dnaSeq)
    for key in keys:
        index = 0
        count[key] = 0
        keyLen = len(key)
        while(index < seqLen): # iterate through whole seq 1 char at a time
            tempCount = 0
            beginIndex = index
            endIndex = beginIndex + keyLen
            while(dnaSeq.find(key, beginIndex, endIndex) > -1): # if seq is found, continue searching for seq consecutively
                tempCount = tempCount + 1
                beginIndex = endIndex # next search will start after end of last matched seq
                endIndex = beginIndex + keyLen
            if(tempCount > count[key]):
                count[key] = tempCount
            index += 1
    return count

def compareResults(peopleData, keys, counts):
    print(f"consecutive sequence counts: {counts}")
    
    for person in peopleData:
        skip = False
        for key in keys:
            if int(person[key]) != counts[key]:
                skip = True
                break # go to next person
        if skip == False:
            return person['name']
    return "No match"
    
    
main(sys.argv)