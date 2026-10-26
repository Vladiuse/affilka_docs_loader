Released on June 23, 2026


- Brand Access Control for Operators
- Document Upload For Payments
- Balancer Domains Management
- Other changes and improvements
- Detailed information about the release features

Released on April 21, 2026


- Formula Constructor
- Affiliate email confirmation
- API section: updated UI
- Other changes and improvements
- Detailed information about the release features

Released on February 17, 2026


- Commission templates
- Postbacks: {payout} parameter for prequalified and qualified actions
- Priority parameters for promos
- Roles: "Balance Corrections Read" and "Balance Corrections Process"
- Partner archiving
- UI and usability improvements
- Other changes and improvements
- Detailed information about the release features

Released on December 16, 2025


- HTML5 Banners
- New report columns: casino and sportsbook active players
- Traffic Report: filter and group by player
- Reports: "Traffic sources" filter
- Customer API: new pages
- Other changes and improvements
- Detailed information about the release features

Released on October 21, 2025


- Subaffiliate report
- Hierarchy-based roles management (aka General Manager)
- Traffic Report: filter and group by dynamic tags
- Dynamic deep linking
- Operator Interface: player reassignment
- Other changes and improvements
- Detailed information about the release features

Released on August 20-26, 2025


- Sportsbook NGR formula: taxes deduction
- Customer API: “Payments” and “Balance corrections” pages
- New event: Sync health check alert
- Activities import: new validation added
- Other changes and improvements
- Detailed information about the release features

Released on June 24-26, 2025


- Traffic Report for Affiliates
- Import logs page
- Report performance optimization
- Other changes and improvements
- Detailed information about the release features

Released on May 20-22, 2025


- Cross-brand duplicates feature
- Commission constructor: subaffiliate NGR-based reward type and condition
- Landings management: landing domains creation + default status for "landings"
- Partner Statistics: new "Commission" grouper
- Customer API: "Bills" page
- Events: "Casino settings change" and "Partner settings change"
- Roles: "Partner report settings"
- UI and usability improvements
- Other changes and improvements
- Detailed information about the release features

Released on March 11-13, 2025


- Report: "Landing IDs" filter
- Commission constructor: exclude brands from subaffiliate rewards
- Roles: "Commission assign"
- UI and usability improvements
- Other changes and improvements
- Detailed information about the release features

Released on December 18-19, 2024


- Cohort Analysis Report
- Traffic Report: new filters, groupers and metric
- Subaffiliate bills connections on parent affiliate bill
- Enable mandatory traffic source for affiliates
- Roles: "News Items Read" and "News Items Process"
- Affilka Team: notifications inside operator interface
- Other changes and improvements
- Detailed information about the release features

Released on November 6-12, 2024


- Geo-Distributed Redirect Feature
- New role: Personal Partner Details
- Improvements to Personal Player Details role
- My Promos page for the Affiliate Interface
- Filters revision throughout the product
- Country, language, tag for Landings
- Integration API changes for players/activities imports
- Other changes and improvements
- Detailed information about the release features

Released on September 17, 2024


- We want to present the freshly updated subaffiliate system which now takes into account all the brands created within one affiliate program during subaffiliate rewards calculations. Refactoring led to changes in previously created commissions, landings, media, campaigns and some minor interface changes.
- Detailed information about the release features

Released on May 27, 2024


- News creation feature
- Priority landings
- External payment systems: "Pix for individuals" and "Pix for business"
- Customer API: separate endpoint for the "Players" page
- Sportsbook admin fee calculation: may be subtracted from SB GGR on affiliate program level

__Misc fixes and improvements:__

- New Field for Partner Registration form: Tax Identification number.
- Possibility to edit SuperOperator in the Operator Interface.
- New "Failed" state is implemented for requested reports.
- "Sign in as Affiliate" action no longer affects "Last seen at" date on a partner user.
- "Processed at" column is added to the "Bills" page in the Affiliate Interface.
- Detailed information about the release features

Released on April 24, 2024


- Traffic sources for affiliate's promo
- Traffic source info sent with referral links to target landing pages
- Traffic Report: new columns and conversion metrics
- Naming for requested reports

__Misc fixes and improvements:__

- Performance optimisation: "Partner Statistics" report should load faster.
- Performance optimisation: players' prequalification status should be applied faster.
- Independent scroll between filter and table section is implemented. The new layout will be applied if your browser viewport is bigger than 950 pixels.
- Reward columns analysed period in the "Partner Statistics" report now corresponds to the analysed period of Partner Income parameter.
- Parameters "dynamic_groupers" and "skip_delay" are removed from the requested reports parameters.
- Possibility to edit values for the "Partner IDs", "Partner emails", "Company names" filters is implemented. Just click on a selected tag in the input to edit it.
- Detailed information about the release features

Released on March 14, 2024


- Reports: Account for Self-excluded and Disabled Timestamps When Calculating Partner Income and Various Reward Types
- Commission Constructor: calculate conditions, qualifiers, rewards in a single base currency
- Stuck payments cancellation
- Roles: Data export
- Players import log on the "Players sync done" and "Players sync failed" events
- Bill corrections: filter by if the bill was edited
- Improved filters on the "List of partners" page

__Misc fixes and improvements:__

- Bills page: page and overall totals are added for "Fiat/Coin amount to be paid" columns.
- New filter "Balancer domains" on "Commissions" page (/casino/commissions). The system looks for the commission at which the specified balancer domain is currently active.
- Beneficiary country, Beneficiary address, Beneficiary city, Beneficiary postal code fields are now mandatory when filling Bank Transfer payment details in.
- Scrollbars are thinner in product interface for Windows users.
- BUG FIX: the selection dropdown for the Strategy filter on the Bills page works correctly.
- BUG FIX: operator's instant log out is fixed while using "Sign in as Affiliate" feature.
- Detailed information about the release features

