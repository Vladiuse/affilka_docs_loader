A commission is a set of rules that determine an affiliate reward for referring players to a casino. Rewards usually depend on players’ activity: deposits, bets, wins, issued/cancelled bonuses, wager, etc.

The following settings precede every commission creation:

| Field | Description | 
|---|---|
| Commission Title | Commission title is visible to affiliates. It should contain the gist of a commission in a few words and should not contain any sensitive info that the operator does not want their affiliates to see. | 
| Tags | Commission tags simplify the commission search process and their segmentation. Commission tags aren't visible to affiliates. After you add the desired tag, press “Enter” to save the tag in the field. Tags can also be assigned to published commissions via “Edit” on the detailed page of each commission. | 
| Strategy | An abstract identifier of a commission that unites different commissions into 1 group. The strategy name is set by the operator and it is not visible to affiliates (but you can make it visible to your affiliates in the reports). Only 1 commission of 1 strategy can be applied to 1 affiliate at a time. If you assign 2 commissions of 2 different strategies to 1 affiliate, they will not overwrite each other and any of them can be used by an affiliate to create affiliate campaigns. Strategy name can be anything you name it: CPA, hybrid, revshare, mixed, etc. IMPORTANT!Spelling matters. Rev_share, rev_share, Revshare, revshare, Rev Share, Rev share, rev share – are all different strategies and cannot overwrite each other. If you want to assign one commission instead of another seamlessly to the affiliate, make sure that you assign the commission of the same strategy as the old one. | 
| Fiat/Crypto base currencies | Allows you to filter the available brands with the corresponding base currencies in the “Choose brands” section, and determines which base currencies will be in the configuration of the new commissions. You will only need to choose something here if the brands present in your affiliate program have different base currency pairs. If the currency pairs are the same, you won't need to choose anything. | 
| Convert all conditions, qualifiers, rewards into one currency checkbox | Allows you to convert all conditions, qualifiers, and rewards into one currency so that all fiat/crypto players' activities are converted during a billing day at the exchange rate. To apply this setting, select a currency pair in the Fiat/Crypto base currencies field, enable conversion checkbox, choose one of the brand's base currencies and create a commission according to your requirements, taking into consideration The Calculation Logic and Debt mechanism when the setting is applied. | 
| Forgive Debts flag | When the condition is `FALSE`, the negative carryover accumulated in the reporting period(s) is transferred to the next billing period.  If the flag is set as`TRUE`, the negative carryover is not transferred to the next billing period at all or is transferred partially – see below. | 
| Forgive Debts Thresholds | These are limits up to which a casino forgives debts to an affiliate. All negative rewards above the set threshold are carried over to the next billing period and affect the overall bill amount. By default debts between fiat and crypto accounts of 1 affiliate user within 1 billing period are mutually offset unless there're specific conditions indicated within the commission itself. | 
| CasinoAdmin Fee | A fee that is deducted from the Casino Real NGR (or Real GGR, depending on the affiliate program initial settings) prior to affiliate reward calculation. The casino admin fee does not apply to CPA reward types. The casino admin fee is not visible to affiliates within commission settings but can be enabled within the reports at the operator's discretion. | 
| Sportsbook Admin Fee | A fee that is deducted from the Sportsbook Real NGR (or Real GGR, depending on the affiliate program initial settings) prior to affiliate reward calculation. The sportsbook admin fee does not apply to CPA reward types. The sportsbook admin fee is not visible to affiliates within commission settings but can be enabled within the reports at the operator's discretion. | 
| Poker Admin Fee | A fee that is deducted from the Sportsbook Real NGR (or Real GGR, depending on the affiliate program initial settings) prior to affiliate reward calculation. The sportsbook admin fee does not apply to CPA reward types. The sportsbook admin fee is not visible to affiliates within commission settings but can be enabled within the reports at the operator's discretion. | 
| Schedule Plan | It determines the periodicity with which a reward, if any, is billed to an affiliate. Rewards can be billed daily, weekly on specific days of the week, monthly on the 1st day of each month for the previous month, or on selected dates. | 
| Subaffiliate | The `Subaffiliate`flag should be enabled if you want to allow your affiliates to refer sub-affiliates to your Affiliate Program. Sub-affiliate commissions are always created separately from the commissions targeting players. As soon as you tick off this check-box, you will need to choose the balancer domain which will be used as a basis for creating sub-affiliate referral links. Please, note! Sub-affiliate commissions are created in the context of an Affiliate Program rather than a Brand – because sub-affiliates are invited to join the Affiliate Program and not a specific brand. Whether or not you will pay sub-affiliate commissions for specific brands, will depend on the individual commission settings. The`Default`checkbox in this commission defines whether the commission will be default for your affiliate program. If a specific commission is marked as`Default`, it means that it will be visible to all affiliates and sub-affiliate campaigns will be created automatically with the commission upon affiliate's registration. You can mark a commission as`Default`only after you've published it. Admin fees and debts are not applicable to Sub-affiliate commission plans. | 
| “Choose brands” section | If the commission is designed to reward affiliates for attracting players, rather than subaffiliates, you will be able to indicate the brands for which the commission is created. Checkboxes in the  | 

The `Enabled` checkbox allows you to set up a commission where you can specify conditions, qualifiers, rewards in one currency, for example EUR, so that all fiat and crypto players' activities are converted to a one brand's base currency. This setting allows you to avoid cryptocurrency exchange rate volatility. 

**Calculation Logic**

The conversion rate for cryptocurrencies to fiat currencies is taken on the day the bill is issued.

**1. CPA Commission**

Commission Rules: We pay €200 (fixed_per_player reward) per player meeting the Min FTD sum: €20 qualifier.

Players for January:

Player ID 123: FTD sum - 0.00055814 BTC

Player ID 456: FTD sum - 0.00038055 BTC

Bill Issued on February 1:

Player 123: Paid 200€ for €22 FTD after BTC conversion (qualifier sum achieved).

Player 456: Not paid for €15 FTD after BTC conversion (qualifier sum not achieved).

Total bill: €200 for 1 qualified player.

**2. RevShare Commission**

Commission Rules: 50% RevShare (ngr_percent) for the previous calendar month.

Players for January:

Player ID 123: NGR - 0.10000000 BTC

Player ID 456: NGR - 0.20000000 BTC

Bill Issued on February 1:

Total NGR for 2 players: 0.30000000 BTC, converted to €11821.70.

Total bill: €5910.85 (50% of total NGR).

**Debt Mechanism**

- If an affiliate has a debt in the base cryptocurrency, and a base fiat currency is selected in the “Convert all conditions, qualifiers, rewards into one currency” checkbox in the commission, then their crypto debt is assigned to the base cryptocurrency, and it will be deducted in the following billing periods at the exchange rate on the billing day.
- If an affiliate has a debt in two base currencies (fiat + crypto), then first the debt is covered in the currency selected in “Convert all conditions, qualifiers, rewards into one currency” checkbox, then the system takes into consideration the debt in the second base currency, not selected in the conversion setting.
- If the conversion setting is enabled in the commission, and a fiat currency is selected, but at the same time 20,000 EUR is set in "Forgive debts in fiat currency up to", and the affiliate has a debt in cryptocurrency, the system will forgive the debt in cryptocurrency based on the converted amount of 20,000 EUR at the exchange rate on the billing day.
- All commission debts with the “Convert all conditions, qualifiers, rewards into one currency” setting are set in the currency that is selected.

