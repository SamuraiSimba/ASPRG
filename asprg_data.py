# asprg_data.py

# This dictionary serves as the core knowledge base for the tool.
# Each key represents a different compliance framework.

FRAMEWORKS = {
    "General Privacy": {
        "description": "General best practices and policies for data privacy.",
        "domains": {
            "Data Protection": {
                "policy_statements": [
                    {"text": "All sensitive data must be encrypted in transit and at rest.", "reference": "Internal Policy 1.2, Page 15"},
                    {"text": "Data classification standards must be applied to all corporate data.", "reference": "Internal Policy 1.1, Page 12"},
                    {"text": "Regular backups of critical data must be performed and tested.", "reference": "Internal Policy 3.4, Page 45"}
                ],
                "technical_controls": [
                    {"text": "Deploy disk encryption on all endpoints and servers that store sensitive data.", "reference": "Internal Procedure 2.1, Page 22"},
                    {"text": "Utilize SSL/TLS for all network traffic containing sensitive information.", "reference": "Internal Procedure 2.3, Page 25"},
                    {"text": "Implement automated backup solutions with a defined retention schedule.", "reference": "Internal Procedure 3.5, Page 47"}
                ],
                "risk_checklist": [
                    {"text": "Is sensitive customer data encrypted at all stages?", "reference": "Internal Audit Checklist, Q2"},
                    {"text": "Are backup procedures regularly tested to ensure data can be restored?", "reference": "Internal Audit Checklist, Q3"},
                    {"text": "Is there a clear data classification policy in place?", "reference": "Internal Audit Checklist, Q1"}
                ]
            },
            "Incident Response": {
                "policy_statements": [
                    {"text": "A formal Incident Response Plan must be in place and communicated to all relevant employees.", "reference": "Internal Policy 4.1, Page 50"},
                    {"text": "All security incidents must be reported and documented within 24 hours.", "reference": "Internal Policy 4.2, Page 52"},
                    {"text": "Regular tabletop exercises must be conducted to test the effectiveness of the plan.", "reference": "Internal Policy 4.3, Page 55"}
                ],
                "technical_controls": [
                    {"text": "Implement a Security Information and Event Management (SIEM) system for centralized logging.", "reference": "Internal Procedure 4.5, Page 60"},
                    {"text": "Establish a clear communication plan for internal and external stakeholders during an incident.", "reference": "Internal Procedure 4.6, Page 62"},
                    {"text": "Deploy a threat detection and response solution across the corporate network.", "reference": "Internal Procedure 4.7, Page 65"}
                ],
                "risk_checklist": [
                    {"text": "Do we have a documented Incident Response Plan?", "reference": "Internal Audit Checklist, Q4"},
                    {"text": "Are employees aware of how to report a security incident?", "reference": "Internal Audit Checklist, Q5"},
                    {"text": "Are our logging systems sufficient for forensic analysis?", "reference": "Internal Audit Checklist, Q6"}
                ]
            }
        }
    },
    "PCI DSS": {
        "description": "Payment Card Industry Data Security Standard for handling cardholder data.",
        "domains": {
            "Access Management": {
                "policy_statements": [
                    {"text": "Access to cardholder data must be restricted on a business need-to-know basis.", "reference": "PCI DSS 4.0 - Requirement 7.2.1, Page 65"},
                    {"text": "All user access must be assigned a unique ID.", "reference": "PCI DSS 4.0 - Requirement 8.2.1, Page 88"},
                    {"text": "Administrative access must be secured with multi-factor authentication (MFA).", "reference": "PCI DSS 4.0 - Requirement 8.3.1, Page 92"}
                ],
                "technical_controls": [
                    {"text": "Implement access control systems that restrict physical access to cardholder data.", "reference": "PCI DSS 4.0 - Requirement 9.1, Page 105"},
                    {"text": "Enforce strong password policies that require a minimum length and complexity.", "reference": "PCI DSS 4.0 - Requirement 8.3.2, Page 95"},
                    {"text": "Automate user de-provisioning for all accounts within the Cardholder Data Environment (CDE).", "reference": "PCI DSS 4.0 - Requirement 8.4.1, Page 98"}
                ],
                "risk_checklist": [
                    {"text": "Are privileged accounts secured with MFA?", "reference": "PCI DSS 4.0 - Requirement 8.3.1, Page 92"},
                    {"text": "Is there a process to review and revoke access for departed employees?", "reference": "PCI DSS 4.0 - Requirement 8.4.1, Page 98"},
                    {"text": "Do we have a clear policy for user access to sensitive data?", "reference": "PCI DSS 4.0 - Requirement 7.2.1, Page 65"}
                ]
            },
            "Security Monitoring": {
                "policy_statements": [
                    {"text": "All system components within the Cardholder Data Environment must have audit logs enabled.", "reference": "PCI DSS 4.0 - Requirement 10.2.1, Page 115"},
                    {"text": "Audit logs must be reviewed at least daily.", "reference": "PCI DSS 4.0 - Requirement 10.4.1, Page 120"},
                    {"text": "Alerts must be generated for all critical security events.", "reference": "PCI DSS 4.0 - Requirement 10.5.1, Page 125"}
                ],
                "technical_controls": [
                    {"text": "Implement a Security Information and Event Management (SIEM) system for centralized logging.", "reference": "PCI DSS 4.0 - Requirement 10.3, Page 118"},
                    {"text": "Utilize automated tools to review security logs for anomalies and suspicious activity.", "reference": "PCI DSS 4.0 - Requirement 10.4.1, Page 120"},
                    {"text": "Maintain logs for a minimum of one year.", "reference": "PCI DSS 4.0 - Requirement 10.6, Page 128"}
                ],
                "risk_checklist": [
                    {"text": "Are audit logs enabled on all in-scope systems?", "reference": "PCI DSS 4.0 - Requirement 10.2.1, Page 115"},
                    {"text": "Are we regularly reviewing system logs for suspicious activity?", "reference": "PCI DSS 4.0 - Requirement 10.4.1, Page 120"},
                    {"text": "Is there a process to handle and respond to security alerts?", "reference": "PCI DSS 4.0 - Requirement 10.5.1, Page 125"}
                ]
            }
        }
    },
    "ISO 27001": {
        "description": "Information Security Management System framework.",
        "domains": {
            "Risk Assessment": {
                "policy_statements": [
                    {"text": "A formal risk assessment process must be in place to identify and mitigate information security risks.", "reference": "ISO 27001 - 6.1.2, Page 22"},
                    {"text": "Risks must be evaluated against the company's risk acceptance criteria.", "reference": "ISO 27001 - 6.1.2, Page 22"},
                    {"text": "All identified risks must have a designated owner and be regularly reviewed.", "reference": "ISO 27001 - 8.2, Page 35"}
                ],
                "technical_controls": [
                    {"text": "Utilize a GRC platform to manage and track all identified risks.", "reference": "ISO 27001 - 6.1.2, Page 22"},
                    {"text": "Perform regular vulnerability scans and penetration testing.", "reference": "ISO 27001 - A.12.6.1, Page 78"},
                    {"text": "Maintain a risk register that is accessible to relevant stakeholders.", "reference": "ISO 27001 - 6.1.2, Page 22"}
                ],
                "risk_checklist": [
                    {"text": "Do we have a documented risk assessment methodology?", "reference": "ISO 27001 - 6.1.2, Page 22"},
                    {"text": "Is our risk register up-to-date?", "reference": "ISO 27001 - 8.2, Page 35"},
                    {"text": "Are stakeholders aware of their risk ownership responsibilities?", "reference": "ISO 27001 - 8.2, Page 35"}
                ]
            },
            "Access Management": {
                "policy_statements": [
                    {"text": "All access to corporate systems and data must be authorized and based on the principle of least privilege.", "reference": "ISO 27001 - A.9.2.1, Page 55"},
                    {"text": "Multi-factor authentication (MFA) is required for all remote and administrative access.", "reference": "ISO 27001 - A.9.4.1, Page 62"},
                    {"text": "User access rights must be reviewed on a quarterly basis.", "reference": "ISO 27001 - A.9.2.5, Page 58"}
                ],
                "technical_controls": [
                    {"text": "Implement a centralized Identity and Access Management (IAM) system.", "reference": "ISO 27001 - A.9.2.1, Page 55"},
                    {"text": "Enforce strong password policies that require a minimum length and complexity.", "reference": "ISO 27001 - A.9.2.1, Page 55"},
                    {"text": "Automate user de-provisioning upon termination of employment or change in role.", "reference": "ISO 27001 - A.9.2.5, Page 58"}
                ],
                "risk_checklist": [
                    {"text": "Are privileged accounts secured with MFA?", "reference": "ISO 27001 - A.9.4.1, Page 62"},
                    {"text": "Is there a process to review and revoke access for departed employees?", "reference": "ISO 27001 - A.9.2.5, Page 58"},
                    {"text": "Do we have a clear policy for user access to sensitive data?", "reference": "ISO 27001 - A.9.2.1, Page 55"}
                ]
            }
        }
    }
}
