Here you can view and manage affiliate bills. Bills are issued automatically based on affiliate performance and the commission rules.

In order to manage Partner Bills, you need to have either SuperOperator access or a role with "Bills Process" permission enabled.

When you approve the bill, it lands on partner account and becomes available for withdrawal. It cannot be withdrawn unless you approve the bill and it ends on partner balance.

You can approve and cancel the bills in a batch by ticking off the checkboxes and applying the corresponding action, but we strongly advise you to review each bill and approve/cancel each bill individually.

Bills can be exported in CSV.

At the bottom of Bills table, you will find the info on the total amounts of Bills in money equivalent. This section contains both Page totals and Overall Totals. For instance, you can filter Bills issued for a specific month and see the Total Bills Amount in fiat and crypto currencies for the whole month as well as specific Page Totals.

To approve/cancel bills in a batch, select the bills you want to process and press "**Batch actions**" at the top of the list. Choose the action (**Pay** or **Cancel**) and confirm/cancel your action in the pop-up window.

Please, note that batch actions are applied to 1 page only. To process more bills, you need to move to next pages following the pagination trail.

| 
 | 
 | 

You can filter the bills by:

- **IDs**: type Bills IDs you want to find. This filter supports multiple values.
- **Brand**(dropdown selector): choose the brand where the bill was issued. Bills are issued separately for each iGaming brand.
- **Strategies**: this filter supports multiple values and an autosuggest feature. Start typing the name of the strategy and it will appear in the dropdown selector. You can select several strategies and the filter will find all bills that were issued for these commission strategies. There can be only one strategy attached to one bill.
- **Commission IDs:**you can use this filter to find the Bills that were issued according to the rules of a specific Commission. Type Commission IDs here. This filter supports multiple values and automatically suggests commission values based on what you're typing.
- **Partner IDs**: type Partner Identifiers here. This filter supports multiple values.
- **Partner emails**: type partners' email addresses here. This filter supports multiple values. Once you start typing the email, you will see a hint with autosuggested emails in the dropdown selector.
- **Partner tags**: this filter supports multiple values and an autosuggest feature. Start typing the name of the tag and it will appear in the dropdown selector. You can select several tags and the filter will find all bills that were issued to those partners who have any of the indicated tags. Use this filter to find and process bills of specific partners united by the same tags faster.
- **Dedicated operator emails:**supports multiple values and an autosuggest feature. You can start typing the dedicated operator's email and it will appear in the dropdown selector. This option allows you to filter the bills of the affiliates to which the specified dedicated operator is assigned.
- **Bill edited**(dropdown selector): select “Yes” to find adjusted bills; select "No" to filter the bills without applying adjustments.
- **Fiat currency and Issued fiat amount (from…to):**indicate bill amount in money equivalent. If you need to find all bills over, say, 20 EUR, choose EUR in the “Fiat currency” filter and type 20 in the “Amount:from” filter. Issued fiat amount filter helps you to find bills with the initial fiat amounts that were issued by the system automatically at the end of the billing period prior to bill corrections.
- **Fiat currency and Fiat amount to be paid (from…to):**indicate bill amount after bill corrections in money equivalent; to find the bill for which the correction was applied, select currency in the "Fiat Currency" filter and specify the amount in the “Amount:from” section. Fiat amount to be paid filter helps you to find bills that have been adjusted for the fiat amounts specified in the from/to field.
- **Crypto currency and Issued coin amount (from…to):**indicate bill amount in money equivalent. If you need to find all bills over, say, 0.001 BTC, choose BTC in the “Crypto Currency” filter and type 0.001 in the “Amount:from” filter. Issued coin amount filter helps you to find bills with the initial coin amounts that were issued by the system automatically at the end of the billing period prior to bill corrections.
- **Crypto currency and Coin amount to be paid (from…to):**indicate bill amount after bill corrections in money equivalent; to find the bill for which the correction was applied, select currency in the "Crypto Currency" filter and specify the amount in the “Amount:from” section. Crypto amount to be paid filter helps you to find bills that have been adjusted for the crypto amounts specified in the from/to field.
- **Created at and Processed at dates:**indicate the date range when a bill was issued and/or processed.
- **Reporting period (from...to):**indicate the dates to which bill can be attributed as a marketing expense. You can read more on reporting period here.

