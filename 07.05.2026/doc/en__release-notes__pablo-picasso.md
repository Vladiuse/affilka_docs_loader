We’ve introduced a powerful feature called **Formula Constructor** that allows operators to create and use their own calculated metrics directly within "Partner Statistics" and "Cohort Analysis" reports — eliminating the need for external tools like Excel, Google Sheets, BI systems and other external analytical systems.

 

- Create custom metrics tailored to your analytical needs
- Use formulas directly in reports and APIs
- Reduce manual calculations and save time
- Gain more flexibility in data analysis
 

In order to create a custom formula, you need to follow:

- **Affiliate Program → Formulas**via Navigator on the left (or directly- `/casino/formulas`) where you can find the list of all your created formulas.
- Click on "New" button in the upper right corner of the page (or directly`/casino/formulas`/new)
- Fill up the form:- **Name**(required)
- **API Identifier**(required, must be unique, lowercase a–z only)
- **Description**(optional)
- **Formula Constructor**(required)
 
- Click on "Save as a draft" button.

**Keep in mind** that formulas are created at the affiliate program level (not at the user level) and apply to all operators within that program.

 

| Name | Desired formula name that will be displayed in the reports. | 
|---|---|
| API Identifier | A unique formula identifier that will be used to export this formula via Customer API /api/customer/v1/casino/report. | 
| Description | A free description of the formula, what problem it solves, why it was added, etc. | 
| Formula constructor | A formula builder that works similarly to Excel, allowing you to create custom calculations. 
 All raw metrics available in the *Partner Statistics*reports (e.g., Visits, Registrations, FTDs, Deposits, Bets, etc.), excluding Partner Income, reward-based columns, and Payable Casino NGR.You can select metrics from the
 **Metrics**dropdown.
 
 Addition (+), subtraction (-), multiplication (×), and division (÷). You can also use brackets ( ) to control the order of operations.You can use both whole numbers (e.g., 1, 2, 3) and decimal numbers (e.g., 1.5, 2.6, 3.79) in your formulas.**Note:**Whole and decimal numbers can't be added to or subtracted from monetary metrics (e.g., FTD Sum, Bets Sum, Cashouts Sum, etc.).
 | 

Once a formula is saved as a draft, it can be published by clicking the “Publish” button in the upper-right corner of the formula's detailed page (`/casino/formulas/:id`).

After publishing, the formula becomes **available** in:

- **Reports:**- `/casino/report`(under the- *Columns*section, at the bottom)
- `/casino/cohort_report`(at the bottom)
 
- **Dashboard:**Usable in- *Quick Stats*and- *Charts*
- **API:**Available via Customer API:- `/api/customer/v1/casino/report`using its API Identifier
- **Partner Reports:**- Can be enabled in Custom Columns under: - `/casino/settings/partner_report`
- `/casino/partners/:id/settings/partner_report`
 
- Once enabled, it appears in the partner’s *Statistics*report (`/partner/report`)
 
 
- Can be enabled in Custom Columns under: 

Formulas can be archived in both **Draft** and **Published** states. Unarchiving action is not possible.

If a published formula is archived (via the “Archive” button on `/casino/formulas/:id`), it becomes **unavailable** in:

- **Reports:**- `/casino/report`
- `/casino/cohort_report`
 
- **Dashboard:**Quick Stats and Charts
- **API:**- `/api/customer/v1/casino/report`
- **Partner Reports:**- Custom Columns settings:- `/casino/settings/partner_report`
- `/casino/partners/:id/settings/partner_report`
 
- Previously enabled formulas will no longer appear in the partner *Statistics*report (`/partner/report`)
 
 
- Custom Columns settings:

The formula can be edited at any time and in any state. Changes take effect immediately. 

This can be done by clicking on the "Edit" button on the formula's detailed page (`/casino/formulas/:id`).

 

- `Click-to-registration = (Registrations/ Visits count) * 100%`

- `Click-to-FTDs = (FTD count/ Visits count) * 100%`

- `FTDs/Deposits ratio = (FTD count / Deposits count) * 100%`

- `SB Bonus Ratio = (Sportsbook Bonuses / Deposits Sum) * 100%`

- `Average Deposit per FTD = Deposits sum / FTD count`

- `Deposit Frequency = Deposits count / FTD count`

- `Casino ARPU = Casino Real NGR / Casino active players`

- `Casino ARPPU = Casino Real NGR / Depositors`

- Formulas are currently **not supported**in the Commission Constructor.
- All of the custom formulas are calculated on the currency level.
 