**IMPORTANT! **If the feature "Convert all conditions, qualifiers, reward into one currency" is enabled, you will need to create Rule Groups only in 1 currency.

If the conversion feature isn't enabled, then you need to create a Rule Group for your crypto-currency. Otherwise, crypto-stats will be ignored, and affiliates will not get paid for crypto traffic.

When creating commissions, you may use the Default modifiers autofill option so that the following modifiers are added automatically by default:

- activity from last bill: added to conditions, qualifiers, rewards
- omit duplicates, omit self-exclusions, omit disabled: added to qualifiers

We recommend to use `activity_from` modifier set to **"From last bill"** to ensure the system calculates reward for the current billing period.


You can use the option to duplicate rules and rule groups in order not to create them from scratch. The duplicated Rule group or Rule will have the same structure as the original one. The only thing you need to do is to change the numbers in the newly created Rule Group/Rule.

- If you duplicate Rule group the system will create the identical Rule group and place it right after the original one.

- If you duplicate Rule the system will create the identical Rule within the same Rule group and place it right after the original Rule.


Different Rule Groups can be created when setting up affiliate commissions. The number of Rule Groups you can create is unlimited. **All of them will be taken into account during commission calculation. **

For each Rule Group**,** you define the currency in which the commission is calculated: it can be either your casino’s base fiat or cryptocurrency or both.

If the feature "Convert all conditions, qualifiers, reward into one single currenct" is enabled, you will need to create Rule Groups only in 1 currency – the currency into which all stats will be converted.

If, however, the conversion feature isn't enabled, then you will need to create Rule Groups both in base fiat currency and in base crypto currency, otherwise, if you indicate just 1 currency, fiat, for example, then crypto-stats will be ignored, and affiliates will not get paid for crypto traffic


Every Rule Group consists of a set of Rules (or even 1 rule) that define the affiliate reward for players’ activity. The Rules of one Rule Group are checked in order of their appearance. When one rule in the rule group is triggered – the reward is paid for this rule, all other rules in the group are ignored by the system and the reward is not paid for them.


Each Rule may include the following entities:  

• Conditions

• Qualifiers

• Rewards  

One rule can include several conditions, qualifiers and rewards. Each of these entities serves a **defined** purpose. 


Players’ activity is checked against the Conditions set in the Rule. All conditions set in 1 rule must be satisfied for the Reward to be possible. 

 

The Conditions serve 1 purpose only: they check whether players’ activity meets the conditions or not.

**IMPORTANT!** If the conditions are satisfied, qualifiers and rewards may be applied. If not, the system goes over to the next rule, if any. Qualifiers and rewards are not even checked. The condition is considered to be satisfied only if players meet all the conditions of the same rule.

By default, the conditions are applied to all players referred by an affiliate (unlike Qualifiers which are applied to players on a per**-**player basis).  

**Example situation:  **

- *Condition 1: NGR of all referred players must be ≥1000 EUR*
- *Condition 2: Deposits count of all referred players must be ≥ 20*

*If both these conditions are met, then the system may go over to checking qualifiers and rewards settings. If not, the condition is not considered to be satisfied and there can be no further checks or rewards.*


Please, note, that you can create a commission without a reward (e.g. for analytical purposes). If you do not create a reward, the affiliate will not get paid, even when the conditions are met.

**You can apply modifiers to your conditions – and they will limit the scope of the conditions**. E.g. by default, the conditions check all players activity throughout their lifetime in a casino. However, if you add modifiers to Condition 1 and Condition 2 above, you will end up with different results.  


**Example situation:  **

*Condition 1: NGR of all referred players must be ≥1000 EUR. Modifier: activity to be taken into account: from last bill.  *

*Condition 2: Deposits count of all referred players must be ≥ 20. Modifier: activity to be taken into account: from last bill.  *

This modifier limits your conditions to a specific period of time. If from the last bill to the new bill calculation the affiliate’s players’ haven’t generated 1000 EUR NGR and haven’t made at least 20 deposits, the conditions above are not satisfied.


You can add an unlimited number of modifiers to your conditions. Each of them will limit the scope of your condition in its own way. As you can see, the modifier** activity_from** is used to indicate the timeframe for which the calculation should be carried out. By default, the lifetime is analysed. However, you can limit the scope to 1 month, 1 week, 1 day or the billing period.  


**IMPORTANT! **You should always indicate the modifier **activity_from** with the value **"from last bill"** in the Conditions if you want the Conditions to be calculated for the billing period. If you do not indicate any period modifier, the whole lifetime of players’ activity will be analyzed. 


If all the conditions in the rule are met, the system goes over to checking qualifiers and rewards.

Qualifiers are similar to conditions since they analyze player activity and can be limited with modifiers. However, unlike conditions, qualifiers check each single**-**player compatibility with its settings and analyzes players on a per-player basis. The player is considered to be qualified when qualifier settings are met. As soon as the player is qualified, the qualification criteria are no longer applied to them.  

All qualifiers of 1 rule must be passed for the player to be considered qualified

**Example situation:**  

*Qualifier: deposits sum ≥ 100 EUR.  *

*Modifier: period from registration 2 weeks.  *

*Each player whose total deposits amount during 2 weeks after registration is at least 100 EUR will be qualified.  *

*If the total deposits amount is lower – qualification is not passed.  *

*If the total deposits amount is ≥100 EUR, but this amount was reached 3 months after registration – qualification is not passed.*  

**IMPORTANT!** If you do not indicate the modifier **activity_from**, the qualification criteria will be applied to the whole lifetime of players’ activity.**IMPORTANT!** Our commission constructor doesn't support 0 value in qualifiers. If you place 0 value into qualifier the system will ignore qualifiers and modifiers, all registered players will be qualified.


If all the conditions (or qualifiers) in the rule are met, the system goes over to rewards.

Rewards define the fee that the affiliate will get for referring players to the casino. You can set a fixed amount of money, percent from NGR, fixed amount per player, etc.


By default, rewards calculation is also carried out for the whole lifetime of players’ activity in a casino. The scope of calculation can also be limited by such a modifier as **Activity from**.  

Rewards are summed up for all Rule Groups and within one Rule. If the amount is positive, the reward is paid. If the amount is negative, the partner’s debt is either forgiven, or carried over, either in full or in part, into the next billing period (depending on the configuration of your commission pre-sets).

The **Templates** dropdown, located in the top-right corner of the **Commission Rules** section, provides access to the most common commission structures in Affilka. You can choose from pre-configured templates for **CPA, Revshare, Hybrid,** and **Subaffiliate** deals.

