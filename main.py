import requests
import csv

# Your Hunter.io API key
API_KEY = '18236675eb2fef16b4bef72e313da963c00623af'
BASE_URL = 'https://api.hunter.io/v2/domain-search'

# Function to search emails by domain
def get_emails_by_domain(domain):
    params = {
        'domain': domain,
        'api_key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'emails' in data['data']:
            return data['data']['emails']
        else:
            print(f"No emails found for domain: {domain}")
            return []
    else:
        print(f"Error: {response.status_code}")
        return []

# Example: search for emails from a pharmacy domain
domain = 'walgreens.com'
emails = get_emails_by_domain(domain)

# Save the emails to a CSV file
if emails:
    with open('pharmacy_emails.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Email'])
        for email in emails:
            writer.writerow([email['value']])
    print(f"Emails from {domain} saved to 'pharmacy_emails.csv'")
