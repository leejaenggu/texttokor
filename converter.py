import os
import re
import json

HOME_PATH = os.path.dirname(os.path.abspath(__file__))

jsondic = dict()

# list.json -> dictionary
def init():
    jpath = HOME_PATH + os.sep + 'conf/list.json'
    json_data = open(jpath).read()
    python_data = json.loads(json_data)

    for _, v in enumerate(python_data):
        jsondic[v['key'].lower()] = v['value'].lower()


# text -> json value
def listtokor(text):
    
    lowtext = text.lower()
    
    for key, val in jsondic.items():
        if key in lowtext:
            lowtext = lowtext.replace(key, val)
        
    return lowtext

# text -> numbers to ordinal Korean
def positionnumtokor(text):
    reg = re.compile('([0-9]+)')
    
    namesInSeat = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    namesInSeats = ["", "십", "백", "천"]
    namesInFourSeat = ["", "만", "억", "조"]

    numArr = list(text)
    numStr = ""
    i = 0
    x2 = ""

    for n in range(len(numArr)-1, -1, -1):
        m = reg.match(numArr[n])

        if m != None:
            x = int(numArr[n])

            if x == 1 and len(numArr) > 0:
                x2 = namesInSeats[i%4]
            elif x > 0:
                x2 = namesInSeat[x]
                x2 += namesInSeats[i%4]
            
            if i%4 == 0:
                numStr = x2 + namesInFourSeat[int(i/4)] + numStr
            else:
                numStr = x2 + numStr

            i = i+1
        else:
            numStr = numArr[n] + numStr
            
            
        if numArr[n] == " ":
            i = 0

    return numStr

# text -> English to Korean
def engtokor(text):
    engdic = {
        "a": "에이",
        "b": "비",
		"c": "씨",
		"d": "디",
		"e": "이",
		"f": "에프",
		"g": "쥐",
		"h": "에이치",
		"i": "아이",
		"j": "제이",
		"k": "케이",
		"l": "엘",
		"m": "엠",
		"n": "엔",
		"o": "오",
		"p": "피",
		"q": "큐",
		"r": "알",
		"s": "에스",
		"t": "티",
		"u": "유",
		"v": "브이",
		"w": "떠블유",
		"x": "엑스",
		"y": "와이",
		"z": "제트",
    }

    lowtext = text.lower()
    numArr = list(lowtext)
    ret = ""

    for c in numArr:
        
        if c in engdic:
            ret += engdic[c]
        else:
            ret += c

    
    return ret