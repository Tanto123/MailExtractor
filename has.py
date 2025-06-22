import requests

def extract_emails_from_file(file_path, api_key=None):
    """
    Upload a file to hashes.com email extractor API and get extracted emails.

    Args:
        file_path (str): Path to the text file to upload.
        api_key (str or None): Your API key if required by the service.

    Returns:
        list: Extracted email addresses.
    """
    url = "https://hashes.com/en/api/emails/extract"  # Hypothetical API endpoint

    files = {'file': open(file_path, 'rb')}
    data = {}

    if api_key:
        data['key'] = api_key  # If API key is required

    try:
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        result = response.json()

        # Assuming the response JSON contains a list of emails under 'emails' key
        emails = result.get('emails', [])
        return emails

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []
    except ValueError:
        print("Failed to parse JSON response.")
        return []

if __name__ == "__main__":
    file_to_upload = "sample.txt"  # Replace with your file path
    api_key = None  # Replace with your API key if needed

    emails = extract_emails_from_file(file_to_upload, api_key)
    print("Extracted emails:")
    for email in emails:
        print(email)
