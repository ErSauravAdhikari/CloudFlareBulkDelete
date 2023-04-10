# Cloudflare Bulk Delete
Cloudflare Bulk Delete is a Python script that connects to the Cloudflare API and deletes all DNS records for a specified zone. This script is useful if you need to delete a large number of DNS records from a Cloudflare zone, as it automates the process and saves you from having to manually delete each record one by one.

## Motivation
The Cloudflare platform automatically imports all DNS records associated with a newly added zone for a seamless transition. However, this often results in a clutter of unnecessary records that are no longer needed. In some cases, these records are from domain sellers or resellers and point to a multitude of random addresses, making it a hassle to remove them one by one. Unfortunately, Cloudflare does not support bulk delete natively, so I created the "cloudflare bulk delete" project to automate the process. By connecting to the Cloudflare API and running the script, all DNS records associated with a given zone are deleted in one fell swoop, saving time and effort for the user and making the process of managing DNS records in Cloudflare more efficient.

## Prerequisites
Before you can run this script, you need to have the following:

1. A Cloudflare account
2. A Cloudflare API token with Zone.DNS permissions
3. Python 3.6 or later installed on your machine

## Installation
### Clone this repository to your local machine:
```bash
git clone https://github.com/ErSauravAdhikari/CloudFlareBulkDelete.git
```
### Navigate to the project directory:
```bash
cd CloudFlareBulkDelete
```
### Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
This will install the following dependencies:
```
python-dotenv==1.0.0
```

### ENV File Setup
Copy the .env.example file to .env and update the values of CF_API_KEY and ZONE_ID with your Cloudflare API token and zone ID, respectively.

## Usage
To run the script, simply execute the following command from the project directory:

```bash
python main.py
```

This will delete all DNS records for the specified zone.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