Released on December 21, 2023


- Reports: Account for Self-excluded and Disabled Timestamps When Calculating Partner Income and Various Reward Types
- Traffic Report: New filters and Groupings by "Visit IP" and "Referrer"
- Bill corrections
- Bill corrections: filters by amount to be paid
- Roles: Commissions Read and Commissions Process
- Improved filters on "Players" page

__Misc fixes and improvements:__

- Performance optimisation: Postback Logs page should load faster.
- UX: Implemented validation on selecting a landing page when creating a campaign. Now it's impossible to skip step 2 without a landing selected during a campaign creation.
- Improved filter: now you can filter "Commission will expire", "Commission expired" events by commission id on the "Events" page.
- Performance optimisation: the list of operators when assigning a dedicated operator should load faster.
- The processing time for the resource-intensive "Partner Income" column in reports has been significantly reduced by approximately 400% on average for CPA rewards. This improvement is expected to reduce overall report generation time.
- BUG FIX: now we set the next day after "to" into "exchange_rates_date" filter when requesting report favorites in the Partner Interface.
- BUG FIX: now Partner Statistics will represent correct items quantity per page while using "Registrations" column, we plan to fix other columns (qualified, duplicates, self-excluded, disabled, FTD conversion) in the next releases.
- Detailed information about the release features

Released on August 17, 2023


- Reports: Account for Duplicate Timestamps When Calculating Partner Income and Various Reward Types
- Unlock casino/partner user via Interface
- Customer API: separate endpoint for the "List of partners"
- "Exchange rates" page
- UI: Independent filter and data display section scrolling + sticky elements
- UI: Commission constructor: ability to duplicate "Rule group" + "Rule" structure
- Implement default currency for the user to use in report

__Misc fixes and improvements:__

- UI: Sensitive filter and columns hints displayed on partner report setting page.
- Page loading optimisation: Events page and Events section on the Dashboard should load faster.
- Autosuggest filtration by commission ids added to the Partner Statistics(/casino/report) page.
- Traffic Report: inability to specify from/to earlier than 2023-01-01.
- Security: casino users are able to see only their statistic tokens.
- BUG FIX: Partners with visits and registrations data whose players don't have any activities (deposits, bets, wins, etc.) are now displayed in the reports.
- BUG FIX: 504 error is no longer displayed when exporting players with Deposits count filter on the /casino/players page.
- BUG FIX: FTD conversion rate % is now displaying 100% if registrations count and FTD count equals 1.
- BUG FIX: "Reset" button in the "Traffic report" resets groupings to the default ones.
- BUG FIX: inactive "download" button on the "Requested reports" page no longer opens requested reports page in a new tab.
- BUG FIX: admin fee filters show "from...to" on the /casino/commissions page.
- Language localisation setting for the Operator Interface (no translations are available for now, but will be added in the future).
- Error message on login form when casino or partner user fails to login was improved tp reflect various login failure scenarios.
- Refactoring: all filters with autosuggest now use the newly developed autosuggest component.
- Detailed information about the release features

Released on August 17, 2023


- Traffic Report: Landing IDs filter/grouping, Traffic Report API
- Bills: new state "On hold"
- Roles: "Bills Read" and "Bills Process"
- Reports: Net Deposits Column
- Verified Players Info and Filter
- Commissions: Published at filter, Admin fee filters, tags, batch actions
- Commissions' Tags: Assign & Filter
- UI: Filters Sorting

__Misc fixes and improvements:__

- Traffic Report now shows 100 rows per page instead of 20.
- Traffic Report: "User Agent" autosuggest filter improved. Previously the autosuggest searched for the first letters in a word that you type, right now the User Agent filter searches all matches regardless of their position in a word.
- Traffic Report: "Reset" button behaviour fixed. When you press "Reset", the Traffic Report shows default report view.
- Traffic Report: obligatory grouping by period removed.
- 2fa code lifetime increased to 180 seconds. Now every user will have 180 seconds to fill in the 2fa code from the moment it was generated. We hope this will fix the issue with devices time sync many users are experiencing.
- Stuck payments reason is displayed on a detailed payment page.
- Commission Tags are displayed on the /casino/commissions page.
- System emails: affiliate system domain name displayed as sender instead of affilka and softswiss domains.
- Payments and Bills pages: checkboxes aren't displayed if batch actions are unavailable.
- "Approved at" column added into CSV export on the /casino/payments page.
- Brand name added into CSV export from the /casino/report page.
- Events: whenever an Operator acts on behalf of a Partner, they are logged as an actor behind every event.
- Bonus codes page contains the information on players who registered with this bonus code. By clicking on the players count, you will be redirected to the /casino/players page filtered by this bonus code.
- Brand filter on the /casino/media page improved. Previously the filter was pre-filled with some brand, now it shows all media of all brands. If you need to find media belonging to a specific brand, you need to choose this brand from a dropdown selector.
- "Forgiven fiat/crypto debt amount since previous bill" field behaviour fixed. Previously it showed accrued forgiven debts accumulated throughout the partner's lifetime, whereas now it shows only the amount forgiven from the previous bill.
- “From-To” period filters removed from report settings and are now always available to partners. If this filter wasn't enabled, it created problems with access to the reports. Reports without this filter are not functional. So we decided to make the filter available to all partners by default with no possibility to change that.
- "Your account is blocked" message is now shown upon login for blocked operators.
- New event in Partner Interface: Bill Approved. Affiliates are now notified when their Bills are approved. They can find the corresponding event on the /partner/events page. The event contains the information about the approved Bill and its amount. The partner also receives a corresponding email notification following the event.
- Detailed information about the release features

