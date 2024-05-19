import json
import requests
from autentication import oauth
from reports import report


def main():
    # Get the access token from the OAuth function
    access_token_response_str = oauth()
    # Print the access token response
    print(access_token_response_str)
    # Assuming access_token_response_str contains the JSON response
    access_token_response = json.loads(access_token_response_str)
    access_token = access_token_response["access_token"]
    results_str = report(access_token)
    # Parse the JSON string to a dictionary
    results = json.loads(results_str)
    # Check if the 'file_url' is present in the results
    if "file_url" in results:
        file_url = results["file_url"]
        # Download the Excel file using requests
        response = requests.get(file_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the file content to a local file
            with open("output.xlsx", "wb") as f:
                f.write(response.content)
            print("Excel file downloaded successfully!")
        else:
            print("Failed to download Excel file. Status code:", response.status_code)
    else:
        print("No file URL found in the results.")
    
    print(results)

if __name__ == "__main__":
    main()

