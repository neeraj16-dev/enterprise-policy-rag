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
            font-family: 'Arial', sans-serif;
            color: #333;
            line-height: 1.6;
            font-size: 11pt;
            margin: 0;
        }
        .header {
            border-bottom: 3px solid #2980b9;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        .header h1 {
            color: #2c3e50;
            margin: 0;
            font-size: 26pt;
        }
        .header p {
            margin: 5px 0 0 0;
            color: #7f8c8d;
            font-size: 10pt;
        }
        h2 {
            color: #2980b9;
            font-size: 14pt;
            margin-top: 25px;
            border-bottom: 1px solid #ecf0f1;
            padding-bottom: 5px;
            page-break-after: avoid;
        }
        .section-content {
            margin-bottom: 20px;
        }
        .policy-clause {
            background-color: #f9f9f9;
            border-left: 4px solid #34495e;
            padding: 12px 15px;
            margin-bottom: 12px;
            page-break-inside: avoid;
        }
        .policy-clause strong {
            display: block;
            color: #2c3e50;
            margin-bottom: 5px;
        }
        .highlight-box {
            background-color: #e8f4f8;
            border: 1px solid #bce8f1;
            color: #31708f;
            padding: 15px;
            border-radius: 4px;
            margin: 20px 0;
            page-break-inside: avoid;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            color: #333;
        }
        .page-break {
            page-break-before: always;
        }
    </style>
