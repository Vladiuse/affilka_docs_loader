This page can be reached via the** /casino/report** link.

This report allows you to view and analyse the performance of all of your brands, affiliates, their campaigns and promos. You can filter the report by specific date range, brand, affiliate, commission strategy, campaign, promo, etc.

You can choose what columns you'd like to see in the report and reorganize them in the order that suits you by dragging and dropping the column names.

You can also view performance report in one single currency – EUR (or another base fiat currency if it's different from EUR). To do that, tick off the checkbox "Convert all currencies to EUR" in the filters block. By default, today's exchange rates are applied. If you want some other date, indicate the required Exchange rates date in the Filter above.

You can get the report in CSV/XLSX/XML/JSON formats by clicking on the corresponding button at the top of your statistics table. You can also get the report via the Customer Report API.

In the Partner Statistics report, you can analyze data on players and activities. More detailed information about clicks is available in the Traffic Report

By default, when you first load the report, you will see the data in the following format:

- The report shows player activities for the current calendar month grouped by every partner for all of your brands taken together;
- The current date is used for the exchange rates which are used to calculate total values;
- You will see Visits count, Registrations count, FTDs count, FTDs sum, Deposits count, Deposits sum, Cashouts count, Cashouts sum, and, depending on the products enabled, you will see such activities as Casino GGR, Casino Bonus Issues sum, Casino Additional Deductions sum, Casino Real NGR, Casino NGR, Sportsbook GGR, Sportsbook bonuses sum, Sportsbook balance corrections sum, Sportsbook third party fees sum, Sportsbook NGR, Poker rounds count, Poker bets sum, Poker rake sum, Poker NGR

If you want more metrics or other filters and you want the data to be represented and broken down differently, apply the required filters in the “Filter” section, tick off the required columns in the “Columns” sections, apply data groups in the “Group by” section and drag and drop the columns and data groups in the desired order.

**Please, note!** The analysis period for the reports containing the “Partner Income” column must not exceed 1 month. If you want to view Partner Income for older periods, you will need to change the date range in the report filters.


With this sorting, you can select your mostly used filters on the Partner Statistics and thereby optimize the space of the page you are viewing.

In order to set this, please do the following:

- Point a cursor on one of the filters and you'll see the UNPIN icon next to the filter name.
- Click on the UNPIN icon.
- After that filter will be sorted down to the “Show more” section.
- To pin the filter back you will need to open the “Show more" section and click on the PIN icon next to the filter.

**  NOTE! **Settings are applied for each account individually.

This is the complete list of all available metrics on player activities that can be found in the report:

| Metric/Parameter | Description | 
|---|---|
| Visits | the number of unique player visits. | 
| Registrations | the number of player registrations. | 
| Prequalified | the number of players who are potentially going to pass the qualification criteria set in the affiliate commission plan if the bill were issued today. The “Prequalified Accounts" column shows only those players who may potentially get qualified during a specific date range. Once a player is marked as qualified, they can no longer be marked as “prequalified”. | 
| Qualified | the number of players that were qualified in accordance with the qualification criteria set in a commission plan. The "Qualified Accounts" column shows only those players who were qualified during a specific date range. For example, if a player was qualified on January 1, 2021, and you're viewing the report for February 2021, this player will not be among the accounts qualified in February because this player was qualified earlier. If you're viewing the report for the last 3 months (e.g. December-January-February) and the report is grouped by month and broken down by player,  the values in the "Qualified Accounts" column for this player will show 0 for December, 1 for January (because the player was qualified in January), and 0 for February. | 
| Duplicates | the number of player accounts that were marked as "Duplicates" during a specific date range. The same rules of calculation are applied to this column as with the "Qualified accounts" column. | 
| Self-excluded | the number of player accounts that set a self-exclusion limit during a specific date range. The same rules of calculation are applied to this column as with the "Qualified accounts" column. | 
| Disabled | the number of player accounts that were disabled within an iGaming brand at a given time. The same rules of calculation are applied to this column as with the "Qualified accounts" column. | 
| Cross-brand duplicates | the number of player accounts that were marked as "Cross-brand duplicates" during a specific date range. The same rules of calculation are applied to this column as with the "Qualified accounts" column. | 
| Depositors | the number of players with deposits in an indicated period. | 
| Casino active players | the number of players who placed at least one bet within the selected period (specified in Date range filter). In reports grouped by day/week/etc., the active players number will be shown for each day/week/etc. when the player was active (placed a bet) | 
| SB active players | the number of players who placed at least one Sportsbook bet within the selected period (specified in Date range filter). In reports grouped by day/week/etc., the active players number will be shown for each day/week/etc. when the player was active (placed a bet) | 
| FTD count and FTD sum | |
| FTD conversion rate % | represents the ratio of FTDs to registrations in a percentage form. The metric is calculated according to the following formula: `FTD conversion rate = FTD count ÷ Registrations * 100%`.Example: if the total number of registrations for the selected period is 1000 and the total FTDs count for the same period in all currencies is 145, then the FTD conversion rate is 14,5%. If you view the report in the original player currencies, the FTD conversion rate is calculated for each currency.For example, the total number of registrations for a selected period is 1000. The number of first deposits in EUR is 100, in SEK - 20, in BTC - 25. FTD conversion rate for each currency will be the following: EUR - 10%, SEK - 2%, BTC - 2,5%. | 
| Avg FTD amount  | the average first deposit amount in money equivalent of a group of players. The column is calculated according to the following formula:  `Avg FTD Amount = FTD sum ÷ FTD count`. If the report you’re viewing is broken down by player, the Average FTD amount of a selected player will be equal to their First Deposit amount. In the report, the average values will be rounded to 2 decimal places. In CSV/XLSX exports there will be no such rounding. | 
| Deposits count and Deposits sum(including first deposits) | |
| Avg Deposits count | shows you how many deposits on average a player makes. The column is calculated according to the following formula: `Avg Deposits Count = Deposits count ÷ Depositor`. When grouping the data by player, the average deposits count will be equal to the deposits count of a specific player for the selected period. In the report, the average values will be rounded to 2 decimal places. In CSV/XLSX exports there will be no such rounding. | 
| Avg Deposit Amount | the average deposit amount in money equivalent of a player or a group of players. The column is calculated according to the following formula: `Avg Deposit Amount = Deposits sum ÷ Deposits count`. In the report, the average values will be rounded to 2 decimal places. In CSV/XLSX exports there will be no such rounding. | 
| Cashouts count and Cashouts sum | |
| Chargebacks count and sum | contains the info on any chargebacks/refunds made by/to players in your iGaming brand. Chargeback is a return of a transaction amount to a payer's account. It occurs when a payer disputes their transaction (claim it wasn't them who performed the transaction) and asks their bank/payment system to reverse the transaction. | 
| PSPfees | the sum of transactional fees paid by your iGaming brand to payment systems for deposits and cashouts made by your players. | 
| Casino Bets sum | the total sum of bets in money equivalent made by players in your iGaming brand. The column is calculated according to the following formula: `Bets Sum - Casino Bets Rollbacks Sum` | 
| Casino Wins sum | the total sum of wins in money equivalent made by players in your iGaming brand. The column is calculated according to the following formula: `Wins Sum - Casino Wins Rollbacks Sum` | 
| Casino Bets count | the number of bets made by casino players. | 
| Casino Wager | depending on the integration, this column may be equal to casino bets sum or may representbets in money equivalent multiplied by Bet Playthrough Percentages of each game. E.g. if bet playthrough percent of a specific roulette is 50% and a player made 100 EUR bets in this roulette, the total wager amount is 50 EUR. However, it can also coincide with bets. | 
| Casino Real GGR | Casino Gross Gaming Revenue generated by casino players invited by affiliates prior to Admin Fee deduction. The formula is calculated as: `Casino Bets - Casino Wins`.You will see this metric only if there is a setting for your affiliate program specifying that Admin Fee should be deducted from Casino GGR. | 
| Casino GGR | Casino Gross Gaming Revenue generated by casino players invited by affiliates. The formula is calculated as: `Casino Bets - Casino Wins`.If in your affiliate program Admin Fee is deducted from Casino Real GGR, then this formula will be calculated as . | 
| Casino bonuses | the total amount of bonuses in money equivalent that were issued to casino players. As a rule, the bonus amount is calculated as Issued Bonuses minus Cancelled Bonuses. | 
| Casino Bonus Ratio % | represents the ratio of Casino Bonuses to Deposits Sum. This column is calculated according to the following formula: `Casino Bonus Ratio = Casino Bonuses / Deposits Sum * 100%`. | 
| Casino balance corrections | normally these are positive and negative balance corrections performed by casino managers when they add/subtract money to/from player accounts. As a rule, this is calculated as Positive Balance Corrections minus Negative Balance corrections. | 
| Casino Taxes | the amount of money a casino paid in taxes for their players. Calculated on a player level. | 
| Game providers fees | the sum of royalty fees paid by casinos to game providers (usually it's a percent of GGR from their games) for the use of their games. | 
| Jackpot fees | the sum of jackpot contributions from all jackpot games played within a specific period. Jackpot contributions are collected from players’ bets in jackpot games regardless of the win/loss of that bet. Jackpot contributions top up jackpot pool from which jackpots are paid. | 
| Casino Real NGR | Net Gaming Revenue generated by casino players invited by affiliates prior to Admin Fee deduction. The formula is calculated as: `Casino Bets – Casino Wins – Casino Bonuses – Casino balance corrections – Casino Taxes`.You will see this metric only if there is a setting for your affiliate program specifying that Admin Fee should be deducted from Casino NGR. | 
| Casino Admin fee | an additional fee which is calculated as a percent of either Casino Real GGR or Casino Real NGR (depending on your affiliate program configuration) and which is then subtracted from Casino Real GGR or Casino Real NGR and is used to share various ongoing expenses with affiliates  (e.g. third party fees, VAT, operational expenses, promos). Admin fee can be different in different commission plans and different for different affiliates. | 
| Casino NGR | Net Gaming Revenue generated by casino players invited by affiliates. If in your affiliate program Admin Fee is deducted from Casino Real NGR, then this formula will be calculated as . | 
| PayableCasinoNGR | Casino Net Gaming Revenue which is used as a basis for Revshare (Casino NGR %) reward calculation. The Payable Casino NGR metric excludes irrelevant players' activities from its calculation. It serves as a basis for Bill Calculation. The Commissions Constructor allows operators to exclude certain players from revshare calculation. For example, you may decide not to pay NGR % for those players who are duplicates, self-excluded, disabled and/or not verified during a specified reporting period. The casino net gaming revenue which they generate during this period is thus excluded from revshare reward calculation. Another scenario is non lifetime revshare, where you pay NGR % only for a limited amount of time after player's registration date (e.g. 6 months only). This metric will be empty for those promos/campaigns/partners who don't have the following reward types: Casino NGR % and NGR % per player. **IMPORTANT!****Payable Casino NGR calculations presented in the report are only estimations at a given point of time. The total Payable Casino NGR amounts MAY CHANGE at the end of the billing period if a player moves through status (e.g. yesterday a player was not marked as duplicate, today they've been marked as duplicates – thus they are excluded from Payable Casino NGR calculation and commission reward accordingly).**
 
 | 