**Note:** If the **"Convert all conditions, qualifiers, and rewards into one currency"** checkbox is unchecked, the template will automatically generate two separate Rule Groups: one for fiat currencies and one for cryptocurrencies.


**Casino & Sportsbook CPA Templates**

Standard CPA commissions for both Casino and Sportsbook are built using three core components: **Qualifiers**, **Modifiers**, and **Rewards**. For qualifiers `first_deposit`* and *`sb_bets_sum `are used accordingly. 

Please check Classic CPA for more details.


**Casino & Sportsbook Dynamic Revshare Templates**

Dynamic Revshare commissions utilize a **ladder concept**: as the Net Gaming Revenue (NGR) generated by a partner’s players increases, the percentage of NGR rewarded to the partner also increases. These templates consist of **Conditions** and **Rewards** components.

Please check Classic Casino Revshare for more details.


**Hybrid Commission Templates**

A **Hybrid commission** combines both CPA and Revshare structures into a single deal. The template automatically organizes these into two separate **Rule Groups** so that the partner is rewarded for both types of activity simultaneously.

Please check Classic Hybrid Commission for more details.


**Revshare Commissions Templates**

Unlike CPA or Hybrid structures, standard **Revshare commission templates** consist of the **Reward** component. They are designed to payout a percentage of the revenue generated by a partner's players. Reward percentage is to be specified in the commission template.

Please check Revshare commissions for more details


**Subaffiliate Commission Template**

The **Subaffiliate commission** is designed for "Master Affiliates" to incentivize them to recruit and manage other affiliates (Subaffiliates). This template defines the percentage of a Subaffiliate’s total earnings that the Master Affiliate will receive as a reward.

Please check Sub-affiliate commissions for more details.

In CPA commissions affiliates usually get rewarded for specific player actions such as deposits (deposits sum) and bets (wager sum). As soon as a player meets qualification criteria set in qualifiers (e.g. makes a certain amount of deposits or bets during a set timeframe), the player is marked as qualified and further player actions will not be analyzed by the system in CPA commissions.


| 
 
 *First deposit sum ≥ 20 EUR**Wager ≥ 200 EUR*
 
 | |
| 
 
 | |
| 
 
 **Conditions:**empty**2 Qualifier:**first deposit sum min 20 EUR and casino wager min 200 EUR**Modifiers for qualifiers (same for each qualifier):**activity from: last bill; omit duplicates; omit self-exclusions; omit disabled players
**Rewards:**100 EUR fixed per player
 
 
 
 
 | |


If there is a need to test traffic from an affiliate by paying for a particular number of qualifying players, independent of how many qualifying players will be brought by the affiliate in the billing period, there is a possibility to set a cap on the CPA reward. No matter how many players will be referred by this affiliate and qualified, the bill sum will be no more than the set maximum fixed reward.

| 
 
 *First deposit ≥ 20 EUR;**Depositors must not have duplicates, active self-exclusion limits and must not be disabled/-blocked.*
 
 | |
| 
 
 | |
| 
 
 **Conditions:**empty**Qualifier:**first deposit sum min 20 EUR.**Modifiers for qualifier:**activity from: last bill; omit duplicates; omit self-exclusions; omit disabled players
**Rewards:**50 EUR fixed per player, 1000 EUR maxed fixed reward
 
 | |

Geo-specific CPA

In some cases, CPA rewards are paid only for traffic from specific geographic regions. For example, an operator agrees with an affiliate that they’ll get paid higher CPA for players from Scandinavia and DACH countries while other traffic will either be ignored or paid for less.

| 
 
 *100 EUR for every referred player from Sweden, Norway and Finland**50 EUR for every referred player from Germany, Austria and Switzerland**20 EUR for all other regions excluding CIS and its former states*
 
 *First deposit ≥ 20 EUR**Wager ≥ 200 EUR*
 | |
| 
 
 | |
| Such a commission will have as many Rule Groups as geographic tiers for which affiliates will get paid. In this particular case, the commission settings will feature at least 3 Rule Groups. 
 **Conditions:**empty**2 Qualifiers:**first deposit sum min 20 EUR, wager sum min 200 EUR**Modifiers for qualifiers****(same for each qualifier)**: player countries – only Sweden, Norway and Finland
**Reward:**100 EUR fixed per player
 
 
 | |
| 
 **Conditions:**empty**2 Qualifiers:**first deposit sum min 20 EUR, wager sum min 200 EUR**Modifiers for qualifiers (same for each qualifier)**: player countries – only Germany, Austria and Switzerland
**Reward:**50 EUR fixed per player
 | |
| 
 **Conditions:**empty**2 Qualifiers:**first deposit sum min 20 EUR, wager sum min 200 EUR**Modifiers for qualifiers (same for each qualifier)**: player countries – except Russian Federation, Belarus, Ukraine, Azerbaijan, Kazakhstan, Kyrgyzstan, Armenia, Moldova (Republic of), Tajikistan, Uzbekistan, Germany, Austria, Switzerland, Sweden, Finland, Norway
**Reward:**20 EUR fixed per player
 | |

CPA + conditions

Adding conditions to a CPA commission might produce an interesting effect. Conditions precede qualifiers, so **the system does not check the qualifiers till all conditions of the rule are met.** Such commission configuration can be used if you have signed off a CPA deal with an affiliate but you do not want to pay CPA rewards for the referred players till certain conditions (=activity thresholds) are met.  

| 
    *Total deposits sum ≥ 5000 EUR**Total deposits count ≥ 100**Effective deposits sum ≥ 2500 EUR**Total wager sum ≥ 10000 EUR*
 
 *Min deposits sum ≥ 20 EUR**Wager ≥ 200 EUR*
 | |
| 
 
 | |
| 
 
 **4 Conditions:**min deposits sum 5000 EUR; min deposits count 100; min effective deposits sum 2500 EUR; min wager 10000 EUR.**Modifiers for conditions (same for each condition):**empty. The system will analyze the lifetime of all players activity.
**2 Qualifiers:**min deposits sum 20 EUR; min wager sum 200 EUR**Modifiers for qualifiers (same for each qualifier):**empty. The system will analyze the lifetime of all players activity.
**Rewards:**50 EUR fixed per player reward
 | |

Complex CPA

Players can **be qualified against various criteria: deposits sum, wager, deposits count, first deposit amount, effective deposits sum.  **

You may choose not to pay CPA for players who have passed the qualification criteria after a long period of time. E.g. a player followed an affiliate, registered, made no deposits, disappeared for 2 months and then reappeared and made a deposit. The player likely returned thanks to the efforts of the casino’s player retention team and the affiliate has nothing to do with it. Thus, you can **limit your qualifiers with period modifiers (e.g. 1 month).  **

| 
 
 *deposits sum ≥ 20 EUR**wager ≥ 200 EUR*
 
 | |
| 
 
 | |
| 
 
 **Conditions**: empty**2 Qualifiers**: min deposits sum 20 EUR, min wager 200 EUR**Modifiers for qualifiers****(same for each qualifier)**: period since registration 1 month, activity from: last bill (30 days/60 days, etc.)
