How often are statistics updated in the system?

It depends on the frequency with which your iGaming platform provider send us data on players and their activities. Traditionally if the frequency is set at once an hour, then the data for the ended hour is updated on the 15th minute of the new hour (UTC). For example, if a player gets registered between 07:00:00 and 07:59:59 – the sync will happen at 08:15. Bills are issued after 6 a.m. (UTC) on the new day following the reporting period.

What exchange rates are used in Affilka?

We rely on ECB rates for fiat currencies. For those fiat currencies that are not supported by ECB, we apply xe.com. We rely on Coinmarketcap rates for crypto currencies.

The exchange rates for the bills  are taken 00:00 UTC of the day the bill is issued.

The exchange rates for the report are taken 00:00 UTC of the day indicated in the *Exchange rates date* field.

How long are cookies stored in the system?

Affiliate attribution cookie lifespan is managed by casino platform providers and commonly stored 30 days.

If a player has followed the link within this period with no registration and comes back for registration 31st day - as the cookie will be removed, that player will not be assigned to this affiliate.

Visit cookie lifespan is managed by Affilka and stored 30 days by default for the whole affiliate program.**Please, NOTE!** Do not confuse Affiliate attribution cookie with Visit cookie

 

Click uniqueness is tracked at the brand level. This means that if a partner A clicks a link from Promo 1 and later clicks a link from Promo 2 belonging to another partner, both under the same brand, the first click will be counted as unique, while the second click will be considered non-unique.

 

“First/Last cookie win” policy is managed by platform providers and in most of the cases “Last cookie win policy” is applied. Meaning that if a player has followed the link of one affiliate and didn't accomplish the registration, and then followed the link of other affiliate - the player will get assigned to the second affiliate.


No, it is not possible to change the email address used to log in to the interface.

**Alternative solutions:**

- **For affiliates:**
 Block the user with the incorrect email address and create a new user with the correct email under the existing affiliate account.
 Go to:- **List of Partners**- **→ Affiliate detailed page → “Users” tab**- `/casino/partners/:id/users`
- **For operators:**
 Block the user with the incorrect email address and create a new user with the correct email on the- **“Operators”**page:- `/casino/users`
 

Is it pоssible to configure several rewards within one Rule and Rule Group?

Yes, but the following peculiarities should be taken into account: all rewards will be summed up with each other, as there is no possibility to set a separate condition on each of them. For example, negative revshare will be deducted from positive fixed/fixed per player reward or other positive revshare.

 

Till when can I change the commissions configuration?

Until it's assigned to at least one affiliate.

 

Prove that checkboxes "Enabled"/"Default" are ticked off on the commission.

 

If this is the only commission in the overall commissions list with such a strategy, this commission will continue to work for old campaigns of the affiliate.

If there is a default commission of same strategy as the expired one or there is another individual commission of same strategy as the expired commission, assigned to an affiliate, it will be applied to old campaigns starting from next day. A bill will be issued on the expired commission next day. New commission will become available for new campaigns creation starting from next day.

 **Please, NOTE! **that an individual commission of same strategy as a default commission always prevail over default commission in terms of rewrite.

 

- The commission was archived in the common commissions list at `casino/commissions` page
- The commission was manually archived via click on `Expire`.
- `Scheduled to` date of the commission is applied and the commission is transferred under “Archived” tab to Commissions history.
 

If the commission in "Archived" state was not rewritten by another commission of same strategy, it will keep working for old campaigns. If an old campaign needs to be fully deactivated, one can rewrite the archived commission with the commission of same strategy, but empty Rule Groups.

 

- Expire the current affiliate commission.
- Create a new commission with the same strategy.
- Assign a new commission to an affiliate in the “Assign Commission” section.
- Upon rewrite, next day the bill will be issued on old commission, the new commission will automatically get assigned to old campaigns and will be available for new campaigns. 
 

Does it make sense to indicate the locale in the Landing Url?

It makes sense.

- If the locale is not indicated, a player will be referred to the locale according to browser language settings.
- If the locale is indicated and does not coincide with the browser language settings, a player will be referred to the locale, indicated in the Landing URL.

`<script type="text/javascript"src="https://balancerdomain/sources/b94geb3b9.js"></script>`, still wants a referral link to be via a banner. What is a solution?An affiliate should approach the following scenario:

