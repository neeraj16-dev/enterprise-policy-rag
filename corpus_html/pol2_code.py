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
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #333333;
            margin: 0;
            padding: 0;
            line-height: 1.5;
            font-size: 10.5pt;
        }

        /* Header / Title Section */
        .header-banner {
            background-color: #16a085; /* Teal */
            color: #ffffff;
            padding: 25px 20px;
            margin: -20mm -15mm 20px -15mm; /* Bleed into margins */
            text-align: center;
        }
        
        .header-banner h1 {
            margin: 0 0 10px 0;
            font-size: 28pt;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .header-banner p {
            margin: 0;
            font-size: 11pt;
            opacity: 0.9;
        }

        /* Headings */
        h2 {
            color: #2c3e50;
            font-size: 15pt;
            border-left: 5px solid #16a085;
            padding-left: 10px;
            margin-top: 30px;
            margin-bottom: 15px;
            page-break-after: avoid;
        }

        h3 {
            color: #16a085;
            font-size: 12pt;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }

        /* Policy Blocks */
        .policy-block {
            background-color: #ffffff;
            border: 1px solid #e0e6ed;
            border-radius: 4px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            page-break-inside: avoid;
        }

        .policy-block strong.title {
            display: block;
            color: #2c3e50;
            font-size: 11.5pt;
            margin-bottom: 8px;
            border-bottom: 1px solid #ecf0f1;
            padding-bottom: 4px;
        }

        /* Callouts / Warnings */
        .alert {
            background-color: #feebe8;
            border-left: 4px solid #e74c3c;
            padding: 12px 15px;
            margin: 15px 0;
            color: #c0392b;
            font-weight: 500;
            page-break-inside: avoid;
        }

        .highlight {
            background-color: #e8f8f5;
            border: 1px solid #1abc9c;
            padding: 15px;
            margin: 20px 0;
            text-align: center;
            border-radius: 6px;
        }

        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            margin-bottom: 20px;
            background-color: #ffffff;
            page-break-inside: avoid;
        }
        
        th, td {
            border: 1px solid #bdc3c7;
            padding: 12px 10px;
            text-align: left;
        }
        
        th {
            background-color: #2c3e50;
            color: #ffffff;
            font-weight: bold;
        }
        
        tr:nth-child(even) {
            background-color: #f9fbfb;
        }

        .footer-note {
            margin-top: 40px;
            font-size: 9pt;
            text-align: center;
            color: #7f8c8d;
            border-top: 1px solid #bdc3c7;
            padding-top: 10px;
        }

        .page-break {
            page-break-before: always;
        }

    </style>