**Reward:**50 EUR per player
 | |



| Example situation Need to pay: 60 EUR fixed per player reward is paid for min first deposit of 20 EUR + sportsbook bets of 100 EUR (for the last billing period). Not paying for duplicated, self-excluded, disabled players. | |
| 
 
 
 **2 Qualifier:**first_deposit 20 EUR and sb_bets_sum 100 EUR.**Modifiers for qualifiers****(same for each qualifier):**Activity from last bill; omit duplicates; omit self-exclusions, omit disabled players.
**Reward:**60 EUR fixed per player
 | |


Where a single player wallet is used, deposits are not divided between casino and sportsbook. Hence, the qualifiers for the CPA commission should be wisely selected, especially when CPA rewards for sportsbooks and casinos are configured within one commission. To conclude, choosing Casino Wager as an additional or only qualifier for casino reward is crucial so that you don't pay casino reward for sportsbook deposit.

| 
 *100 EUR fixed per player reward is paid for min first deposit of 20 EUR + casino wager of 20 EUR (for the last billing period). Not paying for duplicated, self-excluded, disabled players.**60 EUR fixed per player reward is paid for min first deposit of 20 EUR + sportsbook bets of 100 EUR (for the last billing period). Not paying for duplicated, self-excluded, disabled players.*
 | |
| 
 
 
 **2 Qualifier:**first_deposit 20 EUR and casino_wager 20 EUR**Modifiers for qualifiers (same for each qualifier):**Activity from last bill; omit duplicates; omit self-exclusions, omit disabled players.
**Reward:**100 fixed per player
 | |
| 
 
 **2 Qualifiers:**first_deposit 20 EUR and sb_bets_sum 100 EUR.**Modifiers for qualifiers (same for each qualifier):**Activity from last bill; omit duplicates; omit self-exclusions, omit disabled players.
**Reward:**60 EUR fixed per player
 | |
| 
 If the strategy is to pay CPA for players, who meet both deposit and wager criteria in the billing period, and the player doesn't qualify for casino reward, such a player will be checked against both deposit and bets/wager qualifiers of the Rule Group, where sportsbook reward is configured. 
 A player can't be qualified twice in the system, therefore the qualification will happen by the Rule Group, which is configured first by the structure of the commission. | |


If you want to pay an affiliate a fixed reward for each player who uses deposits in poker room or you want players to qualify only if the poker rake condition is met, then in the classic CPA commission you can combine poker and deposit qualifiers.


| 
 
 *First deposit sum ≥ 10 EUR**Poker rake sum ≥ 50 EUR*
 | |
| 
 
 
 **2 Qualifier:**First deposit sum min 10 EUR and Poker rake sum min 50 EUR.**Modifier for qualifiers (same for each qualifier):**Activity from last bill.
**Rewards:**Fixed per player 100 EUR
 
 | |


In cases where you need to set up a commission with **a fixed fee per each lead**, you can use the **Qualifier - registration**. This qualifier may be also limited by modifiers. 


| Example situation:You want to pay 50 EUR for each registration, and players should not be duplicates, self excluded or disabled. At the same time, players should be from certain countries (let’s say, only from Norway, Romania and Italy).  | |
| 
 **Qualifier:**registration**Modifiers for qualifiers:**Sign up at from:last bill -this modifier limits the period during which the registration needs to occur in order for a player to be qualified;
 omit duplicates, self-excluded and disabled, player countries.
**Reward:**50 EUR fixed per player
 
 | |
| 
 You may also add other qualifiers to the commission, but  | |

In revshare commissions, affiliates get a share of Casino NGR generated by players they referred. NGR stands for Net Gaming Revenue. It is calculated according to the following formula: Bets – Wins – Bonuses - Additional Deductions - Casino Taxes - Admin Fee.

| 
 *If*the*NGR of the referred players is ≥ 5000 EUR, an affiliate will get 50% of NGR.**If NGR is ≥ 2500 EUR, the affiliate will get 40% of NGR.**If NGR is between 0 – 2500 EUR, the affiliate will get 30% of NGR.*
 | |
| 
 
 | |
| 
 
 
 **Conditions**: min NGR 5000 EUR**Modifiers for condition:**activity from last bill. Modifier**activity_from**with the value “from last bill” indicates that only NGR for the period from the last bill will be taken into account.
**Qualifiers**: empty**Rewards:**ngr percent 50%**Modifiers for reward:**activity from last bill. Modifier**activity_from**with the value “from last bill” indicates that only NGR for the period from the last bill will be taken into account.
 | |
| 
 **Conditions:**min NGR 2500 EUR**Modifiers for condition:**activity from last bill. Modifier**activity_from**with the value “from last bill” indicates that only NGR for the period from the last bill will be taken into account.
**Qualifiers:**empty**Rewards:**ngr percent 40%**Modifiers for reward:**activity from last bill. Modifier**activity_from**with the value “from last bill” indicates that only NGR for the period from the last bill will be taken into account.
 | |
| 
 **Conditions:**empty. If the 2 rules above haven’t been triggered, the 3rd one will definitely be triggered because there are no additional conditions for it.**Qualifiers:**empty**Rewards:**ngr percent 30%**Modifiers for reward:**activity from last bill. Modifier**activity_from**with the value “from last bill” indicates that only NGR for the period from the last bill will be taken into account.
 | |


In a standard case of a revshare deal, an affiliate is paid every next month a particular revshare part from the NGR of the newly registered in this billing period players and from the new NGR of the already referred in the past billing periods players. If you would like that activity of already referred players has counted towards the total billing for a limited time period from these players' registration, you can set an additional modifier called "period since registration" on the reward for this purpose. Thus, when the indicated period since registration ends, the NGR of these old players will not get into calculations of the sum of the overall bill, but at the same time, the activity of these old players will keep falling into reports and stats.

| 
 
 | |
| 
 
 | |
| 
 **Conditions:**empty**Qualifiers:**empty**Rewards:**ngr percent 45%**Modifiers for reward:**activity from last bill; period since registration - 365 days
 
 | |
| 
 Period since registration: week - the limit will be 7 days from the date of registration (sign up at date).
 For example, in the commission we have period since registration: week, Schedule plan: Wednesday. The player registered on October 5 at 8 AM, his activities will be counted until October 12, 8 AM. Billing starts every Wednesday: October 5,12,19. And billing, which will be on October 12, will take into account gaming activities from October 5, 8 AM to October 12, 00:00, then billing, which will be on October 19, will calculate gaming activities from October 12, 00:00 to October 12, 8 AM. Period since registration: month - takes into account the period of 30 days from the date of registration. If you want activities to be counted within 31 days after registration, you need to select Days Count and add 31.
 | |

Deposit-tiered Revshare

Classic revshare commissions (where a reward is determined exclusively by NGR) have their flaws, namely: casinos may suffer losses due to big wins. As a rule, casinos do not transfer negative carryover to the next billing period. If in the next billing period the player loses money, the casino will pay the affiliate their share of NGR from this player, even though in reality this player hasn’t generated money for the casino.

