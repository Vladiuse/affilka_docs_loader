We have added a new **Subaffiliate Report** to provide operators with a more detailed view of subaffiliate activity, their parent–subaffiliate relationships, and associated performance metrics.**The "Subaffiliate Report" page** is available under `/casino/subaffiliate_report`or can be found under *Reports *tab *→ Subaffiliate report.***You will be able to filter this report using different filters like:** Date Range, Parent Affiliate IDs, Subaffiliate IDs, Subaffiliate Level, Subaffiliate campaigns/promos/promo codes/strategies, Brands, Exchange rates date, etc.

Filtering logic for some filters that we want to cover:

- **Date range**- this filter limits the activities period displayed for the subaffiliates.
- **Parent Affiliate ID**– partner id should be used. The system shows if the specified partner has any subaffiliates across all levels.
- **Subaffiliate Level**– 1, 2, 3, 4, etc. numbers needs to be used. The system will reflect all parent-subaffiliate connections with the specified subaffiliate level.
- **Subaffiliate ID**– partner id should be used. The system shows if the specified partner is someone’s subaffiliate.

**You will have access to such metrics like:** Player Registrations, FTDs count, FTDs sum, Deposits count, Deposits sum, Subaffiliate Casino NGR, Subaffiliate Sportsbook NGR, Subaffiliate Poker NGR. “Subaffiliate Casino/Sportsbook/Poker NGR” metric are the analogous of “Casino/Sportsbook/Poker NGR” in the “Partner Statistics” report, meaning that Admin fee is already substracted.**You can group the data using groupers:** Period (Month, Week, Day, Year), Parent Affiliate ID, Subaffiliate ID, Subaffiliate Level, Brands, Strategy, Campaign, Promo.**Report export:**

This report can be conveniently exported in **XLSX**, **XML**, or **JSON** formats using the **“Export report” **button. For exports in **XLSX format**, the report will be sent to your email or can be downloaded at any time from the **Requested Reports** page (`/casino/requested_reports`).**Keep in mind** that Usual Operators will be able to see the connections and statistics only if they are a dedicated operator to the partner affiliate and to their subaffiliate at the same time.

We’ve introduced **Hierarchy-Based Roles Management system**, a new way to structure data visibility across operators. This feature allows operators (General Manager) to see only the data of partners managed by their assigned dedicated operators (Affiliate Managers), ensuring stricter access control and better alignment with organisational hierarchies.

Let's imagine the situation that you have next team structure in your team:

| General manager | Henry | |||
| Mid-manager | Olivia | Liam | ||
| Aff managers | Alex | Daisy | Yana | Daria | 
| John | Maggie | Mikita | Gleb | |

New feature allows to link:

- Aff managers Alex, Daisy, John, Maggie to Olivia.
 Meaning that Olivia will see data only related to partners to whom her aff managers are assigned and to whom Olivia is dedicated operator.
- Aff managers Yana, Daria, Mikita, Gleb to Liam. 
 Meaning that Liam will see data only related to partners to whom aff managers are assigned and to whom Liam is dedicated operator.
- Mid managers Olivia, Liam to general manager Henry.
 Meaning that Henry will see the data related to partners to whom all the managers below are assigned and to whom Henry is dedicated operator.

Keep in mind that the user is still limited by the roles structure and if Henry doesn't have access to "Bills read" role it means that he won't be able to see Bills even if the managers below the hierarchy have access to "Bills read" role.

 

To assign operator to another operator you need:

- Follow the detailed page of the casino (/casino/users/:id) user to whom you want to assign an operator;
- Find the "Assigned operators" field under the "Role" field;
- Click on "Assign" button and select the desired user.
- Click on "Assign" button once again to confirm your choice.

- **SuperOperators**cannot be assigned to usual operators.
- **Blocked users**are excluded from the dropdown.
- Promoting usual operator to superoperator automatically removes all their assignments and they are not restored if the user is returned to the role of a usual operator.
 F.e. if Olivia is promoted to superoperator then:- Alex, Daisy, John, Maggie are no longer assigned to Olivia.
- Olivia is no longer assigned Henry, meaning that Henry losts visibility for partners related to Olivia and her managers.
 
