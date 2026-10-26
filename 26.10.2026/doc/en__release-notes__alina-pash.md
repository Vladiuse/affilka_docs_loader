The "Self-excluded" and "Disabled" player statuses show if a player closed his account by themself (self-excluded) or the player was blocked by a casino (disabled). We capture not only the status itself (True or False), but also the timestamp when these statuses were changed. These timestamps are now accounted for in the Partner Income calculation for a selected period, making this metric more accurate. The changes come into effect **from 1 December**, retrospectively the data has not yet been changed.

For example: if a player is active in November, is marked as a self-excluded/disabled later in December, and you use the "omit self-excluded/omit disabled" modifiers in the commission plan under which affiliate players are referred, then this player's activities will be excluded from the Partner Income calculation only in December. The Partner Income calculation of November will remain unaffected. The same goes for all other reward types present in the report, which may use the "omit self-excluded/omit disabled" modifiers.

In the Traffic Report, you can now break down clicks by IP of the visit and by the source from which visit came (i.e. referrer). To do that, group the report by "Visit IP" and "Referrer". As a result, you will see how many visits each IP or Referrer have within a specified timeframe. It's not a rare case when referrer is blank for a visit, this means that the system or site, from which the redirect was made, hid this information or the redirect was made by pasting referral link into the browser's address bar.

You can also filter the report by specific "Visit IP" and "Referrer URL". Both filters support only single values. 

The "Referrer URL" filter supports partial search, f.e. if you indicate "affilka.com/bonus" the system will display all the visits which referrer contains "affilka.com/bonus".

The "Visit IP" filter supports "starts with" search, f.e. there are 3 visits with the next IPs:

- 110.148.141.1
- 110.148.141.2
- 148.140.131.1

If you indicate in filter:

- "110.148"
 then the system will search for "110.148*", it will display options 1 and 2.
- ".148."
 then the system will search for ".148.*", it won't display any option.
- "148"
 then the system will search for "148*", it will display only option 3.

We have also added "Visit IP" and "Referrer" into CSV exports from the Traffic Report page. When you group the data by "Visit IP" and "Referrer" and download a CSV file, the information on "Visit IP" and "Referrer" will be under the "ip_address" and "referrer" column names.

Due to various reasons, sometimes a bill issued for a partner has to be modified. Now you have the ability to do this, the steps are the following:

- Go to the detailed page of the bill and press on the "Edit" button in the upper right corner of the page.
- In the window that appears, you need to make sure that the checkbox next to the currency with for correction **is activated**.
 Next, you need to indicate the amount that you are going to add to the bill or subtract from the bill. The action of the sum/subtraction is indicated in the "Action" section.
 You can leave the comment for the correction with "Visible to operators only" or "Visible to operators and affiliates" setting.
- Click on "Submit" button if you want to apply changes.

The sum of the bill after corrections is specified in "Fiat amount to be paid" or "Coin amount to be paid" on the bill's detailed page and the Bills page (/casino/bills), the initially issued sum of a bill is indicated under the "Issued fiat amount" or "Issued coin amount" columns on the same pages.**If the bill is accepted, **the partner’s balance will be replenished by the amount specified in the “Fiat amount to be paid” or “Coin amount to be paid” fields.

The bill's corrections history and info: amount, action, actor, comment, etc. can be found under "Bill corrections" section on the bill's detailed page. Partner **can see all the corrections** performed by the operator (exact operator is not indicated) in the affiliate interface under the "Bill corrections" section on the bill's detailed page.

Please note: in order to perform bill corrections you must have the "Bills Process" role activated.

"Fiat amount to be paid" and "Coin amount to be paid" are also added to the csv exports from the Bills page.

While adding corrections to bills, it becomes necessary to filter by adjusted amounts. You can find filters "Fiat amount to be paid" and "Coin amount to be paid" on the bills page (/casino/bills).

To use it please indicate currency in "Fiat currency" or "Coin currency" filters and specify amounts in "Fiat amount to be paid" and "Coin amount to be paid" filters.

We've split the "Commissions" role into two separate ones: "Commissions Read" and "Commissions Process". Here's how it works:

- If an operator doesn't have access to the "Commissions Read" and "Commissions Process" roles: they don't have access to the "Commissions"(/casino/commissions), no access to the "Commissions" tab on the partner's detailed page(casino/partners/id/commissions), no access to the "Commissions" tab on the casino user detailed page (/casino/users/id/commissions), they are not able to perform any actions to commissions. Such operator can't see events related to the commissions, except "Commission expired", "Commission will expire" (these events will be hidden in future releases).
- If an operator has access to the "Commissions Read" role, but doesn't have to the "Commissions Process" role: they have access to the "Commissions" page (/casino/commissions), can see all created commission, but are unable to modify commissions (can't edit, publish, set tags, etc.), unable to assign and expire commissions for the dedicated partners, and they can see all the events related to the commissions ("Commission archived", "Commission assigned", "Commission expired", "Commission will expire").
- If an operator has access to the "Commissions Read" and "Commissions Process" roles: they have access to the "Commissions" page (/casino/commissions), have access to modify commissions (can edit, publish, set tags, etc.), able to assign and expire commissions for the dedicated partners, can see all the events related to the commissions ("Commission archived", "Commission assigned", "Commission expired", "Commission will expire").

The roles "Commissions Read" & "Commissions Process" will be activated automatically to all users which have previously had access to the "Commissions" role. If there is a need to (de-)activate these roles for the operators, please use the "Roles" page.

You can also limit which SuperOperators can have access to this page by using the SuperOperator exclusions "Commissions Read" and "Commissions Process". Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

We've improved "Original Player IDs", "Emails", "Partner IDs" filters on players page (/casino/players), now support:

- Original Player IDs: multiple values
- Emails: multiple values + partial search.
 When two values "test@yahoo.com" and "@gmail.com" are specified in one filter, the system will return the player with "test@yahoo.com" email and every player whose email contains "@gmail.com".
- Partner IDs: multiple values.

- Performance optimisation: Postback Logs page should load faster.
- UX: Implemented validation on selecting a landing page when creating a campaign. Now it's impossible to skip step 2 without a landing selected during a campaign creation.
- Improved filter: now you can filter "Commission will expire", "Commission expired" events by commission id on the "Events" page.
- Performance optimisation: the list of operators when assigning a dedicated operator should load faster.
- The processing time for the resource-intensive "Partner Income" column in reports has been significantly reduced by approximately 400% on average for CPA rewards. This improvement is expected to reduce overall report generation time.
- BUG FIX: now we set the next day after "to" into "exchange_rates_date" filter when requesting report favorites in the Partner Interface.
- BUG FIX: now Partner Statistics will represent correct items quantity per page while using "Registrations" column, we plan to fix other columns (qualified, duplicates, self-excluded, disabled, FTD conversion) in the next releases.