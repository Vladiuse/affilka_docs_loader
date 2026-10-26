We're excited to introduce the **Cohort Report for Affiliates** — now available under **Reports → Cohort Analysis**, or at `/partner/cohort_report`. This tool lets affiliates dig into how their traffic performs over time — grouped by registration, FTD, or deposit date — mirroring the cohort analysis capabilities previously available only to operators.

Just like the operator-side version, the affiliate cohort report supports full flexibility in **filters**, **columns**, and **cohort settings** (cohort type, cohort size).

You can configure visibility globally or tailor access for specific affiliates via a new **"Cohort Report" tab** added to the **"Partner Report"** settings page (`/casino/settings/partner_report`), letting you control which filters, columns, and cohort types are available to affiliates.

**Default Affiliate Access Settings**

As of this release, the default settings for affiliate visibility are as follows:

- **Cohort Report Enabled:**- `true`
- **Filters:**Brands, Campaign IDs, Promo IDs, Player dynamic tags, Exchange rates date
- **Columns:**Registrations, Prequalified, FTDs count, Deposits sum, Casino NGR, SB NGR, Poker rounds count, Poker rake sum, Poker NGR
- **Cohort settings:**Cohort type – Player registration date, Cohort type – Player FTD date

Reports can be exported to **XLSX**, either directly or via the Requested Reports page (`/partner/requested_reports`).

 

Affiliates can now create campaigns and promos through the Customer API — no more clicking through the UI every time a new campaign is needed.

**Why this matters**

For affiliates running things at scale, campaign creation is a repetitive, high-frequency task — and that's exactly the kind of work that's painful to do by hand and easy to automate. This update is especially useful for:

- **Large affiliate networks and media buyers**, who often need to spin up dozens of campaigns and tracking links per day across many brands and traffic sources.
- **Affiliates with their own tracking/CRM stack**, who can now keep campaign and promo data in sync automatically instead of duplicating setup work in two places.
- **Agencies managing multiple accounts or brands**, who can template and script campaign creation instead of repeating the same manual steps for each one.
- Any basically any affiliate who wants tighter turnaround times.

**What's new**

- **API key authentication.**Each partner user can generate their own API Key + API Secret. Requests are signed using a combination of timestamp, HTTP method, path, query, and body, sent via the- `X-Authorization-Key`and- `X-Authorization-Sign`headers (timestamp in- `X-Timestamp`). Invalid signatures or stale timestamps return a clear- `401`with an- `invalid_signature`or- `expired_timestamp`error.
- **Self-service credential management.**A new- **My account → API credentials**(- `/partner/api_credentials`) section lets affiliates create, view, edit, and archive their own keys. Both API Key & Secret are shown only once at creation — after that, only the last 4 characters are visible for API Key.
- **Operator-side control.**A new API tab on the partner settings page (- `/casino/partners/:id/settings/api`) lets operators enable API access and, separately, enable campaign/promo creation via API on a per-partner basis. Both are off by default, so nothing changes unless an operator opts an affiliate in.
- **New endpoints:**- `POST /api/customer/v2/partner/campaigns`— create a campaign, with validation that the brand and commission are available to the affiliate and correctly linked to each other.
- `POST /api/customer/v2/partner/promos`— create a promo under an existing campaign, with validation that the landing/medium matches the campaign and the traffic source is valid.
 
 

Alongside the campaign/promo feature, we've added several new read endpoints that let affiliates pull their own account data programmatically. A few of these are worth highlighting because they pair directly with campaign/promo creation: creating a campaign requires a `brand_id` and `commission_id`, and creating a promo requires a `landing_id` — so affiliates can now look those values up via the API first, then feed them straight into the campaign/promo creation calls, without ever needing to check the UI.

- **/api/customer/v1/partner/bills**
- **/api/customer/v1/partner/payments**
- **/api/customer/v1/partner/commissions**
- **/api/customer/v1/partner/landings**
- **/api/customer/v1/partner/brands**

All API documentation is available under "Partner API" tab (`/partner/api_docs/customer_partner`) in the Navigator.

 

Operators can now track affiliates who haven't confirmed their email yet, from a single dedicated page.

**Value**

