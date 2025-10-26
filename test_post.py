from requests.sessions import Session

server='http://webquest.local'
#server='http://localhost'
#server='http://127.0.0.1'
testCorrectAnswer = True

### Opgave 1
questGet = {
    'cmd'    : 'get',
    'questNo'  : 1,
    'user'   : 'Anders And'
}

s = Session()
r = s.post(server, json=questGet)
data = r.json()
print (data)

questAnswer = {
    'cmd'        : 'answer',
    'outputData' : data['inputData'] if testCorrectAnswer else ""
}

r = s.post(server, json=questAnswer)
data = r.json()
print (data)

### Opgave 2
questGet = {
    'cmd'    : 'get',
    'questNo'  : 2,
    'user'   : 'Anders And'
}

r = s.post(server, json=questGet)
data = r.json()
print (data)

values = data['inputData']
questAnswer = {
    'cmd'        : 'answer',
    'outputData' : values[0] + values[1] if testCorrectAnswer else 0
}

r = s.post(server, json=questAnswer)
data = r.json()
print (data)

### Opgave 3
questGet = {
    'cmd'    : 'get',
    'questNo'  : 3,
    'user'   : 'Terminator T1000'
}

r = s.post(server, json=questGet)
data = r.json()
print (data)

values = data['inputData']
questAnswer = {
    'cmd'        : 'answer',
    'outputData' : sum(values) / len(values) if testCorrectAnswer else 0
}

r = s.post(server, json=questAnswer)
data = r.json()
print (data)

### Opgave 42
questGet = {
    'cmd'    : 'get',
    'questNo'  : 42,
    'user'   : 'Ford Prefect'
}

r = s.post(server, json=questGet)
data = r.json()
print (data)

values = data['inputData']
questAnswer = {
    'cmd'        : 'answer',
    'outputData' : 'The Ultimate Question of Life, the Universe, and Everything' if testCorrectAnswer else 42
}

r = s.post(server, json=questAnswer)
data = r.json()
print (data)