Released on June 7, 2023


- Security Measures
- Payment Methods Verification: CoinsPaid
- Roles: "Payment Methods Verification"
- Roles: "Log in as affiliate: wallet"
- Roles: "Payments Read" & "Payments Process"
- Roles: "Balance Correction"
- Commissions' Tags: Assign & Filter
- UI: Filters Sorting

__Misc fixes and improvements:__

- Sticky totals are implemented on Partner Statistics (/casino(partner)/report) and Traffic Report (/casino/traffic_report). Now whatever the size of the page, you will always have the totals in front of your eyes
- New Dedicated operator filter on /casino/payments page
- Events: add info to csv export for commission_event type
- Partner ID is implemented on "Bills" and "Payments" pages and on detailed bills' and payments' pages
- "Finished at" column on /partner/payments page
- Implemented warning icons on "Payments" page for payments which payment details were never used before
- New base cryptocurrency support for new setups
- New currency filter on commission creation page (/casino/commissions/new) was implemented to help you find the brand with the corresponding base currency pair (EUR/USDT, EUR/BTC, etc.)
- Multiple input support for the "Commission IDs" filter on Partner Statistics (/casino/report) page
- Events: ID filter is disabled for Actor type "System" and "None"
- Rate limiter implementation for events "players_sync_empty" and "activities_sync_empty": 1 per hour
- "Partner Income" and "Payable Casino NGR" tooltips description on the reports is automatically adjusted to the page's width

Released on March 22, 2023


- Operator Interface: Traffic Report MVP. Unique/non-unique clicks, click GEOs, user agents, OS, etc.
- Report Favorites: save report templates and reuse them.
- Reports: history of requested reports, report generation progress, download report in 1 file via browser
- Partner Income Shows Negative Values Where Applicable
- Activities Report: Filter Report by Commission ID
- Set Custom Cookie Lifespan on Brand/Promo level (default – 30 days on affiliate program level)
- Forced User Session Expiration: terminate active sessions from unknown devices
- Assign Subaffiliates to Parent Affiliates Manually in the Operator Interface
- Assign Subaffiliates Role and Event

__Misc fixes and improvements:__

- V1 API: optional `converted_from` parameter added into /api/v1/activity endpoint.
- V1 API: casino_bets_rollbacks_sum_cents and casino_wins_rollbacks_sum_cents parameters added into /api/v1/activity endpoint. Thus, the casino bets sum in the report will be calculated as the sum of casino bets sum minus rolled back bets, and the casino wins sum will be calculated as the sum of casino wins minus rolled back wins.
- V1 API: from…to validation added on players activities import. It cannot exceed 1 calendar day (UTC) and it has to end at 00:00:00.
- New events: players/actvities sync empty. For every import with an empty array of items, we will create a corresponding event.
- Emails are no longer sent to blocked users.
- Casino Operators are automatically blocked after 30 days of inactivity regardless of their role.
- Report date range filter was changed. Not only can you indicate a custom period for analysis, but also select ready periods (relative periods such as current/last week, current/last month, etc)
- Detailed Promo Page now includes a Landing URL to which the referral link redirects traffic.
- Landing URL filter was added on Campaigns/Promos pages.
- Campaigns/Promos Count was added to the List of Landings. So you can see how many campaigns and promos were created with the specific Landing.
- Campaign/Promo is shown on Subaffiliates Page. You can now see which campaign and promo created by parent affiliate brought in subaffiliates to your affiliate program.
- Players’/partners’ emails are no longer exported in CSV if not allowed by operator role.
- Players’ emails are no longer shown on a detailed Bill page in the Player Qualifications section if not allowed by operator role
- Skype/Telegram columns were added into CSV exports from /casino/partners page.
- New Field for Partner Registration form: Referral Source. Here partners can indicate (at Registration or while editing their profile) from which source they learnt about your affiliate program. You can enable it in the "All settings" tab under "Profile fields management" section.
- Bank Transfers: 5 optional fields added - Beneficiary Country, City, Address, ZIP, Reference
- Comments to Balance Corrections are now exported in CSV from balance corrections page

Released on December 5, 2022


- Tech: Integration with MINIO file storage, Migration to Active Storage
- Partner tags in report CSVs
- Operator Interface: all partner tags displayed within the list of partners
- Reports: Payable Casino NGR used as a base for Bill Calculation with an account of all modifiers included into Commission plan
- API docs role and Interface Role
- Bills and Payments: overall and page totals
- Events: filter by creation date, subject and actor
- Player IDs in Postback Logs CSV
- Statistic Token: added into Partner Intrerface on Detailed Account Page
- UI: Hide Navigation Menu (Collapsed State)
- UI: Page Items – Choose 20-50-100 Results per Page
- Affiliate Interface: Archive Unused Campaigns

__Misc fixes and improvements:__

- Commission Constructor: removed the ability to set up several identical modifiers for one and the same condition/qualifier/reward.
- Commission Constructor: removed the ability to set up modifiers for "fixed" and "fixed per player" rewards. Modifiers cannot be used in conjunction with these rewards, they should be used with conditions or qualifiers instead.
- Conversion currency checkbox removed from Individual and Global report visibility settings.
- Affiliates are now redirected to the affiliate program landing page after log out. Previously, for those affiliate programs that relied on their own frontend, the redirect happened to our standard system landing page.
- Player Reassignment to another affiliate: we now send the data to the SOFTSWISS casino platform when a player was reassigned. Thus your players will be marked with correct stags in the casino back-office

Released on August 18, 2022