- Download the banner from https://balancerdomain/sources/b94geb3b9.js and upload it at the web-site
- Create the promo with direct link and place the link on the uploaded banner.
 

If I create a dynamic tag in the system, will the previously sent parameters under this tag be shown in the report?

Yes, you can migrate a tag to players with the specified parameters who were registered before the dynamic tag was created. To do this, click the "Migrate" button after creating the tag. The tag will then be applied to the relevant players, allowing you to analyze reports by tags.

Bills review

How to understand the sums of revshare and cpa rewards in the bill on a hybrid commission?

The bill contains the total sum for both rewards:

- To calculate the revshare part from it, find "Partner Data" block in the bill, get fiat_ngr and coin_ngr sums and apply them to the configured in the commission reward revshare percent.
- To calculate the cpa part, find "Players Data" block in the bill, get the qualifications count and apply to the cpa reward, configured in the commission.

The player has bet the needed sum for meeting wager qualification criteria, but is not qualified. Why?

The wager sum which counts towards qualification in affiliate system depends on set bonus playthrough percent of games. If bets were made in the games with zero or partial bonus playthrough percent, the wager sum will be calculated as **Bets * Bonus playthrough percent**

Please check in the casino the player's bets sums and the games bonus playthrough percent and calculate the final wager sum.

**Please NOTE! **this formula applies specifically to projects on the SOFTSWISS casino platform. For projects operating on external casino platforms, it may differ.

How are the duplicates counted within modifier "omit duplicates" on revshare and cpa rewards?

Only players without duplicates and primary duplicates count towards qualification on cpa and revshare  rewards. Secondary duplicates are ignored.

If a player is qualified being a duplicate at the moment of bills check with "omit duplicates" modifier enabled on the qualifier in the commission, that only means that casino platform sent us this info on the player after the bills had been issued.

 

- Scheduled to date was applied on the commission.
- The commission used was expired.
- The current commission was rewritten by the new one with same strategy name.
 

Yes, if the result in one currency is a negative value, it will be converted into the currency of positive result and deducted from it for further reward calculation.

If you don't want negative results to be deducted from positive ones, you can set the condition of `min ngr: 0` with modifier `activity from: last bill `on both Rule Groups.


Partner debt is formed only if there is a negative reward in place. Negative reward is calculated only if the conditions/qualifiers are met. The debt sum is exactly the negative reward sum. The partner debt sum can be retrieved from Transactions overview at the detailed page of the partner.

If no condition/qualifier is met, no reward is issued, therefore no debt is assigned.

 

In Affilka it is possible to choose one of two formulas for calculating Casino NGR **at the setup stage**, depending on what the base of Admin fee calculation will be. 

- Admin fee is calculated from Casino NGR:`Casino NGR = (Bets - Rollback Bets) - (Wins - Rollback Wins) - (Issued Bonuses - Cancelled Bonuses) - (Positive Corrections - Negative Corrections) - Casino taxes sum] - [(Bets - Rollback Bets) - (Wins - Rollback Wins) - (Issued Bonuses - Cancelled Bonuses) - (Positive Corrections - Negative Corrections) - Casino taxes sum] * %Admin Fee (when set)`
- Admin fee is calculated from Casino GGR:`Casino NGR = [(Bets - Wins) - (Bets - Wins) * %Admin Fee (when set)] - [(Issued Bonuses - Cancelled Bonuses) - (Positive Corrections - Negative Corrections) - Casino taxes sum]`
 

**Please, NOTE! **The calculation formula is selected by the operator during the setup stage and cannot be changed later in live.

 

Rewrite their current commission with an empty one. Empty commission is a commission with 0 Rewards in the Rule Groups. Empty commission should have same strategy as the currently active one.

Statistics

How do visits count towards statistics?

It's cookie-based, so in the new system visit is a unique click with one set of cookie (**click over referral link with a unique s-tag visit value**). Towards "visits id=click" count:

- A unique click over the link without further registration
- A unique click over the link with further registration
- A unique click over the link after the cleared cookie after the previous click.
 

The data on visits = clicks in the Traffic report is updated almost in real-time.

 

