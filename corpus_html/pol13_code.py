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
            color: #2f3640;
            line-height: 1.6;
            font-size: 10.5pt;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #273c75;
            color: #f5f6fa;
            padding: 25px;
            border-radius: 6px;
            margin-bottom: 25px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .header h1 {
            margin: 0 0 5px 0;
            font-size: 24pt;
            letter-spacing: 0.5px;
            color: #ffffff;
        }
        .header p {
            margin: 0;
            font-size: 10.5pt;
            color: #dcdde1;
        }
        h2 {
            color: #273c75;
            font-size: 14pt;
            border-bottom: 2px solid #487eb0;
            padding-bottom: 5px;
            margin-top: 25px;
            margin-bottom: 15px;
            page-break-after: avoid;
        }
        .policy-section {
            background-color: #ffffff;
            border-left: 5px solid #487eb0;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            page-break-inside: avoid;
        }
        .policy-section strong {
            display: block;
            color: #2f3640;
            font-size: 11.5pt;
            margin-bottom: 6px;
        }
        .warning-box {
            background-color: #fdeaea;
            border: 1px solid #ff7979;
            color: #eb4d4b;
            padding: 12px 15px;
            border-radius: 4px;
            margin: 15px 0;
            page-break-inside: avoid;
            font-size: 10pt;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            background-color: #ffffff;
            page-break-inside: avoid;
            font-size: 10pt;
        }
        th, td {
            border: 1px solid #dcdde1;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f5f6fa;
            color: #273c75;
            font-weight: bold;
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
        <h1>Recruitment & Onboarding Policy</h1>
        <p>Document Ref: HR-POL-013 | Effective: January 2027 | Scope: Global Operations</p>
    </div>

    <p>TechV-Flash aims to attract, evaluate, and onboard top-tier talent through a transparent and compliant process. This policy dictates the standards for hiring, background verifications, document submission, and the probationary lifecycle.</p>

    <h2>1. Employee Referral Program</h2>
    <div class="policy-section">
        <strong>1.1 Referral Bonus Eligibility</strong>
        Active employees who refer a candidate successfully hired for a Full-Time role are eligible for a Referral Bonus of 25,000 INR for L1-L3 positions and 50,000 INR for L4+ positions. Intern conversions do not qualify for referral bonuses.
    </div>
    <div class="policy-section">
        <strong>1.2 Bonus Payout Timeline</strong>
        The referral bonus is disbursed in two tranches: 50% in the payroll cycle immediately following the new hire's joining date, and the remaining 50% upon the new hire's successful completion of their 90-day probationary period.
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Background Verification (BGV)</h2>
    <div class="policy-section">
        <strong>2.1 Mandatory Checks</strong>
        All offers of employment are contingent upon the successful completion of a comprehensive Background Verification (BGV). This includes education validation, criminal record checks, and employment history (for the past 5 years or last 2 employers, whichever is greater).
    </div>
    <div class="warning-box">
        <strong>Falsification of Records:</strong> Any discrepancy found during the BGV process, including forged experience letters, undisclosed terminations, or fake educational degrees, will lead to the immediate withdrawal of the offer letter or instant termination if the candidate has already joined.
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Day 1 Documentation</h2>
    <p>New hires must submit self-attested digital copies of the following documents to the HR portal at least 48 hours before their Date of Joining (DOJ). Original documents must be presented on Day 1 for visual verification.</p>
    <table>
        <tr>
            <th>Document Category</th>
            <th>Specific Requirements</th>
        </tr>
        <tr>
            <td>Identity & Address Proof</td>
            <td>Aadhaar Card, PAN Card, and Valid Passport (mandatory for international travel eligible roles).</td>
        </tr>
        <tr>
            <td>Educational Proofs</td>
            <td>Highest degree certificate and consolidated mark sheets.</td>
        </tr>
        <tr>
            <td>Previous Employment</td>
            <td>Relieving letter / Experience letter from the immediate past employer, and the last 3 months' payslips.</td>
        </tr>
        <tr>
            <td>Financial Info</td>
            <td>Cancelled cheque for salary account mapping.</td>
        </tr>
    </table>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Probationary Period</h2>
    <div class="policy-section">
        <strong>4.1 Duration and Confirmation</strong>
        All newly hired Full-Time Employees undergo a mandatory 90-day probationary period. At the end of 90 days, the manager will conduct a confirmation review. If performance is satisfactory, a formal Confirmation Letter will be issued. 
    </div>
    <div class="policy-section">
        <strong>4.2 Extension of Probation</strong>
        If performance metrics are not fully met, TechV-Flash reserves the right to extend the probationary period by an additional 30 to 60 days, during which time the employee will not be eligible for standard benefits such as the Annual Learning Allowance or internal transfers.
    </div>
    <div class="policy-section">
        <strong>4.3 Notice Period During Probation</strong>
        During the probationary period, either party (the employee or TechV-Flash) may terminate the employment contract by serving a written notice of 15 days, without assigning any specific reason.
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Recruitment Sourcing Channels & Guidelines</h2>
    <div class="policy-section">
        <strong>5.1 Sourcing Channels</strong>
        Candidate sourcing is managed via job portals, direct website applications, campus recruitment, and registered recruitment agencies. Direct listings on the company job board are the preferred sourcing channel.
    </div>
    <div class="policy-section">
        <strong>5.2 Sourcing Agency Engagement</strong>
        Engagement of external staffing agencies is permitted only when approved by the Talent Acquisition Head. Placement fees are governed by the Corporate Staffing Agreement.
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Candidate Interview & Assessment Protocol</h2>
    <div class="policy-section">
        <strong>6.1 Structure of Interview Rounds</strong>
        Hiring involves a structured process: resume screening, technical assessment, technical panel interview, and manager review. Critical engineering roles include a hands-on system coding round.
    </div>
    <div class="policy-section">
        <strong>6.2 Candidate Feedback SLAs</strong>
        Interview panels must submit written feedback scorecards via the recruitment system within 24 hours of completing the round. This ensures timely candidate updates.
    </div>

    <h3>6.3 Table of Interview Evaluation Matrix</h3>
    <table>
        <tr>
            <th>Interview Phase</th>
            <th>Primary Evaluated Focus Areas</th>
            <th>Minimum Score Target</th>
            <th>Required Panel Sign-offs</th>
        </tr>
        <tr>
            <td>Technical Assessment</td>
            <td>Problem-solving capabilities, algorithm speed, coding syntax correctness.</td>
            <td>70% on test portal</td>
            <td>Talent Acquisition Coordinator</td>
        </tr>
        <tr>
            <td>Technical Panel Round</td>
            <td>Architectural awareness, tech stack depth, design patterns.</td>
            <td>3.5 out of 5.0</td>
            <td>Two Senior Engineers / Tech Leads</td>
        </tr>
        <tr>
            <td>Manager / Culture Round</td>
            <td>Team collaboration, communication skills, adaptability.</td>
            <td>Pass / Fail check</td>
            <td>Department HOD / Engineering Director</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Offer Release & Negotiation Standards</h2>
    <div class="policy-section">
        <strong>7.1 Compensation Band Adherence</strong>
        Salary offers must align with defined corporate compensation bands. Exceptions require written approval from the Chief Financial Officer (CFO) and HR Director.
    </div>
    <div class="policy-section">
        <strong>7.2 Offer Validity and Acceptance</strong>
        Released offer letters are valid for 5 business days. Candidates must accept and submit their digital signatures on the portal within this timeline, or the offer is revoked.
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Onboarding Logistics & IT Setup</h2>
    <div class="policy-section">
        <strong>8.1 Email & Corporate Credentials</strong>
        IT Operations provisions corporate email accounts and security keys 48 hours prior to DOJ. Access cards are prepared and issued at the reception desk on Day 1.
    </div>
    <div class="policy-section">
        <strong>8.2 Hardware Shipping for Remote Hires</strong>
        Laptops and welcome kits for remote employees are shipped to their verified addresses, scheduled to arrive at least 1 day before the DOJ. Remote setups are coordinated by IT support.
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Relocation Support for New Hires</h2>
    <div class="policy-section">
        <strong>9.1 Travel & Logistics Reimbursement</strong>
        New hires relocating to the Pune HQ are eligible for travel support. Economy flights or train tickets are booked by the corporate travel desk.
    </div>

    <h3>9.2 Table of Candidate Travel Slabs for Interviews</h3>
    <table>
        <tr>
            <th>Outstation Location</th>
            <th>Approved Travel Mode</th>
            <th>Hotel Lodging Cap</th>
            <th>Meal per Diem Allowance</th>
        </tr>
        <tr>
            <td>Within 500 km radius</td>
            <td>AC 2-Tier Train / Bus</td>
            <td>3,000 INR per night (Max 2 nights)</td>
            <td>1,000 INR per day</td>
        </tr>
        <tr>
            <td>Above 500 km radius</td>
            <td>Economy Class Flight (Lowest fare)</td>
            <td>4,000 INR per night (Max 2 nights)</td>
            <td>1,200 INR per day</td>
        </tr>
        <tr>
            <td>International Locations</td>
            <td>Economy Class Flight (Manager approved)</td>
            <td>$120 USD per night (Max 3 nights)</td>
            <td>$60 USD per day</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Buddy Program & Onboarding Milestones</h2>
    <div class="policy-section">
        <strong>10.1 Onboarding Buddy Allocation</strong>
        To facilitate socialization, new hires are paired with an onboarding buddy from a neighboring team. Buddies help navigate office logistics and introducing company culture.
    </div>

    <h3>10.2 Table of New Hire Milestones & SLAs</h3>
    <table>
        <tr>
            <th>Milestone Target</th>
            <th>Required Action Item</th>
            <th>Primary Responsible Owner</th>
            <th>Verification Checklist Target</th>
        </tr>
        <tr>
            <td>Day 1</td>
            <td>Document verification, hardware setup, security keys provisioning.</td>
            <td>HR Operations & IT Helpdesk</td>
            <td>Access card and laptop active</td>
        </tr>
        <tr>
            <td>Day 30</td>
            <td>SMART KPI goals definition, project training modules completion.</td>
            <td>Reporting Manager & New Hire</td>
            <td>KPIs logged in HR portal</td>
        </tr>
        <tr>
            <td>Day 60</td>
            <td>Mid-probation review, checking task completions and feedback.</td>
            <td>Reporting Manager</td>
            <td>Progress report filed in portal</td>
        </tr>
        <tr>
            <td>Day 90</td>
            <td>Final probationary appraisal, confirmation scorecard submission.</td>
            <td>Reporting Manager & HRBP</td>
            <td>Confirmation letter generated</td>
        </tr>
    </table>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Induction Training & Core Values</h2>
    <div class="policy-section">
        <strong>11.1 Day 1 Corporate Induction</strong>
        The HR team conducts the corporate induction program on Day 1, covering TechV-Flash history, leadership structures, and core operating values.
    </div>
    <div class="policy-section">
        <strong>11.2 Compliance Training Deadlines</strong>
        New hires must complete basic compliance training modules (Information Security, Data Privacy, and POSH guidelines) within the first 15 days of joining. Access to production servers is restricted until these are completed.
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Recruitment_Onboarding_Policy.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")