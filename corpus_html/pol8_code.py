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
            margin: 25mm 20mm;
            background-color: #faf9f6;
            @frame footer {
                -pdf-frame-content: footer_content;
                bottom: 10mm;
                margin-left: 20mm;
                margin-right: 20mm;
                height: 10mm;
            }
        }
        body { font-family: 'Georgia', serif; color: #2c3e50; line-height: 1.6; font-size: 10.5pt; margin: 0; }
        .header { border-bottom: 2px solid #8e44ad; padding-bottom: 15px; margin-bottom: 25px; }
        .header h1 { color: #8e44ad; margin: 0 0 5px 0; font-size: 24pt; font-family: 'Arial', sans-serif;}
        .header p { margin: 0; font-size: 10pt; color: #7f8c8d; font-family: 'Arial', sans-serif;}
        h2 { color: #2c3e50; font-size: 13pt; margin-top: 25px; border-left: 4px solid #8e44ad; padding-left: 10px; page-break-after: avoid; font-family: 'Arial', sans-serif;}
        .clause { background-color: #f9f6fa; border: 1px solid #d2b4de; padding: 12px 15px; margin-bottom: 12px; page-break-inside: avoid; border-radius: 4px;}
        .clause strong { display: block; color: #8e44ad; margin-bottom: 5px; font-family: 'Arial', sans-serif; font-size: 11pt; }
        .warning-box { background-color: #fdedec; border-left: 5px solid #e74c3c; padding: 12px; margin: 20px 0; font-size: 10pt; page-break-inside: avoid;}
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            background-color: #ffffff;
            page-break-inside: avoid;
            font-size: 10pt;
            font-family: 'Arial', sans-serif;
        }
        th, td {
            border: 1px solid #bdc3c7;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #8e44ad;
            color: #ffffff;
        }
        .page-break {
            page-break-before: always;
        }
    </style>
</head>
<body>
    <div id="footer_content" style="text-align: right; font-family: 'Arial', sans-serif; font-size: 10pt; color: #555;">
        Page <pdf:pagenumber>
    </div>

    <div class="header">
        <h1>Data Privacy Policy</h1>
        <p>Document Ref: LEG-POL-008 | Effective: August 2026</p>
    </div>
    <p>TechV-Flash respects the privacy rights of its employees, clients, and users. This policy aligns with the Digital Personal Data Protection (DPDP) Act of India and global standards such as the GDPR to ensure lawful data handling.</p>
    
    <h2>1. Scope and Definitions</h2>
    <div class="clause"><strong>1.1 Personal Identifiable Information (PII)</strong>PII refers to any data that can identify an individual, including but not limited to names, personal email addresses, phone numbers, and government-issued identification numbers (e.g., Aadhaar, PAN, SSN).</div>
    <div class="clause"><strong>1.2 Sensitive Personal Information (SPII)</strong>SPII includes financial records, biometric data, health and medical records, and passwords. SPII requires the highest level of encryption and strict access controls.</div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Data Collection & Processing Principles</h2>
    <div class="clause"><strong>2.1 Lawful Basis and Consent</strong>Data must only be collected for specified, legitimate business purposes. Explicit consent must be obtained from individuals before collecting their PII, unless another lawful basis applies (e.g., fulfillment of an employment contract).</div>
    <div class="clause"><strong>2.2 Data Minimization</strong>Employees must only collect the minimum amount of personal data necessary to accomplish a specific business objective. Storing excessive user data "just in case" is prohibited.</div>
    <div class="clause"><strong>2.3 Retention Limitations</strong>Personal data must not be kept longer than necessary. Candidate resumes must be purged from the recruitment database after 24 months unless the candidate explicitly opts in for a longer retention period.</div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Employee Obligations</h2>
    <div class="warning-box"><strong>Strict Prohibition on External Sharing:</strong> Employees must never share client PII or employee records with unauthorized third parties, external vendors, or unsecured AI transcription/summarization tools.</div>
    <div class="clause"><strong>3.1 Clean Desk and Screen Policy</strong>Physical documents containing PII must be shredded immediately after use or locked away. Screens displaying PII must be locked when unattended.</div>
    
    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Data Breach Notification</h2>
    <div class="clause"><strong>4.1 The 72-Hour Rule</strong>In the event of a suspected data breach, employees must immediately notify the Data Protection Officer (DPO) at dpo@techv-flash.com. TechV-Flash is legally obligated to report qualifying breaches to regulatory authorities within 72 hours of discovery.</div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Data Subject Rights (Rights of Data Principals)</h2>
    <div class="clause"><strong>5.1 Right to Access and Correction</strong>Individuals have the right to request a digital copy of all PII held by TechV-Flash. They also hold the right to demand correction of inaccurate records or completion of incomplete information.</div>
    <div class="clause"><strong>5.2 Right to Erasure (Right to be Forgotten)</strong>Data subjects can request the deletion of their personal database entries under specific circumstances (e.g., when the consent is withdrawn, or data is no longer necessary for original business purposes).</div>

    <h3>5.3 Table of Data Subject Request (DSR) Response SLAs</h3>
    <table>
        <tr>
            <th>DSR Request Type</th>
            <th>Standard Response SLA</th>
            <th>Maximum Extension Allowed</th>
            <th>Required Verification Details</th>
        </tr>
        <tr>
            <td>Access to personal data copies</td>
            <td>15 Calendar Days</td>
            <td>15 Days (With HOD notification)</td>
            <td>Government photo ID copy, email authentication</td>
        </tr>
        <tr>
            <td>Correction / Rectification</td>
            <td>10 Calendar Days</td>
            <td>None</td>
            <td>Official supporting documents (marriage certificate, PAN)</td>
        </tr>
        <tr>
            <td>Erasure / Deletion request</td>
            <td>30 Calendar Days</td>
            <td>15 Days (Legal review justification)</td>
            <td>Written request form signed, secondary OTP validation</td>
        </tr>
    </table>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Data Privacy Impact Assessments (DPIA)</h2>
    <div class="clause"><strong>6.1 Triggering DPIA Projects</strong>A DPIA is mandatory before launching new software development or product features that involve processing sensitive PII, large-scale biometric capture, or automated profiling.</div>
    <div class="clause"><strong>6.2 DPO Auditing Review</strong>The DPIA report must outline data protection risks, planned mitigation controls, and obtain final authorization from the Data Protection Officer (DPO) before deployment into production staging.</div>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Cross-Border Data Transfers</h2>
    <div class="clause"><strong>7.1 Statutory Adequacy Compliance</strong>Transferring PII outside the borders of India is strictly restricted to countries approved by the government under the DPDP Act rules. Transfers to other locations require pre-authorization or specific corporate bindings.</div>
    <div class="clause"><strong>7.2 Standard Contractual Clauses (SCC)</strong>All cross-border transfers to partner locations must be governed by Standard Contractual Clauses (SCCs) defining security controls and privacy obligations.</div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Third-Party Vendor Data Processing</h2>
    <div class="clause"><strong>8.1 Vendor Risk Assessment</strong>Before onboarding any SaaS tool or external consulting vendor, a privacy and compliance risk assessment must be completed. High-risk vendors require corporate security audits.</div>
    <div class="clause"><strong>8.2 Data Processing Agreements (DPA)</strong>All vendor contracts involving PII access must execute a DPA. This document legally binds the vendor to notify TechV-Flash of any breaches within 24 hours.</div>

    <h3>8.3 Table of Vendor Risk Ratings & Requirements</h3>
    <table>
        <tr>
            <th>Risk Class Rating</th>
            <th>Example Vendor Profile</th>
            <th>Mandatory Agreement / Security</th>
            <th>Audit Frequency</th>
        </tr>
        <tr>
            <td>High Risk</td>
            <td>Third-party payroll processors, cloud hosting services, customer database tools.</td>
            <td>Full DPA, AES-256 encryption, ISO 27001 certificate verification.</td>
            <td>Annual Security Audit</td>
        </tr>
        <tr>
            <td>Medium Risk</td>
            <td>Office administrative tools, recruitment boards, CRM platforms.</td>
            <td>Standard NDA, data retention clauses, data deletion guarantee.</td>
            <td>Bi-annual Risk Review</td>
        </tr>
        <tr>
            <td>Low Risk</td>
            <td>Office stationery suppliers, marketing agency list (public content only).</td>
            <td>Standard NDA.</td>
            <td>None</td>
        </tr>
    </table>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Employee Personal Data Processing</h2>
    <div class="clause"><strong>9.1 PII Collected from Employees</strong>TechV-Flash processes employee PII (academic records, financial accounts, address proofs) solely for employment contracting, payroll processing, and statutory tax compliance.</div>
    <div class="clause"><strong>9.2 Access Restrictions</strong>HR and Payroll records are restricted. Access is granted exclusively to HR managers and finance auditors on a need-to-know basis.</div>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Privacy by Design Principles</h2>
    <div class="clause"><strong>10.1 Pseudonymization and Masking</strong>Software engineers must ensure database records containing user contact details are masked or pseudonymized during application testing and QA development cycles.</div>
    <div class="clause"><strong>10.2 Default Privacy Configurations</strong>All product builds must deploy with privacy-first default settings, requiring users to explicitly opt in for supplementary profiling or newsletter mailings.</div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Compliance Audits & Training</h2>
    <div class="clause"><strong>11.1 Mandatory Annual Privacy Training</strong>All employees must complete the annual data privacy awareness course. Failure to complete this course within 30 days of release will restrict access to staging servers.</div>
    <div class="clause"><strong>11.2 Log Auditing and Non-compliance</strong>The security team logs database reads. Any unauthorized data extraction or non-compliance is subject to disciplinary action, including immediate termination.</div>

    <h3>11.3 Table of Data Retention Periods by Type</h3>
    <table>
        <tr>
            <th>Personal Data Category</th>
            <th>Statutory Retention Period</th>
            <th>Approved Disposal Method</th>
            <th>Primary Purpose / Justification</th>
        </tr>
        <tr>
            <td>FTE Employee HR Records</td>
            <td>7 Years post-separation</td>
            <td>Secure file shredding / digital record purging</td>
            <td>Tax audits and legal certification verification</td>
        </tr>
        <tr>
            <td>Recruitment Resumes (Rejected candidates)</td>
            <td>24 Months</td>
            <td>Digital database purging</td>
            <td>Talent pipeline mapping</td>
        </tr>
        <tr>
            <td>Customer Transaction Records</td>
            <td>8 Years</td>
            <td>Database archive & encryption</td>
            <td>Financial audit compliance under RBI guidelines</td>
        </tr>
    </table>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Data_Privacy_Policy.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")
