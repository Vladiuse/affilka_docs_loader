What is a postback?

A postback (also known as s2s post back, server tracking post back, cookie-less tracking, s2s pixel, etc) is a type of conversion tracking protocol that happens on the side of the server. It allows the advertiser's server (e.g. an affiliate program) to send the required conversion data to an affiliate tracker whenever a certain event (conversion goal) occurs (e.g. registration, first deposit, etc).

An affiliate sets up a postback URL in the affiliate program interface. To set up a postback url the affiliate needs to indicate the url of the affiliate server which will receive the data from the affiliate program server and configure special variables that will be added to their url and will help track statistics and conversion goals properly (e.g. click id, visit id, amount, etc).

The following scheme explains how postbacks work in practice — from the user’s click to the final postback being sent to the affiliate.

Postback event types

We support the following event types on which postbacks are triggered:

 

An affiliate program server sends this postback when a user referred by an affiliate registered in an online casino.

This postback is sent when a user referred by an affiliate makes their first deposit.

**IMPORTANT!** If an affiliate has set up this postback, they will get the information on every first deposit of every user they referred to a casino regardless of the commission they work with. For example: an affiliate program pays CPA for every first depositing player who deposits 20 EUR with the exception of self-excluded players and players with duplicates. The affiliate will get paid only for those FTDs who do not have an active self-exclusion limit and/or do not have duplicated accounts. The affiliate will, nonetheless, get the stats on every first deposit because they've configured a postback on this conversion goal. *(If an affiliate only wants to get the statistics on those users who have passed the qualification criteria, they should configure a QUALIFICATION-type postback.)*

This postback is sent on every deposit of every user referred by an affiliate.

NGR stands for Net Gaming Revenue. Net Gaming Revenue is calculated according to the following formula: Total Bets – Total Wins – Bonuses – Balance corrections – Casino Taxes – Admin Fee (if any). NGR is not an event but a dynamic value so it cannot be triggered. Hence the postback with information on NGR is sent only **once per hour **(or at a rate when your iGaming brand is synced with our affiliate software - e.g. once in every 15 mins or once a day, etc).

Sportsbook NGR stands for net revenue from sports betting activities and is calculated according to the following formula: SB GGR - SB Bonuses - SB Balance corrections - SB 3rd party fees. This postback will be sent with Sportsbook NGR amount for each player (for period). Similar to Casino NGR postback it is not triggered but is sent **once per hour **(or at a rate when your iGaming brand is synced with our affiliate software - e.g. once in every 15 mins or once a day, etc).

Poker NGR stands for net revenue from poker activities and is calculated according to the following formula: Poker NGR = Poker rake - Poker bonuses - Poker balance corrections - Poker 3rd party fees - Poker Admin Fee. This postback will be sent with Poker NGR amount for each player (for period). Similar to Casino NGR postback it is not triggered but is sent once per hour (or at a rate when your iGaming brand is synced with our affiliate software - e.g. once in every 15 mins or once a day, etc).

This postback is sent when a player generates poker rake during a specific period. It includes the total amount of poker rake attributed to that player. This is commonly used for CPA deals where player qualification depends on reaching a defined rake threshold. If the player meets the threshold, they are considered qualified; otherwise, they are excluded from billing.

This postback is sent only when certain player qualification criteria are met and the system starts bills calculations according to commission schedule plans. For example, whenever a total deposits sum of a given user reaches 1000 EUR the affiliate will get this postback. **Please Note!** Only those parameters, which are set as qualifiers in the commission, are sent with the qualification postback (when configured in the postback as well). For example, if in the commission only qualifier on first deposit is set, and in the postback are included wager and effective deposits sum as parameters additionally, we will send only first deposit sum with the postback.

Sent as soon as a player meets qualification criteria before bill calculation. E.g. a player made a deposit and completed wager requirement set in the commission and has no self-exclusions, duplicates, and their account is active. The event equals to "qualification" event provided that "disqualification" postback for this player id is not sent within the billing period.

