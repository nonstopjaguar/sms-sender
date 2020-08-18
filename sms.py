import nexmo

client = nexmo.Client(key='your key', secret='your secret key')

client.send_message({
    'from': 'your name',
    'to': 'registered phone number',
    'text': 'sample text',
})