- Circular self-assignment is prevented.
 F.e. if Daisy is assigned to Olivia, Olivia can't be assigned to Daisy.
 

The "Operator Assign Read" and "Operator Assign Process" roles allow to manage which operators can view and assign users to operators. This is how it works:

- **If the "Operator Assign Read" and "Operator Assign Process" roles are disabled:**
 On the user's detailed page (/casino/users/:id), the "Assigned operators" field will not be displayed; the operator will not be able to assign users to another user.
- **If the "Operator Assign Read" role is enabled and "Operator Assign Process" is disabled:**
 On the user's detailed page (/casino/users/:id), the "Assigned operators" field will be displayed; the operator will not be able to assign operators to /casino/users/id.
- **If the "Operator Assign Read" and "Operator Assign Process" roles are enabled:**
 On the user's detailed page (/casino/users/:id), the "Assigned operators" field will be displayed; the operator will be able to assign operators to /casino/users/id.

The same approach applies to SuperOperator role.

Starting from the release, the "Operator Assign Read" role will be activated automatically for all Operators, SuperOperators will have full access to this feature. To (de-)activate this role for the operators, please, use the "Roles" page (/casino/roles).

You can also limit which SuperOperators can have access to this role by using the SuperOperator exclusions "Operator Assign Read" and "Operator Assign Process" roles. Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

 

We’ve added the ability to filter and group the **Traffic Report** by dynamic tags, providing operators and affiliates more in-deep analysis for traffic glow and ability to discover new insights.

| Filters | Grouper | 
|---|---|
| **Location:**Operator interface: `/casino/traffic_report`Partner interface: `/partner/traffic_report`
Operator interface: **Filters added**(placed under Traffic Sources):**Dynamic tag keys**– multiple input with autosuggest (operators only).Filters by exact match, case sensitive.Autosuggest includes both active and archived tags from `/casino/settings/tags`.
**Dynamic tag values**– multiple input.Filters by partial match, case insensitive.
Filters are also available in report visibility settings: `/casino/settings/partner_report`→ "Traffic report" tab`/casino/partners/:id/settings/partner_report`→ "Traffic report" tabBoth filters **are enabled by default**for all partners upon release.
 | **Location**:Operator interface: `/casino/traffic_report`Partner interface: `/partner/traffic_report`
Operator interface: **Groupers added**(placed under "**Group by**" tab):Dynamic tag grouper will be added to the "Group by" tab automatically upon its creation on /casino/settings/tags page.The same flow as with the "Partner Statistics" report (
 `/casino/report`).
Dynamic tag grouper will be added to the "Group by" tab automatically upon its creation on /casino/settings/tags page.Groupers are also available in report visibility settings: `/casino/settings/partner_report`→ "Traffic report" tab`/casino/partners/:id/settings/partner_report`→ "Traffic report" tabGroupers **are not enabled by default**for partners.
 | 

**Data inputs:**

- Visits/Regs/Deposits with `clickid=123voirekok4`
- Visits/Regs/Deposits with `clickdID=2346ijjiggs657`
- Visits/Regs/Deposits with `clickid=123voirekok4`and`clickdID=2346ijjiggs657`
- Visits/Regs/Deposits with `sub_id=`

**Output:**

| If filter by | Result | 
|---|---|
| Dynamic tag value = `123`and`46` | Returns visits/regs/deposits from the 1st, 2nd, 3rd cases. | 
| Dynamic tag key = `clickid`and`sub_id` | Returns visits/regs/deposits from the 1st, 3rd, 4th cases. | 
| Dynamic tag value = `123`and`46`Dynamic tag key = `clickid` | Returns visits/regs/deposits from the 1st and 3rd cases. | 
| Dynamic tag value = `abc`Dynamic tag key = `clickid` | No results. | 
| Dynamic tag value = `123voirekok4`and`2346ijjiggs657`Dynamic tag key = `utm_campaign` | No results. | 
| Dynamic tag value = `voirekok`and`abc`Dynamic tag key = `clickid` | Returns visits/regs/deposits from the 1st and 3rd cases. | 
| Dynamic tag value = `voi`Dynamic tag key = `clickid`and`CLICKID` | Returns visits/regs/deposits from the 1st and 3rd cases. | 