Sent as soon as a "prequalified" player no longer satisfies the qualification criteria. E.g. "prequalified" player set a self-exclusion limit before bill calculation.

 

The table below shows the sending frequency of postbacks for all supported event types.

 

| `any_deposit` | Depends on the sync frequency with the iGaming brand’s platform; triggered only after Affilka receives deposit data. | 
| `first_deposit` | Depends on the sync frequency with the iGaming brand’s platform; triggered only after Affilka receives first deposit data | 
| `poker_rake` | Depends on the sync frequency with the iGaming brand’s platform; triggered only after Affilka receives poker rake data. This parameter is only sent if the commission settings include a qualification based on a poker rake sum. | 
| `registration` | Depends on the sync frequency with the iGaming brand’s platform; triggered only after Affilka receives player's registration data. | 
| `casino_ngr` | Sent upon parameter update  (e.g. once per hour) | 
| `sb_ngr` | Sent upon parameter update  (e.g. once per hour) | 
| `poker_ngr` | Sent upon parameter update  (e.g. once per hour) | 
| `qualification` | Sent on the billing date, based on the Schedule Plan set in the commission settings. | 
| `prequalification` | Sent once all qualification criteria are met, before the billing date. | 
| `disqualification` | Sent before billing if a previously prequalified player no longer meets the qualification criteria. | 

Default postback parameters

Postback parameters and their description, available for every type of event, can be found in the postback configuration interface of affiliate profile.

| Parameters | Description | Postback action | 
|---|---|---|
| `campaign_id` | Unique identifier of a campaign on which the postback is triggered | Any depositFist DepositRegistrationCasino NGRSportsbook NGRPoker NGRQualificationPrequalificationDisqualification
 | 
| `promo_id` | Unique identifier of a promo on which the postback is triggered | Any depositFist DepositRegistrationCasino NGRSportsbook NGRPoker NGRQualificationPrequalificationDisqualification
 | 
| `visit_id` | Unique identifier of a user visit. Typically, the parameter is equivalent to the click_id parameter used in the affiliate’s tracking systems. | Any depositFist DepositRegistrationCasino NGRSportsbook NGRPoker NGRQualificationPrequalificationDisqualification
 | 
| `amount``amount_cents` | Amount in money Amount in cents | Any depositFist DepositCasino NGRSportsbook NGRPoker NGR
 | 
| `currency` | Currency ISO code | Any depositFist DepositCasino NGRSportsbook NGRPoker NGRQualificationPrequalificationDisqualification
 | 
| `player_id` | Unique identifier of a player in Affilka database | Any depositFist DepositRegistrationCasino NGRSportsbook NGRPoker NGRQualificationPrequalificationDisqualification
 | 
| `deposit_id` | Unique identifier of a user deposit. | Any depositFist Deposit
 | 
| `deposits_count` | Deposits count | QualificationPrequalificationDisqualification
 | 
| `deposits_sum``deposits_sum_cents` | Deposits sum in money Deposits sum in cents | QualificationPrequalificationDisqualification
 | 
| `effective_deposits_sum``effective_deposits_sum_cents` | Effective deposits sum in money Effective deposits sum in cents | QualificationPrequalificationDisqualification
 | 
| `is_ftd` | Indicates whether the deposit triggering the postback is a First Time Deposit (FTD). Sends `true`if the deposit is the player's first-ever deposit, and`false`for any subsequent deposits. | Any deposit | 
| `wager``wager_cents` | Casino Wager in money Casino Wager in cents | QualificationPrequalificationDisqualification
 | 
| `sb_bets_sum``sb_bets_sum_cents` | Sportsbook Bets Sum in Money Sportsbook Bets Sum in Cents | QualificationPrequalificationDisqualification
 | 
| `poker_rake_sum``poker_rake_sum_cents` | Poker Rake Sum in Money Poker Rake Sum in cents | QualificationPrequalificationDisqualification
 | 
