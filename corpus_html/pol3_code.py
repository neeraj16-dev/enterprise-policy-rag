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
            color: #212529;
            line-height: 1.6;
            font-size: 11pt;
            margin: 0;
        }
        .header {
            background-color: #2b5876;
            color: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header h1 { margin: 0 0 10px 0; font-size: 24pt; }
        .header p { margin: 0; font-size: 11pt; opacity: 0.9; }
        
        h2 {
            color: #2b5876;
            border-bottom: 2px solid #4e4376;
            padding-bottom: 5px;
            margin-top: 25px;
            page-break-after: avoid;
        }
        .rule-box {
            background: #ffffff;
            border-left: 4px solid #4e4376;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            page-break-inside: avoid;
        }
        .rule-box strong { color: #2b5876; display: block; margin-bottom: 5px; font-size: 11.5pt;}
        
        .warning {
            background-color: #fff3cd;
            border: 1px solid #ffe69c;
            color: #856404;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            page-break-inside: avoid;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            background-color: white;
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #dee2e6;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #e9ecef;
            color: #495057;
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
        <h1>Remote & Hybrid Work Policy</h1>
        <p>Document Ref: HR-POL-003 | Effective: March 2026</p>
    </div>

    <p>TechV-Flash is committed to providing flexibility while maintaining high levels of collaboration and productivity. This policy defines the operating guidelines for on-site, hybrid, and fully remote work models.</p>

    <h2>1. Work Models & Eligibility</h2>
    
    <div class="rule-box">
        <strong>1.1 Hybrid Model (Default)</strong>
        The standard operating model for TechV-Flash employees based within a 50km radius of the Pune HQ is Hybrid. Employees are required to work from the office a minimum of 3 days per week. Tuesdays and Thursdays are mandatory "Anchor Days" for in-person collaboration.
    </div>
    
    <div class="rule-box">
        <strong>1.2 Fully Remote Model</strong>
        Employees residing outside the 50km radius of a TechV-Flash office may be classified as Fully Remote. This status requires approval from the Department Head and HR. Remote employees must overlap at least 4 hours with the standard IST working day.
    </div>

    <div class="rule-box">
        <strong>1.3 Interns and Probationary Employees</strong>
        Interns and full-time employees in their 90-day probationary period are required to be on-site 5 days a week to facilitate onboarding, training, and integration, unless explicit written exemption is provided by the CEO, Neeraj Mayekar.
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Work-From-Anywhere (WFA) Allowance</h2>
    
    <p>To support global mobility, Hybrid employees are granted a "Work-From-Anywhere" allowance. This permits employees to work fully remotely from any domestic or international location for up to <strong>30 calendar days per year</strong>, subject to manager approval.</p>

    <div class="warning">
        <strong>Tax & Compliance Warning:</strong> WFA requests exceeding 30 days or involving international relocation must be reviewed by the Legal & Compliance team to avoid creating permanent establishment or unexpected tax liabilities for the company.
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Equipment & Setup Stipend</h2>
    
    <table>
        <tr>
            <th>Classification</th>
            <th>Hardware Provided</th>
            <th>One-time WFH Stipend</th>
            <th>Monthly Internet Allowance</th>
        </tr>
        <tr>
            <td>Hybrid</td>
            <td>Laptop, Charger, Headset</td>
            <td>15,000 INR</td>
            <td>1,000 INR</td>
        </tr>
        <tr>
            <td>Fully Remote</td>
            <td>Laptop, Dual Monitors, Headset</td>
            <td>30,000 INR</td>
            <td>2,000 INR</td>
        </tr>
    </table>
    <p><em>*Stipends are subject to expense submission and must be utilized within the first 60 days of employment or status change.</em></p>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Security & Confidentiality</h2>

    <div class="rule-box">
        <strong>4.1 Secure Networks</strong>
        Employees working remotely must connect through a secure, password-protected Wi-Fi network. Accessing company systems via public, unsecured Wi-Fi (e.g., cafes, airports) is strictly prohibited unless connected through the official TechV-Flash VPN.
    </div>

    <div class="rule-box">
        <strong>4.2 Physical Workspace Security</strong>
        Remote workstations must ensure visual privacy. Employees must lock their screens when stepping away and ensure unauthorized individuals (including family members) cannot view confidential company or client data.
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Workspace Ergonomics & Health</h2>
    
    <div class="rule-box">
        <strong>5.1 Furniture & Layout Standards</strong>
        To maintain long-term physical health, employees are advised to configure a dedicated workspace with an ergonomic chair, desk, and monitor positioned at eye level. Avoid working from beds, sofas, or layouts with insufficient back support.
    </div>

    <div class="rule-box">
        <strong>5.2 Ergonomic Assessment Process</strong>
        Employees experiencing physical discomfort or requiring ergonomic adjustments may request a virtual workspace evaluation by the Health & Safety team. Approved adjustments may qualify for additional equipment funding under the wellness program.
    </div>

    <h3>5.3 Table of Workspace Ergonomic Standards & Allowances</h3>
    <table>
        <tr>
            <th>Furniture / Equipment Item</th>
            <th>Recommended Standard</th>
            <th>Reimbursement Status</th>
            <th>Maximum Cap (INR)</th>
        </tr>
        <tr>
            <td>Ergonomic Office Chair</td>
            <td>Adjustable height, lumbar support, 3D armrests</td>
            <td>Eligible under One-time Stipend</td>
            <td>12,000 INR</td>
        </tr>
        <tr>
            <td>Adjustable Working Desk</td>
            <td>Min width 120cm, stable frame (standing optional)</td>
            <td>Eligible under One-time Stipend</td>
            <td>10,000 INR</td>
        </tr>
        <tr>
            <td>Monitor Arm / Stand</td>
            <td>Eye-level viewing angle adjustment</td>
            <td>Eligible under One-time Stipend</td>
            <td>3,000 INR</td>
        </tr>
        <tr>
            <td>Ergonomic Keyboard & Mouse</td>
            <td>Split keys, vertical wrist support</td>
            <td>Eligible under One-time Stipend</td>
            <td>5,000 INR</td>
        </tr>
    </table>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Communication Guidelines & SLAs</h2>

    <div class="rule-box">
        <strong>6.1 Tool Usage & Availability</strong>
        Our primary collaboration tools are Slack, Google Workspace, and Jira. Hybrid and Remote employees are expected to maintain active presence indicators and keep calendars updated during standard core business hours.
    </div>

    <div class="rule-box">
        <strong>6.2 Meeting Etiquette</strong>
        For all internal syncs and client reviews, video-on is highly encouraged to facilitate visual engagement. Use appropriate virtual backgrounds and ensure noise-canceling headsets are used in loud environments.
    </div>

    <h3>6.3 Table of Communication SLAs by Channel</h3>
    <table>
        <tr>
            <th>Communication Channel</th>
            <th>Nature of Query / Task</th>
            <th>Expected Response SLA</th>
            <th>Escalation Path</th>
        </tr>
        <tr>
            <td>Slack (Direct Messages)</td>
            <td>Ad-hoc questions, quick syncs</td>
            <td>Within 2 Hours (during Core Hours)</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>Slack (Incident Channels)</td>
            <td>Critical bugs, production issues</td>
            <td>Immediate (Within 15 Minutes)</td>
            <td>Department Head call</td>
        </tr>
        <tr>
            <td>Email (Internal)</td>
            <td>Status updates, general reports</td>
            <td>Within 24 Hours</td>
            <td>Slack DM reminder</td>
        </tr>
        <tr>
            <td>Jira Ticket Updates</td>
            <td>Task assignments, code reviews</td>
            <td>Within 1 Business Day</td>
            <td>Weekly Stand-up sync</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Expense Reimbursements & Internet Subsidies</h2>

    <div class="rule-box">
        <strong>7.1 Internet Subsidy Eligibility</strong>
        To support high-speed connectivity, the monthly internet allowance is provided to cover broadband bills. Employees must submit broadband invoices showing a minimum connection speed of 50 Mbps under their registered name to claim the monthly reimbursement.
    </div>

    <div class="rule-box">
        <strong>7.2 Non-reimbursable Home Expenses</strong>
        Operating costs like residential electricity, water, home repairs, heating, or personal mobile phone bills are not covered under the remote policy and are considered private employee expenses.
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Data Protection & GDPR/ISO 27001 Compliance</h2>

    <div class="rule-box">
        <strong>8.1 Device Security & Encryption</strong>
        All corporate laptops must have BitLocker or FileVault active. USB mass storage devices are blocked by default. Hard copies of documents containing customer or product metadata must be shredded immediately after use and never stored at home.
    </div>

    <div class="rule-box">
        <strong>8.2 Incident Reporting for Lost Assets</strong>
        In the event of a laptop theft, loss of access card, or suspicious software warnings on remote devices, the employee must report the incident to security@techvflash.com within 1 hour to initiate remote wipe sequences.
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Business Travel for Remote Employees</h2>

    <div class="rule-box">
        <strong>9.1 Mandatory Travel Cycles</strong>
        Fully Remote employees are required to travel to the Pune HQ for team-building, product planning reviews, or company events up to 4 times a year. Travel, accommodation, and food costs are fully covered by the corporate travel desk.
    </div>

    <div class="rule-box">
        <strong>9.2 Travel Booking Timelines</strong>
        To optimize cost structures, travel bookings must be initiated through the internal travel portal at least 21 days in advance for domestic flights. Last-minute bookings require written approval from the HOD.
    </div>

    <h3>9.3 Table of Travel Reimbursement Slabs</h3>
    <table>
        <tr>
            <th>Expense Category</th>
            <th>Standard Provision / Limit</th>
            <th>Required Approvals</th>
            <th>Receipts & Verification</th>
        </tr>
        <tr>
            <td>Domestic Flights</td>
            <td>Economy Class (Lowest Logical Fare)</td>
            <td>Manager Pre-approval</td>
            <td>Boarding Pass & Invoice</td>
        </tr>
        <tr>
            <td>Hotel Stay</td>
            <td>3-Star / Corporate Partner Tie-up</td>
            <td>Travel Desk Booking</td>
            <td>Hotel GST Invoice</td>
        </tr>
        <tr>
            <td>Daily Meal Allowance</td>
            <td>Up to 1,500 INR per day</td>
            <td>Standard Expense Claim</td>
            <td>Individual food receipts</td>
        </tr>
        <tr>
            <td>Local Commute</td>
            <td>Uber/Ola Corporate rides or local taxi</td>
            <td>Standard Expense Claim</td>
            <td>App receipt or manual bill</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Performance & Productivity Management</h2>

    <div class="rule-box">
        <strong>10.1 Key Performance Indicators (KPIs)</strong>
        Remote productivity is evaluated based on output quality, task completion velocity, and meeting SLAs, rather than minutes active on screen. Activity tracking or keystroke monitoring softwares are not used at TechV-Flash.
    </div>

    <div class="rule-box">
        <strong>10.2 Review of Hybrid / Remote Status</strong>
        If an employee's performance rating falls below expectations (Rating < 3.0), the company reserves the right to suspend Remote status and require the employee to work from the Pune HQ full-time for structured coaching.
    </div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Workplace Health Safety (Home Safety Assessment)</h2>

    <div class="rule-box">
        <strong>11.1 Safety Checklist</strong>
        Employees working from home must complete a self-assessment checklist annually. This includes confirming proper electrical grounding, absence of trailing cables across walkways, adequate ventilation, and working smoke detection systems.
    </div>

    <div class="rule-box">
        <strong>11.2 Liability Boundaries</strong>
        TechV-Flash's worker safety liability is strictly confined to injuries occurring during standard work hours inside the designated home office workspace. Injuries arising from general household activities are not covered by workplace injury insurance.
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Remote_Hybrid_Work_Policy.pdf"
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")