from flask import Flask, request, Response, stream_with_context
import requests

app = Flask(__name__)

TELEGRAPH_URL = 'https://api.openai.com'

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    global TELEGRAPH_URL
    url = TELEGRAPH_URL + '/' + path
    headers = dict(request.headers)
    headers['Host'] = TELEGRAPH_URL.replace('https://', '')
    headers['Access-Control-Allow-Origin'] = headers.get('Access-Control-Allow-Origin') or "*"
    
    response = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        stream=True)

    def generate():
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

    # Filter out headers not to be forwarded
    excluded_headers = ['content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in response.raw.headers.items()
               if name.lower() not in excluded_headers]

    # Flatten header list to dictionary
    headers = {name: ", ".join(values) for name, values in headers}

    return Response(stream_with_context(generate()), response.status_code, headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