With this sorting, you can select your mostly used filters on the Bills and thereby optimize the space of the page you are viewing.

In order to set this, please do the following:

- Point a cursor on one of the filters and you'll see the PIN icon in front of the filter name.
- Click on the active PIN icon.
- After that filter will be sorted down to the “Show more” section.
- To pin the filter back you will need to click on the non - active PIN icon of the filter.

**NOTE!** Settings are applied for each account individually.

You can view a detailed bill page by clicking on the bill id in the bills table.

This page contains detailed information about the bill. From here you can approve, cancel, edit, put the bill on hold or remove it (this unlocks “Pay” or “Cancel” actions).

The page is broken down into 3 sections: overview, partner data, player qualifications.

Here you will see bill ID, date and time when this bill was issued and processed (either paid or cancelled), the reporting period to which this bill applies, the info on bill amount in fiat and/or crypto currency – essentially this is partner reward for the ended billing period, the amount to be paid (these fields shows the amount if a bill correction has been applied.), the amount of partner debt before the bill, if any, in fiat and/or cryptocurrency forgiven from the previous billing period; brand on which the bill was issued, the partner it was issued to, the commission plan according to which it was issued, bill state (possible options: pending, paid, canceled, on hold).

The following actions are available on the bill's detailed page:

- **Pay**— allows you to approve the issued bill, as soon as it's confirmed by the operator, the affiliate's balance in the partner interface is top up by the specified amount, and the affiliate is notified that the bill has been approved. Pay action is irreversible.
- **Cancel**— allows you to cancel the bill and leave the cancelling reason comment in cases if you do not want to pay for it; the affiliate will be able to see that it has been canceled in its interface. Cancel action is irreversible.
- **Put on Hold**— allows you to put the issued bill on hold, so you can use this option in cases when there is a need to check the affiliate traffic or if your affiliate has violated the terms of the partner agreement. Put on Hold action is reversible, and is only available for bills in the pending state.
- **Remove a Hold**— allows you to remove the issued bill from the hold, so you can use it after you decide to pay or cancel the bill. Remove a Hold action is reversible, and available only for bills on hold.
- **Report**– if you click on it, you will be redirected to the activities report associated with this bill. The report will be pre-filtered by "Data range", "Partner IDs", "Brands", "Commission IDs", "Exchange rates date", "Convert all currencies" filters. For the "Data range", "Exchange rates date", "Convert all currencies" we use the data from the bill's "Reporting period start date – Reporting period end date", "Billed at", "Billing fiat currency" fields respectively. If the "Reporting period start date" field is empty on the bill's page, the report will use the first day of the month from the "Reporting period end date" field.
- **Edit**— allows you to edit the issued bill; this option can be applied when an additional payment is required to an affiliate, or if the payment was added to the affiliate's balance before the bill was issued, and a correction of the current one is needed; the bill correction also helps you to monitor financial information by affiliates, if necessary.

This section shows the corrections applied to the bill and contains detailed information about it. Here you can find the Bill correction ID, date and time when this correction was made, the info on bill correction amount in fiat or crypto currency; the actor who changed it, what the action was (Add or Subtract types), a comment added by the operator to this bill correction, and a comment scope in which either an operator can be specified (this means that the comment is visible only to the operators), or a partner (this means that the comment is visible to the operators and the partner).

You can edit bill by clicking on the “Edit” button in the upper right corner of the bill's detailed page.You’ll be prompted to a pop-up window where you may add or subtract funds from affiliate's bill, activate currency, indicate the amount of bill correction, add a comment describing the correction, choose comment visibility, and press “Submit”.

