By providing great flexibility, the commission builder can sometimes feel complex and time-consuming, especially for new users. Additionally, certain terms and configuration steps may not always be intuitive. Commission templates help reduce setup time and make the process clearer by providing ready-made commission structures that can be quickly adjusted to your needs.

 

- Navigate to the commission creation page:`/casino/commissions/new`
- In the **Commission rules**section, locate the**Templates**dropdown on the left side.
- Select the appropriate commission type template (CPA, Revshare, Hybrid, etc.) for particular module:- Casino
- Sportsbook
- Casino + Sportsbook
 
- The commission rules will be generated automatically.
 You only need to adjust the required conditions, qualifiers, and payout values.

Our templates support the most commonly used commission models, including CPA, RevShare, Dynamic (Tiered) RevShare, Hybrid, and Subaffiliate Commission.

`{payout}` parameter for prequalified and qualified actionsAffiliates frequently use the `payout` parameter when sending postbacks to external trackers. In most cases, this parameter represents the CPA reward amount paid for a qualified player.

We’ve introduced a solution that automates this process by dynamically passing CPA reward data directly in postbacks.

When creating a postback for the **prequalification** or **qualification** actions, affiliates need to select the following parameters in the **Available parameters** section:

- **payout -**CPA reward amount paid per player according to the commission (in monetary units).- **Postback syntax:**- `payout=${payout}`
- **payout_cents -**CPA reward amount paid per player according to the commission (in cents).- **Postback syntax:**- `payout_cents=${payout_cents}`

F.e. if the player triggered prequalification postback; CPA reward is 200 EUR, according to the commission. The parameters in the sent postback will look like this:

...&`payout=200&payout_cents=20000`

We recommend using at least the following parameters: `payout` and `currency`. This ensures clear identification of both the CPA reward amount and its currency within the tracker.

 

Operators often need to analyze traffic performance using dynamic parameters (click_id, sub_id, utm_campaign, etc.) in reports. While this has been possible through dynamic tags added manually to referral links, partners may accidentally modify or remove these parameters, leading to inconsistent or inaccurate analytics.

With this update, operators can now define specific **key–value parameters** within a campaign. These parameters will be automatically send to the redirect URL specified in promo on our side whenever a user clicks them, ensuring consistent and reliable tracking.

 

- Navigate to the campaign detailed page:`/casino/campaigns/:id`
- Click on "Edit" button in the upper right corner.
- Specify the key and value parameters that should be automatically send to the redirect URL specified in promo.**Keep in mind!**Since the settings is applied on campaign level, those parameters will be applied for all promos under specified campaign.
- Click "Submit" button to apply settings.
 

- Duplicate keys across different rows are not allowed.
- Key and value fields cannot be empty.
- The following system-reserved parameters cannot be used:`stag`,`tr_src`,`affb_id`,`http_referrer`,`tracking_link`,`cmp`,`prm`,`dplnk`
- Only the following characters are allowed:- Letters (A–Z, a–z)
- Numbers (0–9)
- Underscore (`_`)
- Hyphen (`-`)
- Dot (`.`)
 
 

- If a user arrives with a parameter key that matches one defined at the campaign level, the parameter value will be **overwritten**with the value specified in the campaign settings.- Affiliate sends `utm_source=instagram`, in campaign level the`utm_source=meta`parameter is configured: the system will save`utm_source=meta`param on visit and, hense, on user.
 
- Affiliate sends 
- If the key or value configured in the campaign is modified, the updated parameters will be send to the redirect URL starting from the moment the changes are saved (no retrospective changes in saved parameters on visits or users).
- Other parameters (with keys not defined at the campaign level) remain unchanged and are also stored on the visit.
 

We've split the "Balance Correction" role into two separate ones: "Balance Corrections Read" and "Balance Corrections Process". Here's how it works:

