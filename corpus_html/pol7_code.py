import os
from xhtml2pdf import pisa

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        @page {
            size: A4;
            margin: 20mm;
            background-color: #ffffff;
            @frame footer {
                -pdf-frame-content: footer_content;
                bottom: 10mm;
                margin-left: 20mm;
                margin-right: 20mm;
                height: 10mm;
            }
        }
        body { font-family: 'Segoe UI', sans-serif; color: #2c3e50; line-height: 1.5; font-size: 10.5pt; margin: 0; }
        .header { background-color: #1a252f; color: #2ecc71; padding: 20px; border-bottom: 5px solid #27ae60; margin-bottom: 25px; }
        .header h1 { color: #ecf0f1; margin: 0 0 5px 0; font-size: 24pt; text-transform: uppercase; }
        .header p { margin: 0; font-size: 10pt; color: #bdc3c7; }
        h2 { color: #2980b9; font-size: 13pt; border-bottom: 2px solid #3498db; padding-bottom: 5px; margin-top: 25px; page-break-after: avoid; }
        .rule-box { background-color: #f8f9fa; border-left: 4px solid #e67e22; padding: 12px 15px; margin-bottom: 15px; page-break-inside: avoid; }
        .rule-box strong { display: block; color: #d35400; margin-bottom: 5px; font-size: 11pt; }
        .critical-alert { background-color: #fadbd8; border: 1px solid #e74c3c; color: #c0392b; padding: 15px; border-radius: 4px; margin: 20px 0; font-weight: bold; page-break-inside: avoid; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; background-color: #ffffff; page-break-inside: avoid; }
        th, td { border: 1px solid #bdc3c7; padding: 10px; text-align: left; font-size: 10pt; }
        th { background-color: #34495e; color: #ffffff; }
        .page-break {
            page-break-before: always;
        }
    </style>
</head>
<body>
    <div id="footer_content" style="text-align: right; font-family: 'Segoe UI', sans-serif; font-size: 10pt; color: #555;">
        Page <pdf:pagenumber>
    </div>

    <div class="header">
        <h1>IT & Information Security Policy</h1>
        <p>Document Ref: IT-POL-007 | Effective: July 2026</p>
    </div>
    <p>As a technology-driven organization, safeguarding TechV-Flash's intellectual property, client data, and internal systems is paramount. This policy applies to all employees, contractors, and interns using company-provisioned IT assets or accessing company networks.</p>
    
    <h2>1. Password & Authentication Protocols</h2>
    <div class="rule-box"><strong>1.1 Password Complexity Rules</strong>All system passwords must be at least 14 characters long, containing a mix of uppercase, lowercase, numbers, and special characters. Passwords must not contain personal details (e.g., names, birthdays).</div>
    <div class="rule-box"><strong>1.2 Mandatory Rotation & History</strong>Passwords must be updated every 90 days. The system will restrict users from reusing any of their last 5 previous passwords.</div>
    <div class="rule-box"><strong>1.3 Multi-Factor Authentication (MFA)</strong>MFA is strictly enforced across all TechV-Flash applications (Google Workspace, AWS, GitHub, HR Portal). Authenticator apps (e.g., Google Authenticator, Authy) are permitted. SMS-based OTPs are prohibited due to SIM-swapping vulnerabilities.</div>
    
    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Hardware & Device Management</h2>
    <div class="rule-box"><strong>2.1 Asset Allocation</strong>Employees are strictly forbidden from sharing their company-issued laptops, phones, or security keys with anyone, including family members. Hardware remains the sole property of TechV-Flash.</div>
    <div class="rule-box"><strong>2.2 BYOD (Bring Your Own Device) Limitations</strong>Personal devices may only be used to access company email and Microsoft Teams, provided Mobile Device Management (MDM) software is installed. Source code and client databases must never be downloaded to personal devices.</div>
    <div class="critical-alert">Incident Reporting Timeline: Any loss, theft, or suspected compromise of a TechV-Flash device must be reported to the IT Helpdesk (it-sec@techv-flash.com) within 2 hours of discovery. Failure to report promptly will result in disciplinary action.</div>
    
    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Network Security & VPN</h2>
    <div class="rule-box"><strong>3.1 VPN Mandate for Remote Work</strong>When working remotely (as per HR-POL-003), employees must be connected to the TechV-Flash corporate VPN at all times before accessing internal servers, staging environments, or client data.</div>
    <div class="rule-box"><strong>3.2 Public Wi-Fi Restrictions</strong>Accessing company resources over unsecured public Wi-Fi networks (e.g., airports, coffee shops) without the VPN is classified as a critical security violation.</div>
    
    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Data Classification</h2>
    <p>All data processed by TechV-Flash is categorized into four tiers. Handling requirements depend on the tier:</p>
    <table>
        <tr><th>Classification</th><th>Description</th><th>Examples</th><th>Sharing Rules</th></tr>
        <tr><td>Public</td><td>Information meant for general consumption.</td><td>Marketing materials, Press releases</td><td>No restrictions.</td></tr>
        <tr><td>Internal Use</td><td>Company operations info, not for external release.</td><td>Organizational charts, Intranet pages</td><td>Share only with TechV-Flash staff.</td></tr>
        <tr><td>Confidential</td><td>Sensitive business data requiring protection.</td><td>Financial reports, Source code, Vendor contracts</td><td>Need-to-know basis internally; NDA required externally.</td></tr>
        <tr><td>Restricted</td><td>Highly sensitive PII or client data subject to regulations.</td><td>Employee passwords, Client databases, PHI</td><td>Strictly limited to authorized personnel only. Encryption mandatory.</td></tr>
    </table>
    
    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Software Installation & "Shadow IT"</h2>
    <div class="rule-box"><strong>5.1 Administrator Privileges</strong>Standard employee accounts do not possess local administrative rights. Software installations must be requested via the IT Service Portal.</div>
    <div class="rule-box"><strong>5.2 Prohibition of Unauthorized Tools</strong>The use of unapproved third-party applications or SaaS tools ("Shadow IT") for company business is strictly forbidden. This includes unauthorized Generative AI tools where confidential code might be pasted.</div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Remote Work Infrastructure & Physical Security</h2>
    <div class="rule-box"><strong>6.1 Clean Desk and Workstation Security</strong>When working in open offices or remote spaces, employees must lock their screens (`Win + L` or `Cmd + Ctrl + Q`) before leaving the workstation. Hard copies containing confidential data must be filed in lockable drawers.</div>
    <div class="rule-box"><strong>6.2 Home Office Security Standards</strong>Remote workers must ensure that smart home assistant devices (e.g., Alexa, Google Home) are disabled or muted in rooms where confidential work discussions are conducted.</div>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Social Engineering & Phishing Prevention</h2>
    <div class="rule-box"><strong>7.1 Security Training Obligation</strong>All employees must participate in quarterly cybersecurity awareness and social engineering training. Critical modules cover spoofed emails, social engineering calls, and identity validation.</div>
    <div class="rule-box"><strong>7.2 Simulated Phishing Exercises</strong>IT Security conducts unannounced simulated phishing tests. Repeated failure (clicking malicious links, inputting credentials in tests) triggers mandatory review and administrative actions.</div>

    <h3>7.3 Table of Phishing Drill Consequences</h3>
    <table>
        <tr>
            <th>Fail Cycle Frequency</th>
            <th>Immediate Consequence</th>
            <th>Required Remediation</th>
            <th>HR File Status</th>
        </tr>
        <tr>
            <td>First Failure</td>
            <td>Notification from Security Team</td>
            <td>Online micro-learning course (15 mins)</td>
            <td>No Entry</td>
        </tr>
        <tr>
            <td>Second Failure (within 12 months)</td>
            <td>Manager Notified</td>
            <td>Assigned Security Bootcamp (1 hour)</td>
            <td>Logged as Warning</td>
        </tr>
        <tr>
            <td>Third Failure (within 12 months)</td>
            <td>Local Admin privileges revoked</td>
            <td>In-person Security Interview with DPO</td>
            <td>Written Disciplinary Record</td>
        </tr>
    </table>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Cryptographic Standards & Data Transfer</h2>
    <div class="rule-box"><strong>8.1 Symmetric Encryption</strong>Restricted database files and corporate backup bundles must be encrypted using AES-256 standard before transfer or storage on third-party cloud containers.</div>
    <div class="rule-box"><strong>8.2 Shared Transmission Channels</strong>Confidential and Restricted data must only be transmitted through approved company channels (e.g., authenticated SFTP servers, OneDrive with link validation). Email attachments for Restricted documents are prohibited.</div>

    <h3>8.3 Table of Approved File Transfer & Cryptographic Tools</h3>
    <table>
        <tr>
            <th>Data Tier Category</th>
            <th>Approved File Transfer Tool</th>
            <th>Minimum Encryption Protocol</th>
            <th>Authorization Required</th>
        </tr>
        <tr>
            <td>Internal Use</td>
            <td>Google Drive (Standard sharing)</td>
            <td>TLS 1.2 in transit</td>
            <td>None (All staff accessible)</td>
        </tr>
        <tr>
            <td>Confidential</td>
            <td>OneDrive (Password-protected link)</td>
            <td>AES-256 at rest & TLS 1.3</td>
            <td>Manager Approval</td>
        </tr>
        <tr>
            <td>Restricted</td>
            <td>Secure SFTP Server / AWS S3 KMS</td>
            <td>AES-256 with KMS key controls</td>
            <td>Security Officer sign-off</td>
        </tr>
    </table>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Vulnerability Management & Access Reviews</h2>
    <div class="rule-box"><strong>9.1 Device Patching Schedule</strong>All endpoint devices must keep auto-updates active. Critical security patches pushed by the corporate Mobile Device Management (MDM) software must be installed within 48 hours of publication.</div>
    <div class="rule-box"><strong>9.2 Access Audits</strong>Department heads must conduct access audits quarterly to review employee privileges on repository codes, AWS roles, and customer databases, following the principle of Least Privilege.</div>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Incident Response & Disaster Recovery</h2>
    <div class="rule-box"><strong>10.1 Incident Triage Matrix</strong>Cybersecurity incidents are classified into severity levels by the Incident Response (IR) team. SLAs for resolution and customer notification depend on these classes.</div>

    <h3>10.2 Table of Incident Severity Levels & SLAs</h3>
    <table>
        <tr>
            <th>Severity Class</th>
            <th>Definition / Impact Area</th>
            <th>Incident Response SLA</th>
            <th>Resolution Target SLA</th>
        </tr>
        <tr>
            <td>Severity 1 (Critical)</td>
            <td>Active data breach, root credentials compromised, customer database leaked.</td>
            <td>Immediate (Within 15 minutes)</td>
            <td>Under 6 Hours</td>
        </tr>
        <tr>
            <td>Severity 2 (High)</td>
            <td>Individual system compromise, phishing email click with credentials entered.</td>
            <td>Within 1 Hour</td>
            <td>Under 24 Hours</td>
        </tr>
        <tr>
            <td>Severity 3 (Medium/Low)</td>
            <td>Loss of offline laptop with active BitLocker, policy bypass without data access.</td>
            <td>Within 4 Hours</td>
            <td>Under 72 Hours</td>
        </tr>
    </table>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Termination & Asset Deprovisioning</h2>
    <div class="rule-box"><strong>11.1 Privilege Deactivation Timeline</strong>Upon notification of resignation or termination, IT Security schedules privilege deactivation. On the last working day at the exit time, all company application access (Google, Slack, GitHub) will be deactivated immediately.</div>
    <div class="rule-box"><strong>11.2 Asset Reclamation & Wipe</strong>Returned laptops are held in quarantine for 15 days for legal review if required. Subsequently, the device storage undergoes a secure multi-pass data wipe compliant with DoD 5220.22-M standards before reissue.</div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_IT_Security_Policy_v2.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")
