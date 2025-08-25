# asprg_data.py

# This dictionary serves as the core knowledge base for the tool.
# Each key represents a different compliance framework.

FRAMEWORKS = {
    "General Privacy": {
        "description": "General best practices and policies for data privacy.",
        "domains": {
            "Data Protection": {
                "policy_statements": [
                    "All sensitive data must be encrypted in transit and at rest.",
                    "Data classification standards must be applied to all corporate data.",
                    "Regular backups of critical data must be performed and tested."
                ],
                "technical_controls": [
                    "Deploy disk encryption on all endpoints and servers that store sensitive data.",
                    "Utilize SSL/TLS for all network traffic containing sensitive information.",
                    "Implement automated backup solutions with a defined retention schedule."
                ],
                "risk_checklist": [
                    "Is sensitive customer data encrypted at all stages?",
                    "Are backup procedures regularly tested to ensure data can be restored?",
                    "Is there a clear data classification policy in place?"
                ]
            },
            "Incident Response": {
                "policy_statements": [
                    "A formal Incident Response Plan must be in place and communicated to all relevant employees.",
                    "All security incidents must be reported and documented within 24 hours.",
                    "Regular tabletop exercises must be conducted to test the effectiveness of the plan."
                ],
                "technical_controls": [
                    "Implement a Security Information and Event Management (SIEM) system for centralized logging.",
                    "Establish a clear communication plan for internal and external stakeholders during an incident.",
                    "Deploy a threat detection and response solution across the corporate network."
                ],
                "risk_checklist": [
                    "Do we have a documented Incident Response Plan?",
                    "Are employees aware of how to report a security incident?",
                    "Are our logging systems sufficient for forensic analysis?"
                ]
            }
        }
    },
    "PCI DSS": {
        "description": "Payment Card Industry Data Security Standard for handling cardholder data.",
        "domains": {
            "Access Management": {
                "policy_statements": [
                    "Access to cardholder data must be restricted on a business need-to-know basis.",
                    "All user access must be assigned a unique ID.",
                    "Administrative access must be secured with multi-factor authentication (MFA)."
                ],
                "technical_controls": [
                    "Implement access control systems that restrict physical access to cardholder data.",
                    "Enforce strong password policies that require a minimum length and complexity.",
                    "Automate user de-provisioning for all accounts within the Cardholder Data Environment (CDE)."
                ],
                "risk_checklist": [
                    "Are privileged accounts secured with MFA?",
                    "Is there a process to review and revoke access for departed employees?",
                    "Do we have a clear policy for user access to sensitive data?"
                ]
            },
            "Security Monitoring": {
                "policy_statements": [
                    "All system components within the Cardholder Data Environment must have audit logs enabled.",
                    "Audit logs must be reviewed at least daily.",
                    "Alerts must be generated for all critical security events."
                ],
                "technical_controls": [
                    "Implement a Security Information and Event Management (SIEM) system for centralized logging.",
                    "Utilize automated tools to review security logs for anomalies and suspicious activity.",
                    "Maintain logs for a minimum of one year."
                ],
                "risk_checklist": [
                    "Are audit logs enabled on all in-scope systems?",
                    "Are we regularly reviewing system logs for suspicious activity?",
                    "Is there a process to handle and respond to security alerts?"
                ]
            }
        }
    },
    "ISO 27001": {
        "description": "Information Security Management System framework.",
        "domains": {
            "Risk Assessment": {
                "policy_statements": [
                    "A formal risk assessment process must be in place to identify and mitigate information security risks.",
                    "Risks must be evaluated against the company's risk acceptance criteria.",
                    "All identified risks must have a designated owner and be regularly reviewed."
                ],
                "technical_controls": [
                    "Utilize a GRC platform to manage and track all identified risks.",
                    "Perform regular vulnerability scans and penetration testing.",
                    "Maintain a risk register that is accessible to relevant stakeholders."
                ],
                "risk_checklist": [
                    "Do we have a documented risk assessment methodology?",
                    "Is our risk register up-to-date?",
                    "Are stakeholders aware of their risk ownership responsibilities?"
                ]
            },
            "Access Management": {
                "policy_statements": [
                    "All access to corporate systems and data must be authorized and based on the principle of least privilege.",
                    "Multi-factor authentication (MFA) is required for all remote and administrative access.",
                    "User access rights must be reviewed on a quarterly basis."
                ],
                "technical_controls": [
                    "Implement a centralized Identity and Access Management (IAM) system.",
                    "Enforce strong password policies that require a minimum length and complexity.",
                    "Automate user de-provisioning upon termination of employment or change in role."
                ],
                "risk_checklist": [
                    "Are privileged accounts secured with MFA?",
                    "Is there a process to review and revoke access for departed employees?",
                    "Do we have a clear policy for user access to sensitive data?"
                ]
            }
        }
    }
}