- Reports: Account for Duplicate Timestamps When Calculating Partner Income and Various Reward Types
- Reports: Qualified Player Registrations are now Calculated within Partner Income and Fixed Per Player Rewards
- Casino Taxes Accounted for at Bill Calculation
- Leave comments when cancelling payments
- UI Filters improvements: separate values with enter key, space bar, commas; Copy and paste values from your worksheets into filter inputs
- UI: Action Buttons Made Sticky in Filter Panels Across the App
- Commission Constructor: predefined modifiers for conditions, qualifiers, rewards
- Global Postbacks: Can Be Created and Sent on an Account Level
- Clean Net Revenue formula: (Casino Bets - Casino Wins - Casino Bonuses - Casino balance corrections - Casino admin fee - Casino taxes - Games providers Fees - Jackpot fees) + (SB bets - SB cancelled bets - SB wins - SB bonuses - SB balance corrections - SB 3rd party fees - SB Admin Fee) + (Poker rake - Poker bonuses - Poker corrections - Poker 3rd party fees - Poker Admin Fee) - PSP fees

__Misc fixes and improvements:__

- UI: All affiliate campaigns are now presented as a list view instead of a card view. We've also added multiple filters on the "Campaigns" page for the affiliates to easily navigate among their marketing campaigns.
- Campaign ID Variable Added to Postbacks: your affiliate can add the "campaign_id" variable to their POstback URLs, thus receiving info on which campaign a specific postback was triggered.
- V1 Integration API: Changes to the Required Activities Fields. The following casino parameters have been made optional: bets_sum_cents, wins_sum_cents, additional_deductions_sum_cents, rounds_count, bonus_issues_sum_cents. Chargebacks_sum_cents and chargebacks_count are also optional now. If you were sending zeroes in this fields, you can change the integration and ignore these fields altogether now.
- V1 Integration API: Sportsbook 3rd Part Fees May Be Negative.
- Partner IDs Reflected within the Reports
- Commission IDs Reflected in the Commissions List
- You can now filter by Commission ID + Title on the Commissions Page
- FTD Conversion Rate Displayed in Quick Stats/Charts Sections

Released on June 14, 2022


- Report: Commission Reward Calculations Added to Partner Statistics. Partner Income Divided into Reward Types (fixed per player, ngr %, etc)
- Coinspaid: withdraw with conversion to different crypto-wallets. BTC, USDT, LTC, BCH, ETH support.
- Roles: Hide Personal Player Details from your team members (email, first and last name). Define what you superoperators can see.
- New Report Metric: Casino Bonus Ratio % = Casino Bonuses Sum / Deposits Sum * 100%.
- Filter Partners by Default/Individual Report Visibility Settings. Assign report visibility settings in a batch on /casino/partners.
- Connect Multiple Affiliate Programs to 1 iGaming brand.
- Quick Stats/Charts: Custom Period and Brand Filters. Quick Charts Metrics Filter Changed.
- Commission Constructor: New Qualifier "Reqistration" for CPL deals.
- New event and email notification: Refund Made
- External Payment System: Piastrix

__Misc fixes and improvements:__

- Reports: Partner Income and Account Attributes (duplicates, self-excluded, disabled, etc) Representation Fixed. However narrow the data grouping is, values in the groupings and total values remain unaffected. Previously, if you broke down the report by player, for instance, the values in Partner Income and Duplicate/Self-excluded/Disabled Accounts differed from the total values if players had no activities associated with their accounts. Now, even if a player has no activities for the specified period, but Partner Income is calculated for their account or they become marked as duplicates, self-excluded or disabled, this data will be presented in the report.
- Operator Interface, Commissions: Filter Commissions by their Title.
- Operator Reports: Dedicated Operator Email added into CSV Report Exports.
- Add non-unique landing domains to different brands across different affiliate programs. Previously, we had a landing domain validation in place which prohibited operators from adding the same landing domain into different brands. We have removed this limitation, thus allowing you to use the same landing domain for different brands (e.g. if you use a layer domain redirecting traffic between different brands).
- Cashout restricted countries for bank transfers: specific countries can be added into a blacklist for processing bank transfers if bank transfers to these countries are not possible. This will reduce the number of failed and refunded bank transfer transactions.
- Chargebacks sum, Chargebacks count, Game Providers Fees, PSP fees and Jackpot fees added to Report Visibility Settings. You can now show these metrics to your affiliates within their reports.
- RUB and GBP currencies added into payment systems configurations and can be used for affiliate cashouts if your affiliate program has RUB or GBP as base fiat currencies.
- Commission ID was added to a detailed commission page.
- Affiliate ID was added to a detailed affiliate page in the operator interface.
- You can now extract the list of commissions in CSV format from the /casino/commissions page.
- Features for Greece Licensed Brands: HGC License Number added into affiliate registration forms, API Endpoint for Payments/Accounts Report, JSON Report Exports
- Affilka and Tracktor Integration with Datadog (Infrastructure and Application Monitoring Tool)
- Tracktor: non-unique visits tracking, visits for redirects outside Tracktor, send visits to Kafka

Released on April 13, 2022


- API Documentation: Front-End API, Customer Reports API, Integration API.
- Interface Theme Customisation: The colours of the affiliate/operator interface are customizable in the Settings > Interface tab.
- New Report Metric: Registrations to FTDs conversion rate. Calculated according to the following formula: FTDs/Registrations*100%.
- Commissions Constructor: New Modifier - Omit Unverified Players. Remove those players whose accounts haven’t been verified in the iGaming brand from commission calculations.
- Commissions Constructor: New Qualifier - Casino Bets Count.
- Block/Unblock Promos in the Operator Interface. To stop receiving traffic from specific referral links, you can block the promo code from the deatiled promo page in the Operator Interface.
- Poker Commissions: poker rake sum percent reward, poker bets sum qualifier.
- Poker Postback Events: Poker NGR.
- Refunds Displayed in the Operator Interface on the Payments page in the "Refunds" tab, on the “Bankroll transactions” page and withing the "Balance transactions" tab on a detailed partner page.
- Detailed Player Page: Player Changes History