Until an affiliate confirms their email, they don't show up on `/casino/partners` at all — which is the page affiliate managers use to work with affiliates. That means unconfirmed affiliates are effectively invisible to the team and easy to lose track of. This page closes that gap: it gives affiliate managers a place to see exactly who's stuck at the confirmation step, so they can proactively reach out and nudge them to confirm, instead of those affiliates just falling through the cracks.

**What's new**

- New page at **Partners → Unconfirmed emails**(`/casino/unconfirmed_emails`), listing every affiliate with an unconfirmed email: Email, Company name, plus any fields marked required for registration in`/casino/settings/profile_fields`(excluding Security question/answer, Receive newsletters, and Default currency for reports), and Created at.
- **Filters:**Emails and Company names (multi-input with autosuggest, matching the same filters on the Partners page), Microsoft Teams and Telegram (multi-input, no autosuggest), and Created at (date range).
- **CSV export**with the same columns as shown on the page.
- **Visibility logic:**the page only shows up for operators with the- *Personal partner details*permission.
 

Operators now have a dedicated page for seeing the full picture of sub-affiliate activity on their casino, instead of piecing it together affiliate by affiliate.

**Value**

Sub-affiliate structures can get complex fast, and until now there was no single place to see all parent–sub-affiliate connections at once. This page gives operators one filterable, exportable view of the whole picture — useful for auditing or tracing a specific referral chain.

**What's new**

- New page at **Partners → Subaffiliates**(`/casino/partner_connections`), showing a table of every parent affiliate ↔ sub-affiliate connection with: Parent Affiliate, Subaffiliate, Level (relative to the parent), Campaign, Promo, Assigned at date, and Strategy (the commission strategy the sub-affiliate was linked under).
- **CSV export**of the table, in the same column order as shown in UI.
- **Role-aware access:**- Superoperators with a Partners exclusion don't see the page or the Subaffiliates tab at all.
- Dedicated operators only see rows for the parent affiliates assigned to them; sub-affiliates of those parents are visible in the table, but the operator can't open a sub-affiliate's detail page unless it's also assigned to them.
- General Manager access is handled accordingly.
 
 

The players list — both the backoffice page (`/casino/players`) and the Customer API endpoint (`/api/customer/v1/casino/players`) — was slow, especially on deep pages. The main culprit was classic offset-based (`page`/`limit`) pagination, which gets slower the deeper you page, since the database has to scan and discard every row before the requested offset.

**What changed**

- **Switched from offset to cursor (keyset) pagination.**Instead of asking for "page 3500," you now ask for records right before or after a specific player ID — a much cheaper operation for the database, since it can jump straight to that point instead of counting through everything before it.
- **A new Customer API endpoint:**- `GET /api/customer/v2/casino/players`, bringing the same fast pagination to API consumers.
- **UI update on**- **/casino/players**- **:**since jumping to an exact page number doesn't map onto cursor pagination, the pager now has dedicated- **First page**/- **Last page**buttons alongside- **Prev/Next**, and the total player count is still shown.

**How to use the new pagination (****/api/customer/v2/casino/players****)**

- **First page:**call the endpoint with no- `id_gt`/- `id_lt`param (optionally set- `per_page`, max 200).
- **Next page:**take the- `id`of the- **last**item in your current response and pass it as- `id_lt=<that id>`— this returns the next batch of older records.
- **Previous page:**take the- `id`of the- **first**item in your current response and pass it as- `id_gt=<that id>`— this returns the previous batch.
- Use `has_next`/`has_prev`in the response to know whether there's more to fetch in either direction — there's no`total_pages`to check against anymore, since cursor pagination doesn't have a fixed page count.

**If you're integrating via API:** `/api/customer/v1/casino/players` keeps its current contract (page-based, same response shape) so nothing breaks today.

That said, **we plan to deprecate and eventually remove ****/api/customer/v1/casino/players**`/api/customer/v2/casino/players` using the parameters above. We'll share a firm deprecation timeline separately, but the earlier you move over, the less of a scramble it'll be later.

 

- **Payments**- Affiliates can now see the transaction ID (`txid`) and the effective conversion rate for crypto withdrawals directly on the payment detail page (`/partner/payments/:id`), for payments processed via the Crypto payment system.
- The payments CSV export (`/casino/payments`) now includes a "Proof of payment" column with the`txid`for successful crypto payments, so operators no longer need to open each payment individually to confirm a payout.
 
