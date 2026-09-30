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
            color: #2d3436;
            line-height: 1.5;
            font-size: 10.5pt;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #8e1c1c;
            color: #ffffff;
            padding: 22px;
            border-radius: 6px;
            margin-bottom: 25px;
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
            color: #8e1c1c;
            font-size: 13pt;
            border-bottom: 2px solid #8e1c1c;
            padding-bottom: 4px;
            margin-top: 22px;
            margin-bottom: 12px;
            page-break-after: avoid;
        }
        h3 {
            color: #2d3436;
            font-size: 11pt;
            margin-top: 14px;
            margin-bottom: 8px;
            page-break-after: avoid;
        }
        .rule-card {
            background-color: #ffffff;
            border-left: 4px solid #8e1c1c;
            border-right: 1px solid #e0e0e0;
            border-top: 1px solid #e0e0e0;
            border-bottom: 1px solid #e0e0e0;
            padding: 12px 14px;
            margin-bottom: 12px;
            page-break-inside: avoid;
            border-radius: 0 4px 4px 0;
        }
        .rule-card strong {
            display: block;
            color: #8e1c1c;
            font-size: 11pt;
            margin-bottom: 4px;
        }
        .alert-box {
            background-color: #fde8e8;
            border: 1px solid #f5c6cb;
            color: #721c24;
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
            border: 1px solid #ddd;
            padding: 9px 10px;
            text-align: left;
        }
        th {
            background-color: #8e1c1c;
            color: #ffffff;
        }
        tr:nth-child(even) {
            background-color: #fafafa;
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
        <h1>Anti-Harassment & Workplace Safety Policy</h1>
        <p>Document Ref: HR-POL-010 | Effective: October 2026 | Location: All TechV-Flash Offices & Remote</p>
    </div>

    <p>TechV-Flash is dedicated to fostering a work environment free of discrimination, harassment, intimidation, and hazards. This document lays out our zero-tolerance stance against workplace harassment, statutory compliance frameworks, and physical emergency procedures.</p>

    <h2>1. Prevention of Sexual Harassment (POSH)</h2>
    <div class="rule-card">
        <strong>1.1 Compliance Framework & POSH Mandate</strong>
        In strict compliance with the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, TechV-Flash has constituted an Internal Committee (IC) to address all complaints of sexual harassment across in-person and digital platforms (Slack, Teams, Email, Offsite events).
    </div>

    <div class="rule-card">
        <strong>1.2 Internal Committee (IC) Composition</strong>
        The IC comprises a Presiding Officer (senior woman employee), two employee members dedicated to social causes or legal compliance, and one external member from an established NGO or legal association.
    </div>

    <div class="rule-card">
        <strong>1.3 Complaint Submission & Inquiry Timeline</strong>
        Any aggrieved person may submit a written complaint to <em>posh@techv-flash.com</em> within 3 months from the date of the incident (extendable up to an additional 3 months by the IC upon written justification). The inquiry must be completed within 90 days of complaint receipt, with the final inquiry report submitted to the CEO within 10 days of completion.
    </div>

    <div class="alert-box">
        <strong>Strict Confidentiality:</strong> As per Section 16 of the POSH Act, identity details of the complainant, respondent, witnesses, and inquiry proceedings must remain confidential. Any employee leaking inquiry information will face immediate termination.
    </div>

    <!-- Section 1 continued -->
    <div class="page-break"></div>
    <h3>1.4 POSH Inquiry Milestones & SLAs</h3>
    <table>
        <tr>
            <th>Inquiry Phase</th>
            <th>Statutory Action Required</th>
            <th>Maximum Legal Timeline</th>
            <th>Output Document Generated</th>
        </tr>
        <tr>
            <td>Complaint Admission</td>
            <td>IC shares copy of complaint with the Respondent for response.</td>
            <td>Within 7 Working Days of receipt</td>
            <td>Notice of Inquiry & Complaint Copy</td>
        </tr>
        <tr>
            <td>Respondent Reply</td>
            <td>Respondent submits written response and list of witnesses.</td>
            <td>Within 10 Working Days of notice</td>
            <td>Written Statement of Defense</td>
        </tr>
        <tr>
            <td>Inquiry Proceedings</td>
            <td>IC conducts cross-examination of parties and witness depositions.</td>
            <td>Completed within 90 Days</td>
            <td>Minutes of Meetings & Hearings Record</td>
        </tr>
        <tr>
            <td>Final Report</td>
            <td>IC submits final findings and recommended actions to CEO & HR.</td>
            <td>Within 10 Days of completion</td>
            <td>Final Inquiry Report & Recommendations</td>
        </tr>
    </table>

    <!-- Section 2 -->
    <div class="page-break"></div>
    <h2>2. General Workplace Harassment & Anti-Bullying</h2>
    <div class="rule-card">
        <strong>2.1 Prohibited Conduct</strong>
        Bullying, verbal abuse, cyber-bullying, public humiliation, derogatory jokes concerning caste, religion, nationality, or identity, and systematic isolation are strictly forbidden. 
    </div>
    <div class="rule-card">
        <strong>2.2 Escalation Process</strong>
        Non-POSH interpersonal harassment complaints must be directed to <em>hr-grievance@techv-flash.com</em> or the direct department head. HR conducts an independent inquiry within 14 business days.
    </div>

    <!-- Section 3 -->
    <div class="page-break"></div>
    <h2>3. Occupational Health & Physical Workplace Safety</h2>
    <div class="rule-card">
        <strong>3.1 Emergency Evacuation & Drills</strong>
        Bi-annual fire and evacuation drills are mandatory for all on-site personnel at Pune HQ. Emergency exit stairwells and fire extinguisher access points must remain clear of all obstructions at all times.
    </div>

    <div class="rule-card">
        <strong>3.2 First Aid & Medical Emergencies</strong>
        Designated first aid kits and certified first-responder employees are present on every floor. For serious medical emergencies on campus, security will contact emergency medical services and notify the emergency contact within 15 minutes.
    </div>

    <!-- Section 4 -->
    <div class="page-break"></div>
    <h2>4. Substance-Free Workplace & Weapons Prohibition</h2>
    <table>
        <tr>
            <th>Prohibited Item / Activity</th>
            <th>Workplace Rule</th>
            <th>Disciplinary Consequence</th>
        </tr>
        <tr>
            <td>Alcohol / Illegal Narcotics Consumption</td>
            <td>Strictly prohibited on office premises, transport shuttles, and company events (except authorized VP-approved client entertainment).</td>
            <td>Immediate suspension pending termination inquiry.</td>
        </tr>
        <tr>
            <td>Firearms, Explosives, or Concealed Weapons</td>
            <td>Zero tolerance on all company property and events without exception.</td>
            <td>Instant termination and police handover.</td>
        </tr>
        <tr>
            <td>Smoking / Vaping</td>
            <td>Permitted only within designated outdoor smoking gazebos.</td>
            <td>Written warning on 1st offense; fine of 1,00,000 INR on subsequent offenses.</td>
        </tr>
    </table>

    <!-- Section 5 -->
    <div class="page-break"></div>
    <h2>5. Workplace Violence Prevention</h2>
    <div class="rule-card">
        <strong>5.1 Identifying Danger Signals</strong>
        Employees are requested to report unusual or threatening behavior (e.g., verbal threats, stalking, physical chest-thumping, destroying company property) to the Security Admin. Early warnings prevent escalation.
    </div>
    <div class="rule-card">
        <strong>5.2 Threat Evaluation Process</strong>
        The safety committee immediately reviews threat reports. If physical harm is threatened, the access badge of the respondent will be deactivated, and they will be suspended pending verification.
    </div>

    <h3>5.3 Table of Physical Safety Hazards & Mitigation</h3>
    <table>
        <tr>
            <th>Hazard Category</th>
            <th>Examples of Risk Source</th>
            <th>Mitigation Action</th>
            <th>Inspection Frequency</th>
        </tr>
        <tr>
            <td>Electrical Safety</td>
            <td>Overloaded multi-sockets, frayed server wiring, exposed cable trays.</td>
            <td>Auto-tripping RCCB breakers, cable management covers.</td>
            <td>Monthly Admin Audit</td>
        </tr>
        <tr>
            <td>Slip, Trip & Fall</td>
            <td>Wet pantry floors, trailing networking cables, loose stair treads.</td>
            <td>"Wet Floor" warning stands, immediate cord tape-downs.</td>
            <td>Daily Janitorial Check</td>
        </tr>
        <tr>
            <td>Fire / Combustion</td>
            <td>Paper storage overload, pantry cooking equipment, server lithium batteries.</td>
            <td>Auto smoke detectors, fire extinguishers, dedicated battery bins.</td>
            <td>Quarterly Vendor Inspection</td>
        </tr>
    </table>

    <!-- Section 6 -->
    <div class="page-break"></div>
    <h2>6. Mental Health Support & Wellbeing</h2>
    <div class="rule-card">
        <strong>6.1 Counseling & EAP Accessibility</strong>
        TechV-Flash provides fully funded access to licensed counselors through our EAP partner. Consults are confidential, and identity details are never shared with HR or reporting managers.
    </div>
    <div class="rule-card">
        <strong>6.2 Psychological Safety</strong>
        We encourage managers to run inclusive, supportive meetings. High-pressure deadlines must be balanced with workload planning. Demeaning criticism or assigning blame in public forums is strictly prohibited.
    </div>

    <!-- Section 7 -->
    <div class="page-break"></div>
    <h2>7. Pandemic & Communicable Disease Safety</h2>
    <div class="rule-card">
        <strong>7.1 Health Screenings & Sanitation</strong>
        During outbreak seasons (e.g., influenza, COVID-19), the company may implement thermal checkups at entry gates. Hand sanitizers are provided at all entry/exit points and meeting rooms.
    </div>
    <div class="rule-card">
        <strong>7.2 Mandatory Quarantine Guidelines</strong>
        Employees testing positive for a contagious infection must report it to HR and undergo mandatory home quarantine for the period recommended by medical officers. WFH will be enabled where health permits.
    </div>

    <h3>7.3 Table of Pandemic Action Level Protocols</h3>
    <table>
        <tr>
            <th>Alert Risk Level</th>
            <th>Office Attendance Cap</th>
            <th>Sanitization Frequency</th>
            <th>Mask / Testing Mandate</th>
        </tr>
        <tr>
            <td>Level Green (Standard)</td>
            <td>100% capacity (Default hybrid)</td>
            <td>Standard daily routine cleaning</td>
            <td>Voluntary</td>
        </tr>
        <tr>
            <td>Level Yellow (Elevated cases)</td>
            <td>50% capacity (Alternate days)</td>
            <td>Twice daily sanitization of touchpoints</td>
            <td>Masks mandatory in meeting rooms</td>
        </tr>
        <tr>
            <td>Level Red (Local outbreak)</td>
            <td>0% capacity (Mandatory fully remote)</td>
            <td>Deep chemical sanitization weekly</td>
            <td>Negative PCR required for essential visits</td>
        </tr>
    </table>

    <!-- Section 8 -->
    <div class="page-break"></div>
    <h2>8. Ergonomic Safety & Workplace Hygiene</h2>
    <div class="rule-card">
        <strong>8.1 Air Quality & Filtration</strong>
        Office air systems are maintained with MERV 13 filtration units. Carbon dioxide levels are monitored constantly in meeting rooms to prevent fatigue and ensure oxygen levels are healthy.
    </div>
    <div class="rule-card">
        <strong>8.2 Office Desk Audits</strong>
        Employees can request ergonomic desk adjustments (such as adding keyboard trays, footrests, or dual-monitor adjustment mounts) by filing a ticket on the admin portal.
    </div>

    <!-- Section 9 -->
    <div class="page-break"></div>
    <h2>9. Safety Audits & Compliance Reviews</h2>
    <div class="rule-card">
        <strong>9.1 Building Stability & Safety Checks</strong>
        The company schedules structural stability checks, lift inspections, and emergency backup generator testing with licensed third-party engineering inspectors annually.
    </div>
    <div class="rule-card">
        <strong>9.2 Electrical Load Management</strong>
        Adding high-load heating or cooling devices (personal heaters, individual ovens) to standard workstation sockets is prohibited to prevent short circuits and fire hazards.
    </div>

    <!-- Section 10 -->
    <div class="page-break"></div>
    <h2>10. Retaliation Protections & Support Systems</h2>
    <div class="rule-card">
        <strong>10.1 Zero Retaliation Guarantee</strong>
        TechV-Flash guarantees that no employee will suffer salary reductions, career blocks, negative performance ratings, or harassment for reporting safety issues or filing harassment complaints.
    </div>
    <div class="rule-card">
        <strong>10.2 Ongoing Counseling Support</strong>
        Complainants and witnesses involved in harassment inquiries are provided free legal and psychological advisory services by the EAP to support their personal recovery.
    </div>

</body>
</html>
"""

output_path = "../corpus/TechV-Flash_Anti_Harassment_Safety_Policy.pdf"
with open(output_path, "w+b") as result_file:
    # pisa.CreatePDF converts the HTML and writes it to the file
    pisa_status = pisa.CreatePDF(html_content, dest=result_file)

if pisa_status.err:
    print("Error generating PDF")
else:
    print(f"File saved successfully at {output_path}")