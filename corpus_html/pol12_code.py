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
            line-height: 1.55;
            font-size: 10.5pt;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #1b4f72;
            color: #ffffff;
            padding: 22px;
            border-radius: 6px;
            margin-bottom: 22px;
        }
        .header h1 {
            margin: 0 0 6px 0;
            font-size: 22pt;
            letter-spacing: 0.5px;
        }
        .header p {
            margin: 0;
            font-size: 10pt;
            opacity: 0.9;
        }
        h2 {
            color: #1b4f72;
            font-size: 13pt;
            border-bottom: 2px solid #2874a6;
            padding-bottom: 4px;
            margin-top: 22px;
            margin-bottom: 12px;
            page-break-after: avoid;
        }
        .rule-card {
            background-color: #ffffff;
            border-left: 4px solid #2874a6;
            border-right: 1px solid #e2e8f0;
            border-top: 1px solid #e2e8f0;
            border-bottom: 1px solid #e2e8f0;
            padding: 12px 14px;
            margin-bottom: 12px;
            page-break-inside: avoid;
            border-radius: 0 4px 4px 0;
        }
        .rule-card strong {
            display: block;
            color: #1b4f72;
            font-size: 11pt;
            margin-bottom: 4px;
        }
        .alert-box {
            background-color: #fef9e7;
            border: 1px solid #f9e79f;
            color: #7d6608;
            padding: 12px 15px;
            border-radius: 4px;
            margin: 15px 0;
            page-break-inside: avoid;
            font-size: 10pt;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 14px 0;
            background-color: #ffffff;
            page-break-inside: avoid;
            font-size: 10pt;
        }
        th, td {
            border: 1px solid #cbd5e1;
            padding: 9px 10px;
            text-align: left;
        }
        th {
            background-color: #1b4f72;
            color: #ffffff;
        }
        tr:nth-child(even) {
            background-color: #f8fafc;
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
        <h1>Learning & Development Policy</h1>
        <p>Document Ref: HR-POL-012 | Effective: December 2026 | Location: Global & Pune HQ</p>
    </div>

    <p>TechV-Flash actively encourages continuous upskilling, professional certifications, and technical development. This policy outlines eligibility, annual budgets, reimbursement rules, and service commitments associated with company-funded learning initiatives.</p>

    <h2>1. Annual Learning Allowance & Eligibility</h2>
    <div class="rule-card">
        <strong>1.1 Eligibility Criteria</strong>
        All Full-Time Employees who have successfully completed their 90-day probationary period are eligible for the Annual Learning Allowance. Part-Time Employees receive a 50% pro-rated benefit. Interns and employees currently on a Performance Improvement Plan (PIP) are not eligible for learning sponsorships.
    </div>

    <table>
        <tr>
            <th>Employee Level</th>
            <th>Annual Allowance Limit</th>
            <th>Permissible Categories</th>
        </tr>
        <tr>
            <td>L1 - L3 (Engineers & Associates)</td>
            <td>35,000 INR</td>
            <td>Technical certifications (AWS, GCP, Azure, CKA), online courses (Coursera, Udemy Pro), technical books.</td>
        </tr>
        <tr>
            <td>L4 - L5 (Leads & Managers)</td>
            <td>60,000 INR</td>
            <td>Advanced architecture certifications, agile/PMP credentials, leadership workshops, specialized tech bootcamps.</td>
        </tr>
        <tr>
            <td>L6+ (Directors & Executives)</td>
            <td>1,00,000 INR</td>
            <td>Executive education, global conference registrations, executive coaching programs.</td>
        </tr>
    </table>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Pre-Approval & Reimbursement Process</h2>
    <div class="rule-card">
        <strong>2.1 Prior Written Approval</strong>
        Employees must submit a Learning Plan Request on the HR Portal at least 10 business days prior to enrollment or exam scheduling. Reimbursement requests submitted without prior approval will be automatically rejected.
    </div>
    <div class="rule-card">
        <strong>2.2 Proof of Completion & Passing Mandate</strong>
        To claim reimbursement for certification exam vouchers, the employee must provide a passing certificate/scorecard along with the original tax invoice. In the event of an exam failure, the cost is borne entirely by the employee; second attempts are not subsidized.
    </div>
    <div class="rule-card">
        <strong>2.3 Expense Submission Window</strong>
        Invoices and certificates must be submitted via the expense portal within 30 calendar days of exam completion or course completion.
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Service Retention Agreement (Clawback Clause)</h2>
    <div class="alert-box">
        <strong>Mandatory Retention Period:</strong> If TechV-Flash sponsors any single certification, specialized training, or executive program where total company expenditure exceeds 25,000 INR, a mandatory 12-month retention agreement applies from the date of certification completion.
    </div>
    <div class="rule-card">
        <strong>3.1 Clawback Recovery Terms</strong>
        If an employee voluntarily resigns within 6 months of completing a sponsored program exceeding 25,000 INR, 100% of the sponsored amount will be deducted during full and final settlement. For resignations occurring between 7 and 12 months, 50% of the sponsored cost will be recovered.
    </div>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Study Leaves & Conference Attendance</h2>
    <div class="rule-card">
        <strong>4.1 Certification Study Leave</strong>
        Eligible FTEs may avail up to 2 days of paid "Study Leave" per calendar year to prepare for and sit for approved high-impact technical certifications. Study leave requires at least 14 days of advance manager approval.
    </div>
    <div class="rule-card">
        <strong>4.2 Tech Conference Sponsorship</strong>
        Employees accepted as speakers at accredited technical conferences (e.g., PyCon, IEEE conferences, React Summit) will receive 100% travel and lodging sponsorship under the Travel Policy (HR-POL-006), separate from their individual learning allowance.
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. External Degree & Executive Education Sponsorship</h2>
    <div class="rule-card">
        <strong>5.1 Higher Education Criteria</strong>
        Confirmed FTEs with at least 3 years of service can nominate themselves for executive programs or specialized master degrees (e.g., Executive MBA). The program must be run by a government-accredited university.
    </div>
    <div class="rule-card">
        <strong>5.2 Approval Flow & Quota</strong>
        Nominations are evaluated by the Executive Committee annually in January. Sponsoring is capped at a maximum of 5 employees per business unit, with funding approved up to 100% depending on role relevance.
    </div>

    <h3>5.3 Table of Executive Degree Sponsorship Slabs</h3>
    <table>
        <tr>
            <th>Course / Degree Category</th>
            <th>Maximum Funding Limit</th>
            <th>Service Bond Period</th>
            <th>Withdrawal/Failure Consequence</th>
        </tr>
        <tr>
            <td>Executive MBA / PGDM</td>
            <td>2,50,000 INR total</td>
            <td>24 Months post degree completion</td>
            <td>100% recovery of disbursed fees</td>
        </tr>
        <tr>
            <td>Part-time Technical Masters (M.Tech/MS)</td>
            <td>2,00,000 INR total</td>
            <td>18 Months post degree completion</td>
            <td>100% recovery of disbursed fees</td>
        </tr>
        <tr>
            <td>Advanced Leadership Certifications (IIM/IIT)</td>
            <td>1,20,000 INR total</td>
            <td>12 Months post program completion</td>
            <td>100% recovery of disbursed fees</td>
        </tr>
    </table>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Professional Body Memberships</h2>
    <div class="rule-card">
        <strong>6.1 Approved Associations</strong>
        TechV-Flash supports membership in professional associations (e.g., IEEE, ACM, Scrum Alliance). Membership must offer access to research repositories, industry networking, and certification discounts.
    </div>
    <div class="rule-card">
        <strong>6.2 Annual Reimbursement Limits</strong>
        Reimbursement is capped at 1 association membership per calendar year per employee. Prior manager sign-off is required before payment.
    </div>

    <h3>6.3 Table of Professional Association Reimbursement</h3>
    <table>
        <tr>
            <th>Association / Guild Category</th>
            <th>Eligible Employee Grades</th>
            <th>Annual Reimbursement Limit</th>
            <th>Required Verification Documentation</th>
        </tr>
        <tr>
            <td>Technical & Engineering Guilds (ACM, IEEE)</td>
            <td>All L1 - L3 Engineering staff</td>
            <td>8,000 INR per year</td>
            <td>Annual membership invoice and digital card</td>
        </tr>
        <tr>
            <td>Management & Agile Guilds (PMI, Scrum Alliance)</td>
            <td>L4 - L5 Managers and Scrum Leads</td>
            <td>12,000 INR per year</td>
            <td>Annual membership invoice and digital card</td>
        </tr>
        <tr>
            <td>Executive Forums (NASSCOM, CII)</td>
            <td>L6+ Directors & Vice Presidents</td>
            <td>25,000 INR per year</td>
            <td>PR team approval notice, invoice and card</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Corporate Academy & Internal Bootcamps</h2>
    <div class="rule-card">
        <strong>7.1 Internal Training Programs</strong>
        The L&D team runs monthly classroom and virtual training cycles on soft skills, agile execution, and advanced tech stacks (e.g., Rust development, kubernetes orchestration). Attendance is tracked.
    </div>
    <div class="rule-card">
        <strong>7.2 Cross-skilling Bootcamps</strong>
        To facilitate project transitions, employees can enroll in 4-week internal tech bootcamps. Enrolling requires HOD approval and a commitment to clear the associated certification.
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Knowledge Sharing (Brown Bag Sessions)</h2>
    <div class="rule-card">
        <strong>8.1 Knowledge Dissemination Goals</strong>
        To foster peer learning, employees completing external certifications or bootcamps are expected to deliver a 45-minute technical session (Brown Bag) to their department.
    </div>
    <div class="rule-card">
        <strong>8.2 Presenter Incentives</strong>
        Delivering a brown bag session earns the presenter a 1,000 INR learning voucher, which can be applied to buy books or technical subscriptions, separate from the standard annual allowance.
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Management & Leadership Development Programs</h2>
    <div class="rule-card">
        <strong>9.1 High-Potential (HiPo) Program</strong>
        Quarterly, top performers are nominated by HODs for the HiPo Leadership Cohort. This cohort receives specialized management workshops, communications coaching, and executive mentorship.
    </div>
    <div class="rule-card">
        <strong>9.2 Internal Mentorship Framework</strong>
        Managers are paired with senior engineers to act as mentors. The framework requires monthly check-ins and target goal setting for career direction and technical depth.
    </div>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Learning Audits & Compliance Requirements</h2>
    <div class="rule-card">
        <strong>10.1 Audit of Reimbursement Invoices</strong>
        All expense claims undergo audits by the finance and HR compliance teams. Forged invoices or certificates will lead to disciplinary proceedings under HR-POL-015.
    </div>
    <div class="rule-card">
        <strong>10.2 Mandatory Security & Compliance Courses</strong>
        Apart from voluntary development, employees must clear the mandatory Information Security (HR-POL-007) and Data Privacy (LEG-POL-008) micro-courses annually within 30 days of release.
    </div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Travel Slabs for Sponsored Education</h2>
    <div class="rule-card">
        <strong>11.1 Travel to Learning Centers</strong>
        When corporate-sponsored courses require physical attendance at national universities or outstation bootcamps, travel costs are funded as per the company Travel Policy (HR-POL-006).
    </div>

    <h3>11.2 Table of Travel Slabs for Learning Programs</h3>
    <table>
        <tr>
            <th>Travel Location Category</th>
            <th>Maximum Hotel Lodging Cap</th>
            <th>Daily Meal Allowance per Diem</th>
            <th>Additional Travel Approval Target</th>
        </tr>
        <tr>
            <td>Tier 1 Cities (Mumbai, Bangalore, Delhi)</td>
            <td>4,000 INR per night</td>
            <td>1,200 INR per day</td>
            <td>L&D Department Manager sign-off</td>
        </tr>
        <tr>
            <td>Tier 2 Cities & Training Resorts</td>
            <td>3,000 INR per night</td>
            <td>1,000 INR per day</td>
            <td>L&D Department Manager sign-off</td>
        </tr>
        <tr>
            <td>International Training Hubs (Singapore, Dubai)</td>
            <td>$120 USD per night</td>
            <td>$60 USD per day</td>
            <td>CFO & HR Director (Dual approval)</td>
        </tr>
    </table>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Learning_Development_Policy.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")