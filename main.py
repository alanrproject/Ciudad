import json
from autentication import oauth
from reports import report
# from export import transform_to_df

def main():
    # Get the access token from the OAuth function
    access_token_response_str = oauth()
    # Print the access token response
    print(access_token_response_str)
    # Assuming access_token_response_str contains the JSON response
    access_token_response = json.loads(access_token_response_str)
    access_token = access_token_response["access_token"]
    results = report(access_token)
    
    print(results)

if __name__ == "__main__":
    main()

