import os
from twilio.rest import Client


account_sid = "ACf55b132f2446471c2eaed6a8299de21a"
auth_token = "4a8d4e6f3e5649180b6a7ca4fcdffbea"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>lanjodaka</Say></Response>',
                        to='+18602801669',
                        from_='+18333552764'
                    )

print(call.sid)