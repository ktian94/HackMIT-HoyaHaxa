import requests

def getTextSentiment(text):
    
    # format for idol api
    text = text.replace('#', '')
    text = text.replace(' ', '+')
    
    # create query url
    url = 'https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?text='
    url += text
    url += '&apikey=a4ee749a-0deb-4ff4-800d-7b00e1290151'
    
    # query
    response = requests.get(url)
    
    # return 0 if fail
    if 'aggregate' in response.json().keys():
        return response.json()['aggregate']['score']
    else:
        return 0