After applying the correction, the total amount to be paid is shown in **Fiat amount/ Coin amount to be paid** fields. **Please note!** The edit option is not available after the bill is paid or cancelled. **If the bill is accepted,** the affiliate’s balance will be replenished by the amount specified in the “Fiat amount to be paid” or “Coin amount to be paid” fields. 

This section uncovers how the conditions set in the commission plan were satisfied. Depending on the commission rules, you may find here the following data:

- **NGR amount**will show you casino NGR generated by affiliate players
- **Wager amount**will show you the amount of money wagered by affiliate players
- **Deposits sum**will show you the amount of money wagered by affiliate players
- **Deposits**- **count**will show you how many deposits were made by affiliate players
- **First deposits**- **count**will show how many first deposits were made by affiliate players
- **Effective deposits sum**will show you the difference between deposits and cashouts in money equivalent of affiliate players
- **Depositing players**- **count**will show you how many affiliate players made a deposit
- **Sportsbook NGR amount**will show you sportsbook NGR generated by affiliate players
- **Subaffiliate earnings**will show you the amount of money that was earned by subaffiliates of this master affiliate

If you have various modifiers on your commission conditions, you will also see them next to the amounts. Modifiers will help you read and understand for what period the condition is calculated (e.g. last billing period, a period between actually issued bills, etc), what players it covers (players from specific countries, players who registered within the last 6 months, players with no duplicates, etc).

This section shows all players who satisfied the qualification criteria set in the commission attached to this bill. The information is organised into cards containing player id, player email, registration and first deposit date and qualification results. Depending on the commission rules, you may find here the following qualification data:

- **Wager amount**will show you the amount of money this player wagered in a casino;
- **Deposits count**will show you how many deposits this player made;
- **Deposits sum**will show you the overall deposits sum in money equivalent this player made;
- **Effective deposits sum**will show you the difference between the amount of deposits and cashouts in money equivalent for this player;
- **First deposit amount**will show you the amount of this player’s frist deposit in money equivalent;
- **Sportsbook**- **bets**- **sum**will show you the amount of sportsbook bets in money equivalent this player placed

As well as conditions, qualifiers are often accompanied by various modifiers. They will help you read and understand when the qualification criteria were supposed to be met *(e.g. during the last billing period, within 3 months from this player’s registration, during the last 2 weeks)*, what additional limitations are imposed on a player to be qualified *(e.g. player must come from a specific country, must have no duplicates or active responsible gambling limits, etc)*.

**The Reporting Period** indicates to which time a specific bill can be attributed. Let's say, that you calculate affiliate earnings on a monthly basis on the first day of each month. The bill is issued on the first day of the new month, but the actual marketing expense is attributed to the previous month to the ended period.

The Reporting Period consists of 2 dates: start and end date.

The Reporting period for bills is set automatically. It corresponds to a billing period preceding the date of bill issuance and relies on schedule plans set in commission settings.

*Examples:*

- **schedule plan monthly:**if a bill is issued on July 1, 2020, then the reporting period is June 1 - 30, 2020
- **schedule plan pick days 1, 13, 25:**if bills are issued on June 1, 13, 25, 2020 then the reporting periods for each bill are May 25-31, 2020; June 1-12, 2020; June 13 - June 24, 2020
- **schedule plan weekly (e.g. Thursdays):**if a bill is issued on July 2, 2020 (Thursday), then the reporting period is June 25, 2020 (Thursday) - July 1, 2020
- **schedule plan daily:**if a bill is issued on July 10, 2020, then the reporting period is July 9 - July 9, 2020
- **schedule plan monthly:**let's assume that a new commission plan is assigned to a partner from July 16, 2020 and it rewrites the old commission; the bill for the old commission plan is issued on July 16, 2020 and it's reporting period is July 1-15, 2020; the bill for the new commission plan will be issued on August 1, 2020, it's reporting period will be July 16 - July 31, 2020

Reporting periods are added to bills table in the Operator Interface and can be extracted with other data in CSV format. You can also filter bills by their corresponding reporting dates using filters on the left.