| SB Bets sum | the total sum of bets in money equivalent made by players in a sportsbook brand. | 
| SB Settled Bets sum | the total sum of bets placed by players in a sportsbook brand that were settled (i.e. have a final status and the bet result is known). | 
| SB Cancelled Bets sum | the total sum of cancelled bets in money equivalent cancelled by sportsbook providers in a sportsbook brand. | 
| SB Wins sum | the total sum of wins in money equivalent received by players in a sportsbook brand. | 
| SB Real GGR | Gross Gaming Revenue generated by sportsbook players invited by affiliates prior to Admin Fee deduction.  Option 1: `SB Bets - SB Cancelled Bets - SB Wins`.Option 2:`SB Settled Bets - SB Wins.`
 | 
| SB GGR | Gross Gaming Revenue generated by sportsbook players invited by affiliates. The formula is calculated according to one of the following approaches that is set during the affiliate program set-up stage: Option 1: `SB Bets - SB Cancelled Bets - SB Wins.`*If in your affiliate program Admin Fee is deducted from SB Real GGR, then this formula will be calculated as**SB Bets - SB Cancelled Bets – SB Wins - SB Admin Fee**.*Option 2: `SB Settled Bets - SB Wins.`*If in your affiliate program Admin Fee is deducted from SB Real GGR, then this formula will be calculated as**SB Settled Bets - SB Wins - SB Admin Fee**.*
 | 