__Misc fixes and improvements:__

- Original Player ID Column and Filter in the Report.
- Partner Events: Balance Correction Made.
- Affiliate Cashout: Amount Autofill at Cashout Request.
- Currency Filters Changed Across the App. All currency filters are now presented as dropdown selectors.
- Links to Promos and Campaigns added in the List of Players and on a detailed player page.
- Blocked Operators are no longer reflected in the dropdown list of the available operators when assigning an operator to affiliate.
- Commission Strategy is no longer reflected on a detailed campaign page in the affiliate interface.
- V1 API: Sportsbook Bonuses - can be negative.

Released on February 09, 2022


- Customer API singled out into a separate endpoint. Reports API for operators and partners;
- Report, New Columns: Prequalified Accounts, Casino Bets Count, Sportsbook Settled Bets Sum;
- Simplified Business Health Check Alerts;
- Poker Module, Commissions Constructor: rake qualifier, net revenue percent reward, net revenue condition;
- Poker Module: Postbacks;
- New Exclusions for SuperOperator Roles;
- Activity Import Log Added to Activities Sync Event Types;

__Misc fixes and improvements:__

- Timestamps behaviour for duplicate, self-excluded, disabled player attributes fixed. We used to rewrite the timestamp on the attribute whenever there was any update of player data, not necessarily within the said attributes. As a result, some of the attributes had incorrect timestamps associated with them which complicated the bill verification procedure. Now we only store the timestamps of when the selected attribute was changed;
- Player Dynamic Tags are now displayed on the detailed player page in the operator interface;
- Player emails were added to CSV report exports in the Operator Interface;
- Fin API: reporting period start and end date for bills and balance corrections were added to the Financial API;
- All activities are converted into the brand’s base currency in the affiliate interface;
- Bank transfers, account number length validation removed;
- Integration API, verified players: we can now receive, store and update the “Verified” player attribute;
- Full query redirect on a brand level: we can now send every parameter the referral link contains while redirecting your players to the target landing page.

Released on December 22, 2021


- Automatic Inactivity Session Timeout for all user types;
- Commissions Constructor: payment systems fees can be subtracted from affiliate rewards;
- Financial API: new action for payments - select for processing;
- Player Dynamic Tags: added to the players table, filters and exports on the players page;
- Affiliate Interface: Refunds displayed among payments and balance transactions, payments filters changed;
- Total deposits sum and count: added to the players table, filters and exports on the players page;
- New event and system notification: 2fa enabled;
- Operator Interface: Detailed Bankroll Transaction Page.

__Misc fixes and improvements:__

- Operator Interface: Detailed Promo Page Added;
- Operator Interface: Campaign ID filter added on the /casino/campaigns page;
- Statistic Token Cooldown Limit Changed. The API rate limit is now set at 1 request per 1 second;
- Tracktor: user agent parser for player visits. Tracktor can now parse such data as user device, operating system and browser from the user agent info stored in player visits. This info will later be used in our upcoming Traffic Report;
- Integrational API: casino bets count added to the activities import endpoint. Sportsbook third party fees sum added to API documentation;
- Operator and Partner Login forms can now be distinguished by their unique headers and buttons: "Log In As Operator" and "Log In As Affiliate" accordingly;
- BTC bills on the Operator Dashboard: no longer displayed in exponential form;
- Brand currencies are now automatically updated to include new currencies whenever there is an activities import with new currencies.

Released on November 4, 2021


- Adaptive Interface for Bigger Screen Resolutions;
- Affiliate Interface: Quick Stats Customisation;
- Partner Income: Duplicate Status Timestamps Accounted for in PI Calculation;
- Bank Transfer Fields Validation improved;
- Unified exchange rates for reports and bills;
- Payment System Sets Refactoring;
- all application errors are now sent to the error tracking platform Sentry.

__Misc fixes and improvements:__

- report API rate limits: frequency of 1 request in 5 seconds;
- report date range + Partner Income: the analysis period for reports containing Partner Income column must not exceed 1 month;
- campaign ID is now stored within every visit in Tracktor;
- Integration API: chargebacks can be negative;
- Integration API: player activities imports received via API can now be checked automatically by launching a rake task;
- Integration API: imports of player activities received via API now have a time frames validation, a specific error indicates the import’s time and date inconsistency;
- all Tracktor errors are now sent to the error tracking platform Sentry;
- Fin API: filters by account ID added.

Released on August 30, 2021


- Casino Taxes Subtracted from NGR Formula;
- Poker Module: Poker Activities Displayed in the Reports;
- HTTP Referrer and Tracking Link Info Sent with Referral Links to Target Landing Pages;
- Quick Charts: Fields Customisation and a Second Line for the Ended Periods;
- websockets: Centrifugo engine integrated;
- all application errors are now sent to the error tracking platform Sentry.

__Misc fixes and improvements:__

- a warning pop-up message was added to the “Archive” and “Expire” buttons in the commissions;
- Financial API: refunded payment id added to the API;
- UI: media filters redesigned; instead of checkboxes we now use a multiple dropdown selector with the autosuggest feature;
- Postbacks log: affiliates can now extract a CSV file with the log of their postbacks from the /partner/postbacks_log page;
- UI: the list of commissions on a detailed partner page in the operator interface is now divided into 3 tabs: active, scheduled, archived.

