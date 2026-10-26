The "Duplicate" player status shows if a player is a duplicate of another existing player. We capture not only the status itself (True or False), but also the timestamp when this status was changed. This timestamp is now accounted for in the Partner Income calculation for a selected period, making this metric more accurate. The changes come into effect **from 1 October**, retrospectively the data has not yet been changed.

For example: if a player is active in October, is marked as a duplicate later in November, and you use the "omit duplicates" modifier in the commission plan under which affiliate players are referred, then this player's activities will be excluded from the Partner Income calculation only in November. The Partner Income calculation of October will remain unaffected. The same goes for all other reward types present in the report, which may use the "omit duplicates" modifier. We will extend this logic for other "omit-type" modifiers in our next releases.

If a user is locked, it means that they were blocked due to 4 unsuccessful login attempts. Normally users can unlock themselves using a special link received via email. If for any reason, however, the email didn't get through to a user, you will always have a possibility to unlock them via interface. 

To unlock a casino user you need to enter the detailed page of the operator(/casino/users/:user_id), find the "Locked" status and untick the corresponding checkbox.


To unlock a partner user you need to enter the detailed page of the partner to the users tab and click on the user(/casino/partners/:user_id/users/:user_id), find the "Locked" status and untick the corresponding checkbox.


In order for you to export your partners' information via the API, we have created a separate endpoint for the "List of partners" page, available via ** /api/customer/v1/casino/partners**. When making requests to the Customer API, you need to send your user’s unique statistic token in the authorisation header. Your unique statistic token can be found on your operator’s detailed page: /casino/users/:user_id page. 

You can find new API documentation following the API tab - Customer Operator - Partners section and click on "Partners list".


The "Exchange rates" page (/casino/exchange_rates) available under the "Finance" tab helps you find the conversion rates that are applied to the reports and are used in billing calculation.


By using the "Exchange rates date" filter you can specify the date for which you want to view the rates. 

By using the "Currency pairs" filter  you can specify the currencies for which you want to view the rates. Multiple input is supported, autosuggest includes all currencies available in your affiliate program. Here's how the filter works:

- If "EUR"**/**"USD, GBP, BTC" currencies are specified in the filter, then EUR/BTC, EUR/GBP, EUR/USD pairs will be displayed in the report.
- If "EUR, CAD"**/**"USD, GBP" currencies are specified in the filter, then CAD/GBP, CAD/USD, EUR/GBP, EUR/USD pairs will be displayed in the report.

We've improved our user interface by implementing an independent scroll for filter and data display sections. So however long the list of items is, filters and paging navigation sections will always be in front of your eyes.

We also implemented sticky sections on our pages so that you don't have to do unnecessary scrolls.


With the ability to duplicate Rule Groups and/or Rules, you won't need to create each Rule group or Rule structure manually from scratch. The duplicated Rule group or Rule will have the same structure as the original one. The only thing you need to do is to change the numbers in the newly created Rule Group/Rule. You can perform this action by clicking on this icon.

Here's some explanation:

- If you duplicate Rule group the system will create the identical Rule group and place it right after the original one.
- If you duplicate Rule the system will create the identical Rule within the same Rule group and place it right after the original Rule.

You and your affiliates can now specify a default currency to be used in the report (/casino/report or partner/report) and the Quick stats/charts sections on the Dashboard. It means that the activities in the reports and Quick stats/charts sections will be **displayed in** the specified currency.

You can find this setting on the casino user page in the edit mode (/casino/users/:user_id/edit) at the bottom of the list. To change the default currency, you need to click on the dropdown and you will see the list of all available currencies in your casino. After selecting the currency, click on the "Submit" button to apply the settings. If you have a superoperator role and this setting needs to be changed, please contact your account manager.

You can also set the default currency for a partner. Go to the "Users" tab on the detailed partner page and click on the "Edit" button next to the corresponding user (/casino/partners/:user_id/users/user_id/edit). Partners can set this setting by themselves in their interface by following "My account" tab - Account info - Edit button (/partner/profile/edit).

**NOTE: **This setting affects the way the data is displayed only in the reports for a specific user. Commissions, bills and payments are calculated in brands' base curr

The currency indicated in the saved "report favorites" templates overrides the "default currency for reports" setting. If you want to change the currency saved in your favorite report, you need to create a new favorite report template.

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