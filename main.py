import requests
import re
import json


def parse_scholar(request):
    # Code to handle CORS (from docs)
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json()
    if request_json and 'user' in request_json:
        url = f'https://scholar.google.com/citations?user={request_json["user"]}'
    else:
        user = request.args.get('user')
        url = f'https://scholar.google.com/citations?user={user}'

    r = requests.get(url)

    hits = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', r.text)
    fields = ['citations', 'citations_recent', 'h_index', 'h_index_recent', 'i10_index', 'i10_index_recent']

    return (json.dumps(dict(zip(fields, hits))), 200, headers)
