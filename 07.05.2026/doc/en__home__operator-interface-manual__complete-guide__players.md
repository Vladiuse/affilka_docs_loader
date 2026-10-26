This tab contains all players invited to your iGaming brand by affiliates via referral links or bonus codes. You can view the full list on **/casino/players** page or extract a CSV export of the table.

**You can filter and find players by:**

- **Player IDs**(full match mode; supports multiple values): these are the player IDs with the affiliate system. You can type several Player IDs separated by a comma, “Space” or “Enter” key and find all players with the enumerated IDs.
- **Original Player IDs**(full match mode, supports multiple values separated by a comma, “Space” or “Enter” key.): this is the ID passed over by your iGaming brand to our Affiliate System; knowing player’s id in your casino/sportsbook you can easily find this player in the affiliate program.
- **Emails**(partial search, supports multiple values separated by a comma, “Space” or “Enter” key ): email address of a player. You can type players' emails partially and press “Filter”, and you will see all players whose emails contain what you’ve just typed.
- **First Name and Last Name**(partial match mode): first and last name of a player. You can start typing any letters and the filter will find all players whose names match the indicated letters.
- **Partner IDs**(full match mode, supports multiple values): the unique id (or stag) of a partner in the affiliate system. You can type several partners' IDs separated by a comma, “Space” or “Enter” key and find all players who registered under the specified affiliates' IDs.
- **Brands**(dropdown selector; multiple values): iGaming brand where a player registered an account. You can choose several brands and find all players who registered with any of these brands.
- **Campaign IDs**(full match mode; supports multiple values): numeric ID of partner campaign. A player can be attached to only 1 campaign. You can type several campaign IDs separated by a comma, “Space” or “Enter” key and find all players who registered following the links in any of the enumerated campaigns.
- **Promo IDs**(full match mode; supports multiple values): numeric ID of partner promo. A player can be attached to only 1 promo. You can type several promo IDs separated by a comma, “Space” or “Enter” key and find all players who registered following the links in any of the enumerated promos.
- **Promo codes**(full match mode; supports multiple values): the unique alphanumeric code you can find in affiliate referral links. A player can be attached to only 1 promo code. You can type several promo codes separated by a comma, “Space” or “Enter” key and find all players who registered following the referral links containing any of these codes.
- **Player dynamic tags contain and Player dynamic tags exclude**(the filter uses peculiar syntax; supports partial match mode and multiple values separated by a comma, “Space” or “Enter” key). You can either include or exclude certain dynamic tag names or their values (typed fully or partially) from filter results.

**Please, note:**

- 1 filter, e.g. "contain", finds all players for whom any of the specified tags/values are true, not necessarily all of them

- if you use both filters, contain and exclude, simultaneously, the filters will find players for whom both filters are true

**Filter example:**

*player dynamic tags contain: **clickID**, **utm=**, **=12345**, **webID=678*

*player dynamic tags exclude: **twitch**, **source=**, **=facebook**, **webID=789*

**Filter results:**

**the filter will include players who have:**

*a tag/tag value which contains **clickID** and/or a tag which contains **utm** and/or a tag value which contains **12345** and/or a tag which contains **webID** whose value contains **678*

**AND**

**the filter will exclude players who have:**

*a tag/tag value which contains **twitch** and/or a tag which contains **source** and/or a tag value which contains **facebook** and/or a tag which contains **webID** whose value contains **789*