</head>
<body>
    <div id="footer_content" style="text-align: right; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 10pt; color: #555;">
        Page <pdf:pagenumber>
    </div>

    <div class="header-banner">
        <h1>Leave & Attendance Policy</h1>
        <p>TechV-Flash | Document Ref: HR-POL-002 | Effective: January 2026</p>
    </div>

    <div class="highlight">
        <strong>Objective:</strong> To establish clear guidelines regarding employee time off, ensuring a healthy work-life balance while maintaining operational continuity for TechV-Flash globally.
        <br>
        <em>Approved by: NEERAJ MAYEKAR, CEO</em>
    </div>

    <h2>1. Paid Time Off (PTO) & Casual Leave</h2>
    
    <div class="policy-block">
        <strong class="title">1.1 Annual Allotment</strong>
        Full-Time Employees (FTE) are entitled to 18 days of Paid Time Off (PTO) per calendar year, accrued at a rate of 1.5 days per month. Part-Time Employees accrue PTO on a pro-rated basis aligned with their contractual hours.
    </div>
    
    <div class="policy-block">
        <strong class="title">1.2 Carryover Policy</strong>
        FTEs may carry over a maximum of 5 unused PTO days into the following calendar year. These carried-over days must be utilized by March 31st of the new year, or they will expire. 
    </div>

    <div class="alert">
        <strong>Intern Exemption:</strong> Interns and trainees are not eligible to accrue or carry over Paid Time Off. Any time off taken by interns is considered Unpaid Leave unless explicitly approved by the Department Head.
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Sick & Medical Leave</h2>

    <div class="policy-block">
        <strong class="title">2.1 Sick Leave Entitlement</strong>
        FTEs are granted 12 days of Sick Leave annually (1 day per month). Sick leave is designed for personal illness, injury, or medical appointments. Sick leave cannot be carried over to the next year and cannot be cashed out upon resignation.
    </div>

    <div class="policy-block">
        <strong class="title">2.2 Medical Documentation</strong>
        If an employee takes more than 3 consecutive days of sick leave, a valid medical certificate from a registered medical practitioner must be submitted to HR on the day they resume work. Failure to provide this may result in the days being marked as Leave Without Pay (LWP).
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Holidays</h2>
    
    <p>TechV-Flash observes 12 public holidays per year for the Pune HQ. Of these, 10 are fixed holidays and 2 are "Floating Holidays" that employees can use for regional or personal cultural events.</p>

    <table>
        <tr>
            <th>Holiday Category</th>
            <th>Number of Days</th>
            <th>Approval Requirement</th>
        </tr>
        <tr>
            <td>Fixed Public Holidays (e.g., Republic Day, Diwali)</td>
            <td>10 Days</td>
            <td>None (Company-wide closure)</td>
        </tr>
        <tr>
            <td>Floating Holidays</td>
            <td>2 Days</td>
            <td>Manager approval via HR Portal, 7 days in advance</td>
        </tr>
    </table>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Special Leave Categories</h2>

    <div class="policy-block">
        <strong class="title">4.1 Maternity & Paternity Leave</strong>
        In accordance with the Maternity Benefit Act, female employees are entitled to 26 weeks of paid maternity leave. Male employees are eligible for 2 weeks (10 working days) of paid paternity leave, which must be taken within 6 months of the child's birth.
    </div>

    <div class="policy-block">
        <strong class="title">4.2 Bereavement Leave</strong>
        In the unfortunate event of the passing of an immediate family member (spouse, child, parent, or sibling), employees are entitled to up to 5 days of paid Bereavement Leave.
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Attendance & Clock-in Protocol</h2>

    <div class="policy-block">
        <strong class="title">5.1 Logging Hours</strong>
        All non-exempt employees must log their start and end times via the internal TechV-Flash HR Portal. A grace period of 15 minutes is allowed for the start of the defined "Core Hours" (11:00 AM).
    </div>
    
    <div class="policy-block">
        <strong class="title">5.2 Unapproved Absence (No Call/No Show)</strong>
        Failing to report to work and failing to notify a manager for 3 consecutive working days is considered job abandonment and may lead to immediate termination.
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Leave Encashment & Financials</h2>
    
    <div class="policy-block">
        <strong class="title">6.1 Encashment Eligibility</strong>
        Only Paid Time Off (PTO) is eligible for encashment. Accumulated Sick Leaves, Special Leaves, and Floating Holidays cannot be encashed. Employees can encash up to 10 days of unused PTO annually during the December payroll window, provided they maintain a minimum balance of 8 PTO days.
    </div>
    
    <div class="policy-block">
        <strong class="title">6.2 Calculation Formula</strong>
        The encashment value is calculated based on the employee's monthly basic salary. The formula applied is: `(Basic Salary / 30) * Number of Days Encashed`. Encashment payments are fully taxable as per the prevailing income tax slabs and are subject to PF deductions.
    </div>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Compassionate & Caregiver Leave</h2>

    <div class="policy-block">
        <strong class="title">7.1 Caregiver Leave</strong>
        Employees are eligible for up to 5 days of paid Caregiver Leave per calendar year to attend to a seriously ill dependent (child, spouse, or parent). This leave is distinct from Sick Leave and requires prior notification to the reporting manager.
    </div>

    <div class="policy-block">
        <strong class="title">7.2 Supporting Documents</strong>
        For Caregiver Leave exceeding 2 consecutive days, a medical certificate or hospital admission proof of the dependent must be shared with HR. Self-declaration forms are accepted for single-day absences.
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Sabbatical Leave Policy</h2>

    <div class="policy-block">
        <strong class="title">8.1 Eligibility Criteria</strong>
        Full-Time Employees who have completed a minimum of 4 consecutive years of service at TechV-Flash are eligible to apply for a Sabbatical. Sabbaticals are granted for personal research, higher education, or health recovery reasons.
    </div>

    <div class="policy-block">
        <strong class="title">8.2 Duration & Re-entry</strong>
        A Sabbatical can range from a minimum of 3 months to a maximum of 6 months. It is an unpaid leave period, and the employee's role is held secure until the agreed re-entry date. Requests must be submitted at least 60 days in advance.
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Compensatory Off (Comp-off)</h2>

    <div class="policy-block">
        <strong class="title">9.1 Earning Comp-off</strong>
        Employees in non-exempt roles who work on a weekend or public holiday for critical project releases or customer deployments are eligible to earn a Compensatory Off. Working on standard weekdays beyond standard hours does not qualify for Comp-off.
    </div>

    <div class="policy-block">
        <strong class="title">9.2 Validity & Approval Workflow</strong>
        All Comp-offs must be approved by the Department Head. Once approved, the Comp-off is credited to the HR Portal and must be utilized within 60 calendar days from the date of earning. Expired Comp-offs cannot be reactivated or encashed.
    </div>

    <h3>9.3 Table of Comp-off Earning & Expiry Rules</h3>
    <table>
        <tr>
            <th>Work Day Type</th>
            <th>Minimum Hours Worked</th>
            <th>Comp-Off Credit</th>
            <th>Validity Period</th>
        </tr>
        <tr>
            <td>Standard Weekend (Saturday/Sunday)</td>
            <td>4 to 6 Hours</td>
            <td>0.5 Day Comp-off</td>
            <td>60 Days from Date of Work</td>
        </tr>
        <tr>
            <td>Standard Weekend (Saturday/Sunday)</td>
            <td>6+ Hours</td>
            <td>1.0 Day Comp-off</td>
            <td>60 Days from Date of Work</td>
        </tr>
        <tr>
            <td>National/Public Holiday</td>
            <td>4+ Hours</td>
            <td>1.5 Days Comp-off</td>
            <td>90 Days from Date of Work</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Special Casual Leaves</h2>

    <div class="policy-block">
        <strong class="title">10.1 Voting / General Elections Leave</strong>
        On days of local, state, or national elections, employees registered to vote in that constituency are granted a full day of paid voting leave to exercise their civic rights. Proof of voting (e.g., inked finger photo) may be requested by HR.
    </div>

    <div class="policy-block">
        <strong class="title">10.2 Marriage Leave</strong>
        Full-Time Employees are entitled to up to 5 consecutive working days of paid Marriage Leave for their own marriage. This benefit can be availed only once during their tenure at TechV-Flash and must be planned 30 days in advance.
    </div>

    <div class="policy-block">
        <strong class="title">10.3 Study / Examination Leave</strong>
        Employees pursuing approved higher education or certifications relevant to their job roles can apply for up to 3 days of paid Study Leave per calendar year to prepare for and write exams. Exam schedules must be submitted to the manager.
    </div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Leave Request & Approval Workflows</h2>

    <p>All leave applications must be filed through the TechV-Flash HR Portal. The table below outlines the standard guidelines and submission timelines required for various leave categories to prevent project disruptions.</p>

    <h3>11.1 Table of Leave Application Workflows</h3>
    <table>
        <tr>
            <th>Leave Type</th>
            <th>Submission Timeline</th>
            <th>Approval Authority</th>
            <th>SLA for Response</th>
        </tr>
        <tr>
            <td>Casual Leave / PTO (1-2 Days)</td>
            <td>3 Days in Advance</td>
            <td>Reporting Manager</td>
            <td>24 Hours</td>
        </tr>
        <tr>
            <td>Casual Leave / PTO (3+ Days)</td>
            <td>14 Days in Advance</td>
            <td>Reporting Manager & HOD</td>
            <td>48 Hours</td>
        </tr>
        <tr>
            <td>Sick & Medical Leave</td>
            <td>On day of absence (before 10 AM)</td>
            <td>Reporting Manager (HR for 3+ days)</td>
            <td>Post-facto approval</td>
        </tr>
        <tr>
            <td>Maternity / Paternity Leave</td>
            <td>30 Days in Advance</td>
            <td>Department Head & HR Team</td>
            <td>5 Business Days</td>
        </tr>
        <tr>
            <td>Sabbatical Leave</td>
            <td>60 Days in Advance</td>
            <td>CEO & HR Director</td>
            <td>10 Business Days</td>
        </tr>
    </table>

    <!-- Section 12 -->
    <div class="page-break"></div>
    <h2>12. Leave Types & Allotments Summary</h2>
    
    <p>Below is a comprehensive summary of all leave entitlements and policy terms applicable to Full-Time Employees at TechV-Flash globally.</p>

    <h3>12.1 Leave Entitlement Matrix</h3>
    <table>
        <tr>
            <th>Leave Type</th>
            <th>Annual Allotment</th>
            <th>Carry-over Limit</th>
            <th>Encashment Option</th>
            <th>Impact on Payroll</th>
        </tr>
        <tr>
            <td>Paid Time Off (PTO)</td>
            <td>18 Days</td>
            <td>Max 5 Days</td>
            <td>Yes (Up to 10 days)</td>
            <td>Fully Paid</td>
        </tr>
        <tr>
            <td>Sick Leave (SL)</td>
            <td>12 Days</td>
            <td>None (Expires Dec 31)</td>
            <td>No</td>
            <td>Fully Paid</td>
        </tr>
        <tr>
            <td>Maternity Leave</td>
            <td>26 Weeks</td>
            <td>N/A</td>
            <td>No</td>
            <td>Fully Paid</td>
        </tr>
        <tr>
            <td>Paternity Leave</td>
            <td>2 Weeks</td>
            <td>N/A</td>
            <td>No</td>
            <td>Fully Paid</td>
        </tr>
        <tr>
            <td>Bereavement Leave</td>
            <td>5 Days</td>
            <td>N/A</td>
            <td>No</td>
            <td>Fully Paid</td>
        </tr>
        <tr>
            <td>Leave Without Pay (LWP)</td>
            <td>Ad-hoc (HOD Approval)</td>
            <td>N/A</td>
            <td>No</td>
            <td>Deduction of basic/allowances</td>
        </tr>
    </table>

    <div class="footer-note">
        Confidential & Proprietary - TechV-Flash Internal Use Only
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Leave_Attendance_Policy.pdf"
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")