**Deep Linking **is a new feature that allows affiliates to direct players to specific personalized destinations by appending custom URLs to their referral links. This feature will be especially useful to sports betting operators and their affiliates, allowing them to guide players directly to the relevant content – whether it's a specific sportsbook event, a prefilled betslip, or a custom registration form.

 

- **Sportsbook affiliates, influencers, tipsters**can attract players by sharing direct links to specific events with prefilled betslip details (event, odds, stake, etc).
- **Odds comparison websites**can generate dynamic betslips with multiple parameters, then redirect players to sportsbooks where their betslip is dynamically rendered.

Note! This feature is not enabled by default. Please, contact your Account Manager to activate this feature.

An affiliate must add the `dplnk=` parameter to their referral link, followed by the specific URL they want to direct players to.

When the `dplnk` parameter and its value are used, our redirect app will send players to the indicated URL, overriding our standard landing pages used in promos.

**Example:**

Referral link with indicated `dplnk` parameter: `https://reflink.com/abcde?dplnk=https://www.example.com/events/event-id-12345`

User will be redirected to: `https://www.example.com/events/event-id-12345?stag=1111_111111111`

Affilka does **not** generate or format deep links. To ensure that deep links are resolved correctly, they must be supported by sportsbooks (e.g. ability to parse event IDs, betslips, etc) and odds comparison sites. Affilka role here is to **transport** these deep link URLs through referral links while preserving affiliate tracking.

Unlike standard embedded landing pages that operators must constantly update, deep links let affiliates, streamers, and tipsters take control and create their own event-specific links. Benefits:

- Players land on timely, relevant, personalized content > improves conversions and engagement;
- Operators don't have to constantly update landing pages for thousands of changing events.

**What if other parameters are passed with ****dplnk**** parameter within one referral link?**

When a player is redirected to the URL specified in the `dplnk` parameter, our system prioritizes the order of parameters that will be passed to the destination URL. Parameters priority:

- **STAG**
- **deeplink-related parameters**
- **everything else in order of appearance**

If duplicated parameters are present, all values will be passed through.

Such prioritisation is especially important in cases when a browser’s 2048-character URL limit may be exceeded. Thus, we must ensure that the essential attribution parameter (STAG) is always included.

To let the system determine which parameters relate to deep-link domain you need to place `dplnk` parameter at the very end of the referral link and add parameters after it, using the '?' sign. 

**Example:**

- Referral link: `https://reflink.com/abcde?utm_campaign=123&clickid=12345&trsrc=adult&dplnk=https://www.example.com/events/event-id-12345?betcode=XYZ&clickid=67890`
- Parameters: `betcode=XYZ&clickid=67890`are deeplink-related since they are placed right after the deep-link domain.
- User will be redirected to considering the parameters priority: `https://www.example.com/events/event-id-12345?stag=1111_111111111&betcode=XYZ&clickid=67890&utm_campaign=123&clickid=12345&trsrc=adult`- `stag`- the 1st position
- `betcode=XYZ, clickid=67890`- the 2nd position
- `utm_campaign=123&clickid=12345&trsrc=adult`- the remaining ones
 

Additional rules:

- Invalid/missing/HTTP protocol will be replaced with HTTPS.
- If extra `stag`parameters are added, they will be stripped from the link.
- If multiple `dplnk`values are nested, only the first will be used, the rest will be ignored.
 

To ensure security and prevent abuse, we've implemented deep link domains whitelisting. Only approved domains can be used in deep link values, giving you full control over where your traffic is redirected.

Deep link whitelist feature is available via the /casino/deep_link_whitelist link or can be found under the *Affiliate Program → Deep Link *tab*.*

 

On `/casino/deep_link_whitelist` click on "Create" button and fill in the form: 

- *Name*– free text
- *Brand*– dropdown (only brands with Allow Deep Links = TRUE)
- *Deep Link URL*– manual input (placeholder:- `example.com`). Validations:
- Checkboxes:- Allow all subdomains (Setting allows any subdomain of the entered domain. `E.g.``subdomain.example.com`)
- Allow all paths (Setting allows any URL path after the domain. `E.g. /tournaments/vip`)
 
