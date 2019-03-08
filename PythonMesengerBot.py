#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'facebook üzerinden alınan token değeri'
#örnek token ZDFDjQzCyAZBEBAE3hYIFdIZCCO6ZBIobzEVgUZBnvuqqLEoCJ3Jj736shK9ZAQKd3ZBL4ZAlgYZAAGpZBbUDKV7sjlUATt2mv3q5EZB3iY5m6TLwv6NG0Ar6zIXjxWyw0c9DGJZCPvJew1FZCmSlcRCIBUEK1Q71i5NO9mZBuqlaxrQem7QZDZD

VERIFY_TOKEN = 'facebook mesenger bölümünde kendi seçimimizle oluşturduğumuz token'

bot = Bot(ACCESS_TOKEN)

#Facebook botun mesakları alması
@app.route("/", methods=['GET', 'POST'])
def receive_message():

    if request.method == 'GET':
        """Botun aldığı tüm istekleri facebooktan geldiğini doğrular"""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:

        # kullanıcının gönderdiği mesajı bot ile birlikte alma(json datası) type dict
       output = request.get_json()
       #convert(output) dict yapısında gelen veri içinde gezmek için kullandığımız döngü
       for event in output['entry']:
          messaging = event['messaging']

          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    # gelen mesaj içeriğinde kullanıcı tarafından duyuru yazılıp yazılmadığının kontrol sağlanması
                    if message['message']['text']=="duyuru":
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    elif message['message']['text']!="duyuru":
                        response_sent_text = get_message1()
                        send_message(recipient_id, response_sent_text)





                #eğet kullanıcı text içerik olmayan bir resim,video,gif gibi dosyalar paylaşırsa
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"



def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a  message to send to the user
def get_message():
    filetoRead = open("/home/asim/Masaüstü/projectone/duyurular.txt","r")

    for i in filetoRead:
        sample_responses = i

    filetoRead.close()

    # return selected item to the user
    return sample_responses

def get_message1():
    sample_responses = ["duyuru yazman yeterli"]

    # return selected item to the user
    return random.choice(sample_responses)




#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"





if __name__ == "__main__":
    app.run()
