The **Unconfirmed emails** page gives your affiliate team a dedicated workspace to track and manage registered affiliates who have not yet verified their email addresses.

Since unconfirmed accounts are excluded from the main **Partners** list (/casino/partners), this page ensures no leads are lost in the sign-up funnel. Affiliate managers can use this view to identify stuck users and proactively reach out via Telegram, Teams, or email to assist them through onboarding and convert them into active partners.

- **Navigation:**Partners → Unconfirmed emails
- **URL Path:**- `casino/unconfirmed_emails`
 

**Data Table**

- **Core Columns:**- Email (non-clickable text)
- Company name
- Created at (registration timestamp)
 
- **Dynamic Columns:**Displays all custom fields marked as required for registration in /casino/settings/profile_fields (excluding- *Security question*,- *Security answer*,- *Receive newsletters*, and- *Default currency for reports*).
 

**Available Filters**

- **Emails**- multi-input with autosuggest (matches the behavior on casino/partners).
- **Company names**- multi-input with autosuggest.
- **Microsoft Teams**- multi-input without autosuggest.
- **Telegram**- multi-input without autosuggest.
- **Created at**- date range selector.
 

**CSV Export**

- **Export Name:**Unconfirmed emails
- **Export Content:**Downloads a CSV file containing the exact set of columns displayed in your current table view.