Just remove all the checkboxes in the "Group by" block of the filter.

Is the information on manual deposits and cash-outs reflected in statistics?

Yes, both manual deposits and manual cash-outs are displayed in the system.

**Partner Income** is an analytical value, calculated each day, which aims at giving you an idea on how much you would pay to an affiliate if the commission bill were issued today.

Partner Income calculations in the Report tab are only **estimations** at a given point of time. The total billing amount could change at the end of the billing period. You need to **rely not on Partner Income but on partner bills while paying to your partners**.

To view Partner Income in the report, tick off the checkbox "Partner Income" on the */casino/report* page. If the calculation is complex and takes too much time to calculate, it will be emailed to you in csv.

To make this field visible to your partners, enable it on the */casino/settings* page in the "Partner Report Columns" tab. If your partner wants to see this field in the XML feed, they need to tick off the checkbox "Partner Income" on the */partner/report* page and press "Filter" first. Once the setting is saved, they can press "Report in XML" and it will be generated for them with the fields they've just set.

Before using this metric, please, note the **following peculiarities**:

**1)**  Please, be advised that Partner Income calculations presented in the report are only estimations at a given point of time. The total billing amounts **WILL CHANGE** at the end of the billing period. When paying commissions to your partners, you should always rely on partner bills rather than partner income.

**2)**  The total Partner Income at the end of the Report table is **not the sum of its selected rows**. It is Partner Income Calculation for this specific date for the ended period. Please mind this, especially while using grouping settings in your reports!

E.g. you have a progressive revenue share commission plan with FTD tiers where your partner gets 30% of NGR if the number of FTDs referred is ≤5 and 35% of NGR if the number is ≥6. On the first day, your partner invited 3 players. The calculation of Partner Income for this day will be based on the first tier - 30%. On the second day, your partner invited 5 players. The calculation of Partner Income for this day will be based on the first tier - 30%. The total, however, will be calculated according to the second tier - 35% because the total amount of the referred FTDs is over 6.

**3)** If you analyze Partner Income within the date range, when the commission rewrite happened, Partner Income will be calculated per **old** commission **till** **the rewrite** date and per the **new **working commission **starting from** **the rewrite** date in such report.

**4)** Partner Income **can be negative if applicable. **If NGR for a particular day is negative, PI will be negative. But if all the NGR for the same month is positive, then PI will be counted from the total NGR of the month, not like a sum of daily Partner Incomes.

**5) **If a player's status has changed (from self-excluded "false" to "true", from disabled "false" to "true", from duplicate "false" to "true".), and the commission has modifiers which are set by player attributes, Partner Income for the closed billing period remembers their status during that period and it isn't recalculated according to the new status. In other words: timestamps of status changes are accounted for in Partner Income calculations. The players who originally were qualified and paid for do not fall under Partner Income calculations for the closed billing period.

- **Duplicate status: applicable from October 1, 2023**

Example: if a player refers to a commission where the omit duplicates modifier was used and they were active for example in October, but received the duplicate status in November, Partner Income will exclude their activity in November, while it will not affect the calculations of Partner Income when viewing the report for October.

- **Self-excluded/ disabled statuses: applicable from December 1, 2023**

Example: if a player refers to a commission where the omits self-excluded/ disabledmodifiers were used and they were active in November, but received one of these statuses in December, Partner Income will exclude their activity in December, while it will not affect the calculations of Partner Income when viewing the report for November.

- If a player's status has changed from **verified "false" to "true"**, and the commission has modifiers which are set by player attributes, the Partner Income for the closed billing period will be recalculated, and the players who originally were qualified and paid will get into Partner Income for the closed billing period.*(will be fixed with later releases).*

We are constantly working on improving our system and on fixing the possible bugs. However, what we have to remember is that the logic of Partner Income Calculations and Commission Constructor features will remain the same.

 

Partner gets "IBAN is invalid" mistake all the time while entering the Bank Transfer details. What can be advised?

IBAN is the compulsory data field in the Bank Transfer form, apart from Beneficiary Name and Swift. Its number is formed from country code and under particular digit sequence rules.

One can check the validity of IBAN online via the following resources:

https://www.iban.com/iban-checker__https://www.ibancalculator.com/iban_validieren.html__