To avoid such losses, it is best to create revshare commissions whose calculation will depend not only on NGR but also on player deposits.

| 
 
 *total deposits sum ≥ 5000 EUR, deposits count ≥ 100, depositing players count ≥ 20 – will land affiliate with 70% reward**total deposits sum ≥ 2500 EUR, deposits count ≥ 50, depositing players count ≥ 15 – will land affiliate with 60% reward**if the conditions of the above-mentioned rules are not satisfied, the affiliate will get 10% of*the*NGR*
 | |
| 
 
 | |
| The Rule Group will consist of 3 Rules. Each Rule represents a specific Deposit tier according to which reward calculation will be carried out. The Rules of one Rule Group are checked in order of their appearance so you should indicate higher numbers first. When one rule in the rule group is triggered – the reward is paid for this rule, all other rules in the group are ignored by the system and the reward is not paid for them.   
 **3 conditions**: min deposits sum 5000 EUR, min deposits count 100, min depositing players count 20**Modifiers for conditions**: activity from last bill
**Qualifiers**: empty**Rewards**: ngr percent 70%**2 Modifiers for rewards:**activity from last bill; players with min 2 deposits
 Modifier  | |
| 
 **3 conditions:**min deposits sum 2500 EUR, min deposits count 50, min depositing players count 15**Modifiers for conditions**: activity from last bill
**Qualifiers**: empty**Rewards**: ngr percent 60%**2 Modifiers for rewards:**activity from last bill; players with min 2 deposit
 | |
| 
 **Conditions:**empty**Qualifiers:**empty**Rewards**: ngr percent 10%**2 modifiers for rewards:**activity from last bill; players with min 2 deposits
 | |


In a standard scenario, when no reward is issued because no conditions are met for rewarding, the condition results are reset every billing period. With the help of a modifier **"activity from last issued bill"** on condition and reward, the condition results can be accumulated for several billing periods and taken for reward calculation.

| 
 
 *FTD >31 from last issued bill = 45% of NGR from last issued bill**FTD 11-30 from last issued bill = 40% from NGR from last issued bill**FTD 6-10 from last issued bill = 35% from NGR from last issued bill**FTD 1-5 from last issued bill = 30% from NGR from last issued bill*
 | |
| 
 
 
 **Condition**: min FTD count 31**Modifiers for conditions**: activity from last issued bill
**Qualifiers**: empty**Rewards**: ngr percent 70%**Modifiers for rewards:**activity from last issued bill
 | |
| 
 
 modifier:Let's assume that your affiliate invited 10 FTDs during the 1st month, 15 FTDs during the 2nd month and 5 FTDs during the 3rd month of your partnership. For the first 2 months, their cumulative NGR was negative (-300 EUR and 200 EUR), so no bills were issued. For the 3rd month, their NGR was positive (400 EUR) and cumulative NGR for the 3 months was positive as well (-300+200+400). 
 
 1) 200*40% (15 FTDs) = 80 EUR for the 2nd billing period2) 400*30% (5 FTDs) = 120 EUR for the 3rd billing periodtheNOTE!If you usemodifier  "activity from last issued bill" on condition and reward, please use  "forgive debts true" only, as the reward is billed from cumulative condition/qualifier met and there is no sense to keep and carryover any partner debts. | |


The configuration of the commission will be similar to the classic revshare commission in the casino with the only difference being that you should use Poker Admin Fee % parameter instead of the Casino Admin Fee.

| 
 *If Poker NGR is more than 5000 EUR for the billing period, then the Poker NGR % will be 40%.**If Poker NGR is less than 5000 EUR for the billing period then the Poker NGR % will be 35%.*
 | |
| 
 
 
 **Condition:**Min Poker NGR 5000 EUR,**Modifiers for condition:**Activity from last bill
**Reward:**Poker NGR Percent 40%,**Modifiers for reward::**Activity from last bill
 | |
| 
 **Condition:**Min Poker NGR 0 EUR,**Modifiers for condition:**Activity from last bill
**Reward:**Poker NGR Percent 35%,**Modifiers for reward::**Activity from last bill
 | |
| 
 
 | |


You can subtract Game Providers Fees and Payment Systems Fees from the Casino NGR percent reward. The setting is available within the casino `ngr_percent` reward type. **Please, note! **Game providers fees and Payment systems fees are subtracted from the reward, and not NGR itself.

To subtract 3rd party fees from the affiliate reward, indicate the desired percentage (e.g. game providers fees - 45%, payment systems fees - 45%) in the input field. The modifiers you apply to this reward (e.g. `activity_from_last_bill`) will be true for the game providers fees and payment systems fees settings as well.

**IMPORTANT!** Game providers fees and Payment systems fees should be subtracted proportionally to the amount of the reward. We strongly recommend that you i**ndicate the same percent as the percent of the reward** here and that you do not charge your affiliates 100% of the fees. Otherwise you may find yourself in a situation where your NGR reward is a negative one due to the negative NGR amount. And when you subtract 100% of negative game providers fees or payments systems fees, you may end up paying an affiliate though their NGR is negative.

**EQUALLY IMPORTANT!** If you decide to subtract game providers fees or payment systems fees from the reward, you should **lower your Admin fee **if you use one. Third party fees may account for up to 30% of NGR. If you charge an Admin fee of 35%, you're already subtracting game providers fees or payment systems fees from the reward. There's no need to subtract them twice. So when subtracting 3rd party fees, you should definitely lower the Admin fee or scrap it altogether.

Hybrid commissions normally represent a mix of CPA + revshare rewards where affiliates get a share of the revenue from referred players as well as one-time payments when players reach specific qualification criteria.

 

| 
 
 *first deposit ≥ 20 EUR**wager ≥ 200 EUR*
 
 | |
| 
 
 | |
| This Rule Group governs the CPA reward.  
 **Conditions:**empty**2 Qualifiers:**min first deposit 20 EUR, min wager 200 EUR**Modifiers****for qualifiers (same for each qualifier**): period since registration 90 days, activity from: last bill
**Rewards**: 100 EUR per qualified player
 | |
| This Rule Group governs the RevShare reward.  
 **Conditions**: empty**Qualifiers:**empty**Rewards:**50% of NGR**Modifier for rewards**: activity from last bill
 | |
| 
 **Condition type:**`casino_ngr`**Min casino NGR:**0
 This ensures the system only calculates rewards when the NGR value is positive. We recommend to use  | |

Сomplex Hybrid Commission


| 
 
 *effective deposits sum ≥ 20 EUR**deposits count ≥ 5**wager ≥ 200 EUR*
 
 *if NGR ≥ 5000 EUR and wager ≥ 10000, the affiliate will get 50% of NGR and 10% of*the*wager sum**if NGR ≥ 2500 EUR and wager ≥ 5000, the affiliate will get 20% of NGR and 4% of*the*wager sum**if none of the above is true, the affiliate will not get paid.*
 | |
| 
 
 | |
