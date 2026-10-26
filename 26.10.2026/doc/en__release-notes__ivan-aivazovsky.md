You can find a filter by Landing ID on the "Partner statistics" (/casino/report) page. The filter helps you filter players' activities by specific landing, using its id. This filter will make the traffic analysis process more convenient and will help you gain insight on conversions for particular landings.

**Keep in mind** that the system will attribute visits, players and their activities to the landing to which the player was redirect initially: e.g. if the player was redirected to the landing "example.com/bonus" (landing id: 46) by clicking on the referral link, then the system will attribute their visit, registration and all future activities to this landing id.

We don't track landing URLs history change. So if you edit the URL of landing id: 46 from "example.com/bonus" to "test.com/freespins", the data in the report on all historical visits, registrations and activities will be grouped under "test.com/freespins" URL, but the landing id: 46 will remain the same.

The new "brand_ids" modifier for subaffiliate commissions allows you to choose which brands will count towards the parent affiliate commission calculation. This modifier can be applied for the "Conditions" and "Rewards" sections in the commission constructor.

The modifier has two modes: "Only" and "Except":

- "Only": **ONLY**the indicated brands will be included during billing calculation;
- "Except": all brands **EXCEPT**the indicated ones will be included during billing calculation.

E.g. subaffiliates have bills that were issued for "Test 1", "Test 2", "Test 3" brands:

- If the reward modifier is set as **"Only brands Test 1 and Test 2",**then the parent affiliate bill will be calculated**based on the "Test 1" and "Test 2" bills of their subaffiliates**.
- If the reward modifier is set as **"Except brands Test 1 and Test 2",**then the parent affiliate bill will be calculated**based on the "Test 3" bills of their subaffiliates**.

The same logic applies when specifying this modifier for condition, if they are present in the commission.

The "Commission assign" ability allows to manage which operators can assign commissions to affiliates. Here's how it works with various combinations:

- If **"Commissions read" + "Commissions assign" enabled, "Commissions process" disabled:**operators with such a role can view the commissions on the /casino/commissions page, view all the events related to the commissions on the /casino/events page and are able to assign and expire commissions for affiliates.**However**, they are unable to modify commissions (can't edit, publish, set tags, etc).
- **"Commissions read" enabled; "Commissions assign" and "Commissions process" disabled:**operators with such a role can view the commissions on the /casino/commissions page and view all the events related to the commissions on the /casino/events page.- **However,**they are unable to assign and expire commissions for affiliates and unable to modify commissions (can't edit, publish, set tags, etc).

Starting from the release, the "Commission assign" role will be activated automatically for all Operators that already have access to the "Commission process" role. For SuperOperators the exclusion won't be activated if they already have the "Commission read" exclusions. 

To (de-)activate these roles for the operators, please, use the "Roles" page (/casino/roles).

You can also limit which SuperOperators can have access to this role by using the SuperOperator exclusions "Commission assign". Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

We've improved our product and interface with the following minor adjustments:

- No longer possible to create partners, commissions, landings, media tags with "space" characters at the beginning and end of the name. To make the data consistent, we trimmed unnecessary spaces from the beginning and end of erroneously created tags.
- No longer possible to save global report settings (/casino/settings/partner_report) and individual partner report settings without selecting report columns. The "At least 1 column must be selected." error will occur.
- When creating a campaign, a partner will see only those brands that have active commissions assigned to this partner. If no commissions are available, the brand will not be shown.
- No longer possible to create promos in campaigns if campaign's commission is not active for a partner.
- New columns:
 "ID" on the "Brands" page (/casino/brands).
 "Created at" on the "Landings" (/casino/landings), "Media" (/casino/media) pages.
 "Subaffiliate" column on the "Campaigns" (casino/campaigns), "Promos" (/casino/promos), "My campaigns" (/partner/campaigns) pages.
- New filters:
 "Subaffiliate" on the "Landings" (/casino/landings), "Media" (/casino/media), "Campaigns" (casino/campaigns), "Promos" (/casino/promos), "My campaigns" (/partner/campaigns) pages.
 "Operator emails" on the "Operators" (/casino/users) page.
- The players that were imported on the wrong brand can be found on the players sync failed event under "not_imported" section with "brand_mismatch" error.

- New SB GGR formula. If you plan to open a new sportsbook brand you will be offered to choose one of the two formulas:- SB GGR = SB Bets - SB Cancelled Bets - SB Wins
- SB GGR = SB Settled bets - SB Wins
 
- Partner and Promo Traffic source data is added to csv export on the "List of partners" page (/casino/partners).
- Commission amount data for pending payments is added to csv export on the "Payments" page (casino/payments).
- The process of generating a partner statistics report in csv/xlsx has been accelerated due to data caching.
- New promo traffic sources are added.
- "USDT" and "PHP" currencies are added to "Player account" and "Other" payment systems respectively.
- "async" parameter is added to Customer API for Partner Statistics report (/api/customer/v1/casino/report):- **if async: true**-- **a report will be sent**- **to an email**in case of system's inability to calculate the report via API.
- **if async: false**-- **a report won't be be sent**- **to the email**in case of system's inability to calculate the report via API.
- If the "asyns" parameter is not sent the system behaves as with **async: false**parameter.
 
- The comments for cancelled payments are now displayed at the bottom on the detailed page of the payment in the Operator Interface.
- Validation period is now adjusted for deposits processed_at validation.
- BUG FIX: no more "is not included in the list" error for "from last bill"/"from last issued bill" periods with "period since registration" modifier.
- BUG FIX: team member lock status is now displayed on the detail page of partner user in the Affiliate Interface.
- BUG FIX: subaffiliate status value is now correctly displayed on the Promos page (/partner/promos) in the Affiliate Interface.
- BUG FIX: no longer possible to create landing without "Landing" ability.
- BUG FIX: commission autosuggest during commission assignment to a partner can be filtered by special characters.
- BUG FIX: "Bills" page (/partner/bills) no longer crashes in the Affiliate Interface if multiple values are applied in the "Brand" filter.
- BUG FIX: "Landings" (/casino/landings) page no longer crashes in some cases when using "Active"/"Archived" filters.