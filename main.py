import requests
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
API_KEY = os.getenv('HUNTER_API_KEY')

if not API_KEY:
    raise ValueError("API Key not found! Please set it in the .env file.")

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

# List of pharmacy-related domains (add more as needed)
pharmacy_domains = [
    'walgreens.com',
    'riteaid.com',
    'cvs.com',
    'boots.com',
    'pharmacy.com',
    'goodrx.com',
    'healthmart.com',
    'pharmaprix.ca'
]

# Collect emails for each pharmacy domain
emails = []
for domain in pharmacy_domains:
    print(f"Fetching emails from {domain}...")
    domain_emails = get_emails_by_domain(domain)
    emails.extend(domain_emails)

# Save the emails to a CSV file
if emails:
    with open('pharmacy_emails.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Email'])
        for email in emails:
            writer.writerow([email['value']])
    print(f"Done! -Emails from pharmacies saved to 'pharmacy_emails.csv'")
else:
    print("No pharmacy emails were found.")
