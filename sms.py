import nexmo

client = nexmo.Client(key='768bd160', secret='Yjhic3pfcnHriRc5')

client.send_message({
    'from': 'your name',
    'to': 'registered phone number',
    'text': 'sample text',
})
