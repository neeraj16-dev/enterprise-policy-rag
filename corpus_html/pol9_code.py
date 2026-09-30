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
            color: #2c3e50; 
            line-height: 1.6; 
            font-size: 10.5pt; 
            margin: 0; 
        }
        .header-section { 
            border-top: 8px solid #c0392b; 
            padding-top: 20px; 
            margin-bottom: 30px; 
            text-align: center; 
        }
        .header-section h1 { 
            color: #2c3e50; 
            font-size: 26pt; 
            margin: 0 0 10px 0; 
            text-transform: uppercase; 
            letter-spacing: 1px;
        }
        .header-section p { 
            color: #7f8c8d; 
            font-size: 10pt; 
            margin: 0; 
            font-weight: bold;
        }
        h2 { 
            color: #c0392b; 
            font-size: 14pt; 
            margin-top: 30px; 
            border-bottom: 2px solid #ecf0f1; 
            padding-bottom: 5px; 
            page-break-after: avoid; 
        }
        .policy-item { 
            background-color: #ffffff; 
            border: 1px solid #e0e0e0;
            border-left: 4px solid #2c3e50; 
            padding: 15px; 
            margin-bottom: 15px; 
            page-break-inside: avoid; 
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .policy-item strong { 
            display: block; 
            color: #2c3e50; 
            margin-bottom: 5px; 
            font-size: 11.5pt; 
        }
        .whistleblower { 
            background-color: #fcf3cf; 
            border: 1px solid #f1c40f; 
            padding: 15px; 
            margin-top: 20px; 
            border-radius: 4px; 
            page-break-inside: avoid; 
        }
        .whistleblower strong {
            color: #b7950b;
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
            border: 1px solid #bdc3c7;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #2c3e50;
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

    <div class="header-section">
        <h1>Code of Conduct</h1>
        <p>Document Ref: LEG-POL-009 | Effective: September 2026</p>
    </div>

    <p>At TechV-Flash, our reputation is built on trust, integrity, and ethical business practices. This Code of Conduct outlines the expected professional behavior for all employees, officers, and directors representing the company.</p>

    <h2>1. Professional Behavior & Respect</h2>
    <div class="policy-item">
        <strong>1.1 Mutual Respect</strong>
        Employees must treat colleagues, clients, and vendors with dignity and respect. TechV-Flash maintains a zero-tolerance policy for bullying, intimidation, or exclusionary behavior in physical or virtual workspaces.
    </div>
    <div class="policy-item">
        <strong>1.2 Public Representation</strong>
        When attending conferences, client sites, or posting on professional social media (e.g., LinkedIn), employees must conduct themselves in a manner that upholds the company’s reputation. Derogatory remarks about competitors or clients are strictly prohibited.
    </div>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. Conflicts of Interest</h2>
    <p>A conflict of interest arises when an employee's personal interests interfere, or appear to interfere, with the best interests of TechV-Flash.</p>
    <div class="policy-item">
        <strong>2.1 Outside Employment & Moonlighting</strong>
        Full-time employees are prohibited from engaging in secondary employment (moonlighting) or consulting work that competes with TechV-Flash or interferes with their primary job duties without prior written approval from HR and the CEO.
    </div>
    <div class="policy-item">
        <strong>2.2 Financial Interests</strong>
        Employees must not hold a significant financial interest (over 5% ownership) in any of TechV-Flash's competitors, suppliers, or clients unless fully disclosed to and approved by the Legal Department.
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Anti-Bribery & Gifts</h2>
    <div class="policy-item">
        <strong>3.1 Acceptance of Gifts</strong>
        Employees may not accept gifts, favors, or entertainment from clients or vendors that could influence business decisions. Occasional, nominal gifts (e.g., festive sweets, corporate swag) valued under 2,000 INR are permissible.
    </div>
    <div class="policy-item">
        <strong>3.2 Prohibition of Bribes</strong>
        TechV-Flash strictly complies with the Prevention of Corruption Act. Employees must never offer, promise, authorize, or accept bribes, kickbacks, or any other improper payments to secure business advantages or government approvals.
    </div>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Protection of Company Assets</h2>
    <div class="policy-item">
        <strong>4.1 Proper Use</strong>
        Company assets, including funds, equipment, software, and physical facilities, must be used solely for legitimate business purposes.
    </div>
    <div class="policy-item">
        <strong>4.2 Intellectual Property</strong>
        All code, designs, documents, and concepts developed by an employee during their tenure at TechV-Flash remain the exclusive intellectual property of the company. 
    </div>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Whistleblower & Non-Retaliation Policy</h2>
    <div class="whistleblower">
        <strong>Reporting Violations:</strong>
        <p>If you suspect a violation of this Code, you have a duty to report it. Reports can be made anonymously via the internal portal or by emailing ethics@techv-flash.com.</p>
        <p><strong>Non-Retaliation:</strong> TechV-Flash strictly prohibits retaliation against any employee who, in good faith, reports a suspected violation or participates in an ethics investigation.</p>
    </div>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Political & Charitable Contributions</h2>
    <div class="policy-item">
        <strong>6.1 Personal Political Involvement</strong>
        Employees may participate in political processes in their personal capacity outside work hours and off company premises. However, employees must not use TechV-Flash funds, facilities, or properties to support any political party or candidate.
    </div>
    <div class="policy-item">
        <strong>6.2 Corporate Contributions</strong>
        All corporate charitable contributions must be routed through the Corporate Social Responsibility (CSR) committee and require final approval from the Board of Directors to ensure legal compliance.
    </div>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Insider Trading & Market Abuse</h2>
    <div class="policy-item">
        <strong>7.1 Material Non-Public Information (MNPI)</strong>
        Employees who have access to confidential, price-sensitive corporate records (e.g., pending merger deals, financial results prior to public disclosure) are strictly prohibited from trading in company shares or tipping others to trade.
    </div>
    <div class="policy-item">
        <strong>7.2 Trading Windows</strong>
        Designated key employees are subject to strict trading window restrictions, typically closing 15 days before the end of each fiscal quarter and opening 48 hours after financial results are published.
    </div>

    <h3>7.3 Table of Insider Trading Window Closures</h3>
    <table>
        <tr>
            <th>Financial Event / Period</th>
            <th>Window Closure Commencement</th>
            <th>Window Re-opening Date</th>
            <th>Designated Restricted Persons</th>
        </tr>
        <tr>
            <td>Q1 Financial Results (Apr - Jun)</td>
            <td>June 15th</td>
            <td>48 Hours post Board approval announcement</td>
            <td>All directors, finance teams, and executive staff</td>
        </tr>
        <tr>
            <td>Q2 Financial Results (Jul - Sep)</td>
            <td>September 15th</td>
            <td>48 Hours post Board approval announcement</td>
            <td>All directors, finance teams, and executive staff</td>
        </tr>
        <tr>
            <td>Q3 Financial Results (Oct - Dec)</td>
            <td>December 15th</td>
            <td>48 Hours post Board approval announcement</td>
            <td>All directors, finance teams, and executive staff</td>
        </tr>
        <tr>
            <td>Q4 Annual Audited Results (Jan - Mar)</td>
            <td>March 15th</td>
            <td>48 Hours post Board approval announcement</td>
            <td>All directors, finance teams, and executive staff</td>
        </tr>
    </table>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Fair Competition & Anti-Trust Laws</h2>
    <div class="policy-item">
        <strong>8.1 Interactions with Competitors</strong>
        Employees must not enter into agreements or discussions with competitors to fix product pricing, divide market segments, rig client bids, or boycott specific suppliers.
    </div>
    <div class="policy-item">
        <strong>8.2 Trade Association Participation</strong>
        When attending technology trade associations, employees must leave immediately if competitors begin discussing unannounced pricing structures, bidding strategies, or resource allocations.
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Media Relations & Public Disclosure</h2>
    <div class="policy-item">
        <strong>9.1 Communication Protocol</strong>
        To ensure accurate information dissemination, only designated spokespersons authorized by the CEO are permitted to speak to journalists or issue press statements on behalf of TechV-Flash.
    </div>
    <div class="policy-item">
        <strong>9.2 Speaking at External Conferences</strong>
        Employees invited to speak at public forums, panel discussions, or academic events as representatives of the company must submit their presentation slide deck to the PR team for approval at least 7 days before the event.
    </div>

    <h3>9.3 Table of Media Request Handling Protocols</h3>
    <table>
        <tr>
            <th>Inquiry Source</th>
            <th>Request Source</th>
            <th>Required Internal Routing Target</th>
            <th>Standard Response SLA</th>
        </tr>
        <tr>
            <td>Financial performance & audits</td>
            <td>Business News Reporters / Analysts</td>
            <td>Chief Financial Officer (CFO) & CEO office</td>
            <td>24 Hours</td>
        </tr>
        <tr>
            <td>Product launch & tech disclosures</td>
            <td>Tech Blogs / PR agencies</td>
            <td>VP of Product & Marketing Director</td>
            <td>48 Hours</td>
        </tr>
        <tr>
            <td>Crisis incidents or legal disputes</td>
            <td>General Print & Digital Media</td>
            <td>Data Protection Officer & Chief Legal Counsel</td>
            <td>Immediate (Within 2 Hours)</td>
        </tr>
    </table>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Equal Employment & Harassment-Free Workspace</h2>
    <div class="policy-item">
        <strong>10.1 Diversity & Equal Opportunity</strong>
        Employment decisions (hiring, training, promotions) are based entirely on qualification and performance. TechV-Flash will not tolerate any discrimination based on race, gender, religion, or orientation.
    </div>
    <div class="policy-item">
        <strong>10.2 Respectful Physical & Virtual Workspaces</strong>
        All communications via Slack, email, or client tools must remain professional. Using offensive language or posting inappropriate images is classified as a code of conduct violation.
    </div>

    <!-- Section 11 -->
    <div class="page-break"></div>
    <h2>11. Health, Safety & Environmental Integrity</h2>
    <div class="policy-item">
        <strong>11.1 Green Workplace Commitment</strong>
        Employees are requested to support sustainability efforts by minimizing paper printing, switching off unused workspace lighting, and separating wet and dry waste at trash stations.
    </div>
    <div class="policy-item">
        <strong>11.2 E-Waste Disposal Standards</strong>
        Obsolete computers, monitors, mobile phones, and cables must not be thrown in general waste bins. All hardware disposal must be processed via the IT Admin's certified e-waste vendor.
    </div>

    <!-- Section 12 -->
    <div class="page-break"></div>
    <h2>12. Ethical AI & Technology Usage</h2>
    <div class="policy-item">
        <strong>12.1 Generative AI Tool Protocols</strong>
        Code development using GenAI tools must only be performed on approved enterprise-licensed platforms. Pasting proprietary source code, client databases, or PII into public AI models is strictly prohibited.
    </div>
    <div class="policy-item">
        <strong>12.2 Open Source Compliance</strong>
        Before integrating open-source packages containing restrictive licensing (e.g., GPL) into proprietary software codebases, developers must obtain clearance from the engineering architecture committee.
    </div>

    <h3>12.3 Table of Gift & Hospitality Approval Thresholds</h3>
    <table>
        <tr>
            <th>Gift/Hospitality Value</th>
            <th>Relationship Type</th>
            <th>Required Action</th>
            <th>Final Approving Authority</th>
        </tr>
        <tr>
            <td>Below 2,000 INR</td>
            <td>Active Vendor / Client Relationship</td>
            <td>No disclosure needed (Nominal/Festive sweets)</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>2,000 INR to 10,000 INR</td>
            <td>Active Vendor / Client Relationship</td>
            <td>Submit Gift Disclosure Form in HR Portal within 5 days</td>
            <td>Reporting Manager & HOD</td>
        </tr>
        <tr>
            <td>Above 10,000 INR</td>
            <td>Active Vendor / Client Relationship</td>
            <td>Strictly prohibited; decline politely or hand over to HR for auction</td>
            <td>Chief Legal Counsel</td>
        </tr>
    </table>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Code_of_Conduct_Policy.pdf"
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")