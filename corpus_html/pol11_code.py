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
            color: #34495e;
            line-height: 1.6;
            font-size: 10.5pt;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #2c3e50;
            color: #ffffff;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header h1 {
            margin: 0 0 8px 0;
            font-size: 24pt;
            letter-spacing: 1px;
        }
        .header p {
            margin: 0;
            font-size: 10pt;
            color: #ecf0f1;
        }
        h2 {
            color: #2c3e50;
            font-size: 14pt;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
            margin-top: 25px;
            margin-bottom: 15px;
            page-break-after: avoid;
        }
        .policy-block {
            background-color: #ffffff;
            border-left: 4px solid #3498db;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            page-break-inside: avoid;
        }
        .policy-block strong {
            display: block;
            color: #2980b9;
            font-size: 11.5pt;
            margin-bottom: 6px;
        }
        .pip-box {
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            color: #856404;
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
    <div id="footer_content" style="text-align: right; font-family: 'Helvetica Neue', sans-serif; font-size: 10pt; color: #555;">
        Page <pdf:pagenumber>
    </div>

    <div class="header">
        <h1>Performance Management Policy</h1>
        <p>Document Ref: HR-POL-011 | Effective: November 2026</p>
    </div>

    <p>TechV-Flash is committed to fostering a high-performance culture. This policy outlines the structured processes for goal setting, continuous feedback, annual appraisals, and performance improvement interventions.</p>

    <h2>1. Performance Review Cycle</h2>
    <div class="policy-block">
        <strong>1.1 Annual Appraisal Cycle</strong>
        The standard performance appraisal cycle aligns with the financial year (April 1st to March 31st). Final evaluations occur in April, with corresponding salary increments or promotions taking effect in the May payroll.
    </div>
    <div class="policy-block">
        <strong>1.2 Mid-Year Reviews</strong>
        A formal mid-year review is conducted every October. This review does not impact immediate compensation but serves to course-correct objectives and provide documented developmental feedback.
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Goal Setting & KPIs</h2>
    <div class="policy-block">
        <strong>2.1 SMART Objectives</strong>
        All employees must define 3 to 5 primary Key Performance Indicators (KPIs) in consultation with their direct manager by April 30th. Goals must follow the SMART framework (Specific, Measurable, Achievable, Relevant, Time-bound).
    </div>
    <div class="policy-block">
        <strong>2.2 Weightage Distribution</strong>
        For evaluation purposes, Core Job Responsibilities hold a 70% weightage, Team Collaboration/Leadership holds 20%, and Individual Learning/Certifications hold a 10% weightage.
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Rating Scale & Normalization</h2>
    <p>Performance is evaluated on a standardized 5-point rating scale. Department heads are responsible for normalizing ratings across teams to ensure fairness.</p>
    <table>
        <tr>
            <th>Rating</th>
            <th>Descriptor</th>
            <th>Implication</th>
        </tr>
        <tr>
            <td>5</td>
            <td>Outstanding</td>
            <td>Significantly exceeds all expectations. Highest bonus eligibility. Fast-track promotion candidate.</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Exceeds Expectations</td>
            <td>Consistently delivers above targets. High bonus eligibility.</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Meets Expectations</td>
            <td>Solid performer; meets all core job requirements. Standard bonus payout.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Needs Improvement</td>
            <td>Inconsistent performance. No bonus payout. May require training intervention.</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Unsatisfactory</td>
            <td>Fails to meet basic expectations. Placed on mandatory PIP.</td>
        </tr>
    </table>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Performance Improvement Plan (PIP)</h2>
    <div class="pip-box">
        <strong>Mandatory PIP Trigger:</strong> Employees receiving a Rating of 1 ("Unsatisfactory") during the annual appraisal, or consistently failing to meet targets for 2 consecutive quarters, will be placed on a Performance Improvement Plan (PIP).
        <br><br>
        <strong>PIP Duration & Outcome:</strong> A standard PIP lasts for 60 days. During this period, the employee will have bi-weekly check-ins with HR and their manager. If the specific PIP goals are not met by the end of the 60-day period, it will lead to immediate termination of employment.
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Continuous Feedback & 1-on-1 Syncs</h2>
    <div class="policy-block">
        <strong>5.1 Weekly 1-on-1 Cadence</strong>
        Managers are required to conduct weekly 1-on-1 feedback syncs with each direct report. These meetings are intended to track task progress, identify dependencies, and offer guidance.
    </div>
    <div class="policy-block">
        <strong>5.2 Documenting Sync Outlines</strong>
        A summary of discussions, including milestones met and pending action points, must be logged in the internal HR performance module on a monthly basis by the manager.
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Promotion Recommendations</h2>
    <div class="policy-block">
        <strong>6.1 Nomination Eligibility</strong>
        To be nominated for a promotion to the next career grade, employees must have spent a minimum of 18 months in their current role and achieved an average performance rating of 4.0 or above in the last two review cycles.
    </div>
    <div class="policy-block">
        <strong>6.2 Review Panel Audit</strong>
        All promotion recommendations are audited by the Promotion Review Committee (Dept HOD, HR Director, and CTO). The panel checks candidate competency logs and project impact metrics.
    </div>

    <h3>6.3 Table of Promotion & Nomination Slabs</h3>
    <table>
        <tr>
            <th>Target Job Level</th>
            <th>Minimum Tenure in Current Level</th>
            <th>Average Rating Required</th>
            <th>Promotion Window</th>
        </tr>
        <tr>
            <td>L2 - L3 (Engineer to Senior)</td>
            <td>18 Months</td>
            <td>Rating of 4.0 or above</td>
            <td>Annual cycle (April review only)</td>
        </tr>
        <tr>
            <td>L4 - L5 (Lead to Manager)</td>
            <td>24 Months</td>
            <td>Rating of 4.2 or above</td>
            <td>Annual cycle (April review only)</td>
        </tr>
        <tr>
            <td>L6+ (Director & Executive Roles)</td>
            <td>36 Months</td>
            <td>Rating of 4.5 or above</td>
            <td>Subject to Board approval</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Rewards & Recognition Program</h2>
    <div class="policy-block">
        <strong>7.1 Monthly Spotlight Awards</strong>
        Exceptional contributions that showcase TechV-Flash core values are recognized monthly. Nominations are submitted by team leads and reviewed by HR on the 25th of every month.
    </div>
    <div class="policy-block">
        <strong>7.2 Spot Cash Awards</strong>
        For emergency project deliveries or critical bug resolutions over weekends, managers can approve instant Spot Cash Awards to recognizing employees' dedication.
    </div>

    <h3>7.3 Table of Spotlight & Milestone Recognition Slabs</h3>
    <table>
        <tr>
            <th>Award Category</th>
            <th>Nomination Frequency</th>
            <th>Cash Reward Amount</th>
            <th>Non-Cash Recognition Benefits</th>
        </tr>
        <tr>
            <td>Monthly Spotlight Award</td>
            <td>Monthly (Max 2 per department)</td>
            <td>5,000 INR</td>
            <td>Digital certificate, company-wide Slack shout-out.</td>
        </tr>
        <tr>
            <td>Spot Cash Award</td>
            <td>Ad-hoc (Manager approved)</td>
            <td>2,500 INR</td>
            <td>Award badge in HR Portal.</td>
        </tr>
        <tr>
            <td>Quarterly Champion Award</td>
            <td>Quarterly (1 per business unit)</td>
            <td>15,000 INR</td>
            <td>Engraved trophy, dinner voucher.</td>
        </tr>
        <tr>
            <td>Annual President's Award</td>
            <td>Annually (Max 3 company-wide)</td>
            <td>50,000 INR</td>
            <td>President's club plaque, extra 2 days PTO.</td>
        </tr>
    </table>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Special Performance-Linked Bonuses</h2>
    <div class="policy-block">
        <strong>8.1 Retention Bonus Schemes</strong>
        For key personnel managing core framework architecture, the company may issue retention bonuses linked to successful multi-year milestones. These bonuses are subject to clawback if the employee exits early.
    </div>
    <div class="policy-block">
        <strong>8.2 Delivery Milestone Rewards</strong>
        Engineering departments working on high-value client releases are eligible for project milestone payouts. These rewards are distributed equally among active project contributors.
    </div>

    <h3>8.3 Table of Performance-Linked Bonus Targets</h3>
    <table>
        <tr>
            <th>Business Unit / Division</th>
            <th>KPI Target Metric</th>
            <th>Standard Payout Rate</th>
            <th>Maximum Payout Cap</th>
        </tr>
        <tr>
            <td>Software Engineering (Product)</td>
            <td>Feature release delivery matching roadmap deadlines.</td>
            <td>10% of monthly basic salary</td>
            <td>15% of monthly basic</td>
        </tr>
        <tr>
            <td>Client Operations & Delivery</td>
            <td>Customer SLA breaches under 0.5% annually.</td>
            <td>12% of monthly basic salary</td>
            <td>18% of monthly basic</td>
        </tr>
        <tr>
            <td>Infrastructure & Site Reliability</td>
            <td>Platform uptime exceeding 99.99% per quarter.</td>
            <td>15% of monthly basic salary</td>
            <td>20% of monthly basic</td>
        </tr>
    </table>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. 360-Degree Peer Feedback</h2>
    <div class="policy-block">
        <strong>9.1 Gathering Multi-Dimensional Input</strong>
        During the annual review, employees select 3 peers from their projects to submit anonymous feedback. The feedback questionnaire is managed by HR and evaluates collaboration and communication.
    </div>
    <div class="policy-block">
        <strong>9.2 Upward Feedback for Managers</strong>
        Direct reports are required to submit anonymous evaluation reviews for their supervisors. These reviews help evaluate leadership behavior and identify training needs for management staff.
    </div>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Performance Grievances & Appeal Process</h2>
    <div class="policy-block">
        <strong>10.1 Submitting a Rating Appeal</strong>
        Employees who disagree with their annual appraisal rating can submit a formal Appeal Form to HR within 7 business days of receiving their scorecard. The appeal must contain objective proof of KPI completions.
    </div>
    <div class="policy-block">
        <strong>10.2 Review Panel Mediation</strong>
        HR will establish an Appeal Review Panel (comprising the HRBP, HOD, and an independent manager). The panel reviews the submissions and schedules a resolution meeting within 15 working days. The panel's rating choice is final.
    </div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Competency & Capability Mapping</h2>
    <div class="policy-block">
        <strong>11.1 Standard Competency Framework</strong>
        Every engineering level has a defined set of tech skills and leadership behaviors. Appraisals verify if the employee's output matches their level's competency definitions.
    </div>
    <div class="policy-block">
        <strong>11.2 Individual Development Plans (IDP)</strong>
        Employees who do not show growth in their competency audits are assigned an IDP. The IDP outlines targeted courses, mentorship programs, and projects to close skill gaps within 90 days.
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Performance_Management_Policy.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")