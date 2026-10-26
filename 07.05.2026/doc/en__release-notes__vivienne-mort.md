Conditions, qualifiers or rewards that operators used to set in the commission constructor for a crypto rule group may become irrelevant due to cryptocurrency exchange rate volatility, leading to frequent commission creations, assignments, and unnecessary communication with affiliates. We've added the "Convert all conditions, qualifiers, rewards into one currency" feature to solve this issue. Configure the commission as follows:

- Select the base currencies pair in "Fiat/Crypto base currencies" setting. This setting filters the brands in "Choose brand" section which have such currencies as base ones.
- Enable the "Convert all conditions, qualifiers, rewards into one base currency" checkbox on the commission creation page.
- Select one of the base fiat/crypto currencies in which you want the commission to be calculated.
- Then build rules for your commission as usual based on your requirements.

During bill creation, commissions with the "Convert all conditions, qualifiers, rewards into one base currency" feature enabled, e.g., in EUR, will verify if players' BTC activities meet the conditions/qualifiers specified in EUR. The bill will be issued in EUR based on the exchange rate on the billing day, despite the activity being in BTC.

Note: When assigning commission with the "Convert all conditions, qualifiers, rewards into one base currency" feature activated in fiat to a partner with cryptocurrency debt, and you set "Forgive debts in fiat currency up to" (e.g., up to €20,000), the system will forgive the cryptocurrency debt based on the converted amount from €20,000 at the exchange rate on the billing day.

**The logic **of this feature is explained in the following examples (for both cases "Convert all conditions, qualifiers, rewards into one base currency" feature is activated in EUR), BTC to EUR Exchange Rate is 39405.67 on February 1:

**1. CPA Commission**

- Commission Rules: We pay €200 (fixed_per_player reward) per player meeting the Min FTD sum: €20 qualifier.
- Players for January:
 Player ID 123: FTD sum - 0.00055814 BTC
 Player ID 456: FTD sum - 0.00038055 BTC
- Bill Issued on February 1:
 Player 123: Paid 200€ for €22 FTD after BTC conversion (qualifier sum achieved).
 Player 456: Not paid for €15 FTD after BTC conversion (qualifier sum not achieved).**Total bill:**€200 for 1 qualified player.

**2. RevShare Commission**

- Commission Rules: 50% RevShare (ngr_percent) for the previous calendar month.
- Players for January:
 Player ID 123: NGR - 0.10000000 BTC
 Player ID 456: NGR - 0.20000000 BTC
- Bill Issued on February 1:
 Total NGR for 2 players: 0.30000000 BTC, converted to €11821.70.**Total bill:**€5910.85 (50% of total NGR).

Due to various reasons, sometimes a payment requested by a partner can be **stuck**. Previously you had to contact your Account Manager to cancel such a payment. This can be time-consuming, that's we have implemented an ability for an Operator to can cancel payments with "stuck" status on their own.

To cancel stuck payment you need to click on the red "Cancel payment" button in the upper-right corner of the payment's detailed page. We also would like to remind you to pay attention to "Stuck reason" field to identify why the payment was stuck and share this info with your partner later.

Right after the payment cancellation the funds will be returned to partner's and affiliate program's bankrolls.

Please note that not all the stuck payments can be cancelled due to our internal reasons. In case there is no "Cancel payment" button on a "stuck" payment, please contact your Account Manager to find a solution.

We've added the "Data export" role for operators. The role limits the ability to export data from all the pages in the Operator Interface. It means that if a user doesn't have access to "Data export" tole:

- They won't be able to export data using CSV, XML, JSON, API;
- They won't be able to see their statistic token;
- All buttons such as "Send CSV to email", "Export report", "Export to CSV" will be hidden from all the pages.

The "Data export" role will be activated automatically to all users. If there is a need to (de-)activate these roles for the operators, please use the "Roles" page.

You can also limit which SuperOperators can have ability to export data from your affiliate system by using the SuperOperator exclusion "Data export". Please, contact your Account Manager if you want to limit the scope of action for any of your SuperOperators.

WWe've added "Players import log" section for the "Players sync done" and "Players sync failed" events pop-up page. Using this section you will be able to see the info of the players (email, first name, country, etc.) that was sent from your casino platform to your affiliate system ("players_to_import"), which data was imported("imported_players"), which was not ("not_imported_players") and the reason for that ("fail_reason").

Please take into account that a regular operator won't be able to see "Players import log" section due to security reasons. If "Personal player details" or "Players Read" exclusions are active for the SuperOperator, they won't be able to see "Players import log" section either.

While making corrections to bills, it becomes necessary to easily find bills which were adjusted. You can find filter "Bill edited" on the bills page (/casino/bills). This is how it works:

- By specifying a "Yes" option in the "Bill edited" filter the system will return all the bills which were adjusted.
- By specifying a "No" option in the "Bill edited" filter the system will return all the bills except the adjusted ones.

We've improved "Partner IDs", "Partner Emails", "Company names" filters on the "List of Partners" page (/casino/partners), now they support:

- Partner IDs: multiple values.
- Partner emails: multiple values + partial search.
 When two values "test@yahoo.com" and "@gmail.com" are specified in one filter, the system will return the partner with "test@yahoo.com" email and every partner whose email contains "@gmail.com".
- Company names: multiple values + partial search. 
 It has the same search logic as the "Partner emails" filter above.

- Bills page: page and overall totals are added for "Fiat/Coin amount to be paid" columns.
- New filter "Balancer domains" on "Commissions" page (/casino/commissions). The system looks for the commission at which the specified balancer domain is currently active.
- Beneficiary country, Beneficiary address, Beneficiary city, Beneficiary postal code fields are now mandatory when filling Bank Transfer payment details in.
- Scrollbars are thinner in product interface for Windows users.
- BUG FIX: the selection dropdown for the Strategy filter on the Bills page works correctly.
- BUG FIX: operator's instant log out is fixed while using "Sign in as Affiliate" feature.