- Affiliates can now see the transaction ID (
- **Brand Access vs "Sign in as Affiliate"**- Brand access restrictions are now also enforced when an operator uses "Sign in as Affiliate": landings, media, bills, commissions, campaigns, promos, postbacks, postback logs, balance transactions, events, and contact details tied to a restricted brand are hidden and non-interactive.
- The same restriction now extends to Traffic Report and Cohort Report — statistics, filters, and autosuggest values are scoped to only the brands the signed-in-as user has access to.
 
- **Affiliate Onboarding:**replaced the confusing post-registration redirect to the login page with a clear on-page message ("Email confirmation required") when email verification is needed, so new affiliates aren't left thinking they can log in right away.
- **Postbacks:**added a new- `IsFTD`variable for "Any Deposit" postbacks, so operators can finally tell first deposits apart from repeat deposits without relying on- `amount`/- `amount_cents`.
- **Security:**- Password reset links now expire after 30 minutes (previously longer) for affiliate, casino, and admin users, with updated email copy reflecting the shorter window.
- Users without the "Personal partner details" permission (including superoperators with that exclusion) can no longer see affiliate emails via the Partner Statistics CSV/XLSX export or the Customer API.
 
 

- **Balancer Domains**- The Balancer domains page (`/casino/balancer_domains`) now shows Partners, Commissions, Campaigns, and Promos counts per domain, each clickable through to a pre-filtered list.
- Added the underlying "Balancer domain" filter to the Partners, Commissions, Campaigns, and Promos pages to support this.
 
- The Balancer domains page (
- **Operators page:**the Block/Unblock checkbox moved from the edit page to the operator's detail page, with a confirmation pop-up now required before unblocking a user.
- **Commission Constructor:**toggling "Convert all conditions, qualifiers, rewards into one base currency" (or changing the fiat/crypto base currency) no longer resets already-filled values in Commission Rules.
- **Filters**- New "Company name" filter on Partner Statistics, also supported via the Customer API.
- New "GEOs", "Language", and "Tags" filters on the landing-selection step of campaign/promo creation.
- The "Dedicated Operator" filter now supports a "None" option to find affiliates with no dedicated operator assigned — available on the Partners, Bills, and Payments pages.
- The "Partner Emails" filter on Partner Statistics is now case-insensitive.
 
- **File upload limits:**reduced maximum upload size for several file types (e.g., landing images, news banners/images, documents, and medium content images down to 5–10 MB) to reduce storage and performance risk.
- **Affiliate-facing:**- Added a new "Landings" page for affiliates (`/partner/landings`), listing the landings they can use to create a promo, with filtering support mirroring the operator-side landings page.
- Traffic source list is updated with "Email no deposit bonus".
- The restricted-countries list on the Bank transfer payment system page now collapses to 2 rows with a "Show more" / "Show less" toggle, instead of dumping the full list inline.
 
- Added a new "Landings" page for affiliates (
- **Added or updated confirmation pop-ups**before impactful actions across the interface — landing domain changes, archiving (bonus codes, landings, media, news, commissions, deep links), and deleting documents/postbacks — so operators get a clear "are you sure" step before something that can't be undone.
- **Standardized:**- Actions presented in tables**:**replaced inconsistent text links with buttons and unified their colors (e.g., white for Edit, red for Archive) across Partners, Brands, Landings, Media, Commissions, Users, and more.
- The naming of "create new entity" buttons to "Create" across all the main list pages (previously a mix of "New", "Add", and "Create").
 
- Actions presented in tables
- **Flow improved:**after creating a dynamic tag, the operator is now redirected straight to the tag's detail page instead of staying on the creation form.
- **BUG FIX:**Added network-timeout detection for balance corrections and bill corrections: if the request can't be confirmed due to a network timeout, operators now see a persistent "Connection Issue" notification telling them to refresh the page before trying again, instead of unknowingly resubmitting and creating a duplicate.
- **BUG FIX:**Fixed the Payments CSV export showing the raw payment system object instead of its readable name (e.g., "Crypto" instead of- `{:humanized_name=>"Crypto", ...}`).
- **BUG FIX:**Fixed the document status label on the document detail page not updating immediately after Approve/Decline, even though the color changed right away.