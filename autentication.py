from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def oauth():
    values = """
    {
      "username": "drendon@ciudadrenovable.com",
      "access_key": "MjMzNzNiMzUtMDNiNS00ZGRlLTkyNDYtOGQ0MDdjNzY2MDUyOj9UOSxidCw2LEI="
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
        return response_body.decode()
    except HTTPError as e:
        return print('HTTP Error:', e.code, e.reason)
    except URLError as e:
        return print('URL Error:', e.reason)

   
