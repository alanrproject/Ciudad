import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def report(token):
  headers = {
        'Content-Type':'application/json',
        'Authorization':f'Bearer {token}',
        'Partner-Id':'Ciudad'
    }
  
  body_data = {
        "account_start": "11050501",
        "account_end": "41750503",
        "year": 2023,
        "month_start": 1,
        "month_end": 13,
        "includes_tax_difference": False
    }
  
  encoded_body = json.dumps(body_data).encode('utf-8')

    # Make a request to the API endpoint that requires the access token
  request = Request('https://api.siigo.com/v1/test-balance-report', headers=headers, data=encoded_body)
    
  try:
      response = urlopen(request)
      response_body = response.read().decode()
      return response_body
  except HTTPError as e:
      error_body = e.read().decode()
      print('HTTP Error:', e.code, e.reason)
      print('Headers:', e.headers)
      print('Body:', error_body)
  except URLError as e:
      print('URL Error:', e.reason)