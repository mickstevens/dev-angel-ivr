from django_twilio.decorators import twilio_view
 
from twilio.twiml import Response
 
@twilio_view
def gather_digits(request):
 
    twilio_response = Response()
 
    with twilio_response.gather(action='/respond/', numDigits=1) as g:
        g.say('Press one to hear a song, two to receive an SMS')
        g.pause(length=1)
        g.say('Press one to hear a song, two to receive an SMS')
 
    return twilio_response