| `first_deposit``first_deposit_cents` | First deposit in money First deposit in cents | QualificationPrequalificationDisqualification
 | 
| `payout``payout_cents` | CPA reward in money CPA reward in cents CPA reward currency | QualificationPrequalification
 | 
| `from``to` | From/ To time (UTC) | Casino NGRSportsbook NGRPoker NGR
 | 

Postbacks Configuration

In our affiliate system postbacks can be set up globally for entire affiliate account, individually for each campaign, or for each promo inside the campaign which will be tracked.

- Open “My postbacks” and press "New".
- Select the Scope: global, campaign or promo postback
- Select the postback action which you want to track - for example, first_deposit
- In the Postback URL field indicate the URL of the website where affiliate tracker is located. This website will receive the info from the affiliate program server whenever a first deposit occurs. Let us imagine, that your affiliate tracker is located at **https://affiliate_postback_url.com**
- To add the variables that you want to receive with this postback, simply click on them and they'll be added to your postback url. 
 Example:**https://affiliate_postback_url.com?visit_id=${visit_id}&amount=${amount}¤cy=${currency}**

This is a format for encoding keys and their corresponding values. All key-value pairs are separated by an '&' character, and each key is separated from its value by an '=' character.

Let us imagine a situation where an affiliate wants to send additional parameters to the affiliate program from their tracker (for example, Campaign ID and Source name) and then receive postbacks with these parameters. Such parameters are not offered by default by our affiliate system so they need to be filled in by an affiliate manually during the postback url configuration.

- To add a custom parameter you need to add a key-value pair to the url according to the following syntax: **param_name=${param_name}****param_name****${param_name}**
- Let's consider the above url example and additional custom parameters webID and clickID. The postback URL with such parameters may look as follows:

**https://affiliate_postback_url.com?visit_id=${visit_id}&amount=${amount}¤cy=${currency}&b=${webID}&c=${clickID}**

We will store these parameters in our system for the configured postback and will return them to your tracker with a postback once the event is triggered. Of course these parameters have to be familiar to and readable by your tracker.


If an affiliate wants to send additional parameters to the affiliate program from their tracker and then receive postbacks with these parameters, these parameters need to be added to the tracking link as well.

- After creating a promo for a specific campaign, an affiliate receives a tracking link. Custom parameters need to be added to this link.
- Let's imagine that the unique affiliate tracking link looks like **https://example.com/e4567do**
- And the custom parameters to be passed, stored and then returned with a postback are **{webID}****{clickID}.**

The tracking link should look like:

**https://example.com/e4567do?webID={aff_variable_for_webID}&clickID={aff_variable_for_clickID}**

The values of **aff_variable_for_webID****aff_variable_for_clickID**

Use Dynamic Tags to group players and break down performance across reports. Follow the steps below to enable reporting by tag:

- Go to Dynamic Tags **/casino/settings/tags**and create a new tag.
- Migrate to historical players *(optional but recommended).*
 After the tag is created, click Migrate. This applies the tag retroactively to all players who have a tag — including players that Affilka received before the tag was created.
- Analyze in Reports by grouping.

How it all communicates with affiliate's tracker

After Postback URL is configured and the referral link is built with all dynamic variables, the affiliate should place this referral link in the Offer section of the Tracker. At the Offer Page the affiliate can enrich the referral link with other dynamic variables, still remembering to feature them all in the postback as well. The ultimate referral link, to test the conversion before affiliate advertises the link in the internet, is normally placed in Campaigns section of the Tracker and might have a different view in comparison with the  referral link from Affilka.

 


| Postback url from affiliate's tracker:  | 
| Referral link with dynamic values:  You insert this final view in the tracker`reqid`is the dynamic variable from the tracker
 | 
| Postback fired from Affilka: where `reqid`will be a different value every time the conversion takes place. | 


| Postback url from affiliate's tracker:  | 
| Referral link with dynamic values   You insert this final view in the tracker`clickid`is the dynamic variable from the tracker
 | 
