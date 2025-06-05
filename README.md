# Smart-Lead-Ranker

## Overview
Smart Lead Ranker enhances your lead generation efforts by validating email addresses and assigning lead scores based on job title and company size. Upload a CSV of leads, and download a cleaned, ranked list.

## Features
- Email validation using regex
- Lead scoring based on title and company size
- Simple web UI with CSV export

## Repository Contents
| File                   | Description                                                     |
| ---------------------- | --------------------------------------------------------------- |
| `app.py`               | Flask web app to upload, verify, and score leads                |
| `verify_email.py`      | Basic email regex checker                                       |
| `scoring.py`           | Simple lead scoring based on title and company size             |
| `templates/index.html` | Bootstrap-based UI to upload and view results                   |
| `requirements.txt`     | Dependencies (`Flask`, `pandas`)                                |
| `README.md`            | Overview, setup guide, and usage instructions (continued below) |


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
| name       | email                                       | title          | company\_size |
| ---------- | ------------------------------------------- | -------------- | ------------- |
| Jane Doe   | [jane@startup.com](mailto:jane@startup.com) | CEO            | Small         |
| John Smith | [john@bigcorp.com](mailto:john@bigcorp.com) | VP Engineering | Large         |
```

## Output
- Ranked leads with email validity and score.
- Exportable CSV file.

## License
MIT

# 7. output/verified_ranked_leads.csv
(Auto-generated after upload)