Released on July 21, 2021


- Commission Constructor: Subtract Game Providers Fees from NGR reward;
- Sportsbook Admin Fee;
- Integrational API: Poker Fields and Casino Taxes Added to Activities Import;
- Operator Interface: List of Promos;
- New Events: Commission Assigned and Commission Expired;
- Operator Interface: Media and Landings Moved to Affiliate Program Tab;
- Operator Interface: Quick Stats Fields Customisation;

__Misc fixes and improvements:__

- Operator Interface: Detailed Campaign Page added; to view the page simply click on the campaign id in the list of campaigns or type the campaign id in the URL /casino/campaigns/:campaign_id;
- Affiliate Interface: Promo Title displayed within promo cards on a detailed campaign page;
- Current partner balance displayed on the /casino/partners page and added to CSV exports;
- Total deposits count and sum displayed on a detailed player page;
- Bonus codes: filter players by bonus codes on the /casino/players page; bonus code displayed on a detailed player page;
- Fin API: Process Refunds via API;
- UI: Report Filters, Columns and Groups Divided into 3 Tabs; Filter and Reset Buttons Made Sticky

Released on June 8, 2021


- External PSPs: Player Account, WebMoney, Other;
- Reports: New Column with Disabled Accounts;
- Reports: Average FTD Amount;
- Postbacks Visibility Settings;
- New events: Balance Correction Made , Commission Archived

__Misc fixes and improvements:__

- Partner Settings Interface : individual partner settings in the operator interface were moved under the “Gear” button;
- Information about refunds and external payment systems was added to our financial API;
- Assign/Unassign Dedicated Operators In a Batch on /casino/partners page;
- Filter partner commissions on a detailed partner page by brand;
- Asc/Desc Sorting Fixed for Visits and Registrations when Avg Dep Amount is Enabled;
- Partner Income: commission schedule plan is now taken into account when calculating partner income;
- Email notification to partners when a new payment method for withdrawal is added.

Released on April 30, 2021


- Report: Average Deposits Count;
- Report: Self-Excluded Accounts Count;
- Events: Notification to Operators on the Upcoming Commission Expiration;
- UI: Partner Media, Partner Landings, Partner Commissions Changed;
- Affiliate Interface: Edit Promo Titles;
- Affiliate Refunds: Create and Process via SuperAdmin Interface.

__Misc fixes and improvements:__

- csv exports were added to /casino/events page, page design was changed;
- you can filter bills on /casino/bills page by Dedicated Operators;
- cashout events on (cashout requested, cashout approved, cashout cancelled) now contain the info on payment system and payment details associated with a specific payment;
- new filters for /casino/players page: Player ID, First Name, Last Name, Promo ID;
- you can filter partners on /casino/partners page by their accounts with such messengers as Telegram and Skype;
- /partner/balance_transactions: various filters added;
- player id column added to postbacks log table on /casino/postbacks_log page;
- Coinspaid payments: response time-out extended for 1 hour;
- numerous report export fixes.

Released on April 8, 2021


- Reports: New Column with Average Deposit Amount;
- Reports: New Column with Duplicate Accounts;
- SoftSwiss Payment Gateway Integration: Yandex Wallet;
- External Payment System: Capitalist.

__Misc fixes and improvements:__

- Skype and Telegram details are displayed on a detailed partner page within partner users table (/casino/partners/:partner_id/users);
- operator roles are now displayed within the operators table on /casino/users page;
- by default media and landings are now filtered by "personal" (or "dedicated") status when an operator assigns media and landings to partners (or other operators);
- bill amounts and payment amounts (as well as payment system info) are sent over to customer.io as event attributes for system notifications on bills and payments; you can include this data into your system notifications whenever a bill is approved or a payment is approved/cancelled;
- events and events subscriptions on /casino/events page are now sorted in alphabetical order;
- "approved at" date added to a detailed payment page and to the list of payments /casino/payments - especially useful for tracking bank transfers status;
- campaign name and promo code added to csv exports in /casino/reports;
- fixed: filters on payments and bills pages, filters by stag visit, duplicate, qualified, access limit, disabled on players page, bills csv export, report csv exports.

Released on March 18, 2021


- Reports: Asc/Desc Data Sorting;
- Reports: New Column with Qualified Accounts;
- Dynamic Player Tags: Bind Tags to Players Who Registered prior to Tags Creation;
- Casino Admin Fee Calculation: May be Subtracted from Casino GGR on Affiliate Program Level;
- Players: Filter by Stag Visit;
- Detailed Bill Page in Affiliate Interface;
- New Event and Email: 2fa Disabled;

__Misc fixes and improvements:__

- Affiliate reports in json/xml formats: no more validation errors for the whole report if an affiliate requests an xml/json export with the unavailable fields. We now return the export without the unavailable fields;
- Transaction ID added to a detailed payment page via Cryptoprocessing in the Operator Interface;
- Roles added to /casino/operators ;
- Reports: csv format update. All data is grouped by currency, and there is a separate row for every currency;
- Quick Stats and Charts: Last Week/Month/Year Added;
- Partner ID Column Added to /casino/players;
- Balance Corrections Made Clickable on Partner Balance Transactions Page /casino/partners/:partner_id/balance_transactions ;
- Manual bankroll transactions added to reference type filter on Bankroll Transactions Page;
- Decimal separators changed: we now support only dots as decimal separators in all filters; if you're used to commas, you'll be prompted to use dots instead;
- Partner Company Name added to csv report exports;
- Settings Tabs (Profile Fields Management, Partner Report, Available locales, Dynamic Tags) can now be reached via links of their own
- SB: Pending Bets Removed from Reports, Settled Bets Accepted via API.

