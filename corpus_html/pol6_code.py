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
            color: #2d3436;
            line-height: 1.5;
            font-size: 10.5pt;
            margin: 0;
        }
        .header {
            border-bottom: 4px solid #0984e3;
            padding-bottom: 15px;
            margin-bottom: 25px;
        }
        .header h1 {
            color: #2d3436;
            margin: 0;
            font-size: 24pt;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .header p {
            margin: 5px 0 0 0;
            color: #636e72;
            font-size: 10pt;
            font-weight: bold;
        }
        h2 {
            color: #0984e3;
            font-size: 13pt;
            background-color: #dfe6e9;
            padding: 8px 12px;
            margin-top: 25px;
            margin-bottom: 15px;
            border-radius: 4px;
            page-break-after: avoid;
        }
        .rule-block {
            background-color: #ffffff;
            border: 1px solid #b2bec3;
            padding: 15px;
            margin-bottom: 15px;
            border-left: 5px solid #0984e3;
            page-break-inside: avoid;
        }
        .rule-block strong {
            display: block;
            color: #2d3436;
            margin-bottom: 5px;
            font-size: 11pt;
        }
        .exception {
            background-color: #ffeaa7;
            border: 1px solid #fdcb6e;
            padding: 12px;
            margin: 15px 0;
            color: #d63031;
            font-weight: bold;
            border-radius: 4px;
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
            border: 1px solid #b2bec3;
            padding: 10px;
            text-align: left;
            font-size: 10pt;
        }
        th {
            background-color: #0984e3;
            color: #ffffff;
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
        <h1>Travel & Expense Policy</h1>
        <p>Document Ref: HR-POL-006 | Effective: June 2026</p>
    </div>

    <p>This policy dictates the guidelines and financial limits for TechV-Flash employees undertaking approved domestic and international business travel. All expenses must adhere to the principles of fiscal responsibility.</p>

    <h2>1. Travel Approvals & Booking</h2>
    <div class="rule-block">
        <strong>1.1 Approval Matrix</strong>
        All domestic travel must be pre-approved by the employee's direct Reporting Manager. International travel requires a dual-approval from the Department Head and the Chief Financial Officer (CFO).
    </div>
    <div class="rule-block">
        <strong>1.2 Advance Booking Mandate</strong>
        Flights must be booked at least 14 days in advance for domestic travel and 30 days in advance for international travel. Late bookings require a justification note approved by the Department Head.
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Transportation Limits</h2>
    <table>
        <tr>
            <th>Employee Grade</th>
            <th>Domestic Flight</th>
            <th>International Flight</th>
            <th>Train Travel</th>
        </tr>
        <tr>
            <td>L1 - L3 (Associates/Seniors)</td>
            <td>Economy Class</td>
            <td>Economy Class</td>
            <td>AC 2-Tier / Shatabdi CC</td>
        </tr>
        <tr>
            <td>L4 - L5 (Leads/Managers)</td>
            <td>Economy Class</td>
            <td>Premium Economy</td>
            <td>AC 1-Tier / Shatabdi EC</td>
        </tr>
        <tr>
            <td>L6+ (Directors/VP)</td>
            <td>Economy Class</td>
            <td>Business Class</td>
            <td>AC 1-Tier / Shatabdi EC</td>
        </tr>
    </table>
    
    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Accommodation Caps (Per Night)</h2>
    <p>Accommodation limits are inclusive of base room tariff and taxes. Employees are encouraged to use TechV-Flash corporate tie-up hotels where available.</p>
    <table>
        <tr>
            <th>City Tier</th>
            <th>L1 - L3 Limit</th>
            <th>L4 - L5 Limit</th>
            <th>L6+ Limit</th>
        </tr>
        <tr>
            <td>Tier 1 (Mumbai, Delhi, Bangalore)</td>
            <td>4,500 INR</td>
            <td>7,500 INR</td>
            <td>12,000 INR</td>
        </tr>
        <tr>
            <td>Tier 2 & Others (e.g., Jaipur, Indore)</td>
            <td>3,000 INR</td>
            <td>5,000 INR</td>
            <td>8,000 INR</td>
        </tr>
        <tr>
            <td>International (Global Average)</td>
            <td>$150 USD</td>
            <td>$250 USD</td>
            <td>Actuals (CFO Approval)</td>
        </tr>
    </table>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Meals & Daily Per Diem</h2>
    <div class="rule-block">
        <strong>4.1 Daily Allowances</strong>
        Employees are eligible for a daily meal allowance of 1,200 INR for domestic travel and $75 USD for international travel. This allowance covers breakfast, lunch, dinner, and incidentals.
    </div>
    
    <div class="exception">
        Alcohol Policy: The cost of alcoholic beverages is strictly non-reimbursable for standard travel. Alcohol expenses are only permitted during approved Client Entertainment events, capped at 2,500 INR per head, and require explicit Vice President (VP) approval on the expense report.
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Expense Submission & Reimbursement</h2>
    <div class="rule-block">
        <strong>5.1 Receipt Mandates</strong>
        Original GST invoices or digitized receipts are mandatory for any individual expense exceeding 500 INR. Credit card slips without itemized bills will be rejected.
    </div>
    <div class="rule-block">
        <strong>5.2 Submission Timeline</strong>
        All expense reports must be submitted via the Zoho Expense portal within 30 calendar days of the trip's completion. Expenses submitted after 30 days will be automatically rejected by the system with no exceptions.
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Entertainment & Client Hospitality</h2>
    <div class="rule-block">
        <strong>6.1 Client Business Meals</strong>
        Client entertainment expenses are permissible only when directly related to the active pursuit of business contracts. The host employee must record client names, designations, and business purposes in the expense portal.
    </div>
    <div class="rule-block">
        <strong>6.2 Spending Caps</strong>
        Hospitality expenditures are capped at 3,000 INR per guest for dinner and 1,500 INR per guest for lunch, excluding service tax. Expenses exceeding these boundaries will require HOD sign-off.
    </div>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Spousal & Dependent Travel</h2>
    <div class="rule-block">
        <strong>7.1 Personal Travel Exclusion</strong>
        TechV-Flash does not fund or reimburse travel, lodging, or meal costs for spouses, children, or family members accompanying employees on corporate assignments.
    </div>
    <div class="rule-block">
        <strong>7.2 Combined Work & Personal Trips</strong>
        If an employee extends a business trip for personal vacation, all additional lodging, flight delta costs, and personal meals are paid directly by the employee. Company corporate card must not be used for personal transactions.
    </div>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Travel Insurance & Medical Emergencies</h2>
    <div class="rule-block">
        <strong>8.1 Corporate Insurance Coverage</strong>
        All employees traveling internationally on behalf of the company are covered by TechV-Flash's group business travel insurance. Coverage details include emergency hospitalization, baggage loss, and flight delay payouts.
    </div>
    
    <h3>8.2 Table of Travel Insurance Coverage Slabs</h3>
    <table>
        <tr>
            <th>Coverage Category</th>
            <th>L1 - L3 Benefit Cap</th>
            <th>L4 - L5 Benefit Cap</th>
            <th>L6+ Benefit Cap</th>
        </tr>
        <tr>
            <td>Emergency Medical Evacuation</td>
            <td>$50,000 USD</td>
            <td>$100,000 USD</td>
            <td>Actual costs (Fully Covered)</td>
        </tr>
        <tr>
            <td>Accidental In-hospitalization</td>
            <td>$20,000 USD</td>
            <td>$50,000 USD</td>
            <td>$100,000 USD</td>
        </tr>
        <tr>
            <td>Baggage Delay / Loss</td>
            <td>$500 USD max</td>
            <td>$1,000 USD max</td>
            <td>$1,500 USD max</td>
        </tr>
    </table>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Vehicle Rental & Local Conveyance</h2>
    <div class="rule-block">
        <strong>9.1 Car Rental Class Permitted</strong>
        Car rentals must be limited to standard compact vehicles unless traveling with more than 3 clients or team members. Executive sedan rentals require VP approval.
    </div>
    <div class="rule-block">
        <strong>9.2 Personal Car Mileage Reimbursements</strong>
        When using personal vehicles for business trips exceeding 20km, employees can claim a fixed per-kilometer mileage rate. The mileage log must start and end at the office or place of residence.
    </div>

    <h3>9.3 Table of Local Conveyance & Mileage Slabs</h3>
    <table>
        <tr>
            <th>Vehicle Category</th>
            <th>Ownership / Profile</th>
            <th>Reimbursement Rate</th>
            <th>Daily Limit Cap</th>
        </tr>
        <tr>
            <td>Two-Wheeler (Motorcycle/Scooter)</td>
            <td>Employee Owned</td>
            <td>6 INR per km</td>
            <td>500 INR daily max</td>
        </tr>
        <tr>
            <td>Four-Wheeler (Hatchback/Sedan)</td>
            <td>Employee Owned</td>
            <td>12 INR per km</td>
            <td>2,000 INR daily max</td>
        </tr>
        <tr>
            <td>Ola/Uber Corporate Profile</td>
            <td>App Booked (Business Account)</td>
            <td>Actual fare (Direct corporate bill)</td>
            <td>Subject to project budget</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Lost or Damaged Baggage & Cancellations</h2>
    <div class="rule-block">
        <strong>10.1 Airline Ticket Cancellations</strong>
        If a trip is cancelled due to business rescheduling or family emergencies, the employee must cancel bookings immediately to minimize cancellation penalties. Refund credits must be directed to the corporate travel card.
    </div>
    <div class="rule-block">
        <strong>10.2 Administrative Procedures</strong>
        For damaged or lost baggage during transit, the employee must file a Property Irregularity Report (PIR) with the airline before leaving the arrival hall, and copy the incident report to the travel desk.
    </div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Non-Reimbursable Expenses Checklist</h2>
    <p>The following table serves as the official guide for identifying items that are strictly personal and cannot be charged to corporate budgets.</p>

    <h3>11.1 Table of Non-Reimbursable Expenses Summary</h3>
    <table>
        <tr>
            <th>Expense Category</th>
            <th>Strictly Prohibited Items</th>
            <th>Approved Exception Cases</th>
        </tr>
        <tr>
            <td>Hotel Room Charges</td>
            <td>In-room movie rentals, mini-bar snacks, personal dry cleaning (trips < 5 days).</td>
            <td>Dry cleaning for business trips exceeding 5 consecutive days.</td>
        </tr>
        <tr>
            <td>Personal Care & Wellbeing</td>
            <td>Spa treatments, hotel gym fees, barber services, beauty parlor visits.</td>
            <td>None.</td>
        </tr>
        <tr>
            <td>Travel Accessories</td>
            <td>Purchase of luggage, power banks, neck pillows, travel adapters.</td>
            <td>IT-Helpdesk approved hardware for urgent staging issues.</td>
        </tr>
        <tr>
            <td>Communication Costs</td>
            <td>International roaming packages without pre-approval, personal phone calls.</td>
            <td>Pre-approved business roaming plans for critical client deliveries.</td>
        </tr>
    </table>

    <!-- Section 12 -->
    <div class="page-break"></div>
    <h2>12. Travel Advances & Reconciliation</h2>
    <div class="rule-block">
        <strong>12.1 Requesting Cash Advances</strong>
        Employees traveling for longer than 7 days or to locations with low digital payment options may request a cash advance via Zoho Expense. Requests must be submitted at least 7 days before departure.
    </div>
    <div class="rule-block">
        <strong>12.2 Outstanding Balance Reconciliation</strong>
        Unused cash advances must be deposited back to the company bank account within 10 days of return. Outstanding balances will be deducted from the payroll if reconciliation is delayed beyond 30 days.
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Travel_Expense_Policy.pdf"
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")