The official country limitations list is: Afghanistan, Irak, Iran, Jemen, Myanmar, Nordkorea, Sudan, Syrien, Uganda, Kuba.

We do not guarantee full success rate for the rest countries as we don't influence such factors as intermediary banks restrictions or internal policy of the recipient's banks.

From practice, sometimes banks may require additional documents to go on with the payment processing.


The formula is Issued Bills - Cancelled Bills + Balance Corrections

- where**issued bills**are all bills (paid, pending and cancelled) that were**created (=billed)**within the following time range: from the 1st day of accounting month after 10 am UTC till the 1st day of next accounting month before 10 am UTC
- where **cancelled bills**are bills with a**cancelled status**that were**processed**within the following time range: from the 1st day of accounting month after 10 am UTC till the 1st day of next accounting month before 10 am UTC
- where **balance corrections (positive-negative)**are taken within the following time range: from the 1st day of accounting month any time till the 1st day of next accounting month anytime

**Please keep in mind, **the described formula is relevant to projects running on the SOFTSWISS casino platform. In the context of other casino platforms, it may differ or may not be supported.

Is it possible to cancel a payment that has been successfully sent to e-wallet? (e.g. the partner states that the payment was sent to wrong details).

No, the successfully processed payment cannot be cancelled on our side. 

In such a case, you can advise your partner to contact the payment system directly by providing the transaction ID and describing the issue.

As for the transaction ID, you can find it in the payment's ‘Extra' field.

 

What is the payment schedule for parent affiliate to be paid for the earnings of the sub-affiliate?

Assuming that schedule plan in subaffiliate commission is set as Monthly, if a sub-affiliate is billed on the 1st of November, parent affiliate is billed on the 1st of December from sub-affiliate earnings, based on the sub-affiliate commission. You may set the subaffiliate commission schedule plan as the 2/5/10/etc. day of the month to shorten the bill waiting time.


Sportsbook formulas

`SB NGR = SB GGR - SB Bonuses - SB Balance Corrections - SB 3rd Party Fees - SB taxes`

`SB GGR = SB Bets - SB Cancelled Bets - SB Wins `

OR

`SB GGR = SB Settled bets - SB Wins`

 

For betting brands, it’s possible to customize two formulas: the calculation of Sportsbook GGR and the deduction of the SB Admin Fee.

The operator can choose one of the available options for deducting the Sportsbook Admin Fee.

- SB GGR = SB Bets - SB Cancelled Bets - SB Wins
- Admin fee Calculation **from GGR**, then:

| SB Real GGR = SB Bets - SB Cancelled Bets - SB Wins SB GGR = (SB Bets - SB Cancelled Bets - SB Wins) - (SB Bets - SB Cancelled Bets - SB Wins)*Admin Fee SB Real NGR = (SB Bets - SB Cancelled Bets - SB Wins) - (SB Bets - SB Cancelled Bets - SB Wins)*Admin Fee - SB Bonuses - SB Balance corrections - SB 3rd party fees - SB taxes SB NGR = (SB Bets - SB Cancelled Bets - SB Wins) - (SB Bets - SB Cancelled Bets - SB Wins)*Admin fee - SB Bonuses - SB Balance corrections - SB 3rd party fees - SB taxes | 

- SB GGR = SB Bets - SB Cancelled Bets - SB Wins
- Admin fee Calculation **from NGR**, then:

| SB Real GGR = SB Bets - SB Cancelled Bets - SB Wins SB GGR = SB Bets - SB Cancelled Bets - SB Wins SB Real NGR = (SB Bets - SB Cancelled Bets - SB Wins) - SB Bonuses - SB Balance corrections - SB 3rd party fees -SB taxes SB NGR = (SB Bets - SB Cancelled Bets - SB Wins) - (SB Bets - SB Cancelled Bets - SB Win - SB Bonuses - SB Balance corrections - SB 3rd party fees)*Admin Fee - SB Bonuses - SB Balance corrections - SB 3rd party fee - SB taxes | 

- SB GGR = SB settled bets sum - SB wins sum
- Admin fee Calculation **from GGR**, then:

