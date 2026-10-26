You can now unassign a sub-affiliate from its parent affiliate directly on the affiliate's detail page (`/casino/partners/:id`).

**Value:** Subaffiliates sometimes end up linked to the wrong parent — either through operator error or an affiliate self-attaching incorrectly. Previously there was no clean way to fix this. Operators can now correct these relationships themselves, with action logs retained and commissions calculated correctly at every step.

**How it works**

- A new Unassign button appears next to the **Parent Affiliate**field whenever a parent is set. Clicking it opens a confirmation pop-up — "Affiliate unassignment" — naming both affiliates before the change is applied, so there's no risk of an accidental click quietly breaking a relationship.

**What happens to the chain**

- Unassigning only breaks the specific link you removed — everything else in the chain stays intact. For example, in A → B → C → D → E, unassigning D from C leaves A → B → C untouched and lets D → E continue on as its own branch. The link disappears from **Partner Connections**immediately, on both the operator and affiliate side, and every assign/unassign action is logged, so the full history can be reconstructed later even after several reassignments. The**Subaffiliate Report**itself still only ever shows the**current**relationships,**not historical**ones.

**Billing follows the relationship, not the activity**

- Subaffiliate-based rewards are calculated based on who the parent is *at the moment of billing*, not when the underlying activity happened. So if a sub-affiliate is unassigned mid-period — or reassigned to a different parent — the reward simply follows to whoever holds the link on the billing date.

**Roles and events**

- The existing **Subaffiliate assign**role has been renamed to**Subaffiliate (Un)Assign**and now also governs who can unassign (`/casino/roles/new`).
- A new Subaffiliate unassigned event has been added alongside Subaffiliate assigned, and can be subscribed to via Event Subscriptions.
 

Affilka can now attribute players who arrive through Google Ads campaigns back to the correct affiliate, without relying on matching redirect chains.

**Value:** Operators running Google Ads campaigns can now track and analyze this traffic in Affilka just like any other source, closing a gap where Google Ads clicks weren't reliably tied back to an affiliate stag causing inability to import player from Google Ads.

**What's new:**

- Google Ads' Parallel Tracking sends two simultaneous requests on click — one to the affiliate tracking link, one straight to the casino landing page — both carrying the same `gclid`value. Affilka now stores a mapping of`gclid → stag`when the tracking link is hit.
- A new API parameter, `parallel_tracking_id`, is available on`POST /api/v1/players`for importing a player by`gclid`. Affilka looks up the matching visit, creates the player, and returns`id`and`stag`for the casino platform to store on the player — the same pattern already used for bonus codes.
- Priority when multiple identifiers are present on import: `bonus_code`always wins if present; otherwise`stag`takes priority over`parallel_tracking_id`.
 

- **New "Bankroll Transactions" role**— access to the Bankroll card on the Dashboard and the- `/casino/bankroll_transactions`page can now be restricted via a dedicated ability/exclusion, keeping visibility into project funds limited to authorized users.
- **Comments on bill cancellation**— operators can now leave an optional comment when cancelling a bill, either individually or via batch actions, and mark it as visible to operators only or to operators and affiliates. Comments appear in a new- **Bill Comments**block on the bill's detail page (and on the affiliate-facing bill page, without the author field).
- **Traffic Report CSV export improvements**— export column headers have been renamed to plain, human-readable labels (e.g.- `foreign_partner_id`→ "Partner ID"), and additional columns are now included depending on which groupers are active — such as Brand Name, Company name, Partner tags, Campaign name, Promo code/name, Player Email, Original player ID, and Dedicated operator email.
- **"Reassign" button for active commissions**— a new Reassign button next to each active commission on a partner lets you reopen the assignment form pre-filled with that commission's brand and subaffiliate context, speeding up reassigning the same commission across multiple brands.
 

- In report tables with grouping (Partner Statistics, Traffic Report, Subaffiliate Report), entity IDs are no longer part of the clickable link text for Partner/Campaign/Promo. The name stays clickable; the ID now renders as plain text next to it.
- **Schedule payments filter (**- **/casino/partners**- **)**— filter affiliates by whether they have a scheduled payment configured for a given payment system (including a "None" option to find affiliates with no scheduled payments). Also available via the Customer API. Visibility is tied to the Payments Read ability.
- **BUG FIX:**Fixed the Commission ID filter on the Cohort Analysis report, which wasn't being applied. This caused FTD counts to mismatch against Partner Statistics whenever a player's activity spanned more than one commission.
- **BUG FIX:**Fixed the preview banner image failing to load on Casino News entries and Landing pages.
- **BUG FIX:**Fixed Dedicated Operator occasionally showing as "N/A" in Traffic Report groupings.
- **BUG FIX:**Fixed a broken, blank page when clicking a Parent Affiliate link the current operator doesn't have access to. That link now renders as plain text instead with a proper "Requested resource is not found" message.
- **BUG FIX:**Fixed several Brand Access issues for operators with restricted brand access:- The Balancer Domains filter on `/casino/partners`no longer surfaces domains from inaccessible brands.
- The "Latest issued bills" total on the dashboard no longer includes figures from brands the operator can't see.
- The partner-facing Commission Plans/Brands view no longer reveals a brand hidden from the impersonated operator.
 
- The Balancer Domains filter on 
- **BUG FIX:**Fixed Priority Landing not being shown first when creating a campaign, even when correctly flagged and set as the default shared landing.