</head>
<body>
    <div id="footer_content" style="text-align: right; font-family: Arial, sans-serif; font-size: 10pt; color: #555;">
        Page <pdf:pagenumber>
    </div>

    <div class="header">
        <h1>Payroll & Compensation Policy</h1>
        <p>Document Ref: HR-POL-004 | Effective: April 2026</p>
    </div>

    <div class="highlight-box">
        <strong>Overview:</strong> This document outlines the compensation structure, payroll processing cycles, tax deductions, and bonus eligibility for all TechV-Flash employees globally, with specific clauses for the India HQ.
        <br><br><em>Authorized by: NEERAJ MAYEKAR, CEO</em>
    </div>

    <h2>1. Salary Disbursement Cycle</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>1.1 Payday</strong>
            Salaries are credited to the employee's registered salary bank account on the last working day of every month. If the last day of the month falls on a weekend or a public holiday, salaries will be disbursed on the preceding working day.
        </div>
        <div class="policy-clause">
            <strong>1.2 Payslips</strong>
            Digital payslips are generated and made available on the TechV-Flash HR Portal by the 2nd calendar day of the subsequent month. Employees are responsible for reviewing their payslips and reporting discrepancies within 5 business days.
        </div>
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Statutory Deductions & Taxes</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>2.1 Tax Deducted at Source (TDS)</strong>
            TechV-Flash deducts income tax at source based on the income tax slab applicable to the employee's projected annual income. Employees must submit their investment declarations by April 15th and proofs by January 31st of the financial year to adjust their TDS accurately.
        </div>
        <div class="policy-clause">
            <strong>2.2 Provident Fund (PF)</strong>
            For Indian employees, 12% of the Basic Salary is deducted as the employee's contribution to the Employee Provident Fund (EPF), with an equal matching contribution from TechV-Flash, subject to statutory limits.
        </div>
        <div class="policy-clause">
            <strong>2.3 Professional Tax (PT)</strong>
            Professional Tax is deducted monthly in accordance with the state laws where the employee's primary office is located (e.g., Maharashtra state slabs for Pune HQ).
        </div>
        <div class="policy-clause">
            <strong>2.4 Income Tax Form 16</strong>
            Digital Form 16, which outlines annual earnings and taxes deducted for the financial year, will be released by June 15th of the subsequent year. Employees can download the signed PDF from the payroll tax portal.
        </div>
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Variable Pay & Bonuses</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>3.1 Annual Performance Bonus</strong>
            Eligible Full-Time Employees receive an annual performance bonus based on individual KPIs and company revenue targets. This is calculated for the financial year (April-March) and paid out in the May payroll cycle.
        </div>
        <div class="policy-clause">
            <strong>3.2 Bonus Eligibility Criterion</strong>
            To be eligible for the annual performance bonus, an employee must have completed at least 6 months of continuous service by March 31st. Additionally, the employee must be on the active payroll and not serving a notice period on the actual date of bonus disbursement.
        </div>
        <div class="policy-clause">
            <strong>3.3 Joining Bonus / Sign-on Bonus</strong>
            If a sign-on bonus is part of the employment offer, it is paid in the first month's salary. A clawback clause applies: if the employee resigns within 12 months of joining, 100% of the joining bonus will be recovered during the final settlement.
        </div>
    </div>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Overtime Compensation</h2>
    <div class="section-content">
        <table>
            <tr>
                <th>Employee Category</th>
                <th>Overtime Eligibility</th>
                <th>Rate of Compensation</th>
            </tr>
            <tr>
                <td>Software Engineers & Management (Exempt)</td>
                <td>Not Eligible</td>
                <td>N/A (Comp-off applicable for weekend critical deployments)</td>
            </tr>
            <tr>
                <td>L1/L2 IT Support Staff (Non-Exempt)</td>
                <td>Eligible (Requires Manager Pre-approval)</td>
                <td>1.5x of calculated hourly basic rate</td>
            </tr>
            <tr>
                <td>Interns</td>
                <td>Not Eligible</td>
                <td>N/A</td>
            </tr>
        </table>
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Allowances & Tax-Efficient Reimbursements</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>5.1 House Rent Allowance (HRA)</strong>
            HRA constitutes 40% (for non-metros) or 50% (for metro cities) of the basic salary. Rent receipts and rent agreements must be submitted on the tax portal to claim tax exemption under Section 10(13A). PAN of the landlord is mandatory if the annual rent exceeds 1,00,000 INR.
        </div>
        <div class="policy-clause">
            <strong>5.2 Leave Travel Allowance (LTA)</strong>
            LTA can be claimed twice in a block of four calendar years for domestic travel with family. Claims must be submitted with valid flight/train boarding passes and tax invoices. The exemption is limited to actual travel costs, excluding lodging and food.
        </div>
        <div class="policy-clause">
            <strong>5.3 Books & Periodicals Allowance</strong>
            Employees are eligible for a tax-free allowance up to 12,000 INR per year for books, magazines, and technical subscriptions related to their professional growth. Expense claims must be submitted quarterly with proper GST invoices.
        </div>
        <div class="policy-clause">
            <strong>5.4 Fuel & Vehicle Maintenance Allowance</strong>
            For employee-owned vehicles used for business commutes, tax-exempt reimbursements can be claimed up to 21,600 INR annually. Proper fuel bills and vehicle registration details must be uploaded on the portal.
        </div>
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Shift Allowances</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>6.1 Night Shift Eligibility</strong>
            Employees scheduled to work in the designated night shift (starting after 8:00 PM and ending after 4:00 AM) are eligible for a Shift Allowance. Shift schedules must be logged and approved in the attendance system by the reporting manager.
        </div>
        <div class="policy-clause">
            <strong>6.2 Transport and Cab Facility</strong>
            Female employees working in late night shifts (ending after 10:00 PM or starting before 6:00 AM) will be provided free home drop/pickup cab services equipped with GPS tracking and security escorts.
        </div>
    </div>

    <h3>6.3 Table of Shift Allowance Rates</h3>
    <table>
        <tr>
            <th>Shift Timing</th>
            <th>Role Eligibility</th>
            <th>Daily Allowance Rate</th>
            <th>Transport Provision</th>
        </tr>
        <tr>
            <td>General Shift (9:00 AM - 6:00 PM)</td>
            <td>All Employees</td>
            <td>N/A (Standard)</td>
            <td>Not Provided</td>
        </tr>
        <tr>
            <td>Evening Shift (2:00 PM - 11:00 PM)</td>
            <td>Support & Operations Teams</td>
            <td>250 INR per day</td>
            <td>One-way drop facility provided</td>
        </tr>
        <tr>
            <td>Night Shift (10:00 PM - 7:00 AM)</td>
            <td>IT Infrastructure & Support Teams</td>
            <td>500 INR per day</td>
            <td>Two-way cab facility provided</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Salary Advances & Loan Schemes</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>7.1 Emergency Salary Advance</strong>
            FTEs who have completed 1 year of service can apply for an emergency salary advance. The maximum advance is limited to 1 month's basic salary, and approvals are subject to HR and Finance verification. Sickness, natural disaster, or family emergencies are valid reasons.
        </div>
        <div class="policy-clause">
            <strong>7.2 Repayment Terms & Interest Rates</strong>
            All salary advances are interest-free and will be recovered in a maximum of 6 equal monthly installments, starting from the payroll cycle immediately following the month of disbursement.
        </div>
        <div class="policy-clause">
            <strong>7.3 Resignation / Notice Period Recovery</strong>
            If an employee with an active salary advance resigns, the entire outstanding balance will be recovered in full from the final settlement statement. Slabs or installment extensions are not permitted during the notice period.
        </div>
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Final Settlement & Exit Payroll</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>8.1 Gratuity Calculations</strong>
            In accordance with the Payment of Gratuity Act, employees who complete 5 years of continuous service are eligible for gratuity. The formula is: `(Last Drawn Basic Salary * 15 / 26) * Number of Years of Service`.
        </div>
        <div class="policy-clause">
            <strong>8.2 Leave Encashment Calculations</strong>
            Unutilized accrued PTO days (up to a maximum of 45 days) can be encashed at the time of separation. The payment is calculated as: `(Basic Salary / 30) * Accrued PTO Days`. No other leave categories are eligible for exit encashment.
        </div>
        <div class="policy-clause">
            <strong>8.3 Notice Buy-out Recovery</strong>
            If an employee leaves without serving the required notice period, a notice recovery fee equivalent to basic salary for the unserved period will be added to the exit payroll deductions.
        </div>
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Relocation Assistance & Allowance</h2>
    <div class="section-content">
        <p>TechV-Flash provides financial support to new hires and existing employees relocated by the company to a different city (e.g., relocating to the Pune HQ).</p>
    </div>

    <h3>9.1 Table of Relocation Slabs & Allowances</h3>
    <table>
        <tr>
            <th>Relocation Distance</th>
            <th>Role Grade Level</th>
            <th>Max Packers & Movers Cap</th>
            <th>Temporary Stay Provision</th>
        </tr>
        <tr>
            <td>Less than 200 km</td>
            <td>All Levels</td>
            <td>10,000 INR</td>
            <td>2 Days (Hotel booking)</td>
        </tr>
        <tr>
            <td>200 km to 1000 km</td>
            <td>L1 - L3 (Associates to Seniors)</td>
            <td>25,000 INR</td>
            <td>7 Days (Guest house/Hotel)</td>
        </tr>
        <tr>
            <td>200 km to 1000 km</td>
            <td>L4 - L6 (Leads & Managers)</td>
            <td>40,000 INR</td>
            <td>10 Days (Guest house/Hotel)</td>
        </tr>
        <tr>
            <td>Above 1000 km / International</td>
            <td>All Levels (Approved relocation)</td>
            <td>60,000 INR (Domestic max)</td>
            <td>14 Days (Guest house/Hotel)</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Retirals & Long-term Benefits</h2>
    <div class="section-content">
        <p>Long-term financial benefits and savings schemes are maintained by the company to ensure financial security post-retirement.</p>
    </div>

    <h3>10.1 Table of Retiral Benefits Summary</h3>
    <table>
        <tr>
            <th>Retiral Benefit</th>
            <th>Employee Contribution</th>
            <th>Company Contribution</th>
            <th>Tax Exemption Status</th>
        </tr>
        <tr>
            <td>Employee Provident Fund (EPF)</td>
            <td>12% of Basic Salary (Mandatory)</td>
            <td>12% of Basic Salary (Matching)</td>
            <td>Exempt under Section 80C</td>
        </tr>
        <tr>
            <td>Voluntary Provident Fund (VPF)</td>
            <td>Up to 88% of Basic (Voluntary)</td>
            <td>None</td>
            <td>Exempt under Section 80C</td>
        </tr>
        <tr>
            <td>National Pension Scheme (NPS)</td>
            <td>Up to 10% of Basic (Voluntary)</td>
            <td>Corporate plan matching up to 10%</td>
            <td>Exempt under Section 80CCD(2)</td>
        </tr>
        <tr>
            <td>Gratuity Scheme</td>
            <td>None</td>
            <td>100% funded by company trust</td>
            <td>Tax-free up to 20,00,000 INR</td>
        </tr>
    </table>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Payroll Dispute Resolution</h2>
    <div class="section-content">
        <div class="policy-clause">
            <strong>11.1 Raising a Payroll Query</strong>
            In case of salary credit errors, tax miscalculations, or missing allowances, employees must raise a query via payroll@techvflash.com with their employee ID and digital payslip copy.
        </div>
        <div class="policy-clause">
            <strong>11.2 Payroll Corrections & SLA</strong>
            Approved payroll corrections (such as underpaid allowances) will be processed through an off-cycle payroll run within 3 business days if the discrepancy exceeds 5,000 INR. Minor corrections will be adjusted in the next monthly payroll run.
        </div>
        <div class="policy-clause">
            <strong>11.3 Overpayment Recovery Guidelines</strong>
            If an employee is overpaid due to administrative or system errors, the finance team will notify the employee and adjust the excess amount in the subsequent month's payroll. High overpayment sums may be split over 3 months.
        </div>
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Payroll_Compensation_Policy.pdf"
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")