Released on January 28, 2021


- Framework for Adding Non-integrated External PSPs;
- Customer.io: Unsubscribe Token;
- Dedicated Operator Filter on /casino/partners;
- Report: Columns Enabled by Default Changed;
- Report: Group Data by Dedicated Operator;
- Postbacks for Campaigns;
- New Postback Variables: Promo ID and Player ID
- Integration API: Non-binary Gender Option Added to Player Import

__Interface changes:__

- **Freeze Rows: Sticky Headers in Various Tables**The headers in most tables in the Affiliate and Operator Interfaces have acquired sticky properties: the headers remain frozen in one place so that the names of all columns always stay visible as you scroll down the table;
- **Pagination on Team Members Page in the Affiliate Interface**Making our interface more consistent, we've added one more pagination component to yet another page in the affiliate interface - /partner/users;
- **Campaign creation: view landing name, url, state, preview.**When creating a campaign and choosing a landing to refer traffic to, affiliates can now see not only the landing url which isn't always self-explanatory, but also its name, preview (you need to upload landing previews for a specific brand first), state (personal/shared);

Released on December 22, 2020


- Chargebacks and 3rd Party Fees Added to Operator Report;
- Operator Interface: Comments Added to Detailed Partner Page;
- Postbacks: Sportsbook NGR event and Sportsbook bets sum variable;
- Partner Verification: no longer obligatory;
- Partner Interface: Balance Transactions Page;
- Reassign Players to other Promos and Campaigns via SuperAdmin Interface;
- New Event in Affiliate Interface: Payment Method Added

__Miscellaneous bug fixes and improvements:__

- **Fixed:**no more random email notifications; previously if ever did anything to an affiliate account, you would receive email notifications whenever anyone else did smith to that affiliate - even if you didn't subscribe to receiving email notifications.In this release we have decided to kill this feature. From now on you will receive only those emails to which you have subscribed;
- **Improved:**cashout data added to csv exports from /casino/payments page: you can see affiliate payment details when exporting payment requests; especially useful for those operators who process their payments outside of the affiliate system (e.g. Turnkey casinos with their own merchant accounts and bank transfers);
- **Improved:**pagination in the affiliate interface added to campaigns, bills and payments pages thus boosting loading speed of these pages;
- **Improved:**navigation menu: fixed position and independent scroll;
- **Improved:**external payment id added to payments page for Turnkey brands and in superadmin interface;
- **Improved:**integration API: player email is no longer an obligatory field in players import;
- **Improved:**Fin API: GGR and Partner Income Parameters per Brand added to Financial API and can be sent to SoftSwiss 1c users.

Released on November 18, 2020


- Commissions Constructor: new qualifier "sportsbook bets" and reward "sportsbook bets percent";
- Static IP for Operators;
- New event: New Payment Method Added;
- Block Specific Referral Links;
- UX: Bills History Sorted in Descending Order by Created At Date in Affiliate Interface;
- Filter Postbacks in Postbacks Log by Player ID;
- Beneficiary address made obligatory for non-SEPA bank transfers;
- Dynamic tags: report filters and groupings refactoring

Released on October 22, 2020


- Reporting period on Bills and Balance corrections;
- Bankroll Transactions in the Operator Interface;
- Detailed Balance Correction Page in the Operator Interface;
- Balance Corrections: filter by brand;
- Reports: filter by Dedicated Operator;
- Integration API: accept and store game providers fees, jackpot contributions, payment systems fees;
- New event: csv export requested;
- Redesign: Detailed Partner Page Navigation Improvements;
- Do not show subaffiliate landings at promo creation if the commission doesn't support subaffiliate deals

Released on September 29, 2020


- Operator Interface Redesign;
- Bonus Codes: invite players via bonus codes;
- Reports: group by dynamic tracking parameters (e.g. clickID, webID, etc);
- Sportsbook: commissions constructor, new condition and reward - sportsbook ngr;
- New role: Superoperator without permissions to perform any actions related to finance (bills, payments, balance corrections);
- Partners list: filters on company and traffic sources;
- Fin API: bankroll state at a point in time;
- Report: csv email exports divided into several parts to avoid csv report generation time-outs;

__Miscellaneous bug fixes and improvements:__

- **Fixed:**convert report into any currency even if there are no exchange rates for a specific currency pair;
- **Improved:**Beneficiary Address added as an additional optional field in Bank Transfer Details;
- **Improved:**duplicate database queries removed - faster report loading speed.

Released on August 20, 2020


- Sportsbook: GGR, NGR, Wins, Cancelled bets formulas into reports on player activities;
- Sportsbook: individual and global report visibility settings for affiliates
- Reports: filter by dynamic tracking parameters (e.g. clickID, webID, etc);
- SEO: 301 redirect for Google-bot user-agent for balancer-domains. Send all link juice to your casino domains;
- Bank Transfer Required Fields Changed;
- Fin API: Bankroll Change via 1c;
- Report: csv email exports divided into several parts to avoid csv report generation time-outs
- Partner Income: account for commissions change history when calculating PI for ended periods;
- Skrill API changes;
- Papertrail logging on updates of Commission, Bill, Payment, PaymentCommission, PartnerUser, Partner, CasinoUser, AdminUser.

__Miscellaneous bug fixes and improvements:__

- **Improved:**When a balancer domain is changed, the commission will no longer be archived for the campaign it is used in;
- **Improved:**Default target audience "Players" at promo creation;

Released on July 13, 2020