| Postback fired from Affilka: where `clickid`will be a different value every time the conversion takes place | 


If the dynamic variable is not included in the final referral link, we won't fire it with the postback. **We fire all hardcode params + dynamic variables featured both in referral links and postback. **Whether the dynamic value should be in **##, [] or {}** brackets depends on the tracker software configuration.

 

When the affiliate postback URL is triggered, the system returns an HTTP response code. These codes indicate whether the request was successfully processed or if an error occurred.

For a complete list of HTTP response status codes, please refer to the official documentation: **https://developer.mozilla.org/en-US/docs/Web/HTTP/Status**

 

| HTTP Code | Meaning | Description | 
| 200 | Success | The postback is successfully sent. | 
| 400 | Invalid request | The postback is missing required parameters or contains invalid data. | 
| 401 | Authentication failed | The postback was rejected due to missing or incorrect credentials (if required). | 
| 403 | Access denied | The request was understood but refused. | 
| 404 | URL not found | The postback URL is incorrect or does not exist on the affiliate’s side. | 
| 500 | Server error | An error occurred on the affiliate tracking system's side while processing the postback. | 
| 502 | Temporary issues | The affiliate tracking system is down or temporarily unavailable. | 

Postbacks: check postback logs

Go to **/casino/postback_logs **page.

Here you can find the required postback by:

- **Postback**- **actions**– the filter finds postbacks for any of the indicated events;
- **Response code**– the affiliate tracker response;
- **Postback URL**– the affiliate tracker URL to which the postback is sent;
- **Player**- **IDs**– will find postbacks triggered for any of the indicated player IDs;
- **Promo IDs and Promo codes**– will find postbacks triggered for any of the indicated promos;
- **Campaign IDs**– will find postbacks triggered for any of the indicated campaign IDs;
- **Campaign**- **name**– will find postbacks triggered for the indicated campaign name;
- **Partner name**,- **email**and- **ID**(finds postbacks triggered for any of the indicated partners),
- **Time it was sent**(from…to date range).
 

There can be several reasons for that.

 

In our system, players are synced with the affiliate program once an hour. Players synchronization for the previous hour starts at 11 minutes of every new hour.

So if an affiliate performed a test registration/deposit (or any other action for which the postback was configured) - they will not receive their postback immediately, they will need to wait till synchronization start.

As for qualification postback, this postback is only sent when a player is qualified. Player qualification happens according to commission schedule plans (in other words, when the system starts bills calculations).

 

If an affiliate used wrong syntax to configure a postback, it will not be sent. Compare the following examples:

 

| Wrong Syntax | Correct Syntax | 
|---|---|
|  |  | 
|  |  | 
|  |  | 


An affiliate would like to send their custom parameters with the referral link, e.g. {transactionid}. They add this parameter to the referral link but the actual value which is received, stored and sent by our system may be corrupted.

 

| 
 | 
 | 
| 
 | 
 | 


E.g. an affiliate would like to send their custom dynamic parameters to our system. Using these parameters they can analyze their traffic better. This is usually true about different affiliate networks who need to analyze how different publishers across their network are performing. Thus they send us their custom parameters within the tracking links and would like to receive post backs with these parameters so that they can break down stats per different publisher id.

Let's imagine that the parameter they'd like to send, store and receive is** {publisherID}**

**The correct ways to set up a tracking link and a postback using these dynamic parameters are:**

 

| Postbackin all these examples we store a parameter publisherID. It does not matter how you name the KEY (b, publisherID, id or whatever), we will only store the value which is indicated in the curly brackets. | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 

**Compare:**

 

| An affiliate refers a player via  | An affiliate refers a player via link. | 
| The player registers. | The player registers. | 
| The postback for player registration looks like  | The postback for player registration looks like  | 
| We send the postback to the affiliate.  | We do not know what  So we send the postback to the affiliate. | 
| The affiliate can then break down their traffic per different  | The affiliate can not break down their traffic per different btag , because we do not store this value and do not send it with postback. |