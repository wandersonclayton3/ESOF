

from twilio.rest import TwilioRestClient

accountSID = 'ACda01a1d5c401e755624c011ddbfd582f' #Meu Token ID
authToken = '302a93df0e009cd201529b2e746b1e96'


twilioCli = TwilioRestClient (accountSID, authToken) 
myTwilioNumber = '+551939570565' 
myCellPhone = 'Numero do Telefone pra envio' 
message = twilioCli.messages.create(body='Esta é a menssagem do sms', from_=myTwilioNumber, to=myCellPhone)

