from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def report(token):
  headers = {
        'Content-Type':'application/json',
        'Authorization':f'Bearer {token}',
        'Partner-Id':'Ciudad'
    }

    # Make a request to the API endpoint that requires the access token
  request = Request('https://api.siigo.com/v1/products?created_start=2021-02-17', headers=headers)
    
  try:
      response = urlopen(request)
      response_body = response.read().decode()
      print(response_body)
  except HTTPError as e:
      error_body = e.read().decode()
      print('HTTP Error:', e.code, e.reason)
      print('Headers:', e.headers)
      print('Body:', error_body)
  except URLError as e:
      print('URL Error:', e.reason)



      # values = """
  #   {
  #     "account_start": "\"11050501\"",
  #     "account_end": "\"41350501\"",
  #     "year": 2023,
  #     "month_start": 1,
  #     "month_end": 13,
  #     "includes_tax_difference": false
  #   }
  # """

  # headers = {
  #   'Content-Type': 'application/json',
  #   'Authorization': '[access_token]',
  #   'Partner-Id': 'Ciudad'
  # }
  # request = Request('https://api.siigo.com/v1/test-balance-report', data=values, headers=headers)

  # response_body = urlopen(request).read()
  # return response_body