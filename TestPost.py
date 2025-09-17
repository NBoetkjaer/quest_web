import requests
import json

server='http://webquest.local'
#server='http://localhost'
testCorrectAnswer = True

### Opgave 1
questGet = {
    'cmd'    : 'get',
    'questNo'  : 1,
    'user'   : 'Anders And'
}

r = requests.post(server, json=questGet)
data = r.json()
print (data)

questAnswer = {
    'cmd'        : 'answer',
    'ID'         : data['ID'],
    'outputData' : data['inputData'] if testCorrectAnswer else ""
}

r = requests.post(server, json=questAnswer)
data = r.json()
print (data)

### Opgave 2
questGet = {
    'cmd'    : 'get',
    'questNo'  : 2,
    'user'   : 'Anders And'
}

r = requests.post(server, json=questGet)
data = r.json()
print (data)

values = data['inputData']
questAnswer = {
    'cmd'        : 'answer',
    'ID'         : data['ID'],
    'outputData' : values[0] + values[1] if testCorrectAnswer else 0
}

r = requests.post(server, json=questAnswer)
data = r.json()
print (data)

### Opgave 3
questGet = {
    'cmd'    : 'get',
    'questNo'  : 3,
    'user'   : 'Terminator T1000'
}

r = requests.post(server, json=questGet)
data = r.json()
print (data)

values = data['inputData']
questAnswer = {
    'cmd'        : 'answer',
    'ID'         : data['ID'],
    'outputData' : sum(values) / len(values) if testCorrectAnswer else 0
}

r = requests.post(server, json=questAnswer)
data = r.json()
print (data)

