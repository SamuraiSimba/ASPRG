# asprg_data.py

# This dictionary serves as the core knowledge base for the tool.
# It contains security domains with associated policies, controls, and risks.
# The keys (e.g., "Access Management") are the domains, and the values are
# dictionaries containing the policy statements, technical controls, and a risk checklist.

SECURITY_DOMAINS = {
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
    },
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
