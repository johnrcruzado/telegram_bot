# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel,InputPhoneContact
from telethon import TelegramClient, sync, events
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon import functions, types
import gspread

import time

gc = gspread.service_account()

sht1 = gc.open_by_key('1CV9C2mWMOWzwS4yMN3dyYZl2fJSAtC_ropC2F3Ypai8')
worksheet = sht1.get_worksheet(0)

# With label
val = worksheet.get('A2:E')



# get your api_id, api_hash, token
# from telegram as described above
api_id = '3909738'
api_hash = 'e115eb2c50a57a22aad99a3e3926fb79'
token = '1693043053:AAHh4zuNkNzh_fGx7u4QdoLFdobjkOGsx-8'
#1769446520:AAFh3kwmZQwckA_3K72pioyyIE3Kk_jSYGK  
# your phone number
phone = '+639959213516'
   
# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)
   
# connecting and building the session
client.connect()
  
# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id 

for val_ in val:
    contact_name,contact_number,msg =val_[1],val_[2],val_[3]


def add_contact(val):
    for val_ in val:
        contact_name,contact_number,msg =val_[1],val_[2],val_[3]
        contact = InputPhoneContact(client_id = 0, phone = contact_number, first_name=contact_name, last_name="")
        result = client(ImportContactsRequest([contact]))
    print("contact added")


if not client.is_user_authorized():
    client.send_code_request(phone)
    # signing in the client
    client.sign_in(phone, input('Enter the code: '))
   
   
   
try:
    x = 2
    for val_ in val:
        contact_name,contact_number,msg =val_[1],val_[2],val_[3]

        entity = client.get_entity(contact_number)
        receiver = InputPeerUser(entity.id, entity.access_hash)
        sent = client.send_message(receiver, msg, parse_mode ="html" )
        print(contact_name,)
        time.sleep(10)
        string =""
        for message in client.iter_messages(entity):
            print(message.sender_id, ':', message.text)
            string += str(message.sender_id)+ ':'+ str(message.text)
            #pass
            
        worksheet.update('E'+str(x), string)
        x +=1
        time.sleep(5)
        print("next")
    #print(entity)
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
    
    # sending message using telegram client
    
  

except Exception as e:
      
    # there may be many error coming in while like peer
    # error, wwrong access_hash, flood_error, etc
    print(e);
  


client.disconnect()