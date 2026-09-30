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
            color: #333;
            line-height: 1.5;
            font-size: 10.5pt;
            margin: 0;
        }
        .header {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 6px;
            margin-bottom: 25px;
        }
        .header h1 {
            margin: 0 0 5px 0;
            font-size: 24pt;
        }
        .header p {
            margin: 0;
            font-size: 10pt;
            opacity: 0.8;
        }
        h2 {
            color: #e74c3c;
            font-size: 14pt;
            border-bottom: 2px solid #e74c3c;
            padding-bottom: 5px;
            margin-top: 25px;
            page-break-after: avoid;
        }
        h3 {
            color: #2c3e50;
            font-size: 11.5pt;
            margin-top: 15px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }
        .policy-section {
            margin-bottom: 20px;
        }
        .clause {
            background-color: #f8f9fa;
            border-left: 3px solid #2c3e50;
            padding: 10px 15px;
            margin-bottom: 12px;
            page-break-inside: avoid;
        }
        .clause strong {
            display: block;
            color: #c0392b;
            margin-bottom: 4px;
        }
        .note {
            background-color: #eef2f5;
            border: 1px solid #d2d6de;
            padding: 12px;
            border-radius: 4px;
            font-size: 9.5pt;
            margin: 15px 0;
            page-break-inside: avoid;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 10pt;
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px 10px;
            text-align: left;
        }
        th {
            background-color: #ecf0f1;
            color: #2c3e50;
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
        <h1>Benefits & Insurance Policy</h1>
        <p>Document Ref: HR-POL-005 | Effective: May 2026</p>
    </div>

    <p>TechV-Flash provides a comprehensive benefits package designed to support the physical, mental, and financial well-being of our employees. This policy outlines the insurance coverage and wellness benefits available to eligible staff.</p>

    <h2>1. Group Health Insurance (GHI)</h2>
    <div class="policy-section">
        <p>TechV-Flash partners with leading insurers to provide cashless medical coverage across a wide network of hospitals in India. Coverage begins on Day 1 of employment, with pre-existing diseases covered immediately (waiver of waiting period).</p>
        
        <h3>1.1 Coverage Tiers</h3>
        <table>
            <tr>
                <th>Employee Category</th>
                <th>Sum Insured (Annual)</th>
                <th>Dependents Covered</th>
            </tr>
            <tr>
                <td>L1 - L3 (Associates to Seniors)</td>
                <td>5,00,000 INR</td>
                <td>Employee, Spouse, up to 2 Children</td>
            </tr>
            <tr>
                <td>L4 - L6 (Leads & Management)</td>
                <td>10,00,000 INR</td>
                <td>Employee, Spouse, up to 2 Children</td>
            </tr>
        </table>
        
        <div class="clause">
            <strong>1.2 Parental Coverage (Voluntary)</strong>
            Employees may opt to add up to two parents or parents-in-law to their policy during the annual enrollment window. The premium for parental coverage is funded entirely by the employee via monthly payroll deductions. Parental coverage is subject to a 20% co-payment on all claims.
        </div>
        
        <div class="clause">
            <strong>1.3 Maternity Benefits</strong>
            The GHI policy includes maternity coverage up to 50,000 INR for normal delivery and 75,000 INR for C-section, with a waiver of the standard 9-month waiting period.
        </div>
        
        <div class="clause">
            <strong>1.4 Room Rent Limits</strong>
            Room rent is capped at 1% of the total sum insured per day for normal rooms and 2% per day for ICU admissions.
        </div>
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Additional Insurance Policies</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>2.1 Group Term Life Insurance (GTLI)</strong>
            TechV-Flash provides fully employer-funded Term Life Insurance for all Full-Time Employees. The sum assured is equivalent to 3x the employee's annual Fixed CTC. This benefit is payable to the designated nominee in the event of the employee's death.
        </div>
        
        <div class="clause">
            <strong>2.2 Group Personal Accident Insurance (GPA)</strong>
            This policy covers employees for accidental death or disability. The coverage limit is 20,00,000 INR. It includes provisions for temporary total disability (income replacement) and permanent partial disability.
        </div>
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Wellness & Lifestyle Benefits</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>3.1 Annual Wellness Stipend</strong>
            Eligible employees receive an annual wellness stipend of 12,000 INR. This stipend operates on a reimbursement model and can be used for gym memberships, fitness classes, or specialized wellness apps. 
        </div>
        <div class="note">
            <strong>Tax Implication:</strong> As per Section 17(2) of the Income Tax Act, wellness stipends paid as cash reimbursements are considered taxable perquisites and will be reflected in the employee's Form 16.
        </div>

        <div class="clause">
            <strong>3.2 Employee Assistance Program (EAP)</strong>
            Employees have access to 24/7 confidential counseling services for mental health, financial, or legal advice, fully funded by the company.
        </div>
    </div>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Claims & Reimbursement Process</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>4.1 Cashless GHI Claims</strong>
            For planned hospitalizations, employees must notify the TPA (Third Party Administrator) via the insurer's portal at least 48 hours in advance to secure cashless approval.
        </div>
        <div class="clause">
            <strong>4.2 GHI Reimbursement Claims</strong>
            If treated at a non-network hospital, employees must settle the bill and submit a reimbursement claim within 15 days of discharge, including original bills, discharge summaries, and diagnostic reports.
        </div>
        <div class="clause">
            <strong>4.3 Wellness Stipend Claims</strong>
            Wellness stipend claims must be submitted quarterly via the internal expense portal with valid GST invoices. Submissions without proper documentation will be rejected.
        </div>
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Dental & Vision Care Coverage</h2>
    <div class="policy-section">
        <p>To ensure basic healthcare, the company offers coverage for dental and vision consults and interventions, outside standard medical hospitalization.</p>
        
        <div class="clause">
            <strong>5.1 Dental Treatment Reimbursement</strong>
            Employees can claim up to 5,000 INR annually for non-cosmetic dental treatments (e.g., fillings, root canals, extractions). Cosmetic dental surgeries or orthodontic braces are excluded from reimbursement.
        </div>
        
        <div class="clause">
            <strong>5.2 Vision Care Allowance</strong>
            An allowance of 3,000 INR every two financial years is provided for eye checkups and the purchase of corrective lenses/spectacles. Valid prescription copies and tax invoices are required for processing claims.
        </div>
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Maternity, Paternity & Creche Benefits</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>6.1 Adoption Support Stipend</strong>
            To support diverse family choices, TechV-Flash offers an Adoption Support Stipend of 50,000 INR for employees legally adopting a child under 3 years of age. This helps cover legal filings and agency fees.
        </div>
        
        <div class="clause">
            <strong>6.2 Creche Allowance & Tie-ups</strong>
            Under statutory norms, the company has partnered with premium daycares near the Pune HQ. Employees are eligible for a daycare subsidy of up to 6,000 INR per month for children aged 6 months to 6 years.
        </div>
    </div>

    <h3>6.3 Table of Corporate Creche Tie-ups</h3>
    <table>
        <tr>
            <th>Creche Partner Name</th>
            <th>Location / Coverage</th>
            <th>Eligible Age Range</th>
            <th>Monthly Subsidy (Max)</th>
        </tr>
        <tr>
            <td>Little Angels Daycare</td>
            <td>Kalyani Nagar, Pune</td>
            <td>6 Months to 4 Years</td>
            <td>6,000 INR per month</td>
        </tr>
        <tr>
            <td>First Steps Early Learning</td>
            <td>Kharadi, Pune</td>
            <td>1 Year to 6 Years</td>
            <td>5,000 INR per month</td>
        </tr>
        <tr>
            <td>Kidzee Play & Care</td>
            <td>Hinjewadi Phase 1, Pune</td>
            <td>6 Months to 5 Years</td>
            <td>5,500 INR per month</td>
        </tr>
    </table>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Corporate Discounts & Perks</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>7.1 Technology purchase program</strong>
            Employees are eligible for 10% discount codes on specific hardware manufacturers (e.g., Apple, Dell) for personal purchases. Once a device reaches 3 years of age, employees can buy back corporate laptops at depreciated scrap values.
        </div>
        <div class="clause">
            <strong>7.2 Hotel & Travel Discounts</strong>
            Our corporate flight and hotel rates (typically saving 15-20% compared to retail prices) can be utilized by employees for their personal/family leisure travels when booked via the corporate travel desk.
        </div>
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Education & Skill Development Benefits</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>8.1 Professional Certifications</strong>
            Employees can seek 100% reimbursement for approved technical and management certifications (e.g., AWS, PMP, Scrum Master). The certification must align with current or future business needs and require manager pre-approval.
        </div>
        <div class="clause">
            <strong>8.2 Tuition Assistance for Higher Studies</strong>
            For employees pursuing executive degrees or diplomas, a partial tuition reimbursement of up to 1,00,000 INR per year is available. A service bond of 1 year applies post-completion of the program.
        </div>
    </div>

    <h3>8.1 Table of Tuition & Certification Reimbursements</h3>
    <table>
        <tr>
            <th>Role Grade Level</th>
            <th>Certification Reimbursement</th>
            <th>Annual Tuition Reimbursement Cap</th>
            <th>Minimum Passing/Completion Grade</th>
        </tr>
        <tr>
            <td>L1 - L2 (Associate Roles)</td>
            <td>100% on approved list</td>
            <td>50,000 INR</td>
            <td>B Grade / Pass certificate</td>
        </tr>
        <tr>
            <td>L3 - L4 (Senior & Lead Roles)</td>
            <td>100% on approved list</td>
            <td>75,000 INR</td>
            <td>B Grade or above</td>
        </tr>
        <tr>
            <td>L5 - L6 (Managers & Directors)</td>
            <td>100% on approved list</td>
            <td>1,00,000 INR</td>
            <td>B Grade or above</td>
        </tr>
    </table>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Mental Health & Critical Illness Rider</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>9.1 Health Coaching & Consults</strong>
            Employees have access to virtual health coaching sessions covering nutrition, sleep management, and customized workout plans, fully funded by TechV-Flash.
        </div>
        <div class="clause">
            <strong>9.2 Critical Illness Support Rider</strong>
            An additional critical illness rider of 3,00,000 INR is attached to the GHI policy, providing a lump-sum payout upon diagnosis of designated critical conditions (e.g., stroke, major organ transplant, heart disease).
        </div>
    </div>

    <h3>9.3 Table of Critical Illness Cover Details</h3>
    <table>
        <tr>
            <th>Illness Category</th>
            <th>Sum Insured Provision</th>
            <th>Co-pay Requirement</th>
            <th>Waiting Period</th>
        </tr>
        <tr>
            <td>Major Cancers & Tumors</td>
            <td>3,00,000 INR (Lump-sum)</td>
            <td>None</td>
            <td>90 Days from policy inception</td>
        </tr>
        <tr>
            <td>First Heart Attack & Stroke</td>
            <td>3,00,000 INR (Lump-sum)</td>
            <td>None</td>
            <td>90 Days from policy inception</td>
        </tr>
        <tr>
            <td>Kidney Failure / Organ Transplant</td>
            <td>3,00,000 INR (Lump-sum)</td>
            <td>None</td>
            <td>90 Days from policy inception</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Special Leave Allowances & Awards</h2>
    <div class="policy-section">
        <div class="clause">
            <strong>10.1 Marriage Gift Voucher</strong>
            A congratulatory cash gift voucher of 10,000 INR is given to employees celebrating their marriage. This is processed in the subsequent payroll cycle upon submission of the marriage registration certificate.
        </div>
        <div class="clause">
            <strong>10.2 Long Service Milestone Award</strong>
            TechV-Flash celebrates employee loyalty. Milestone achievements are recognized with corporate plaques and custom reward grants:
            <ul>
                <li>3 Years: Bronze plaque & 25,000 INR cash bonus</li>
                <li>5 Years: Silver plaque & 50,000 INR cash bonus</li>
                <li>10 Years: Gold plaque & 1,00,000 INR cash bonus</li>
            </ul>
        </div>
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Benefits_Insurance_Policy.pdf"
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")