| SB bonuses | these are bonuses which were issued to sportsbook players in money equivalent. | 
| SB balance corrections | positive and negative balance corrections performed by sportsbook managers when they add/subtract money to/from player accounts. | 
| SB 3rd party fees | various third party fees a sportsbook operator is paying to their software providers, risk management fees, etc. | 
| SB Taxes | the amount of money a sportsbook operator paid in taxes for their players. Calculated on a player level. | 
| SB Real NGR | Net Gaming Revenue generated by sportsbook players invited by affiliates prior to Admin Fee deduction. The formula is calculated as follows: `SB GGR - SB bonuses - SB balance corrections - SB 3rd party fees - SB taxes.` You will see this metric only if there is a setting for your affiliate program specifying that Admin Fee should be deducted from SB NGR. | 
| SB Admin fee | an additional fee which is calculated as a percent of either SB Real GGR or SB Real NGR (depending on your affiliate program configuration) and which is then subtracted from SB Real GGR or SB Real NGR and is used to share various ongoing expenses with affiliates. Admin fee can be different in different commission plans and different for different affiliates. | 
| SB NGR | Net Gaming Revenue generated by sportsbook players invited by affiliates. If in your affiliate program Admin Fee is deducted from SB Real NGR, then this formula will be calculated as . | 
| Poker Rounds Count | the number of poker rounds made by a player in a multiplayer poker room. | 
| Poker Bets Sum | the amount of poker bets in money equivalent made by a player in a multiplayer poker room. | 
| Poker Rake Sum | the amount of poker rake charged by the online poker room from their players. | 
| PokerBonuses | these are the bonuses that were issued to multiplayer poker room players. | 
| Poker Balance Corrections | positive and negative balance corrections performed by poker room managers when they add/subtract money to/from player accounts. | 
| Poker 3rd Party Fees | various fees an online poker room is paying to their software providers, taxes, etc. | 
| Poker Real NGR | Net Gaming Revenue generated by poker room players invited by affiliates. The formula is calculated as follows: `Poker Real NGR = Poker Rake Sum - Poker Bonuses Sum - Poker Balance Corrections Sum - Poker 3rd Party Fees Sum` | 
| Poker Admin fee | an additional fee which is calculated as a percent of Poker Real NGR and which is then subtracted from Poker Real NGR and is used to share various ongoing expenses with affiliates. Admin fee can be different in different commission plans and different for different affiliates. | 
| Poker NGR | Net Gaming Revenue generated by poker room players invited by affiliates with deducted Poker Admin Fee. The formula is calculated as follows: `Poker Rake Sum - Poker Bonuses Sum - Poker Balance Corrections Sum - Poker 3rd Party Fees Sum - Poker Admin Fee`. | 
| CleanNetRevenue | shows you your affiliate program revenue after you deduct its various fees. It is calculated according to the following formula: `Clean Net Revenue = (Casino Bets - Casino Wins - Casino Bonuses - Casino balance corrections - Casino admin fee - Casino taxes - Games providers Fees - Jackpot fees) + (SB bets - SB cancelled bets - SB wins - SB bonuses - SB balance corrections - SB 3rd party fees - SB Admin Fee) + (Poker rake - Poker bonuses - Poker corrections - Poker 3rd party fees - Poker Admin Fee) - PSP fees` | 
| Net Deposits | shows you the difference between total deposits amount and total cashouts amount of a player/group of players. The parameter is calculated according to the following formula: `Net Deposits = Deposits - Cashouts` | 
| Partner Income | an analytical value, calculated each day, which aims at giving you an idea on how much you would pay to an affiliate if the commission bill were issued today.  IMPORTANT! Partner Income calculations presented in the report are only estimations at a given point of time. The total billing amounts MAY AND WILL CHANGE at the end of the billing period. When paying commissions to your partners, you should always rely on partner bills rather than partner income. You can read more on Partner Income and its features here.  | 

