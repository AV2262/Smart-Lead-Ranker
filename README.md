# Smart-Lead-Ranker

## Overview
Smart Lead Ranker enhances your lead generation efforts by validating email addresses and assigning lead scores based on job title and company size. Upload a CSV of leads, and download a cleaned, ranked list.

## Features
- Email validation using regex
- Lead scoring based on title and company size
- Simple web UI with CSV export

## Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/your-username/smart-lead-ranker.git
cd smart-lead-ranker
```
2. Create virtual environment:
```bash
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
```
3. Install requirements:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
python app.py
```
5. Visit `http://127.0.0.1:5000` in your browser.

## Sample CSV Format
```
name,email,title,company,company_size
John Doe,john@acme.com,CEO,Acme Inc,Large
Jane Smith,jane@startup.com,Manager,Startup Co,Small
```

## Output
- Ranked leads with email validity and score.
- Exportable CSV file.

## License
MIT


# 7. sample_data/raw_leads.csv
name,email,title,company,company_size  
Alice Chen,alice@bigco.com,CEO,BigCo,Large  
Bob Lee,bob@startup.org,Manager,StartupOrg,Small  
Carla Smith,carla@midbiz.net,Director,MidBiz,Medium


# 8. output/verified_ranked_leads.csv
(Auto-generated after upload)
