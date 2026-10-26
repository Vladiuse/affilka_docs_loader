The Balancer Domains page allows Operators to view, manage, and seamlessly replace active tracking domains directly within the interface. This feature ensures your referral and tracking links remain uninterrupted, providing a quick way to swap out blocked or out-of-date domains.

- Location: Affiliate program ➔ Balancer domains (located right after *Landing domains*)
- URL: /casino/balancer_domains

The page features a comprehensive data table displaying all balancer domains configured for your affiliate program.

 

| Column Name | Description | 
| ID | Unique system identifier of the balancer domain record. | 
| Brand | The specific brand associated with the domain. | 
| URL | The active domain address used in tracking links. | 
| Subaffiliate | Indicates (True / False) if the domain is dedicated to the sub-affiliate system. | 
| 301 Redirect for Search Engine | Visual indicator (Checkmark / Cross) showing if a 301 redirect is enabled. | 
| Partners count | Clickable value showing the total number of partners whose promos use the specified balancer domain. Redirects to /casino/partners pre-filtered by the selected Balancer domain. | 
| Commissions count | Clickable value showing the total number of commissions linked to brands using the specified balancer domain. Redirects to /casino/commissions pre-filtered by the selected Balancer domain. | 
| Campaigns count | Clickable value showing the total number of campaigns whose promos use the specified balancer domain. Redirects to /casino/campaigns pre-filtered by the selected Balancer domain. | 
| Created at | Timestamp when the domain record was created. | 
| Updated at | Timestamp of the last modification. | 
| Actions | Contains the Edit button to modify the domain. | 












You can update domain URLs on the fly using the inline editing mechanism (similar to how media assets are managed on the /casino/media page).

- Click the Edit button in the *Actions*column next to the domain you want to replace.
- The URL field for that specific row will instantly switch to an editable input with an Autosuggest dropdown.
- The Edit button will change to Save and Cancel.

When you start typing or open the dropdown, the system suggests a list of valid domains consisting of:

- Active Balancer Domains: Other domains currently active within your affiliate program.
- Backup Balancer Domains: A pool of pre-approved standby domains **requested by you and pre-configured by your Account Manager.**

Once you select a new domain and click Save, a confirmation pop-up will appear outlining the impact of the change.

Depending on the domain type, you will see one of the following prompts:

Balancer domain change

You are about to change the balancer domain URL for brand: [Brand Name]. This action will affect all referral links using this domain.

Are you sure you want to change *OldDomain.com* to *NewDomain.com*?*[Confirm] [Cancel]*

Balancer domain change

You are about to change the sub-affiliate balancer domain URL. This action will affect all referral sub-affiliate links using this domain.

Are you sure you want to change *OldDomain.com* to *NewDomain.com*?*[Confirm] [Cancel]*

After clicking **Confirm**, the system automatically and instantly updates all existing tracking links, promo materials, and commissions associated with that domain ID.

While the system automatically updates all tracking links, promos, and commissions within your affiliate platform, this change does not update external traffic sources.

**IMPORTANT!**Once a domain is replaced, your partners (affiliates) must manually update the tracking links in their traffic sources (e.g., websites, ad networks, social media channels) to the new domain to ensure continuous traffic routing and accurate tracking. We highly recommend notifying your partners immediately after any domain changes.