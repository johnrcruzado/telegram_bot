import requests
#token = "1769446520:AAFh3kwmZQwckA_3K72pioyyIE3Kk_jSYGK"
token = "1693043053:AAHh4zuNkNzh_fGx7u4QdoLFdobjkOGsx-8"
#url = f'https://api.telegram.org/bot'+token+'/getUpdates'
#reponse = requests.post(url).json()


url = f'https://api.telegram.org/bot'+token+'/sendMessage'
data = {'chat_id': '1730408710', 'text': 'python msg'}
reponse = requests.post(url, data).json()

print(reponse)