We have introduced an email confirmation step during the sign-up process of the affiliate. This update is designed to enhance account security, ensure valid communication channels for password recovery, and protect affiliate programs from unauthorized automated registrations.**Keep in mind** that we haven't enabled this feature with this release automatically, your Account Manager will contact you upfront regarding its enabling. 

In which cases affiliates must confirm their email?

- **Self-Registered Partners**: All affiliates who register via the public sign-up form must now confirm their email addresses. The confirmation link will be sent to the mentioned email right after submitting the registration form.- **Link Lifetime:**Each confirmation link is valid for- **one week**.- **Automated Trust:**Affiliates (as well as Partner users(Team members)) added manually by the Operator or by Affiliates are marked as "Auto-confirmed" and do not require additional confirmation.
- **Functional Restrictions:**Until the email is confirm, the affiliate will not appear in the partner list (- `/casino/partners`), and entities like default campaigns or commissions will not be assigned or created for this affiliate.
 

**Manual Confirmation Link Request**

We’ve added a new interface and endpoint (`/partner/confirmation/new`) that allows partners to manually request a new confirmation link if the original email was lost, the link has expired or the link hasn't worked for various reasons.

**Improved Verification Workflow**

The "Partner Verification Required" setting which may be enabled for your Affiliate Program has been updated to align with the new email confirmation flow:

- If **Partner Verification Required (True)**: Manual operator approval is only possible*after*the partner has confirmed their email.
- If **Partner Verification Required (False)**: Automatic system verification occurs immediately*after*the email is confirmed.

**Customer.io Integration**

- Updated the system to support the `partner_email_confirmation`event.
- The event payload now includes a secure **token**required to complete the verification process via email.
 

We are excited to announce that we have migrated our API documentation to **Swagger UI**. This transition aims to provide a more streamlined and intuitive experience for everyone integrating with our product. While all existing functionality remains fully accessible, you’ll now enjoy a much clearer structure, featuring enhanced visualization of request parameters, response schemas, and authentication methods.

Access all Affilka API documentation via the **API tab** in the left-hand navigation menu or simply `/casino/api_docs/customer_casino` for "Customer API" and `/casino/api_docs/v1` for "Integration" sections.

View of updated API UI:

- Traffic Report (/casino/traffic_report):- New "Stag visits" filter using which you can get more detailed info on the particular visit of the player.
- This filter can be enabled for Affiliates, using Global and Individual partner report settings pages `/casino/settings/partner_report`and`/casino/partners/:id/settings/partner_report`
 
- Traffic source list is updated with "Google Display Network (GDN)".
- Commissions page (/casino/commissions):- "Partners count" column is implemented. Clicking the column redirects you to the 'List of Partners', filtered to show those **assigned this commission**or those with**this commission active in their campaigns**.
- "Forgive debts" filter is implemented which filters commissions by Forgive debts feature usage.
- "Commission IDs" filter is implemented on the "List of Partners" page (/casino/partners) as well.
 
- "Partners count" column is implemented. Clicking the column redirects you to the 'List of Partners', filtered to show those 
- Changed xlsx-files naming related to reports, naming logic as follows:- Partner Statistics: `[report_name]_activities_report_[from]_[to]`, f.e.`daily_performance_activities_report_2026-04-08_2026-04-08`
- Cohort Analysis: `[report_name]_cohort_report_[from]_[to]`
- Traffic report: `traffic_report_[from]_[to]`
 
- Partner Statistics: 
- Import logs page (/casino/import_logs): "Created at" filter is mandatory while using this page, a default range of last 3 months is suggested. Maximum analysis period is 6 months.
- Roles: "Payment methods verification" page (/casino/payment_methods) accessibility is now managed only by "Payments verification" ability.
- BUG FIX: Postback is submitted successfully once postback event is changed.
- BUG FIX: Quick stats works correctly with disabled Casino/Sportsbook/Poker modules.
- BUG FIX: The 'Apply' button in Quick Stats is no longer overlaped by the brand autosuggest dropdown.
- BUG FIX: Commission templates are displayed correctly for usual operators.
- BUG FIX: Batch action: remove tags is working correctly on "Partners" page (/casino/partners).
- BUG FIX: "Bills" page (/casino/bills/:id) no longer crashes in some cases.
- BUG FIX: The {payout} parameter is being sent correctly with the correct number of decimal places.
- BUG FIX: "Parent affiliate ID" filter is fixed on "Subaffiliate" report page (/casino/subaffiliate_report).
- BUG FIX: Changing partner's state via dropdown on "Partners" page is fixed.