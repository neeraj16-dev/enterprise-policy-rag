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
            font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            color: #2c3e50;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            font-size: 11pt;
        }

        /* Cover Page Styling */
        .cover {
            text-align: center;
            padding-top: 50mm;
            page-break-after: always;
        }
        
        .cover h1 {
            font-size: 36pt;
            color: #0b3d91;
            margin-bottom: 10px;
            letter-spacing: 1px;
            border: none;
            padding: 0;
        }
        
        .cover h2 {
            font-size: 18pt;
            color: #e67e22;
            font-weight: normal;
            background: none;
            padding: 0;
            border: none;
        }
        
        .cover p {
            font-size: 12pt;
            color: #7f8c8d;
            margin-top: 50mm;
        }

        /* Typography and Headings */
        h1, h2, h3 {
            font-family: 'Georgia', serif;
        }

        h2 {
            color: #0b3d91;
            font-size: 16pt;
            margin-top: 30px;
            margin-bottom: 15px;
            padding-bottom: 5px;
            border-bottom: 2px solid #e67e22;
            page-break-after: avoid;
        }

        h3 {
            color: #2980b9;
            font-size: 13pt;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }

        /* Policy Blocks for RAG chunking */
        .policy-section {
            margin-bottom: 25px;
        }
        
        .policy-item {
            display: block;
            margin-bottom: 12px;
            padding: 10px 15px;
            background-color: #ffffff;
            border-left: 4px solid #3498db;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .policy-item strong {
            color: #2c3e50;
            display: block;
            margin-bottom: 4px;
        }

        .callout {
            background-color: #fdebd0;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            border: 1px solid #f39c12;
            page-break-inside: avoid;
        }

        .ceo-message {
            font-style: italic;
            padding: 20px;
            background-color: #eef2f5;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            margin-bottom: 15px;
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

        .page-break {
            page-break-before: always;
        }

    </style>
</head>
<body>
    <div id="footer_content" style="text-align: right; font-family: 'Georgia', serif; font-size: 10pt; color: #555;">
        Page <pdf:pagenumber>
    </div>

    <!-- Cover Page -->
    <div class="cover">
        <h1>TechV-Flash</h1>
        <h2>HR & Employee Handbook</h2>
        <p>Document Ref: HR-POL-001<br>Effective Date: January 1, 2026<br>Location: Pune HQ & Global Remote</p>
    </div>

    <!-- Welcome Message -->
    <h2>Welcome to TechV-Flash</h2>
    <div class="ceo-message">
        "At TechV-Flash, we are driven by innovation and a commitment to excellence. As we scale our engineering and operations from our Pune headquarters to the rest of the world, our policies must adapt to support a dynamic, high-performing team. This handbook is designed to ensure a safe, inclusive, and highly productive environment for all of us. Please read it carefully, as it forms the foundation of how we operate."
        <br><br>
        <strong>— Neeraj Mayekar, CEO & Founder</strong>
    </div>

    <!-- Section 1 -->
    <div class="page-break"></div>
    <h2>1. General Employment Policies</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>1.1 Employment Classification</strong>
            TechV-Flash classifies employees into three main categories: Full-Time Employees (FTE), Part-Time Employees (PTE), and Interns/Trainees. Benefits and policy applicability vary by these classifications unless explicitly stated otherwise.
        </div>
        
        <div class="policy-item">
            <strong>1.2 Probationary Period</strong>
            All new Full-Time Employees are subject to a standard 90-day probationary period. During this time, employment may be terminated by either party with a 15-day notice. Interns do not have a probationary period as their contract is strictly term-based.
        </div>

        <div class="policy-item">
            <strong>1.3 Working Hours & Core Hours</strong>
            The standard workweek is 40 hours for Full-Time Employees, running Monday through Friday. While we offer flexible start and end times, all employees must be available online or in-office during the "Core Collaboration Hours" of 11:00 AM to 4:00 PM (IST).
        </div>
        
        <div class="policy-item">
            <strong>1.4 Employee Badges & Office Access</strong>
            Physical ID badges are required for entry to the Pune facility. Badges must be visibly worn at all times. A lost badge must be reported immediately to IT Security. The replacement fee for a lost badge is 500 INR, which will be deducted from the subsequent payroll cycle.
        </div>
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Workplace Etiquette & Environment</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>2.1 Dress Code</strong>
            TechV-Flash maintains a "Smart Casual" dress code. Clothing must be neat, clean, and professionally appropriate. Employees attending client meetings or external conferences must adhere to "Business Professional" attire.
        </div>

        <div class="policy-item">
            <strong>2.2 Hot-Desking & Clean Desk Policy</strong>
            To foster collaboration, the office utilizes a hot-desking model. Desks cannot be permanently claimed. Employees must clear all personal belongings, printed documents, and hardware from their desks at the end of their shift in accordance with our Information Security protocols.
        </div>

        <div class="policy-item">
            <strong>2.3 Open Door Policy</strong>
            We encourage open communication. If an employee has a concern, idea, or grievance, they are encouraged to discuss it first with their direct manager. If unresolved, they may escalate directly to HR or any member of the senior leadership team without fear of retaliation.
        </div>
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Equal Opportunity & Inclusion</h2>

    <div class="policy-section">
        <div class="policy-item">
            <strong>3.1 Non-Discrimination</strong>
            TechV-Flash is an equal opportunity employer. We strictly prohibit discrimination or harassment based on race, color, religion, age, sex, national origin, disability status, genetics, protected veteran status, sexual orientation, gender identity or expression.
        </div>
        
        <div class="policy-item">
            <strong>3.2 Accommodations</strong>
            Employees requiring reasonable accommodations for medical, religious, or ergonomic reasons (e.g., standing desks, specialized hardware) must submit a formal request via the HR portal. Approvals are typically processed within 5 business days.
        </div>
    </div>
    
    <div class="callout">
        <strong>Important Note on Policy Updates:</strong> TechV-Flash reserves the right to modify, revoke, suspend, or terminate any or all policies and procedures outlined in this handbook, in whole or in part, at any time, with or without prior notice.
    </div>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Employee Code of Conduct</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>4.1 Conflict of Interest</strong>
            Employees must avoid any activity, investment, or association that interferes with their independent exercise of judgment in TechV-Flash's best interests. Any potential conflict of interest must be disclosed in writing to HR immediately.
        </div>
        
        <div class="policy-item">
            <strong>4.2 Intellectual Property (IP)</strong>
            All inventions, code, designs, and documentation developed by an employee during their tenure at TechV-Flash are the exclusive property of the company. Employees must sign the standard Proprietary Information and Inventions Agreement upon joining.
        </div>
        
        <div class="policy-item">
            <strong>4.3 Confidentiality</strong>
            Protection of confidential company, client, and vendor information is paramount. Non-disclosure of proprietary technologies, financial data, and personal employee records is strictly enforced. Violations are subject to immediate legal and disciplinary action.
        </div>
        
        <div class="policy-item">
            <strong>4.4 Social Media Policy</strong>
            While TechV-Flash respects employee expression, employees must not post confidential information or represent themselves as official company spokespersons on social media unless authorized. Avoid postings that could negatively impact the company's reputation.
        </div>

        <div class="policy-item">
            <strong>4.5 Use of Company Property</strong>
            Laptops, mobile devices, and other office equipment provided by TechV-Flash are intended for business use. Personal use must be kept to a minimum. Installing unauthorized software on corporate devices is strictly prohibited.
        </div>

        <div class="policy-item">
            <strong>4.6 Anti-Bribery & Corruption</strong>
            TechV-Flash maintains a zero-tolerance policy towards bribery, kickbacks, and corruption. Employees are prohibited from offering, giving, soliciting, or accepting bribes or inappropriate gifts from clients, suppliers, or government officials.
        </div>
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Performance Management & Career Development</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>5.1 Performance Review Cycle</strong>
            Performance appraisals are conducted bi-annually at TechV-Flash: the Mid-Year Review in October and the Annual Appraisal in April. Reviews focus on KPI achievements, behavioral competencies, and setting goals for the next cycle.
        </div>
        
        <div class="policy-item">
            <strong>5.2 Promotion Criteria</strong>
            Promotions are based on merit, consistent high performance, demonstrated readiness for the next level, and organizational business needs. Recommendations are reviewed by the Department Head and the HR Committee.
        </div>

        <div class="policy-item">
            <strong>5.3 Professional Development & Training Reimbursement</strong>
            TechV-Flash supports continuous learning. Full-time employees can request reimbursement for professional courses, certifications, and industry workshops. Approvals must be obtained in writing from the manager prior to enrollment.
        </div>
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Grievance Redressal & Disciplinary Actions</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>6.1 Standard Disciplinary Procedure</strong>
            TechV-Flash follows a progressive disciplinary policy to correct performance or behavioral issues. The process typically starts with verbal warnings, followed by written warnings, performance improvement plans, and ultimately termination if unresolved.
        </div>
        
        <div class="policy-item">
            <strong>6.2 Sexual Harassment Policy (POSH)</strong>
            In accordance with the POSH Act, TechV-Flash is committed to providing a safe work environment free from sexual harassment. The Internal Complaints Committee (ICC) investigates all complaints in a highly confidential and time-bound manner.
        </div>

        <div class="policy-item">
            <strong>6.3 Dispute Resolution Process</strong>
            If an employee has disputes with peers or management, they are encouraged to submit a formal grievance request via the HR portal. The HR department will schedule mediation sessions within 3 business days to facilitate resolution.
        </div>
    </div>

    <h3>6.4 Table of Progressive Disciplinary Actions</h3>
    <table>
        <tr>
            <th>Category of Violation</th>
            <th>First Offense Action</th>
            <th>Second Offense Action</th>
            <th>Severe/Repeated Offense Action</th>
        </tr>
        <tr>
            <td>Minor attendance/punctuality issues</td>
            <td>Verbal Warning</td>
            <td>Written Warning</td>
            <td>Performance Improvement Plan (PIP)</td>
        </tr>
        <tr>
            <td>Negligence or minor property damage</td>
            <td>Written Warning</td>
            <td>Suspension (Unpaid)</td>
            <td>Termination of Employment</td>
        </tr>
        <tr>
            <td>Data breach or policy violation</td>
            <td>Written Warning & PIP</td>
            <td>Suspension (Unpaid)</td>
            <td>Immediate Termination</td>
        </tr>
        <tr>
            <td>Harassment, theft, or physical violence</td>
            <td>Immediate Termination</td>
            <td>Legal Prosecution</td>
            <td>N/A</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Separation & Exit Policies</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>7.1 Notice Period</strong>
            Confirmed Full-Time Employees must serve a notice period of 60 days upon resignation. During probation, the notice period is 15 days. The company reserves the right to waive the notice period or accept payment in lieu of notice.
        </div>
        
        <div class="policy-item">
            <strong>7.2 Exit Interview Process</strong>
            On or before their last working day, the resigning employee must participate in an exit interview with HR. This feedback is highly valued and used to improve the overall employee experience and company culture.
        </div>

        <div class="policy-item">
            <strong>7.3 Return of Company Property</strong>
            Before final clearance, all company-provided assets (including laptops, chargers, access badges, files, and cards) must be returned to the IT and Admin departments in working condition. Cost of unreturned items will be deducted from the final settlement.
        </div>

        <div class="policy-item">
            <strong>7.4 Full & Final Settlement (F&F) Timeline</strong>
            The Full and Final settlement statement and any pending payouts will be processed and credited within 45 calendar days from the employee's last working day, subject to complete asset handover and department sign-offs.
        </div>
    </div>

    <h3>7.5 Table of Notice Periods by Level</h3>
    <table>
        <tr>
            <th>Job Category / Level</th>
            <th>Notice Period (During Probation)</th>
            <th>Notice Period (Confirmed Status)</th>
            <th>Notice Buy-out Option</th>
        </tr>
        <tr>
            <td>L1 - L2 (Junior & Associate Roles)</td>
            <td>15 Days</td>
            <td>30 Days</td>
            <td>Subject to Manager Approval</td>
        </tr>
        <tr>
            <td>L3 - L4 (Senior & Lead Roles)</td>
            <td>15 Days</td>
            <td>60 Days</td>
            <td>Not Allowed (Mandatory Transition)</td>
        </tr>
        <tr>
            <td>L5 - L6 (Managers & Directors)</td>
            <td>30 Days</td>
            <td>90 Days</td>
            <td>Not Allowed (Mandatory Transition)</td>
        </tr>
        <tr>
            <td>Interns & Trainees</td>
            <td>7 Days</td>
            <td>N/A (Term contract)</td>
            <td>N/A</td>
        </tr>
    </table>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Health & Safety Policies</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>8.1 First Aid & Medical Emergencies</strong>
            The Pune HQ is equipped with first-aid kits located on every floor near the pantry area. In case of a medical emergency, employees must immediately contact the Office Admin or security desk, who will coordinate with the nearest network hospital.
        </div>
        
        <div class="policy-item">
            <strong>8.2 Fire Safety & Evacuation Plan</strong>
            Regular fire drills are conducted bi-annually. All employees must familiarize themselves with emergency exits and assembly points. In the event of a fire alarm, immediately evacuate the building using the stairs. Do not use elevators.
        </div>

        <div class="policy-item">
            <strong>8.3 Workplace Violence Prevention</strong>
            TechV-Flash has a zero-tolerance policy for workplace violence, verbal threats, physical intimidation, or possession of weapons on company premises. Violations will result in immediate termination and potential legal action.
        </div>
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Miscellaneous Policies</h2>
    
    <div class="policy-section">
        <div class="policy-item">
            <strong>9.1 Whistleblower Policy</strong>
            Employees are encouraged to report any suspected unethical behavior, financial fraud, or violations of law within the company. Reports can be made anonymously via the dedicated email address (whistleblower@techvflash.com). The company guarantees protection against retaliation for reports made in good faith.
        </div>
        
        <div class="policy-item">
            <strong>9.2 External Engagements & Moonlighting</strong>
            Employees are hired on an exclusive basis and are prohibited from engaging in any other business or employment activity (including freelancing or advisory roles) without prior written consent from the CEO and HR.
        </div>

        <div class="policy-item">
            <strong>9.3 Employee Referral Program</strong>
            TechV-Flash rewards employees who refer qualified candidates for open positions. If the referred candidate is hired and completes 6 months of continuous service, the referring employee is eligible for a referral bonus.
        </div>
    </div>

    <h3>9.4 Table of Employee Referral Rewards</h3>
    <table>
        <tr>
            <th>Role Grade Level</th>
            <th>Candidate Profile Experience</th>
            <th>Referral Reward Amount</th>
            <th>Payout Schedule</th>
        </tr>
        <tr>
            <td>L1 - L2</td>
            <td>1 - 3 Years Experience</td>
            <td>15,000 INR</td>
            <td>Paid in payroll after candidate completes 90 days</td>
        </tr>
        <tr>
            <td>L3 - L4</td>
            <td>4 - 8 Years Experience</td>
            <td>30,000 INR</td>
            <td>Paid in payroll after candidate completes 180 days</td>
        </tr>
        <tr>
            <td>L5 - L6</td>
            <td>8+ Years Experience</td>
            <td>50,000 INR</td>
            <td>Paid in payroll after candidate completes 180 days</td>
        </tr>
        <tr>
            <td>Niche Tech Roles (e.g., AI/ML)</td>
            <td>Any Experience Level</td>
            <td>40,000 INR</td>
            <td>Paid in payroll after candidate completes 180 days</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Document Revision History</h2>
    <table>
        <tr>
            <th>Version</th>
            <th>Date</th>
            <th>Author</th>
            <th>Summary of Changes</th>
        </tr>
        <tr>
            <td>1.0</td>
            <td>Jan 1, 2026</td>
            <td>HR Dept</td>
            <td>Initial baseline handbook creation.</td>
        </tr>
        <tr>
            <td>1.1</td>
            <td>Jun 15, 2026</td>
            <td>HR Dept</td>
            <td>Expanded sections, added code of conduct, performance metrics, progressive discipline tables, and referral benefits.</td>
        </tr>
    </table>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_HR_Employee_Handbook.pdf"

# 1. Ensure the folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# 2. Generate the PDF
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")