# app.py
from flask import Flask, render_template, request
from asprg_data import FRAMEWORKS

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Renders the main form for client input."""
    # Pass the keys of the top-level FRAMEWORKS dictionary to the template
    return render_template('index.html', frameworks=FRAMEWORKS.keys(), frameworks_data=FRAMEWORKS)

@app.route('/generate-report', methods=['POST'])
def generate_report():
    """Generates the security policy and risk report based on form input."""
    client_name = request.form['client_name']
    business_goals = request.form['business_goals']
    selected_framework = request.form['framework_selection']
    selected_domains = request.form.getlist('security_domains')
    
    generated_policy = []
    generated_controls = []
    generated_risks = []
    
    # Loop through the selected domains and pull the relevant data for the chosen framework
    if selected_framework in FRAMEWORKS:
        for domain in selected_domains:
            if domain in FRAMEWORKS[selected_framework]["domains"]:
                generated_policy.extend(FRAMEWORKS[selected_framework]["domains"][domain]["policy_statements"])
                generated_controls.extend(FRAMEWORKS[selected_framework]["domains"][domain]["technical_controls"])
                generated_risks.extend(FRAMEWORKS[selected_framework]["domains"][domain]["risk_checklist"])

    return render_template(
        'report.html',
        client_name=client_name,
        business_goals=business_goals,
        framework_name=selected_framework,
        policy=generated_policy,
        controls=generated_controls,
        risks=generated_risks
    )

if __name__ == '__main__':
    app.run(debug=True)