| This Rule Group shall govern the CPA reward and revshare reward for non-qualified players.  
 **Conditions**: empty**3 Qualifiers**: min effective deposits sum 20 EUR, min deposits count 5, min wager 200 EUR**2 Rewards:**50 EUR fixed per player reward for every qualified player, 1-50% of NGR per player (if an affiliate refers 1 player – 1% of this player’s NGR shall be shared; if 25 players – 25%; if 50 players – 50%; if 60 players – 50%)**2 Modifiers for rewards (same for each reward**)**:**activity from last bill; not qualified players only
 This is how the Rule Group will work: an affiliate refers players who make bets in a casino. Until these players meet the qualification criteria, the affiliate gets 1-50% of NGR generated by these players (percentage depends on the number of referred players but no more than 50%). As soon as some player meets the qualification criteria, this player is marked as qualified, the affiliate gets a one-time CPA reward for this player (50 EUR) and this Rule Group is no longer applied to this player’s activity. | |
| Let’s add Rule Group which will govern the revshare reward for the activity of players who passed the qualification criteria: 
 
 **2 Conditions**: min NGR 5000 EUR; min wager 10000 EUR;**2 Modifiers for conditions****(same for each condition)**: activity from last bill; qualified players only;
**Qualifiers**: empty**2 Rewards**: ngr percent 50%; wager percent 10%**2 Modifiers****(same for each reward)**: activity from last bill; qualified players only.
 
 | |
| 
 **2 Conditions:**min NGR 2500 EUR; min wager 5000 EUR;**2 Modifiers for conditions****(same for each condition)**: activity from last bill; qualified players only
**Qualifiers:**empty**2 Rewards:**ngr percent 20%; wager percent 4%**2 Modifiers****(same for each reward)**: activity from last bill; qualified players only
 
 | |


Each affiliate can invite other Affiliates and get a commission from their earnings. The parent affiliate commission can be calculated only based on:

- the bills issued to their subaffiliates, regardless of the bill status.
- the ngr that were generated by their subaffiliates' players.

One Affiliate can be both a "parent" and a "child" of another affiliate. Parent Affiliate gets a commission not only from their directly referred subaffiliates, but also from sub-affiliates referred by their "children".

It is also possible to exclude certain brands from sub-affiliate commission calculation (e.g. if you want to reward parent affiliate only for brand A, excluding Brand B).

Let’s set up a multi-tier commission where affiliates, depending on their level of affiliation get a percentage of earnings from their sub-affiliates.

| Example situation: Parent affiliate will get 5% of the earnings of the 1st level sub-affiliate, 3% of the earnings of the 2nd level sub-affiliate and 1% of the earnings of the 3rd level sub-affiliate. Preliminary condition: min sub-affiliate earnings should be: 1000, 750 and 500 EUR for every level of sub-affiliation. The earnings shall only be paid for Brand ID: 1. | |
| 
 
 The “Forgive debts” and “Admin fee” settings cannot be applied for subaffiliate commissions. As soon as you tick off the checkbox “Subaffiliate: True”, these fields will not be available for editing. 
 | |
| The commission must be configured via different Rule Groups (not Rules). 
 **Conditions:**min subaffiliate earnings 1000 EUR**3 Modifiers for condition**: subaffiliate level 1; subaffiliate period – activity from last bill; only brand id 1.
**Reward**: subaffiliate earnings percent 5%**3 Modifiers for reward:**subaffiliate level 1; subaffiliate period – activity from last bill, only brand id 1.
 | |
| 
 This Rule Group shall govern the 2nd level of subaffiliation. 
 **Conditions**: min subaffiliate earnings 750 EUR**3 Modifiers for condition**: subaffiliate level 2; subaffiliate period – activity from last bill; only brand id 1.
**Reward:**subaffiliate earnings percent 3%**3 Modifiers for condition**: subaffiliate level 2; subaffiliate period – activity from last bill; only brand id 1.
 | |
| 
 This Rule Group shall govern the 3rd level of subaffiliation. 
 **Conditions:**min subaffiliate earnings 500 EUR**3 Modifiers for condition**: subaffiliate level 3; subaffiliate period – activity from last bill; only brand id 1.
**Reward**: subaffiliate earnings percent 1%**3 Modifiers for reward**: subaffiliate level 3; subaffiliate period – activity from last bill; only brand id 1.
 | |
| Let’s imagine that 1st level subaffiliate earned 5000 EUR on Brand 1 and 1000 EUR on Brand 2.2nd level subaffiliate earned 2000 EUR on Brand 1 and 3000 EUR on Brand 2.3rd level subaffiliate earned 6000 EUR on Brand 1 and 2500 EUR on Brand 2.
 What reward will the “parent” affiliate get? The calculation will take into account only the results generated on Brand 1. It will look as follows: “Parent” affiliate will get:  5% of 5000 eur, 3% of 2000 eur and 1% of 6000 eur. Total: 250+60+60=370 eur
1st level subaffiliate will get:  5% of 2000 eur and 3% of 6000 eur. Total: 100+180=280 eur
2nd level subaffiliate will get:  5% of 6000 eur. Total: 300 eur
 | |


Each affiliate can invite other Affiliates and get a percentage of Net Gaming Revenue generated by sub-affiliate's players for the specified reporting period.

**Configuration options to keep in mind:**

- Sub-affiliate levels: one Affiliate can be both a "parent" and a "child" of another affiliate. Parent Affiliate gets a commission not only from their directly referred subaffiliates, but also from sub-affiliates referred by their "children". If you want to pay only for subaffiliates of level 1, then you need to clearly indicate it in the commission modifiers. If you want to set different settings for different levels, then you need to indicate which settings will be applied to the selected levels.
- Brands: You can exclude certain brands from sub-affiliate commission calculation (e.g. if you want to reward parent affiliate only for brand A, excluding Brand B).
- Product Modules: If your affiliate program features Casino, Sportsbook, and Poker, you can pay a percentage of NGR from all modules or pay a percentage of NGR from specific modules only (e.g. only from Casino NGR).

**Limitations:**

- Admin fee: Keep in mind that during reward calculation the Admin fee is already pre-deducted based on the percentages indicated in player commissions.
- Debts (Negative Carryover): Debts cannot be generated for parent affiliates during sub-affiliate reward calculation. Thus, Negative carryover is not available for Sub-affiliate commission plans.

Let’s set up a multi-tier commission where affiliates will get a percentage of NGR from their sub-affiliates.

 

| 
 
 | |
| 
 
 The “Forgive debts” and “Admin fee” settings cannot be applied for subaffiliate commissions. As soon as you tick off the checkbox “Subaffiliate: True”, these fields will not be available for editing. | |
| The commission must be configured via 4 different Rule Groups (not Rules). 
 
 **Conditions:**min subaffiliate casino NGR 1000 EUR**3 Modifiers for condition**: subaffiliate level 1; subaffiliate period – activity from last bill; only brand id 1.
**Reward**: subaffiliate Casino NGR percent 10%**3 Modifiers for reward:**subaffiliate level 1; subaffiliate period – activity from last bill, only brand id 1.
 | |
