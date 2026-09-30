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
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333333;
            line-height: 1.6;
            font-size: 10.5pt;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #34495e;
            color: #ecf0f1;
            padding: 25px;
            border-bottom: 5px solid #e74c3c;
            margin-bottom: 25px;
            border-radius: 4px;
        }
        .header h1 {
            margin: 0 0 5px 0;
            font-size: 24pt;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .header p {
            margin: 0;
            font-size: 10.5pt;
            color: #bdc3c7;
        }
        h2 {
            color: #2c3e50;
            font-size: 14pt;
            border-bottom: 2px solid #e74c3c;
            padding-bottom: 5px;
            margin-top: 25px;
            margin-bottom: 15px;
            page-break-after: avoid;
        }
        .policy-box {
            background-color: #ffffff;
            border-left: 4px solid #34495e;
            padding: 12px 15px;
            margin-bottom: 15px;
            border-radius: 0 4px 4px 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            page-break-inside: avoid;
        }
        .policy-box strong {
            display: block;
            color: #2c3e50;
            font-size: 11pt;
            margin-bottom: 4px;
        }
        .alert {
            background-color: #fdedec;
            border: 1px solid #e74c3c;
            padding: 12px 15px;
            margin: 15px 0;
            color: #c0392b;
            font-weight: 500;
            page-break-inside: avoid;
            border-radius: 4px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            background-color: #ffffff;
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #bdc3c7;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #ecf0f1;
            color: #2c3e50;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
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
        <h1>Disciplinary & Grievance Policy</h1>
        <p>Document Ref: HR-POL-015 | Effective: March 2027</p>
    </div>

    <p>TechV-Flash is committed to maintaining a fair, transparent, and productive work environment. This policy outlines the framework for addressing employee grievances and detailing the disciplinary actions for misconduct, ensuring natural justice and due process.</p>

    <h2>1. Employee Grievance Redressal</h2>
    <p>Employees are encouraged to raise work-related concerns, interpersonal disputes (excluding POSH cases, which fall under HR-POL-010), or policy misapplications without fear of retaliation.</p>
    
    <div class="policy-box">
        <strong>1.1 Escalation Matrix for Grievances</strong>
        <ul>
            <li><strong>Level 1 (Reporting Manager):</strong> The employee must first attempt to resolve the issue with their direct manager. A written response is required within 5 business days.</li>
            <li><strong>Level 2 (HR Business Partner):</strong> If unresolved at Level 1, the employee can escalate to their HRBP. HR will mediate and provide a resolution within 10 business days.</li>
            <li><strong>Level 3 (Grievance Redressal Committee - GRC):</strong> For severe or unresolved disputes, the matter is escalated to the GRC (comprising the Dept Head, Head of HR, and Legal Counsel). The GRC's decision is final and binding.</li>
        </ul>
    </div>

    <!-- Section 1 continued -->
    <div class="page-break"></div>
    <h3>1.2 Grievance Resolution Milestones & SLAs</h3>
    <table>
        <tr>
            <th>Grievance Level</th>
            <th>Primary Action Authority</th>
            <th>Maximum Investigation SLA</th>
            <th>Escalation Authority</th>
        </tr>
        <tr>
            <td>Level 1 (Reporting Manager)</td>
            <td>Direct Supervisor / Lead</td>
            <td>5 Business Days from submission</td>
            <td>HR Business Partner (Level 2)</td>
        </tr>
        <tr>
            <td>Level 2 (HRBP Review)</td>
            <td>Assigned HRBP</td>
            <td>10 Business Days from escalation</td>
            <td>Grievance Committee (Level 3)</td>
        </tr>
        <tr>
            <td>Level 3 (GRC Hearing)</td>
            <td>Grievance Committee Panel</td>
            <td>15 Business Days from escalation</td>
            <td>CEO Office (Final Board review)</td>
        </tr>
    </table>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Categories of Misconduct</h2>
    <table>
        <tr>
            <th>Category</th>
            <th>Examples</th>
            <th>Standard Consequence</th>
        </tr>
        <tr>
            <td>Minor Misconduct</td>
            <td>Chronic lateness, unauthorized casual absences, minor insubordination, failure to comply with the dress code.</td>
            <td>Verbal Warning, followed by a First Written Warning.</td>
        </tr>
        <tr>
            <td>Major Misconduct</td>
            <td>Breach of IT Security (HR-POL-007), negligent damage to company property, misuse of travel allowances.</td>
            <td>Final Written Warning, potential suspension, or demotion.</td>
        </tr>
        <tr>
            <td>Gross Misconduct</td>
            <td>Fraud, theft, physical violence, gross data privacy breach (LEG-POL-008), intoxication on the premises.</td>
            <td>Immediate termination without notice (Summary Dismissal).</td>
        </tr>
    </table>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Disciplinary Procedure</h2>
    <div class="policy-box">
        <strong>3.1 Show Cause Notice</strong>
        Before any formal disciplinary action (beyond a verbal warning) is taken, the employee will be issued a written "Show Cause Notice" detailing the allegations. The employee has 48 hours to provide a written explanation.
    </div>
    
    <div class="policy-box">
        <strong>3.2 Disciplinary Hearing</strong>
        If the written explanation is unsatisfactory, a formal hearing is convened. The employee has the right to present evidence and may be accompanied by one internal colleague (acting as an observer).
    </div>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Suspension Pending Inquiry</h2>
    <div class="alert">
        <strong>Administrative Suspension:</strong> In cases of suspected Gross Misconduct (e.g., financial fraud, severe data breach), TechV-Flash reserves the right to suspend the employee with immediate effect pending a full investigation. 
        <br><br>
        During this suspension period (maximum 30 days), the employee will receive 50% of their Basic Salary as a subsistence allowance. If exonerated, the remaining balance will be paid in full. If found guilty, employment is terminated from the date of initial suspension.
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Mandate & Composition of Disciplinary Committee</h2>
    <div class="policy-box">
        <strong>5.1 Standing Panel Members</strong>
        The Disciplinary Committee is a standing body convened to hear cases of Major or Gross Misconduct. The panel comprises three voting members: the HR Director, the Chief Legal Officer, and an independent Department Head from outside the respondent's division.
    </div>
    <div class="policy-box">
        <strong>5.2 Quorum Rules</strong>
        No hearing can proceed without the physical or secure virtual presence of all three committee members. The legal counsel acts as the secretary, documenting minutes but does not hold voting rights on findings.
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Investigation & Evidence Collection Protocol</h2>
    <div class="policy-box">
        <strong>6.1 Accessing Workspace Activity Logs</strong>
        During investigations of data leakage, software piracy, or fraud, the security team is authorized to extract server logs, code repositories history, and Slack communication logs.
    </div>
    <div class="policy-box">
        <strong>6.2 Witness Deposition Guidelines</strong>
        Witnesses called to depose before the committee are protected under the non-retaliation clause. Depositions are recorded digitally and signed by the witness to ensure integrity.
    </div>

    <h3>6.3 Table of Evidence Integrity Checklist</h3>
    <table>
        <tr>
            <th>Evidence Category</th>
            <th>Collection Method</th>
            <th>Chain of Custody Owner</th>
            <th>Security Classification</th>
        </tr>
        <tr>
            <td>Digital Logs & Files</td>
            <td>MDM server pull, database audit export, repository hash matching.</td>
            <td>IT Security HOD</td>
            <td>Restricted (Encryption mandatory)</td>
        </tr>
        <tr>
            <td>Written Statements / Depositions</td>
            <td>Signed statement template, secure video recording.</td>
            <td>HR Investigation Lead</td>
            <td>Confidential</td>
        </tr>
        <tr>
            <td>Physical Assets</td>
            <td>Device confiscation, physical inventory tags.</td>
            <td>Admin Manager</td>
            <td>Internal Use Only</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Right to Appeal & Appeal Committee</h2>
    <div class="policy-box">
        <strong>7.1 Filing an Appeal</strong>
        Employees disciplined or terminated under this policy have the right to file an appeal. The written appeal must be submitted to the CEO's Office within 10 calendar days of receiving the final committee report.
    </div>
    <div class="policy-box">
        <strong>7.2 Appeal Committee Mandate</strong>
        The Appeal Committee is chaired directly by the CEO or a designated Board Member. The committee reviews the investigation records to ensure due process and releases their decision within 15 working days. The appeal outcome is final.
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Conflict Resolution & Mediation Services</h2>
    <div class="policy-box">
        <strong>8.1 Voluntary Mediation Cadence</strong>
        For interpersonal team disputes that do not violate code of conduct clauses, HR promotes voluntary mediation. Sessions are led by a neutral HR facilitator to help resolve workspace friction.
    </div>
    <div class="policy-box">
        <strong>8.2 Role of External Mediators</strong>
        If internal mediation fails to resolve executive or department-level conflicts, the company may retain an external mediator. All discussions in mediation are confidential.
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Handling Whistleblower Reports</h2>
    <div class="policy-box">
        <strong>9.1 Intake and Anonymity Protocols</strong>
        Reports submitted via whistleblower channels are routed directly to the Audit Committee. IP logging is disabled on the intake portal to guarantee reporter anonymity.
    </div>
    <div class="policy-box">
        <strong>9.2 Investigation Responsibility</strong>
        Whistleblower allegations concerning financial theft or executive fraud are investigated by an external forensic auditing firm under the supervision of the Board of Directors.
    </div>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Disciplinary Records & HR File Log</h2>
    <div class="policy-box">
        <strong>10.1 Active Warning Periods</strong>
        Written warnings remain active in the employee's HR file for 12 months. If no further disciplinary actions occur, the warning status transitions to "expired" but remains in historical records.
    </div>

    <h3>10.2 Table of Disciplinary Records Retention Slabs</h3>
    <table>
        <tr>
            <th>Record Category / Severity</th>
            <th>Active File Duration</th>
            <th>Automatic Removal Option</th>
            <th>Future Employer Disclosure Policy</th>
        </tr>
        <tr>
            <td>Verbal Warning Summary</td>
            <td>6 Months</td>
            <td>Yes (Archived from active profile)</td>
            <td>Do Not Disclose</td>
        </tr>
        <tr>
            <td>Written / Final Written Warning</td>
            <td>12 Months</td>
            <td>No (Permanent entry in profile)</td>
            <td>Confirm status upon formal BGV request only</td>
        </tr>
        <tr>
            <td>Summary Dismissal (Gross Misconduct)</td>
            <td>Permanent Record</td>
            <td>No</td>
            <td>Explicitly state termination reason to BGV agencies</td>
        </tr>
    </table>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Anti-Retaliation Policy for Grievances</h2>
    <div class="policy-box">
        <strong>11.1 Protecting Complainants</strong>
        TechV-Flash maintains a zero-tolerance policy for retaliation against employees who raise grievances or participate in investigations. Retaliation includes negative task reassignments, salary freezes, or workspace exclusion.
    </div>
    <div class="policy-box">
        <strong>11.2 Post-Resolution Monitoring</strong>
        HR Business Partners are required to check in with grievance complainants at 30, 90, and 180 days post-resolution to verify that no retaliatory actions have occurred.
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Disciplinary_Grievance_Policy.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")