| SB Real GGR = SB Settled Bets - SB Wins SB GGR = (SB Settled Bets - SB Wins) - (SB Settled Bets - SB Wins)*Admin Fee SB Real NGR = (SB Settled Bets - SB Wins) - (SB Settled Bets - SB Wins)*Admin Fee - SB Bonuses - SB Balance corrections - SB 3rd party fees - SB taxes SB NGR = (SB Settled Bets - SB Wins) - (SB Settled Bets - SB Wins)*Admin fee - SB Bonuses - SB Balance corrections - SB 3rd party fees - SB taxes | 

- SB GGR = SB settled bets sum - SB wins sum
- Admin fee Calculation **from NGR**, then:

| SB Real GGR = SB Settled Bets - SB Wins SB GGR = SB Settled Bets - SB Wins SB Real NGR = (SB Settled Bets - SB Wins) - SB Bonuses - SB Balance corrections - SB 3rd party fees - SB taxes SB NGR = (SB Settled Bets - SB Wins) - (SB Settled Bets - SB Wins - SB Bonuses - SB Balance corrections - SB 3rd party fees)*Admin Fee - SB Bonuses - SB Balance corrections - SB 3rd party fee - SB taxes | 

**Please, NOTE! **The calculation formula is selected by the operator during the setup stage and cannot be changed later in live.

Poker Module formulas

`Poker Real NGR = Poker rake - Poker bonuses - Poker balance corrections - Poker 3rd party fees``Poker Admin fee = Poker Real NGR * Poker Admin Fee``Poker NGR = Poker rake - Poker bonuses - Poker balance corrections - Poker 3rd party fees - Poker Admin Fee`


Whether to set up a sportsbook(-s) reward within the current commission(-s), which already includes rewards for activity in a casino, OR create new commission(-s) specifically for sportsbook activity **depends on a need to have specific CAMPAIGNS for sportsbook and casino traffic**.

If the rewards for casino and sportsbook activity are counted **within the framework of one commission**, it is necessary to create 2 promos within the campaign:

- 1 - promo link with a landing page leading to the casino page;
- 2 - promo link with a landing page leading to the sportsbook page.

In case there are different commissions for sportsbook and casino activity created, the promos will have to be created within separate campaigns. Remember that both commissions can work simultaneously for a partner only provided that they are of different strategies.



We recommend you to install 2FA on your account using your PC to enter 2FA code. The code is generated in "Authenticator" app (by Google) right after QR-code scanning using your smartphone.

While setting the 2FA please make sure that:

- the time on the device where you enter the 2FA code and the time on the device where the 2FA codes are generated is the same;
- no additional characters should be used when entering the code. In "Authenticator" app a 2FA code structure is “111 111” but you don't need to put «Space» symbol in the middle, i.e. you need to enter a 2FA code like this “111111”.


Please make sure that:

- you are trying to log in to the Operator Interface (example.com**/casino/**login) as an operator and not to the Partner Interface (example.com**/partner/**login);
- email, password, 2FA code (if applicable) are 100% correct;
- check if your account is blocked. If your account is blocked you won't be able to login to your account (see the details below);
- clear cache and cookies.
 

If the recommendations above did not help please try to login to your account using another device.


After a couple of unsuccessful login attempts your account will be locked automatically by the system.

To unlock your account you need to follow to your email to which your account is linked and find email with “Unlock instructions” subject. Inside the email you will find a “Unlock my account” link, by clicking on this link you will unblock your account.

Keep in mind that if you have several “Unlock instructions” emails you need to follow to the newest one.

- Reach out to your team members. It's possible to unlock and unblock on operator's detailed page `/casino/users/:id`, by ticking off "Locked" field.
 

User (partner or operator) can be **BLOCKED** in two cases:

- User was blocked manually on the corresponding detailed page.
- User was automatically blocked by the system by being inactive for more than 30 days.

User (partner or operator) can be **LOCKED** only in one case:

- When a user maxed out the limit of login attempts.


- Click on “Forgot your password?”.
- Add your account email.
- Press “Send me reset password instructions”.
- Find the reset email (should be the newest one) and click on the link in it to set a new password.

**Please, keep in mind!** that the password reset link is valid for 6 hours from the moment of the request.**Please, note! **You will be able to reset password from your account in the operator interface by the **casino**/password/new link, and affiliates need to use **partner**/password/new.