| 
 This Rule Group shall govern the 1st level of sub affiliation and will pay out rewards as a percentage of sub-affiliate Sportsbook NGR. There will be additional Rule Groups for Casino and Sportsbook for sub-affiliate level 2. 
 **Conditions:**min subaffiliate Sportsbook NGR 1000 EUR**3 Modifiers for condition**: subaffiliate level 1; subaffiliate period – activity from last bill; only brand id 1.
**Reward**: subaffiliate Sportsbook NGR percent 10%**3 Modifiers for reward:**subaffiliate level 1; subaffiliate period – activity from last bill, only brand id 1.
 | |
| 
 This Rule Group shall govern the 2nd level of sub affiliation and will pay out rewards as a percentage of sub-affiliate Casino NGR. There will be additional Rule Group for Sportsbook. 
 **Conditions:**min subaffiliate Casino NGR 1000 EUR**3 Modifiers for condition**: subaffiliate level 2; subaffiliate period – activity from last bill; only brand id 1.
**Reward**: subaffiliate Casino NGR percent 5%**3 Modifiers for reward:**subaffiliate level 2; subaffiliate period – activity from last bill, only brand id 1.
 | |
| 
 This Rule Group shall govern the 2nd level of sub affiliation and will pay out rewards as a percentage of sub-affiliate Sportsbook NGR. 
 **Conditions:**min subaffiliate Sportsbook NGR 1000 EUR**3 Modifiers for condition**: subaffiliate level 2; subaffiliate period – activity from last bill; only brand id 1.
**Reward**: subaffiliate Sportsbook NGR percent 5%**3 Modifiers for reward:**subaffiliate level 2; subaffiliate period – activity from last bill, only brand id 1.
 | |

So how will the commission be calculated in a real-life scenario?

Let's imagine the following:

The Admin fee is calculated as a percentage of Real NGR across the affiliate program.

Parent affiliate has 2 sub-affiliates (a+b) of lvl 1 and 2 sub-affiliates (c+d) of lvl 2. During May 2025 they have generated the following NGR on Brand 1:

| Sub-affiliate | Casino Real NGR | Admin fee | Casino NGR | Sportsbook Real NGR | Admin fee | Sportsbook NGR | 
| A: lvl 1 | 1000 | 30% | 700 | 2000 | 40% | 1200 | 
| B: lvl 1 | 2000 | 40% | 1200 | -500 | 30% | -350 | 
| LVL 1 TOTALS | 1900 | 850 | ||||
| C: lvl 2 | 5000 | 50% | 2500 | 3000 | 30% | 2100 | 
| D: lvl 2 | -1000 | 30% | -700 | 1000 | 50% | 500 | 
| LVL 2 TOTALS | 1800 | 2600 | 

How will the Parent Affiliate be rewarded?