- Tracktor: GO application for processing visits and redirects. High-load, high-availability, fault-tolerance;
- Cashflow changes on bankroll account: funds subtracted from bankroll immediately when you approve a cash-out, no waiting for PSP callback, fewer reasons for stuck payments;
- Upgrade to RoR 6.0.3.1;
- Alert in the Operator Interface on new payment details added by Partner;
- Dynamic tracking parameters settings;.
- Sportsbook: enable SB module for your affiliate program;
- Sportsbook: reflect data on player activities in reports;
- New role: Players;
- Players: show emails to super-operators only;
- Edit Campaign Name in Partner Interface

Released on May 27, 2020


- Players list: filters by self-excluded, duplicate, disabled, qualified account; csv exports with these data.
- Report: json/xml exports for casino operators.
- Neteller: New API integration.
- Postbacks: use proxy to send postbacks.
- Additional protection against brute-force attacks.
- SportsBook: API endpoints for receiving and storing SB stats.
- Interface customization with your affiliate program logo.
- Filter affiliates by their current balance and depositing players count.

__Miscellaneous bug fixes and improvements:__

- **Improved:**Accept BTC addresses in new P2WPKH format;
- **Improved:**Affiliate interface: more info in bills history (id, brand, commission);
- **Improved:**Affiliate Interface: dashboard changes, quick withdrawal from dashboard;
- **Improved:**Affiliate Interface: campaign creation steps changes;
- **Improved:**Affiliate Interface: wallet changes

Released on April 23, 2020


- Postbacks: new events - prequalification and disqualification.
- Postbacks: deposit id parameter
- Commissions Constructor: new modifier - from last ISSUED bill
- Bills: filter by amount
- Reports: partner email added to csv
- Bank Transfers Automated: processing in 1c via Financial API
- Migrated Brands: API end point for passing ALL visits from the old system to the new one

__Miscellaneous bug fixes and improvements:__

- **Fixed:**Partner Income: include qualified players into calculation;
- **Fixed:**Scheduled payments: automatic scheduled cashouts for archived payment details are no longer possible;
- **Improved:**Commissions assignment: You can start typing the commission id, name or strategy into the text input when assigning an individual commission to your partner;
- **Improved:**report in full screen. Affiliates can expand report tables to the full screen mode by pressing the "full screen" button in the right corner of the report;
- **Improved:**tooltip in quick charts. If you hover over a point on the graph, you will see a tooltip with the exact value represented by the point;
- **Improved:**user guide for affiliates added into the navigation menu into the "Affiliate program" section.
- **Improved:**UX: fixed width with no scroll for Filters block

Released on March 26, 2020


- Report: individual access to the report for selected affiliates
- Localization: define affiliate program languages, allow affiliates to set language, remember their language preferences
- Commissions Constructor: max reward in CPA commission plans
- Report: convert report fields into any currency
- Aggregation of player visits per hour. Faster reports
- Affiliate Interface: new page /partner/events
- Affiliate Interface: new page /partner/postbacks_log

__Miscellaneous bug fixes and improvements:__

- **Fixed:**superoperators can bind themselves to affiliates - previously their email was not available in the "dedicated operator" drop-down list;
- **Fixed:**all data in all partner report fields is properly aligned regardless of whether there were any registrations during a specific timeframe;
- **Fixed:**zero visits and registrations are represented as 0 and not empty values in /partner/report as well as .csv and .xml exports;
- **Fixed:**dedicated operators can view and filter postback logs for their affiliates - previously there was a load error;
- **Fixed:**operators with "commissions" in their role permissions can publish ready commissions;
- **Fixed:**quick charts: monthly and yearly charts start from calendar day 1 (and not from Monday), weekly charts start from Monday (and not from the first day of activity), monthly chart is broken down per day, all zero values are presented as 0 in the chart;
- **Fixed:**affiliates can edit "banner" promos and turn them into "direct link" promos;

Released on February 14th, 2020


- Partner Interface Redesign
- Report: filter and break down data by player countries and FTD dates.
- CSV Exports Logs: find out who requested csv exports and when.
- Localization: translation keys ready. Translate affiliate program into multiple languages.

Released on January 15th, 2020


- Partner Debts Refactoring: all debts are calculated within the context of 1 brand commission deal. Debt accumulated under 1 commission plan does not influence another commission plan or another brand that the affiliate promotes.
- Forgive debts up to 'x': validation added - must be greater than 0
- Reports: View Stats by Players in the Operator Interface
- Reports: Pagination Added. Reports loading speed increased
- Coinspaid: Mining Fee Subtracted Dynamically from Bankroll
- Postbacks Log: View and Filter All Sent Postbacks in the Operator Interface
- Landings: Edit Root Landing
- Redirect URL: Additional URL for Balancer Domains

Released on December 9th, 2019


- Reports: Analytical Partner Income. Calculates your approximate running expenses on partner commissions at a given point of time.
- Players list, new fields in csv export: Brand ID and name, Player country, FTD date, FTD amount, FTD amount cents, FTD currency, Qualified at.
- Landings: Add Landing Previews to the Operator Interface
- Coinspaid: Cash-outs in fiat currencies Using Internal Exchange Rates
- Payments and Bills: Partner Tags Added to Filters
- Customer.io: New Attribute - Partner Tags

Released on November 4th, 2019


- Players List: Player Country, Signup Date, FTD date and FTD amount added to Fields and Filters
- Payments and Bills: Process Multiple Transactions in a batch
- Admin fee: Deducted from Negative NGR values
- Affiliate Language Detection: based on user's browser settings
- Commissions Constructor: remove disabled players from commission calculations
- Coinspaid: Update to V2 API
- Terms and cookie policy moved to: /partner/terms-and-conditions and /partner/cookie-policy