# app.py
from flask import Flask, render_template, request
from asprg_data import SECURITY_DOMAINS

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Renders the main form for client input."""
    # Pass the keys of the SECURITY_DOMAINS dictionary to the template
    return render_template('index.html', security_domains=SECURITY_DOMAINS.keys())

@app.route('/generate-report', methods=['POST'])
def generate_report():
    """Generates the security policy and risk report based on form input."""
    client_name = request.form['client_name']
    business_goals = request.form['business_goals']
    selected_domains = request.form.getlist('security_domains')
    
    generated_policy = []
    generated_controls = []
    generated_risks = []
    
    # Loop through the selected domains and pull the relevant data
    for domain in selected_domains:
        if domain in SECURITY_DOMAINS:
            generated_policy.extend(SECURITY_DOMAINS[domain]["policy_statements"])
            generated_controls.extend(SECURITY_DOMAINS[domain]["technical_controls"])
            generated_risks.extend(SECURITY_DOMAINS[domain]["risk_checklist"])

    return render_template(
        'report.html',
        client_name=client_name,
        business_goals=business_goals,
        policy=generated_policy,
        controls=generated_controls,
        risks=generated_risks
    )

if __name__ == '__main__':
    app.run(debug=True)