| Lvl | % | Subaffiliate Casino NGR | Reward: Subaffiliate Casino NGR % | Subaffiliate Sportsbook NGR | Reward: Subaffiliate Sportsbook NGR % | 
| 1 | 10% | 1900 | 190 | 850 | 0 (condition on min sb ngr of 1000 EUR for lvl 1 wasn't met) | 
| 2 | 5% | 1800 | 90 | 2600 | 130 | 
| PARENT TOTALS | 280 | 130 | 


| 
 | |
|    | Applies to Casino NGR generated by the referred casino players. Min Casino NGR is set. | 
|  | Applies to Sportsbook NGR generated by referred sportsbook players. Min Sportsbook NGR is set. | 
|  | Applies to Poker NGR generated by referred poker players. Min Poker NGR is set. | 
|    | Applies to the number of deposits made by affiliate’s players. Min deposit count is set. | 
|  | Applies to the number of affiliate’s players who made deposits. Min depositing players count is set. | 
|  | Applies to the sum of the total deposits in money equivalent made by affiliate’s players. Min deposits sum is set. | 
|   | Represents the difference between total deposits sum and total cashouts sum in money equivalent. It's calculated according to the following formula: deposits sum – cashouts sum. Min effective deposits sum is set. | 
|    | Applies to the number of first depositors referred by an affiliate. Min first deposits count is set. | 
|  | Applies to the casino wager amount in money equivalent completed by affiliate’s players in a casino. Casino Wager is the sum of bets in money equivalent multiplied by Bet Playthrough Percentages of each game. E.g. if bet playthrough percent of a specific roulette is 50% and a player made 100 EUR bets in this roulette, the total wager amount is 50 EUR.Min wager amount is set. | 
| 
 | |
|   | Applies to the earnings of subaffiliates in money equivalent. Min subaffiliate earnings amount is set. | 
|  | Applies to cumulative Casino NGR generated by sub-affiliates' players. By the time the cumulative Sub-affiliate Casino NGR is calculated, the various Admin fees are already pre-deducted based on the percentages indicated in player commissions. | 
|  | Applies to cumulative Sportsbook NGR generated by sub-affiliates' players. By the time the cumulative Sub-affiliate Sportsbook NGR is calculated, the various Admin fees are already pre-deducted based on the percentages indicated in player commissions. | 
|  | Applies to cumulative Poker NGR generated by sub-affiliates' players. By the time the cumulative Sub-affiliate Poker NGR is calculated, the various Admin fees are already pre-deducted based on the percentages indicated in player commissions. | 



| 
 | |
|   | Qualifies each player by the number of deposits the player made. Min deposits count per player is set. | 
|   | Qualifies each player by the sum of deposits in money equivalent that the player made. Min deposits sum per player is set. | 
|  | Qualifies each casino player by the amount of completed casino wager (wager=bets*bonus playthrough percent) in money equivalent. Min casino wager per player is set. | 
|  | Qualifies each player by the total sum of casino bets made casino_total_bets_sum = bets sum cents - casino_bets_rollbacks_sum_cents in money equivalent. Min casino bets sum per player is set. | 
|  | Qualifies each player by their first deposit amount in money equivalent. Min first deposit amount is set. | 
|  | Qualifies each player by the total sum of effective deposits made (effective deposits = deposits – cashouts) in money equivalent. Min effective deposits sum per player is set. | 
|  | Qualifies each sportsbook player by the sum of sportsbook bets in money equivalent. Min sportsbook bets sum per player is set. | 
|  | Qualifies each casino player by the count of casino bets. Min casino bets count per player is set. | 
|  | Qualifies each poker room player by the sum of poker bets in money equivalent. Min poker bets sum per player is set. | 
|  | Qualifies each poker room player by the fee of poker rake that a player needs to pay to an online poker room. Min poker rake sum is set. | 
|  | Qualifies each registered player referred by affiliate. | 

List of All Rewards


|  | Flat fixed one-time fee. The amount in money equivalent is set. | 
| 
 | |
|   | Fixed reward per player who passed the qualification criteria. The fixed reward amount for each player in money equivalent is set. Comes with an additional parameter - `max fixed reward`, where you can indicate the maximum total reward to be paid out. | 
|   | Percentage of casino Net Gaming Revenue generated by the referred casino players. Casino NGR percent is set here. It's a classic revshare reward. Comes with an additional parameter - `Game Providers Fees. Subtract percent`, where you can indicate the percent of game providers fees to be subtracted from this reward. | 
|   | Cumulative casino NGR percentage for each referred casino player who passed the qualification criteria. Percent per player is set and the maximum percentage is indicated. | 
|  | Percentage of Sportsbook Net Gaming Revenue generated by referred sportsbook players. Sportsbook NGR percent is set here. | 
|  | Cumulative sportsbook NGR percent for each referred sportsbook player who passed the qualification criteria. Percent per each player is set and the maximum percent is indicated. | 
|   | Percentage of total deposits sum of referred players. Percent is set. You can use this reward if you pay your affiliates their share of profits not as a percent from NGR but based on the amount of real money the players have deposited. | 
|  | Cumulative percentage of deposits sum of each player who passed the qualification criteria. Percent per each player is set and the maximum percent is indicated | 
|  | Percentage of effective deposits sum (effective deposits sum = deposits sum – cashouts sum) of the referred players. Percent is set. You can use this reward if you pay your affiliates their share of profits not as a percent from NGR but based on the amount of real money the players have actually spent in your iGaming brand. | 
|   | Cumulative percentage of effective deposits sum of each player who passed the qualification criteria. Percent per each player is set and the maximum percent is indicated. | 
| 
 | Percentage of total casino wager amount completed by referred casino players. Percent is set. You can use this reward if you pay your affiliates their share of profits not as a percent from casino NGR but based on the amount of money they wagered in a casino. | 
|  | Cumulative percentage of casino wager amount of each casino player who passed the qualification criteria. Percent per each player is set and the maximum percent is indicated. | 
|  | Percentage of total sportsbook bets sum made by referred sportsbook players. Percent is set. You can use this reward if you pay your affiliates their share of profits not as a percent from sportsbook NGR but based on their sports bets sum. | 
|  | Cumulative percentage of sportsbook bets sum of each player who passed the qualification criteria. Percent per each player is set and the maximum percent is indicated. | 
|  | Percentage of NGR generated by the referred players within a poker room used in classic revshare deals. Poker NGR percent is set here. Comes with an additional parameter - Payment Systems Fees. Subtract percent - where you can indicate the percent of payment systems fees to be subtracted from this reward. | 
|  | Percentage of poker rake sum paid by the referred players within a poker room used in classic revshare deals, and is an alternative to Poker NGR percent. Comes with an additional parameter - Payment Systems Fees. Subtract percent - where you can indicate the percent of payment systems fees to be subtracted from this reward. | 
| 
 | |
|   | Percentage of all subaffiliate earnings regardless of the commission plan the sub-affiliate is working with. | 
|  | Percentage of cumulative Casino NGR generated by sub-affiliates' players. By the time the cumulative Sub-affiliate Casino NGR is calculated, the various Admin fees are already pre-deducted based on the percentages indicated in player commissions. | 
|  | Percentage of cumulative Sportsbook NGR generated by sub-affiliates' players. By the time the cumulative Sub-affiliate Sportsbook NGR is calculated, the various Admin fees are already pre-deducted based on the percentages indicated in player commissions. | 
|  | Percentage of cumulative Poker NGR generated by sub-affiliates' players. By the time the cumulative Sub-affiliate Poker NGR is calculated, the various Admin fees are already pre-deducted based on the percentages indicated in player commissions. | 

List of All Modifiers


| Modifier | Modifier Description | Additional Parameters | Parameter Description | 
|  | Limits the scope of a specific condition, qualifier or reward by indicating the timeframe for which calculation of player activity should be carried out. | From last bill | Relies only on the schedule plan set up in the commission and works during the billing period, regardless of whether the bill was issued or not. | 
| From last issued bill | Limits calculation time span to a period from the last really issued bill. | ||
| Day, week, month | Limits calculation time span to a period of 1 day/ week (7 days)/ month (30 days) ago. | ||
| Days count | Limits the calculation time span to a period of the specified days count ago. | ||
|  | Limits the period during which the registration needs to occur in order for a player to be qualified. | From last bill | Allows to limit the period of registration, and relies on the schedule plan set in the commission, regardless of whether the bill was issued or not. | 
| From last issued bill | Allows to limit the period of registration from the last really issued bill. | ||
| Day, week, month | Allows to limit the period of registration of 1 day/ week (7 days)/ month (30 days) ago. | ||
| Days count | Allows to limit the period of registration to a period of the indicated days count ago. | ||
|  | Excludes duplicated player accounts from the calculation of the reward, condition or qualifier | ||
|  | Excludes disabled (blocked) player accounts from calculation of the reward, condition or qualifier | ||
|  | Excludes players with active self-exclusion limits from calculation of the reward, condition or qualifier. | ||
|  | Excludes players whose accounts haven’t been verified in the iGaming brand from commission calculation of the reward, condition or qualifier. | ||
|  | Excludes players who are marked as “Cross-brand duplicates” from commission calculation. Useful for multi-brand affiliate programs where operators do not want to pay commissions for the same player more than once if that player registers and plays across different brands within the same Affiliate Program. More info on cross-brand duplicates can be found here. | ||
|  | Limits the scope of calculation to a specific timeframe since the moment of player registration. | Day, week, month | Limits the period of 1 day, week (7 days), 1 month (30 days) since registration. | 
| Days count | Limits the period of required days count from registration. | ||
|  | Limits the scope of calculation to depositing players only. Min deposits count and the period when they were made are set in this modifier. | Min deposits count | Limits depositing players by the required deposits count. | 
| From last bill | Limits the deposit period based on the commission schedule, regardless of whether an invoice was issued or not. | ||
| From last issued bill | Limits the deposit period from the last really issued bill. | ||
| Day, week, month | Limits the deposit period of 1 day, week (7 days), 1 month (30 days) ago | ||
| Days count | Limits the deposit period to indicated days count ago. | ||
|  | Limits the reward/condition only to those players who already passed the qualification criteria. | ||
|  | Limits the reward/condition only to those players who haven’t passed the qualification criteria yet. | ||
|  | Applicable to affiliate programs that host several brands. Limits the reward/condition/qualifier only to those players who haven’t yet been qualified on any of the brands. E.g. a player made a deposit on casino 1 and then deposited on casino 2, credit will go to casino 1. The reward will be paid once. | ||
|  | Limits the reward/condition/qualifier only to players from specific countries or excludes players from specific countries. | ||
| 
 | |||
|  | Indicates subaffiliate level. | Level | Indicates the level of subaffiliate to the parent affiliate. | 
|  | Limits the scope of a specific condition or reward by indicating the timeframe for which calculation should be carried out. | From last bill | Relies only on the schedule plan set up in the commission and works during the billing period, regardless of whether the bill was issued or not. | 
| 
 
 | Limits the sub-affiliate reward/condition only to specific brands or excludes certain brands from calculation. 
 | only | Only the indicated brands will count towards reward calculation. | 
| except | All brands except those indicated will count towards reward calculation. | ||