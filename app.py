from flask import Flask
from flask import request

app = Flask(__name__)

seen_strings = {}

@app.route('/')
def root():
    return '''
    <pre>
    Welcome to the Stringinator 3000 for all of your string manipulation needs.

    GET / - You're already here!
    POST /stringinate - Get all of the info you've ever wanted about a string. Takes JSON of the following form: {"input":"your-string-goes-here"}
    GET /stats - Get statistics about all strings the server has seen, including the longest and most popular strings.
    </pre>
    '''.strip()

@app.route('/stringinate', methods=['GET','POST'])
def stringinate():
    input = ''
    if request.method == 'POST':
        input = request.json['input']
    else:
        input = request.args.get('input', '')

    if input in seen_strings:
        seen_strings[input] += 1
    else:
        seen_strings[input] = 1
    ASCII_SIZE = 256

    def getMaxOccuringChar(input):
        # Create array to keep the count of individual characters
        # Initialize the count array to zero
        count = [0] * ASCII_SIZE

        # Utility variables
        max = -1
        c = ''

        # Traversing through the string and maintaining the count of
        # each character
        for i in input:
            count[ord(i)]+=1

        for i in input:
            if max < count[ord(i)]:
                max = count[ord(i)]
                c = i

        return c
    return {
        "input": input,
        "length": len(input),
        "Char": getMaxOccuringChar(input),
    }

@app.route('/stats')
def string_stats():
    return {
        "inputs": seen_strings,
    }
