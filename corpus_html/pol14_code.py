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
            color: #2c3e50;
            line-height: 1.6;
            font-size: 10.5pt;
            margin: 0;
            padding: 0;
        }
        .header {
            border-bottom: 3px solid #7f8c8d;
            padding-bottom: 15px;
            margin-bottom: 25px;
            text-align: right;
        }
        .header h1 {
            color: #2c3e50;
            margin: 0;
            font-size: 24pt;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .header p {
            margin: 5px 0 0 0;
            color: #34495e;
            font-size: 10pt;
            font-weight: bold;
        }
        h2 {
            color: #2c3e50;
            font-size: 13pt;
            background-color: #ecf0f1;
            padding: 8px 12px;
            margin-top: 25px;
            margin-bottom: 15px;
            border-left: 4px solid #34495e;
            page-break-after: avoid;
        }
        .policy-box {
            background-color: #ffffff;
            border: 1px solid #bdc3c7;
            padding: 15px;
            margin-bottom: 15px;
            page-break-inside: avoid;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        .policy-box strong {
            display: block;
            color: #2c3e50;
            margin-bottom: 5px;
            font-size: 11pt;
            border-bottom: 1px solid #ecf0f1;
            padding-bottom: 4px;
        }
        .alert {
            background-color: #fdf2e9;
            border-left: 5px solid #e67e22;
            padding: 12px 15px;
            margin: 15px 0;
            color: #d35400;
            font-size: 10pt;
            page-break-inside: avoid;
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
            font-size: 10pt;
        }
        th {
            background-color: #34495e;
            color: #ffffff;
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
        <h1>Resignation & Exit Policy</h1>
        <p>Document Ref: HR-POL-014 | Effective: February 2027</p>
    </div>

    <p>TechV-Flash strives to ensure a smooth, professional, and transparent offboarding process for employees transitioning out of the organization. This policy governs notice periods, clearance protocols, and final settlement timelines.</p>

    <h2>1. Notice Period Guidelines</h2>
    <div class="policy-box">
        <strong>1.1 Standard Notice Durations</strong>
        The notice period ensures sufficient time for Knowledge Transfer (KT) and replacement hiring. The mandatory notice durations are:
        <ul>
            <li><strong>Confirmed Full-Time Employees (L1 - L3):</strong> 60 Days</li>
            <li><strong>Confirmed Full-Time Employees (L4+):</strong> 90 Days</li>
            <li><strong>Employees on Probation:</strong> 15 Days (as per HR-POL-013)</li>
        </ul>
    </div>
    
    <div class="policy-box">
        <strong>1.2 Notice Period Buyout / Shortfall</strong>
        Notice period buyout (where the employee pays the company in lieu of serving the full notice) is not a guaranteed right. It is entirely at the discretion of the Department Head and HR. If approved, the unserved notice period will be deducted from the Full & Final settlement based on the employee's Basic Salary.
    </div>

    <div class="alert">
        <strong>Leave During Notice Period:</strong> Employees are not permitted to utilize Paid Time Off (PTO) or Casual Leaves while serving their notice period. Any absence due to a medical emergency must be supported by a medical certificate and will extend the last working day by the corresponding number of days.
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Separation Process & Clearance</h2>
    <div class="policy-box">
        <strong>2.1 Resignation Initiation</strong>
        All resignations must be formally submitted via the HR Management Portal. Emailed resignations will not trigger the official clearance workflow until logged in the system.
    </div>
    <div class="policy-box">
        <strong>2.2 Knowledge Transfer (KT) & Handover</strong>
        The resigning employee must submit a comprehensive KT document and obtain sign-off from their Reporting Manager at least 7 days prior to their last working day (LWD).
    </div>
    <div class="policy-box">
        <strong>2.3 IT & Asset Clearance</strong>
        All company-issued assets (laptops, ID badges, corporate credit cards) must be handed over to the IT Department by 3:00 PM on the LWD. Failure to return assets will freeze the Full & Final settlement and may lead to legal recovery actions.
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Full & Final (F&F) Settlement</h2>
    <p>The F&F settlement comprises pending salary, leave encashment, and any applicable deductions or clawbacks.</p>
    
    <table>
        <tr>
            <th>F&F Component</th>
            <th>Policy Rule</th>
        </tr>
        <tr>
            <td>Settlement Timeline</td>
            <td>Processed within 45 calendar days from the Last Working Day, subject to complete clearance.</td>
        </tr>
        <tr>
            <td>Leave Encashment</td>
            <td>Only unused carried-over PTO (up to the max limit of 5 days) will be encashed. Sick leaves lapse completely.</td>
        </tr>
        <tr>
            <td>Clawbacks</td>
            <td>Joining bonuses (if resigning within 12 months, per HR-POL-004) and L&D training costs (per HR-POL-012) will be auto-deducted from the final payout.</td>
        </tr>
        <tr>
            <td>Experience Letter</td>
            <td>Issued digitally within 72 hours of the successful processing of the F&F settlement.</td>
        </tr>
    </table>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Exit Interview</h2>
    <p>An exit interview with the HR Business Partner is mandatory. This confidential discussion is designed to gather constructive feedback about the employee's experience at TechV-Flash and does not impact their F&F settlement.</p>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Access Deactivation & Security Checklist</h2>
    <div class="policy-box">
        <strong>5.1 Identity Access Management (IAM) Deactivation</strong>
        IT security automatically revokes corporate email, repository access, and Single Sign-On (SSO) credentials at 6:00 PM on the LWD. Active sessions on all devices are terminated simultaneously.
    </div>
    <div class="policy-box">
        <strong>5.2 Access Card Revocation</strong>
        Physical building access cards must be handed over to the security desk at exit. Unreturned cards are charged at 500 INR, which is recovered in the exit settlement.
    </div>

    <h3>5.3 Table of Asset Clearance & Sign-off Checklist</h3>
    <table>
        <tr>
            <th>Asset Category</th>
            <th>Sign-off Authority</th>
            <th>Physical Handover Location</th>
            <th>Verification SLA</th>
        </tr>
        <tr>
            <td>Corporate Laptop & Chargers</td>
            <td>IT Helpdesk Officer</td>
            <td>IT Store Room (Floor 3)</td>
            <td>2 Hours (Immediate diagnostics run)</td>
        </tr>
        <tr>
            <td>Access Badges & Keys</td>
            <td>Office Admin / Security Lead</td>
            <td>Main Reception Gate</td>
            <td>Instant deactivation</td>
        </tr>
        <tr>
            <td>Corporate Credit Cards</td>
            <td>Finance & Accounting HOD</td>
            <td>Accounts Wing (Floor 4)</td>
            <td>24 Hours (Checking pending transactions)</td>
        </tr>
    </table>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Return of Company-Owned Vehicles & Housing</h2>
    <div class="policy-box">
        <strong>6.1 Corporate Car Handover</strong>
        Employees provided with company-leased vehicles must schedule a physical inspection with the Admin desk 5 days before LWD. Vehicles must be returned clean, along with all key sets, registration files, and insurance folders.
    </div>
    <div class="policy-box">
        <strong>6.2 Company Leased Accommodations</strong>
        Employees living in corporate guest houses or leased apartments must vacate the premises within 7 calendar days of their LWD. Extensions require HOD and HR Director approval.
    </div>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Gratuity & Pension Benefit Release</h2>
    <div class="policy-box">
        <strong>7.1 Gratuity Claim Submission</strong>
        Separating employees who have completed 5 years of continuous service must submit the statutory Form I to the HR payroll department. Gratuity payouts are processed along with the exit settlement.
    </div>
    <div class="policy-box">
        <strong>7.2 Employee Provident Fund (EPF) Transfer</strong>
        HR shares the member ID and Universal Account Number (UAN) to facilitate EPF transfer. Employees must initiate the transfer to their new employer via the EPFO portal.
    </div>

    <h3>7.3 Table of Gratuity & Retiral Payoff Timeline</h3>
    <table>
        <tr>
            <th>Retiral Benefit</th>
            <th>Service Eligibility</th>
            <th>Disbursement Processing SLA</th>
            <th>Disbursement Channel</th>
        </tr>
        <tr>
            <td>Provident Fund (EPF) withdrawal/transfer</td>
            <td>Minimum 1 month post-exit (unemployed)</td>
            <td>30 days from portal application</td>
            <td>Direct EPFO bank credit</td>
        </tr>
        <tr>
            <td>Gratuity Payout</td>
            <td>Minimum 5 years continuous service</td>
            <td>45 days from LWD (with F&F settlement)</td>
            <td>Company payroll bank transfer</td>
        </tr>
        <tr>
            <td>National Pension Scheme (NPS) transfer</td>
            <td>No minimum tenure (Corporate plan)</td>
            <td>15 days from corporate exit request</td>
            <td>Nodal office to personal PRAN account</td>
        </tr>
    </table>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Employee Health Insurance Coverage Transition</h2>
    <div class="policy-box">
        <strong>8.1 Coverage Termination Date</strong>
        Corporate Group Health Insurance (GHI) coverage for the employee and their dependents ends at midnight on the LWD. Active hospitalizations on the LWD are covered till discharge.
    </div>
    <div class="policy-box">
        <strong>8.2 Insurance Portability Option</strong>
        Employees can opt to migrate their corporate GHI plan to a retail plan with the same insurer without losing waiting-period benefits. Requests must be submitted directly to the insurer within 30 days of LWD.
    </div>

    <h3>8.3 Table of Post-Exit Benefit Transition</h3>
    <table>
        <tr>
            <th>Benefit Component</th>
            <th>Termination Date / Hour</th>
            <th>Portability/Action Window</th>
            <th>Required Employee Action</th>
        </tr>
        <tr>
            <td>Group Health Insurance</td>
            <td>Midnight on LWD</td>
            <td>30 Days from LWD</td>
            <td>Apply for portability directly with the insurer</td>
        </tr>
        <tr>
            <td>Term Life Insurance</td>
            <td>6:00 PM on LWD</td>
            <td>N/A (Lapses completely)</td>
            <td>None</td>
        </tr>
        <tr>
            <td>Corporate Discount perks</td>
            <td>6:00 PM on LWD</td>
            <td>N/A (Lapses completely)</td>
            <td>Deactivate personal accounts linked to corporate mail</td>
        </tr>
    </table>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Outplacement Assistance & Reference Requests</h2>
    <div class="policy-box">
        <strong>9.1 Outplacement Services Eligibility</strong>
        During redundancies or organizational restructures, TechV-Flash may sponsor outplacement agency services for affected employees for up to 3 months to assist in resume building and job searches.
    </div>
    <div class="policy-box">
        <strong>9.2 Verification of Employment History</strong>
        Background verification agencies seeking reference checks must send requests to verify@techvflash.com. The company shares only designation, tenure, and final clearance status.
    </div>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Alumni Network Enrollment</h2>
    <div class="policy-box">
        <strong>10.1 Alumni Portal Registration</strong>
        Departing employees in good standing are invited to register on the TechV-Flash Alumni Portal. The portal lists open jobs, industry insights, and networking events.
    </div>
    <div class="policy-box">
        <strong>10.2 Employee Referral Rewards for Alumni</strong>
        Alumni referring candidates for open roles at TechV-Flash are eligible for the standard employee referral rewards (HR-POL-013), paid out upon the candidate completing 90 days.
    </div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Non-Compete & Non-Solicitation Covenants</h2>
    <div class="policy-box">
        <strong>11.1 Non-Solicitation of Employees</strong>
        For a period of 12 months following their separation, departing employees must not solicit, recruit, or attempt to hire any active employee of TechV-Flash for external businesses.
    </div>
    <div class="policy-box">
        <strong>11.2 Non-Solicitation of Clients</strong>
        Exiting employees are restricted from soliciting business from any active client of TechV-Flash with whom they worked in the 12 months prior to their LWD, for a duration of 12 months post-separation.
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Resignation_Exit_Policy.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")