We have also added all the reward types specific to our Commission Constructor (excluding subaffiliate reward types) into Partner Statistics. Now you and your partners can view not only the overall Partner Income, but specific rewards as well, such as revshare percent or CPA.

The following reward types can be found among the report columns right after the Partner Income column: flat fee, fixed per player reward (=CPA), Casino NGR % (=casino revshare), Casino NGR % per player, Deposits sum %, Deposits sum % per player, Effective deposits sum %, Effective deposits sum % per player, Casino wager %, Casino wager % per player, Sportsbook NGR % (=sportsbook revshare), Sportsbook NGR % per player, Sportsbook bets %, Sportsbook bets % per player, Poker NGR % and Poker rake sum % (=poker revshare). **Keep in mind****,** subaffiliate rewards are not presented in the Partner Statistics report.

You can read more on the reward types in our Commission Constructor guide. As soon as a new reward type is developed in the Constructor, it will be automatically added into the report as well.

This is the complete list of all available filters that can be found in the report:

| Filter | Description | 
|---|---|
| Date range | indicate the time period you’d like to analyze here.  E.g. 3 months, from June 1, 2020 to August 31, 2020. | 
| Brands | choose one or several iGaming brands from the dropdown selector. If a brand is not specified, you will see cumulative statistics on all of your brands taken together. | 
| Partner IDs (full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate unique IDs (stags) of those affiliates you want to analyze. | 
| Partner Emails (full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate full emails of those affiliates you want to analyze. | 
| Partner tags(dropdown selector with autosuggest feature; supports multiple values) | choose or type the partner tags you want to analyze. Partner tags are used to unite affiliates into groups for easier navigation.  E.g. you can tag partners who work on a CPA model with “CPA” tag, enter the tag into the filter and analyze all partners who have this tag assigned to them. If you type several tags, the report will show all partners who have at least one of the indicated tags. | 
| Dedicated operator emails (dropdown selector with autosuggest feature; supports multiple values) | choose or type emails of those dedicated operators whose affiliates you want to analyze. You can filter stats by Dedicated Operator only if you have a SuperOperator Role. | 
| Strategies(dropdown selector with autosuggest feature; supports multiple values) | choose or type commission strategies you want to analyze. | 
| Commission ID(dropdown selector with autosuggest feature) | select the commission for which you want to analyze the partner's performance. | 
| Campaign IDs(full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate unique IDs of those affiliate campaigns you want to analyze. | 
| Promo IDs (full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate unique IDs of those affiliate promos you want to analyze. | 
| Promo codes(full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate unique promo codes of those affiliate promos you want to analyze. | 
| Traffic sources (full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate full Traffic source name used in promos you would like to analyze. The system attributes visits, players, and their activities to the traffic source that the player was originally redirected from. | 
| Landing IDs (full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate unique Landing IDs you want to analyze. Keep in mindthat the system will attribute visits, players and their activities to the landing to which the player was redirect initially: e.g. if the player was redirected to the landing "example.com/bonus" (landing id: 46) by clicking on the referral link, then the system will attribute their visit, registration and all future activities to this landing id.Note! We don't track landing URLs history change. So if you edit the URL of landing id: 46 from "example.com/bonus" to "test.com/freespins", the data in the report on all historical visits, registrations and activities will be grouped under "test.com/freespins" URL, but the landing id: 46 will remain the same. | 
| Player IDs(full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate unique player IDs (their IDs in the affiliate system) you want to analyze. | 
| Original Player IDs (full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate unique player IDs (their original IDs that you see in the iGaming brands back office) you want to analyze. | 
| Player emails(full match mode, supports multiple values separated by a comma, “Space” or “Enter” key) | indicate full emails of those players you want to analyze. | 
| Player Countries(dropdown selector with autosuggest feature; supports multiple values) | choose or type those player countries on which you need the report. Please, note, that Player Country is an attribute of a player. You will not be able to analyse visits (clicks) via Player Country. | 
| Dynamic tags contain and Dynamic tags exclude(the filter uses peculiar syntax; supports partial match mode and multiple values separated by an “Enter” key) | You can either include or exclude certain dynamic tag names or their values (typed fully or partially) from report results.  filter, e.g. "Contain", finds all players for whom any of the specified tags/values are true, not necessarily all of themif you use both filters, “Contain” and “Exclude”, simultaneously, the filters will find players for whom both filters are true
 
 *player dynamic tags contain: clickID, utm=, =12345, webID=678**player dynamic tags exclude: twitch, source=, =facebook, webID=789*
 
 **the filter will include players who have:***a tag/tag value which contains 'clickID' or a tag which contains 'utm' or a tag value which contains '12345' or a tag which contains 'webID' whose value contains '678'***AND****the filter will exclude players who have:***a tag/tag value which contains 'twitch' or a tag which contains 'source' or a tag value which contains 'facebook' or a tag which contains 'webID' whose value contains '789'*
 | 
| Sign up date range | indicate the date range when player registration occurred, and the filter will find all players registered within this period and their activities. You can indicate either both dates or just one (after/up to which players registered). | 
| First deposit date range | indicate the date range, and the filter will find all players who made their first deposit within this period and their activities. You can indicate either both dates or just one (after/up to which players made their first deposit). | 
| Exchange rates date | indicate the exchange rates date to be applied to the report. If you're viewing the report for the ended period,  
 | 
| Convert all currencies into | choose the currency into which you will be converting all data. The available currencies correspond to those currencies you have in your iGaming brands. | 

**PLEASE NOTE! **The exchange rates applied to the Reports and Bills are pulled for 00:00 UTC for the selected exchange rate date.

You can decide how data is presented in the report by breaking it down by brand, partner, campaign, player, dynamic player tags, specific period: year, month, week, day; etc.

If you don't need to break down the data, you can leave the checkboxes empty and you will see the total stats for all partners and brands for the selected date range. If, however, you need to see how different partners or campaigns pair against each other during specific calendar periods, you can set the corresponding grouping.

*E.g. an affiliate has been promoting your casino via 3 campaigns for less than a year (say, from November 2019 till May 2020). The affiliate brings in fiat traffic. Grouping data by campaign and month will show you the total stats of eaсh campaign broken down per calendar month.*

The following data grouping options are available:

- **Period**: you can break down data by day, week, month or year.- *E.g. if you want to view daily performance of a specific affiliate throughout the current month, filter the report by Partner ID and apply data grouping by Period: Day. Remove the data grouping by Partner because it is unnecessary for the current report. If it is convenient for you, convert all data into the currency of your choice. The report will look similar to this:*


- **Partner**: break down data by partner. Use these grouping if you want to compare different affiliates with each other.- *E.g. if you want to compare various affiliates united by 1 tag “scandi” and their performance throughout the month, filter report by Partner tag “scandi”, use currency conversion options if needed and apply the data grouping by partner. The report will look similar to this:*


- **Brand**: break down data by the iGaming brand. Use this grouping if you want to compare different brands with each other.- *E.g. if you want to compare specific affiliate’s performance on 2 different brands during the current year, indicate the required date range, filter the report by Partner ID in question, use currency conversion options if needed, apply the data grouping by Brand and remove all other groupings. The report will look similar to this:*


- **Strategy**: break down data by commission strategy. Use it if you want to analyze affiliate performance on specific deal types and see what kind of traffic each deal is generating for your iGaming brand(s).- *E.g. there are 3 commission strategies in your affiliate program (cpa, hybrid, rev_share) and you want to compare player activities on each such deal for the current month. Group the data by strategy and remove all other groups, if not needed. Use currency conversion options for your convenience. The report will look similar to this:*


- **Commission:**break down data by exact commission. Use it if you want to analyze affiliate performance on specific commission plans and see what kind of traffic each commission plan is generating for your iGaming brand(s). This may be especially useful if a commission changes within the selected period, and you need to see the results before and after the change. The difference between the “strategy” grouper and the “commission” grouper, is that the “strategy” grouper unites different commissions under its name, whereas the “commission” grouper is more granular - and breaks down the data even further.- *E.g. an affiliate started working on a default 35 % revshare plan but your affiliate manager renegotiated a better deal for them – a 45% reshare plan. You want to compare whether performance changed with the commission change during this month. Group the data by commission. Use currency conversion options for your convenience. The report will look similar to this:*

- **Campaign**: break down data by campaign. Use it to compare different campaigns with each other.- *E.g. 1 affiliate account has several different campaigns. The affiliate was on a 3-month test deal in 1 of your brands after which new commission plan was supposed to be applied. To analyze the performance of each affiliate campaign during the 3 months on this specific brand during each month, indicate the corresponding date range, filter the report by Partner ID and Brand, use currency conversion options for your convenience and group the data by campaign and Period: month. Remove other groupings. The report will look similar to this:*


- **Promo**: break down data by promos (referral links). Use it to analyze how each referral link is pairing against each other.- *E.g. an affiliate has several different referral links within 1 campaign. These referral links are placed in different sections on different pages of an affiliate website. To analyze how each promo is performing throughout the month, filter the report by Partner ID, use currency conversion options if necessary and apply data grouping by promo. Remove other data groupings. The report will look similar to this:*


- **Player**: break down data by player. Use these data grouping to analyze reports on a player level.- *E.g. if you want to see how players who followed a specific referral link performed in the current month and find top players in terms of deposits and NGR, filter the report by promo code (or promo id), use currency conversion options for your convenience and apply data grouping by player. Remove other data groupings. Tick off the checkboxes next to column names which you want to see in the report (deposits count, deposits sum, NGR). The report will look similar to this:*

- **Dedicated**- **operator**– break down data by dedicated operators assigned to affiliates. Use this grouping if you want to compare different affiliate managers with each other.- *E.g. if you want to compare specific affiliate managers' performance during the current quarter, indicate the required date range, filter the report by Dedicated Operator emails in question, apply the data grouping by Dedicated operator and remove all other groupings. The report will look similar to this:*

- **Sign up at period**– break down data by registration date. Use this data grouping to analyze how different groups of players who are united by registration date/week/month/year performed during a set period.- *E.g. if you want to see how each group of players who registered on each day of September 2020 and who were invited by a specific affiliate, performed, filter the report by Partner ID and Sign up date range from September 1, 2020, use currency conversion options for your convenience and apply data grouping by Sign up at period: day. Remove other data groupings. The report will look similar to this:*


- **First deposit period**– break down data by first deposit date. Use this data grouping to analyze how different groups of players who are united by first deposit date/week/month/year performed during a set period.- *E.g. if you want to see how each group of players who made their first deposit on each day of September 2020 and who were invited by a specific affiliate, performed, filter the report by Partner ID and First deposit date range from September 1, 2020, use currency conversion options for your convenience and apply data grouping by First deposit period: day. Remove other data groupings. The report will look similar to this:*


- **Player country**– break down data by player country. Use this data grouping to analyze player activities on country level.- *E.g. you have a deal with an affiliate where you pay for player traffic from specific countries only, so you want to see players from which countries the affiliate is inviting and how each country is performing. The deal started in July 2020 and you need to see the data broken down by country and month. Indicate the required timeframe (from July 1, 2020), filter the report by Partner ID, use currency conversion options for your convenience and apply data grouping by Player country and Period: month. Remove other data groupings. Drag and drop Player country grouping so it’s on the top of data groupings. The report will look similar to this:*


- **Various dynamic player tags**– break down data by dynamic parameters sent to you by affiliates in their referral links. The names of groups will correspond to the Dynamic tags configured in the Settings. If you have configured clickID, subID, utm_source, utm_medium, utm_campaign, utm_content, utm_term - these tags will be available for grouping the data in the report- **.**Once you archive the tags, the groups will be removed from the reports and settings but you will still be able to filter reports by these tags.

**Use case:**

**Case 1:** as an Operator, I want to analyze yearly performance of a specific affiliate network. In the report, I want to see all data grouped by subID and clickID. In the report I set the date range to 1 year and filter the report by Partner ID in question. I group the report by subID and clickID and drag and drop them to reflect this order. Other groups are not needed. The report will look similar to this:


**Case 2:** as an Operator, I want to analyze specific affiliate performance by UTM tags, namely: utm_campaign and utm_source. Imagine that during this month this affiliate launched 3 campaigns promoting different games on different media sources and now I want to compare the performance of every media source within these campaigns.

*The campaigns to be analyzed are: berry-burst, fruit-spin and reel-rush. Af all the media sources I'm interested in facebook, twitch and blog. I enter these parameters into the filter.*

*I then group the report by utm_campaign and utm_source and drag and drop them to reflect this order. All other groups are not needed. The report will look similar to this:*

We have a separate Cohort Analysis report located under the Reports > Cohort Analysis tab (reachable via the /casino/cohort_report link).

However, you can also use the “Partner Statistics” report to analyze player cohort behaviour. Using this report and its tools, you can track and analyse the performance of a group of players who registered or made their first deposit within a specific time frame. This type of analysis will help you understand how different cohorts (groups of individuals who registered/made their first deposit during the same period) behave over time and how they differ from one another.

Let's imagine that you want to analyse how players of an affiliate X, who registered in different months of spring 2024, are performing during 6 months: from March till August. You want to see their FTD sum, Deposits sum, and Casino NGR over 6 months.

- In the “Filter” section set the period for analysis: 01/03/2024 – 31/08/2024. Indicate the ID of the partner you want to analyse in the “Partner IDs” filter. Scroll down to the “Sign up date range” filter and indicate the registration period: 01/03/2024 – 31/05/2024
- Go to the “Columns” section and tick off the required data fields: FTDs sum, Deposits sum, Casino NGR
- Go to the “Group by” section and apply 2 data groupings. The first one by Sign up at period: month. Drag and drop it to the top. The second one by Period: month. Remove the grouping by Partner.
- Press filter.

The report will look similar to this:

Let's imagine that you want to analyse how players of an affiliate X, who made their First deposits throughout March 2024, are performing in different days of March 2024. You want to see their FTD sum, Deposits sum, and Casino NGR over the days of 1 month.

- In the “Filter” section set the period for analysis: 01/03/2024 – 31/03/2024. Indicate the ID of the partner you want to analyse in the “Partner IDs” filter. Scroll down to the “First deposit date range” filter and indicate the registration period: 01/03/2024 – 31/03/2024
- Go to the “Columns” section and tick off the required data fields: FTDs sum, Deposits sum, Casino NGR
- Go to the “Group by” section and apply 2 data groupings. The first one by First deposit period: day. Drag and drop it to the top. The second one by Period: day. Remove the grouping by Partner.
- Press filter.

The report will look similar to this:

You can save your favorite report configurations (filters, columns, groupings) and access it at any time from the "Favorite Report". 

Report Favorites are saved on an individual user level in both Operator and Affiliate Interface.

**In order to create and save report favorites you need to:**

- Select required filters, columns and grouping in the report.
- Click on the Filter button to download the report.
- Save it to favorites by clicking on the Star icon at the top of the report page.
- Add the name of the favorite report and click Submit.

**Show All** button next to the “Favorites” section will allow you to see all the saved reports. Here you can also remove a favorite by clicking on Delete or download the required report.

**PLEASE, NOTE!**

- If you select an absolute date range when configuring the favorite report, the system will always show the indicated dates.

For example, you have set the period from July 1, 2023 - July 31, 2023, then the report will always show data for the selected period.

- If you choose a relative date range to the report when configuring the favorite report, it will always show the relative period.

For example, you select last month, then the report will show data for the previous month, regardless of the period when you request the report.

The exchange rates date in the report favorites **adapts to the period indicated in the date range filter** (be it an absolute or a relative period), and always **shows the next day following the specified date range** (billing period). 

The report can be extracted in CSV/XLSX as well as in XML/JSON formats via statistic feed links. If the report is too big to display within the interface, the file (or a link to the report download via the interface) will be emailed to the email you’re signed in with.

To get a report in CSV/XLSX format, first, apply the required filters and data groupings and choose the fields you want to see in the report, and press “Filter”. After that, click “Report export” and choose “CSV/XLSX**”. **As soon as the report is ready, you will be notified via email. 

The email will contain an attached XLSX file, in case you want to view the report straight away. The email will also contain a link to the detailed page of the requested report in the Affilka interface where you can download the report via browser. The available download options include Zipped CSV (consisting of 2 files: report rows and report totals) and XLSX (one file divided into 2 tabs with report rows and report totals).

When you want to extract the report in CSV/XLSX formats from the “Partner Statistics” page, you will be prompted to give a name to your requested report.

If you haven't indicated a name for your report when requesting it or you hit a time-out limit and didn't have a chance to indicate the report name, you can give the name to it on the detailed requested report page by clicking the “Edit” button.

Choose something that reflects the contents of the report so that you could easily navigate among your requested reports once they're ready.

The requested report will have an “activities report” type assigned to it.

If you're requesting a “Favourite Report”, the name of the preset report will be applied to it – but can be edited later on.

Please, note, that average report values (e.g. Average deposit amount, average deposits count, etc) in CSV/XLSX exports will not be rounded to 2 decimal places. Rounding off to the nearest hundredth is only available in the report interface on the /casino/report and /partner/report pages.

You can extract performance report in XML/JSON. To retrieve the statistics feed link, press "Export report" button and choose the desired format. Every link can be copied and opened outside an active session off site thanks to individual statistic tokens assigned to each operator. The statistic token remains static so that you could fetch data across different months without having to log in.

If an Operator is no longer working with the affiliate program and is removed from the team or their access to the operator interface is compromised, you can always expire the statistic token for this operator email. To block access to the statistic feed for a specific operator email, find the Settings>Operators tab (/casino/users), find the Operator's email, click on their ID and press “expire” next to the statistic token on a detailed Operator page.

**IMPORTANT! ****The data fields, data groupings, their order as well as currency representation in the XML/JSON report corresponds to the filters you have configured.**

For example, if you want to retrieve monthly statistic feed broken down per campaign id, promo id and day and you'd like to see visits, registrations, FTDs and NGR and this data is needed in 1 currency EUR according to the current exchange rates date - you need to 1) configure all of these fields in the "Filters" block, 2) press "Filter" and 3) after that retrieve the XML/JSON feed link by pressing "Export report" button and choosing the required format.

Operator and Partner Reports are singled out into separate endpoints available via ** /api/customer/v1/casino/report  **and 

Your unique statistic token can be found on your operator’s detailed page: /casino/users/:user_id or in XML/JSON feed URLs. Affiliates can find their tokens on their Account page (each Partner User has a unique token associated with them) or in their XML/JSON feed URLs.

Any statistic token can be expired so that it's no longer used by a specific user.

The Customer API documentation containing the Information on the Operator Reports API can be found via the **/casino/api_docs/customer/casino/index.md** link in the Operator Interface.

All player activities in the Reports can be sorted in Ascending or Descending order. *E.g. you can sort Registrations in Descending order (from the largest to the smallest number), thus finding affiliates who invited the greatest number of players during a specified period of time. *

The Asc/Desc data sorting feature in **/casino/report **and **/partner/report **applies to columns with numbers only. You will not be able to sort such data types as text strings, currency, date and time, etc. Partner Income column is also excluded from Asc/Desc data sorting for the time being.

Upon the first click on the column name, Descending order is applied; upon the second click on the same column name - Ascending order; upon the third click - the sorting is removed. If you click on any other column name, the sorting is removed from the first column and applied to the other one.

To be able to sort money-related activities (e.g. deposits, bets, cashouts, ngr, etc), you need to use a single exchange currency for the whole report. To convert all activities into one single currency, scroll the filter down to "Convert all currencies" setting and choose the Currency in which you'd like to view the report.