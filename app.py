from flask import Flask, render_template, request, send_file
import pandas as pd
from verify_email import verify_email
from scoring import score_lead
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FILE = 'output/verified_ranked_leads.csv'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('output', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            df = pd.read_csv(filepath)

            results = []
            for _, row in df.iterrows():
                email_valid = verify_email(row['email'])
                score = score_lead(row['title'], row.get('company_size', 'Small'))
                row['email_valid'] = email_valid
                row['lead_score'] = score
                results.append(row)

            result_df = pd.DataFrame(results)
            result_df = result_df.sort_values(by='lead_score', ascending=False)
            result_df.to_csv(OUTPUT_FILE, index=False)
            return render_template('index.html', tables=[result_df.head(20).to_html(classes='data')], download_link=True)

    return render_template('index.html', tables=None, download_link=False)

@app.route('/download')
def download():
    return send_file(OUTPUT_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)