- If **"Balance Corrections Read" and "Balance Corrections Process" roles ARE NOT enabled**, operators:- are not able to adjust partner's balance
- don't have access to the "Balance corrections" page (/casino/balance_corrections)
- don't see balance correction with `reference type: Balance correction`on "Transaction" tab on partner's detailed page (/casino/partners/:id/balance_transactions)
- don't see "Balance correction made" events on the "Events" page and not able to subscribe to the mentioned event
- are not able to do Customer API request to /api/customer/v1/casino/balance_correction endpoint
 
- If **"Balance Corrections Read" IS enabled**and**"Balance Corrections Process" IS NOT enabled**: operator can do all actions above**EXCEPT**adjusting partner's balance.
- If **"Balance Corrections Read" and "Balance Corrections Process" ARE enabled:**all information and actions mentioned above are available for operator.

The roles "Balance Corrections Read" & "Balance Corrections Process" will be activated automatically to all users which have previously had access to the "Balance Corrections" and "Partners" roles. If there is a need to (de-)activate these roles for the operators, please use the "Roles" page.

You can also limit which SuperOperators can have access to this page by using the SuperOperator exclusions "Balance Corrections Read" and "Balance Corrections Process". Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

 

In addition, operators that don't have access to “Bills Read” & "Payments Read roles, don't see balance corrections with `reference type: Bill` & `reference type: Payment: Cashout` respectively on "Transaction" tab on partner's detailed page (/casino/partners/:id/balance_transactions) either.

 

The **List of Partners** page may sometimes include partners who have never generated traffic, created campaigns, or brought any players. To help keep the list clean and manageable, we’ve introduced the ability to archive partners.

Archiving removes inactive partners from the main partners list while preserving their data in the system.

 

- Open the partner details page:`/casino/partners/:id`
- Click the red **Archive**button in the top-right corner.
- Confirm the action in the pop-up.

**Important:**

A partner can only be archived if they have **no visits and no players**.

Upon partner's archiving, they removed from the main **List of Partners** page (`/casino/partners`) and are not able to:

- Log in
- Reset their password
- Register again using the same email address

To unarchive a partner, repeat the same steps on the partner details page and click the **Unarchive** button.

Both archiving and unarchiving actions are also available via Batch actions feature.

To search for archived partners, use the **Archived** filter on the left and select option **Yes**.

 

We've improved our product and interface with the following adjustments:

- Affiliate Interface:- To avoid payment method deletion by misclicking "Delete" button, affiliates must confirm deletion action on the appeared pop-up window.
- New "Media" page available under Affiliate Program section → Media tab or via path `/partner/media`. This page displays the list of all available Media for affiliates.
- Affiliate will be able to check to which payment credentials the funds will be transferred by clicking on payment system name on the "Payments history" page (`/partner/payments`).
 
- If notification confirmation message is displaying longer that you expected too long, you can now simply hide by clicking on "X" icon.
- For better user experience on our system registration form (`/partner/register`), we've marked the required fields during registration.
- To improve readability, we've changed the way enabled role capabilities are displayed on the "Roles" page (`/casino/roles`).
- Affiliates and Operators can now simply download the uploaded media by clicking "Download" icon on the Media pages (`/partner/media + /casino/media`).

- User session cookie are renamed:- for Operator Interface: from "_session_id" to "_casino_session_id".
- for Affiliate Interface: from "_session_id" to "_partner_session_id".
 
- Performance optimisation: "Partner Statistics" report calculation in the interface should be improved while using "First deposit date range" filter.
- "USDT" currency is now supported by "bank transfer" payment system.
- BUG FIX: Players' count column is calculated correctly on Bonus code page (/casino/bonus_codes).
- BUG FIX: Second "Default currency for reports" field on partner user's detailed page is removed.
- BUG FIX: Bill correction window no longer disappears in some cases.
- BUG FIX: Affiliate can edit promo name when promo's traffic source is empty and operator requires that traffic source must be specified on the promo.
- BUG FIX: Hover is displayed while selection options in dropdown.
- BUG FIX: some other minor front-end issues.