- Allow all subdomains (Setting allows any subdomain of the entered domain. 

Keep in mind that upon deep-link whitelist domain creation you won't be able to edit the domain. If you want to change used domain you need to archive the old one by clicking on "Archive" button in the corresponding row and create a new deep-link whitelist domain.

To prevent traffic loss when using the `dplnk` parameter, we’ve added a fallback mechanism. If a deep link cannot be applied, the click will automatically redirect to the promo’s landing page in the following cases:

- Deep-links setting is not enabled on your brand
- Deep-link URL is not whitelisted
- Deep-link URL is brand’s balancer domain
- `dplnk`parameter is empty
 

The "Deep Links Read" and "Deep Links Process" roles allow to manage which operators can view and assign users to operators. This is how it works:

- **If the "Deep Links Read" and "Deep Links Process" roles are disabled:**
 Operator cannot view, create, edit, or archive whitelisted domains. "Deep Links" tab is not displayed.
- **If the "Deep Links Read" role is enabled and "Deep Links Process" is disabled:**
 Operator can only view whitelisted domains, create, edit, or archive action are not available. "Deep Links" tab is displayed.
- **If the "Deep Links Read" and "Deep Links Process" roles are enabled:**
 Operator can view, create, edit (name only), and archive domains via interface. Full access to the feature.

The same approach applies to SuperOperator role.

Starting from the release, these roles won't be enabled automatically for Operators but SuperOperators will have full access to this feature. To (de-)activate this role for the operators, please, use the "Roles" page (/casino/roles).

You can also limit which SuperOperators can have access to this role by using the SuperOperator exclusions "Deep Links Read" and "Deep Links Process". Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

 

Operators can now **reassign exact players directly in the operator interface,** providing operators more control and independency over their players management.

- **Location**: Player detail page (- `/casino/players/:id`).
- **Button**:- **Reassign**– placed on the upper left corner of the player's page.
- **Page**: Clicking the button opens- `/casino/players/:id/reassign`with form.
 In order to successfully reassign player you must indicate to which partner, campaign and promo the player should be reassigned.- **Partner ID**
- **Campaign ID**
- **Promo ID**
 

**Keep in mind** that upon player reassignment all historical player's activities will remain tied to the old partner, campaign, promo.

 

The "Player reassignment" role allows to manage which operators can reassign players to another partners, campaigns, promos. This is how it works:

- **If the "Player reassignment" role is disabled:**
 On the player's detailed page (/casino/users/:id), the "Reassign" button- **will not be displayed**.
- **If the "Player reassignment" role is enabled:**
 On the player's detailed page (/casino/users/:id), the "Reassign" button- **will be displayed**.

The same approach applies to SuperOperator role.

Starting from the release, the "Player reassignment" role won't be enabled automatically for Operators but SuperOperators will have full access to this feature. To (de-)activate this role for the operators, please, use the "Roles" page (/casino/roles).

You can also limit which SuperOperators can have access to this role by using the SuperOperator exclusion "Player reassignment". Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

- Performance optimisation: "Partner Statistics" report calculation via queues should be improved.
- Customer API: the "Bankroll transactions" pages, available via **/api/customer/v1/casino/bankroll_transactions.**Documentation can be found under the API tab → Customer Operator → "Bankroll Transactions" section → "Bankroll transactions list".
- New "Player dynamic tags contain/exclude" filters are added to the "Cohort Analysis" report (`/casino/cohort_report`).
- New "casino_bets_sum" qualifier is added to the "Commission Constructor" (`/casino/commissions/new`). Qualifier analyses the total sum of casino bets done by player.
- Invite affiliates feature:- Referred partners and link id are added on the "Invite affiliates" page (`/casino/referral_links`).
- "Invited by link" and "Invite Link IDs" filters are added on the "List of partners" page (`/casino/partners`).
 
- Referred partners and link id are added on the "Invite affiliates" page (
- UX improvement: automated value separation is disabled for "Strategies" filters on the "Bills" and "Commissions" pages.
- BUG FIX: Cells are no longer shifted during medium edition on the "Media" page.
- BUG FIX: "Show" button for the report favorites is now fixed and requests the desired report.
- BUG FIX: dropdown is fixed during commission assignment to the operator.
- BUG FIX: Browser tab title is changed accordingly to the user's interface locale.