We're excited to introduce the **Traffic Report for Affiliates** — now available under "Reports" section → "Traffic report" tab or at `/partner/traffic_report`. This powerful tool provides your affiliate partners with greater transparency and deeper insight into their traffic performance, mirroring the capabilities previously available only to operators. 

Just like the operator-side version, the affiliate traffic report includes full flexibility in **filters**, **columns**, and **grouping options**. You can configure visibility globally or tailor access for specific affiliates via the "Partner Report" settingspage.**Keep in mind** that affiliates as well as operators will have access to historical data starting from 01/01/2023.

A new **"Traffic Report" tab** has been added to the **"**Partner Report**"** settings page, allowing you to easily customize which components are available to affiliates.

 

As of this release, the default settings for affiliate visibility are as follows:

**Traffic Report Enabled:** `true`

**Filters:** Brands, Campaign IDs, Promo IDs, Promo Codes, Traffic Sources, Visit IP, Visit Countries.

**Columns:** Unique Clicks, Registrations, FTDs Count, Clicks to Regs, Clicks to FTDs, Regs to FTDs.

**Groupers:** Brand, Campaign, Promo, Visit Country, Visit IP, Traffic Source, Period (Day/Week/Month/Year).

 

We've also added the ability to **enable/disable columns** and **reorder them** directly on the "Traffic Report" page — just like you already can on the "Partner Statistics" report.

 

To improve visibility and debugging of data syncs from your casino or sportsbook platform, we’ve introduced a dedicated **Import Logs** page — improving the existing tracking under “Activities/Players sync done/failed/empty” events.

This update brings clarity to sync tracking, helping operators quickly spot and resolve data import issues.

Navigate to **Settings → Import Logs tab** or at `/casino/import_logs`.

This new page presents a structured table listing all import attempts related to player and activity data syncs. Each row in the table represents a sync attempt and includes the following details:

- **Brand**- the brand associated with the import log (sync).
- **Status**- current import status:- **success**(- **green**) - all players/activities were imported successfully
- **partial success**(- **yellow**) - Only part of the players/activities were imported.
- **failed**(- **red**) - None of the players/activities were imported.
- **schema failed**(- **red**) - import request failed due to validation errors.
- **in progress**(- **yellow**) - players/activities is in process of import or queued.
- **empty**(- **black**) - if request contained no data (used to confirm that the syncs are working).
 
- **Progress**- percentage of completion
- **From/To**(- *applicable only for activities*) - indicates the period to which activities sync is related
- **Activities/Players to import**- total number of players/activities sent.
- **Imported activities/players**- count of successfully imported players/activities.
- **Not imported activities/players**- count of players/activities that failed to import.
- **Created at**- timestamp of when the import log was created.
- **Finished at**- timestamp when the final status was assigned.

Quickly locate specific import logs using the filters on the left: "Status", "Brands", "Created at", "Finished at", "Period range" (from-to) filters. Use the tabs in the top-right corner to switch between **Activities** and **Players** views.

On each **Import Log detail page**, you can now see exactly why certain players or activities weren’t imported. This visibility helps you quickly diagnose and resolve sync issues.

|  Reason |  Applies to |  Comment | 
|---|---|---|
| Not bound* | activities | The activity could not be linked to a player due to internal reasons. | 
| Visit not found | activities / players | The visit ID used in the import doesn’t exist — typically caused by using an invalid or non-existent tag (visit id). | 
| Brand mismatch | activities / players | The imported item was linked to a different brand than the one specified. | 
| Currency invalid* | activities | The currency used in the activity is blacklisted (currently ony XTS). | 
| Other not imported* | activities / players | The item wasn’t imported due to other internal system reasons. | 
| Zero | activities | The activity contains only zero values in all fields. | 
| Duplicated | activities | The activity already exists for the same player, brand, period, and currency. | 
| Non-existing bonus code | players | The player wasn't imported due to using non-existing bonus code. | 
| Tracktor error* | players | The system was unable to connect to the redirect application (Tracktor), preventing the import. | 

* For these cases, please contact your Account Manager for further assistance.

If the import log has a **"schema failed"** status, you’ll find the specific failure reason in the **"Fail reason"** field displayed directly beneath the **"Status" **on the import's log detailed page.

In upcoming releases, we’ll remove the legacy **"Activities/Players sync done/failed/empty"** events from the "Events" page and replace them with a smarter, user-friendly version. Stay tuned!


- Report performance optimization with dynamic tag groupers.
- "Skype" filter, fields, etc. are renamed to "Microsoft Teams".
- "Fiat/Coin amount to be paid" is now used for bill-related email events for affiliates.
- UI/UX improvement: 2FA input code field.
- BUG FIX: players commissions are no longer included into subaffiliate commissions autosuggest list during its assignment to affiliates.
- BUG FIX: Traffic report drag&drop groupers order can be changed without any interruptions.
- BUG FIX: Partner Statistics report pagination fix with "Qualified", "Duplicates", "Self-excluded", "Disabled", "FTD conversion rate" enabled columns.
- BUG FIX: During commission creation no longer possible to indicate "space" signs in the beginning and in the end of the strategy name.
- BUG FIX: Duplicated rows under "Partner data" section for subaffiliate bills are no longer displayed.
- BUG FIX: Field names for payments' cashout data are displayed.
- BUG FIX: Stuck reason is displayed on payment's detailed page.
- BUG FIX: Value can be specified in "Min deposits count" field while using "with_deposits" modifier during commission creation.
- BUG FIX: Two factor authorization checkbox is now disabled on partner user's detailed page when 2FA is not set on account.