# quest_web
A Flask web server with a simple inteface to supply a programming quest and verify the answers.

# Idea

1. Get a programming quest description by acccessing http://servername?quest=#no (where #no is a number). This will present at web page with a description of the quest.
2. Get the input data for a given quest by sending a html POST request to the server. The POST request should contain the following data.
```
{
    'user'      : username,
    'getQuestNo': #no
}
```
If the quest number is valid the server will respond with at message of the form:
```
{
    'questNo': #no
    'ID': #UniqueID,
    'inputData' : string/value or array of strings/values
}
```
3. To answer the quest you need to send a html POST request to the server. The POST request should contain the following data.
```
{
    'ID': #UniqueID,
    'outputData' : string/value or array of strings/values
}
```
4. The server will respond with a message that indicates if the answer is correct or not.

## Quest suggestions.

Echo program
- learn to use the framework by simply echoing the input data back to the server.

Math 1
- Input data consist of two or more numbers that should be multiplied.

Math 2 
