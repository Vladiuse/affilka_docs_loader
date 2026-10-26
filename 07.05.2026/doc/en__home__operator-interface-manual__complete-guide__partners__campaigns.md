In this tab (**/casino/campaigns**) you will find all campaigns created by your partners. You can filter and find campaigns by:

- **Campaign**- **IDs**: the filter supports multiple values separated by a comma, “Space” or “Enter” key. You can indicate unique IDs of those affiliate campaigns you want to find.
- **Campaign name:**the filter supports partial search. You can type some campaign name partially and press “Filter”, and you will see all campaigns whose name contains what you’ve just typed.
- **Partner ID:**must be exact match.
- **Partner email:**the filter supports partial search. You can type “gmail” and the filter will find campaigns of all affiliates /their team members who have “gmail” in their email.
- **Traffic Sources:**the filter supports multiple values and autosuggest feature. Start typing “Traffic source” type and it will appear in the dropdown selector. You can choose several traffic sources here and the filter will find campaigns with any indicated traffic source.
- **Brand:**the filter supports multiple values and autosuggest feature. Start typing the name of the brand and it will appear in the dropdown selector. You can choose several brands and the filter will find campaigns in any of the indicated brands.
- **Commission ID**(only 1 commission plan can be applied to 1 campaign): must be exact match.
- **Commission title:**the filter supports partial search. You can type some commission title partially and press “Filter”, and you will see all commissions whose title contains what you’ve just typed.
- **Subaffiliate**(All/Yes/No): finds those campaigns that are targeting either sub-affiliates or players. The Subaffiliate campaigns are governed by subaffiliate commission plans. The destination landing page for users attracted via Subaffiliate campaigns is generally the main affiliate program website.
- **Landing IDs:**the filter supports multiple values separated by a comma, “Space” or “Enter” key. You can indicate unique IDs and find campaigns in which specified landings are used.
- **Landing URL:**the filter supports partial search. You can type some landing URL partially and press “Filter” or “Enter”, and you will find all campaigns that contain the specified landing URL.
- **Created at:**the filter allows to indicate date ranges (from…to) when the campaign was created
- **Players count:**the filter allows to find campaigns by a number of registered players (from…up to a specific number of players).

You can export the table in CSV format and open the full screen version of the campaign table.

If you want to find a specific campaign by its ID, type the ID in the URL in browser (e.g. **/casino/campaigns/356**)

You can view a detailed campaign page by clicking on the campaign id in the campaigns table.

This page contains the following information about the campaign:

- **Campaign**- **ID**– a unique identifier of the campaign.
- **Campaign**- **Name**– the title of the campaign assigned to it either automatically by the system or by a partner at campaign editing.
- **Traffic source**– the traffic source that an affiliate indicated for the referral links under this campaign. Traffic sources refer to the various channels or methods that guide visitors to a website. These include SEO, social media, email marketing, paid advertising, etc. You can use this information to segment and analyze your affiliates based on their traffic sources. You can also send the information on traffic sources to your brands' landing pages when a player clicks on the tracking link. Contact your account manager at Affilka to get this feature enabled for your brand.
- **Partner**– the partner who owns the campaign.
- **Brand**– the brand on which the campaign was created.
- **Commission**– the commission plan attached to this campaign.
- **Created**- **at**- **date**– the date when the campaign was created.
- **Players**- **count**– the number of players referred to the iGaming brand via this campaign.
- **Promos**- **count**– the number of promos created within the campaign.
- **State**- represents the statе of the campaign:- **active**
- **archived**- **IMPORTANT!**Campaign archiving can only be performed by the affiliate or by Operator via “Sign in as affiliate” on the partner’s detailed page. Once a campaign is archived: it is no longer possible to create new promos or postbacks under this campaign; existing redirect links will continue to work.
 
- **Archived At**- the date when the campaign was archived.
- **Parameters**- those added in tracking link by the Operator will be automatically appended to the redirect URL specified in the promo. This ensures consistent and reliable data collection whenever a player clicks the link.

By clicking “Edit” on a campaign’s detailed page, you can insert **Key-Value parameters**. These are automatically sent to the promo’s redirect URL upon a user click. It helps avoid a partner's mistake when inserting the tags manually.

Example: Key (utm_source) = Value (facebook)

**Validation Rules:**

When configuring parameters, the following rules apply:

- No Duplicates: Duplicate keys across different rows are not allowed.
- No Empty Fields: Both Key and Value fields must be completed.
- Reserved Keys: The following system parameters cannot be used: stag, tr_src, affb_id, http_referrer, tracking_link, cmp, prm, dplnk
- Allowed Characters: Only letters (A–Z), numbers (0–9), underscores (_), hyphens (-), and dots (.) are permitted.

**IMPORTANT!**

- **Overwriting Logic**: If an incoming parameter key matches one defined at the campaign level, the campaign value will take priority and overwrite the incoming value. Example: A partner sends utm_source=instagram, but the campaign is configured with utm_source=meta. The system will save and send utm_source=meta.
- **No Retrospective Changes**: Updated parameters only apply to clicks occurring after the changes are saved. Existing data for previous visits or users will not be modified.
- **Preservation**: Any incoming parameters with keys not defined at the campaign level will remain unchanged and will be stored normally.

To enable the parameter in the report, please review how to add a dynamic tag – here.