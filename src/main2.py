import json

from model import  CreateNoteResponse, Note
from datetime import datetime

if __name__ == '__main__':
    tokens = {}
    with open("tokens.txt", "r") as f:
        buf = f.readline().split('. ')
        while buf != ['']:
            bufStr = buf[1][0:len(buf[1]) - 1]
            tokens[bufStr] = buf[0]
            buf = f.readline().split('. ')
    print(tokens)

    # jsonFile = open('data.json', 'w')
    # jsonFile.write(jsonString)
    # jsonFile.close()
    # jsonFile = open('data.json', 'r')
    # jsonStr = jsonFile.read()
    # print(jsonStr)
    # jsonFile.close()
