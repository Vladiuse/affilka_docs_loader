We’ve added a new **Sportsbook Taxes (SB Taxes)** metric to the Partner Statistics report (/casino/report). By default, SB Taxes are subtracted from the NGR calculation. Depending on your project’s **SB Real NGR** formula, the calculation now follows one of the two formats:

- **SB Real NGR**= (SB Bets – SB Cancelled Bets – SB Wins) – SB Bonuses – SB Balance Corrections – SB 3rd Party Fees –- **SB Taxes**, OR
- **SB Real NGR**= (SB Bets – SB Wins) – SB Bonuses – SB Balance Corrections – SB 3rd Party Fees –- **SB Taxes**

In both cases, the **admin fee** is then calculated and subtracted from the Real NGR.

**Where to find it:**

- The **SB Taxes**column is located directly after**SB 3rd Party Fees**in the**Partner Statistics**report.
- The column is **off by default**. To enable it:- Tick the **Casino Taxes Sum**checkbox to display the column.
- To enable it for all affiliates, adjust the **global report visibility settings**at`/casino/settings/partner_report`.
- To enable it for selected affiliates, use the **Settings**tab on the affiliate’s detailed partner page.
 
- Tick the 

The **SB Taxes** metric can be sent by your casino platform provider via API using the `sb_taxes_sum_cents` parameter.

 

In order for you to export your payments and balance corrections information via API, we have created a separate endpoint for the "Payments" and "Balance corrections" pages, available via **/api/customer/v1/casino/payments **and **/api/customer/v1/casino/balance_corrections**. When making requests to the Customer API, you need to send your user’s unique statistic token in the authorisation header. Your unique statistic token can be found on your operator’s detailed page: /casino/users/:user_id page.

When getting a request for a list of payments or balance corrections, the system takes into account the existing "Payments read" or "Balance Corrections" roles that may limit access to payment's data.

You can find new API documentation following the API tab - Customer Operator:

- "Payments" section - "**List of payments with all totals**".
- "Balance Corrections" section - "**Balance corrections list**".
 

IWe’ve added a new validation to the **Activities integration API** to prevent multiple deposits with the **same ID** from being sent for a single player within the same sync.

Previously, this issue could lead to **data inconsistencies** in the **Partner Statistics** and **Traffic Report**.

**How it works:**

- If duplicate deposits are detected, the API will return a **422 Unprocessable Entity**status.
- The response body will contain the error message: `"duplicated deposits"`.
 

In our previous release, we introduced the **"Import Logs"** page (/casino/import_logs) to replace the existing *Activities/Players sync done/failed/empty* events on the **"Events"** page, providing a more convenient and user-friendly experience.

Starting with this release:

- The old *Activities/Players sync done/failed/empty*events have been**removed**.
- A new **Sync Health Check Alert**event has been**added**.

**How it works:**

- The Sync Health Check Alert runs every 2 hours at the 20th minute.
- It will trigger if, during the previous 2 hours, any import log has a status of **Partial Success**,**Failed**, or**Failed Schema**.
- The event pop-up includes direct links to the specific Activities or Players import logs with the relevant statuses.

**In addition, y**ou can subscribe to this event from the **Events** page. When triggered, you’ll receive an **email notification** containing the brand, analysing period and links to the import logs.

 

- News feature: the inserted text formatting are no longer resets during news creation.
- Report calculation process optimization: the newly requested report won't be calculated if the same report from the same users was already requested and is "in progress" status for the last 8 hours.
- "Period range from" and "Period range to" filters are added on the "Import Logs" (/casino/import_logs) page and both support time input. Keep in mind that UTC+0 timezone is used during filter usage.
- BUG FIX: System emails are now send in the same locale as the user's in the interface.
- BUG FIX: Partner Statistics report pagination fix with "Qualified", "Duplicates", "Self-excluded", "Disabled", "FTD conversion rate" enabled columns.
- BUG FIX: Partner statistics and Traffic Report are now available via API for **usual operators**.
- BUG FIX: Two factor authorization field now supports 2fa code autofill via password managers (f.e. Dashlane, 1Password, etc.).
- BUG FIX: On the "Landings", "Media", "Landing Domains" pages, specified page number no longer resets upon page refreshment.
- BUG FIX: "Convert all conditions, qualifiers, rewards into one base currency" field no longer resets when commission is copied.
- BUG FIX: "Subaffiliate assigned" event is created on each subaffiliate assignment.
- BUG FIX: Customer.io integration: the user which is added as a team member for the affiliate is now receiving an email for this action.
- BUG FIX: Emails for "Payment method added" and "Payment method deleted" are sent to the users subscribed to those events.