from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def oauth():
  values = """
    {
      "username": "drendon@ciudadrenovable.com",
      "access_key": "MTRmYzRkYmQtMTU5MC00MmY2LWE3M2MtMzM0NmEwMGQwYzYzOmt4diFqVyEyUEM="
    }
  """

  headers = {
    'Content-Type': 'application/json',
    'Partner-Id': 'Ciudad'
  }

  request = Request('https://api.siigo.com/auth', data=values.encode(), headers=headers)

  try:
      response = urlopen(request)
      response_body = response.read()
      return print(response_body)
  except HTTPError as e:
      return print('HTTP Error:', e.code, e.reason)
  except URLError as e:
      return print('URL Error:', e.reason)
   