- **Bonus codes**(full match mode; supports multiple values): the bonus code via which a bonus was issued to a player and via which a player was attached to an affiliate . A player can be attached to only 1 bonus code. You can type several bonus codes separated by a comma, “Space” or “Enter” key and find all players who registered with these bonus codes.
- **Stag visit**(full match mode): the unique id of a player visit. You can type several stags separated by a comma, “Space” or “Enter” key and find all players who came with these stag visits. If the visit was not unique, the filter will find several players associated with this stag visit. If you have doubts regarding specific affiliate traffic and you notice that the number of registrations during a selected timeframe is considerably higher than the number of visits, you can cherry pick some player(s) who registered during this period, copy their stag visit (available on a detailed player page) and see whether there are other players who have the same visit (click). Such players may be duplicates and may very well represent robotized traffic.
- **Countries**(dropdown selector with autosuggest feature; supports multiple values): country indicated in player profile within the iGaming brand. You can choose several countries and the filter will find all players coming from any of these countries.
- **Disabled:**True/False. Use it to filter and find players who are either disabled in your iGaming brand or have active accounts.
- **Duplicate:**True/False. Use it to filter and find players who are duplicates of other players. Duplicates can be established in many ways (cookies, same payment details, etc). We record and store what your iGaming brand sends to use via an API as duplicates.
- **Qualified:**True/False. Use it to filter and find players who have passed the qualification criteria set in your commission plans.
- **Access Limit**: True/False. Use it to filter and find players who are self-excluded from your iGaming brand in accordance with responsible gambling limits.
- **Verified:**True/False. Use it to filter and find players who are verified in accordance with the requirements of your iGaming brand.
- **Cross-brand duplicate:**True/False. Use it to filter and find players that registered on another brand within the same affiliate program with the same email or email alias of another player that already exists in the Affilka database. You can read more on cross-brand duplicates in our Glossary.
- **Signed Up At Date:**player registration date. Indicate the date range when player registration occurred, and the filter will find all players registered within this period. You can indicate either both dates or just one (after/up to which players registered).
- **Created At Date :**date of the first record of the player within the affiliate system. It may be different from the registration date if data is sent to the affiliate system once a day or if there was a migration of player database from some affiliate system to ours and this player had registered long before the migration.
- **FTD date:**first deposit date. Indicate the date range, and the filter will find all players who made their first deposit within this period. You can indicate either both dates or just one (after/up to which players made their first deposit).
- **FTD currency and amount:**currency and the amount range of the first deposit. Find players who made their first deposit for a specific amount of money.
- **Total Deposits Count**: the total number of deposits (including FTDs). Find players who made a specific number of deposits within your brands.
- **Deposits Currency and Total Deposits Sum:**currency and the range of total deposits sum. Find players whose total deposits sum within your brands corresponds to an indicated range.
- **Qualified at Date:**date when a player qualifued against the qualification criteria set in a commission plan.
- **Visited at Date:**date when a player visit to the iGaming brand occurred. Indicates their first visit and does not contain data on subsequent logins into the iGaming brand.

With this sorting, you can select your mostly used filters on the Players and thereby optimize the space of the page you are viewing.

**In order to set this, please do the following:**

- Point a cursor on one of the filters and you'll see the UNPIN icon next to the filter name.
- Click on the UNPIN icon.
- After that filter will be sorted down to the “Show more” section.
- To pin the filter back you will need to open the “Show more” section and click on the PIN icon next to the filter.

**NOTE!** Settings are applied for each user account individually. 




   **   **









To view a specific player page, press on the player “ID” within the Players list (link **/casino/players/:player_id**)

This page contains 2 tabs: Overview and Changes history.

Here you will find information about player ID in Affilka and the Original Player ID in the iGaming brand, player email, full name, address, etc.

You will also see such player statuses as Duplicate (True/False), Disabled (True/False), Verified(True/False),with Access Limit (True/False). If the attribute is marked as true, you will also see a timestamp of when the player received this attribute.

The information on whether the Player is a cross-brand duplicate is also displayed here. If the player is a cross-brand duplicate of another player, you will see when they were marked as a cross-brand duplicate and who the original player is.

**The “Report” button** on the right will lead you to a default activities report for the current month filtered by this player.

**The “Reassign” button** allows you to reassign a player to a different Partner, Campaign, and Promo. Clicking this button will lead to a player reassignment page. 

To reassign a player fill in the information:

- Partner ID
- Campaign ID
- Promo ID

Click **Submit** to proceed.**IMPORTANT!** Once the reassignment is completed, the system creates a new player with a new Player ID while copying the existing player data like: Original Player ID, email, first and last name, country, and other relevant details. All historical activities remain linked to the previous partner, campaign, and promo. Any new activity is attributed to the newly created player, henсe to the newly assigned partner, campaign, and promo.

Errors you may face:

- Promo_not_changed - cannot reassign a player to the same promo
- Player_already_reassigned - this player has already been reassigned with id=%{id}
- Promo_and_campaign_unavailable - this brand has no partner with such a promo and campaign
- Please reach out to your Account Manager to get access to Player Reassignment action

You can track various changes to player accounts on a detailed player page in the "Changes History" tab.

Here we display such changes as updates in personal details (e.g. name, nickname, country, etc), reattribution of players to other promos/campaigns, time stamps of when the player was marked/unmarked as duplicate/self-excluded/disabled/verified,/cross-brand duplicate, etc. The old data in the change log is stricken-through, the new data after the change is placed right next to it. You can see the actor of the change as well as the date and time the change occurred.