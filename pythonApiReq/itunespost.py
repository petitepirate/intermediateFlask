import requests 

data = {
'username': 'chickenz',
'tweets': ['hello!', 'goodbye!', 'bock bock bock', {'id': 1, 'text': 'my first tweet!'}]
}

requests.post('https://en27bnye2btkl.x.pipedream.net', json=data)
