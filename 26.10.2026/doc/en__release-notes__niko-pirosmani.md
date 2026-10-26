The introduction of HTML5 banners enhances campaign effectiveness by enabling richer interactivity, faster load times, and full mobile optimization. With flexible customization options for offers, languages, and layouts, operators can adapt creatives to any GEO or audience segment. HTML5 also ensures consistent performance across all major ad networks and devices, allowing teams to launch, test, and scale campaigns with greater reliability and efficiency.

To start working with HTML5 Banners, simply upload the banner the same way you would add any other media asset:

- Go to the **Media**page (`/casino/media`) and click**Add**.
- Fill out the form:- Choose whether the banner is intended for **players**or**sub-affiliates**.
- Specify the **casino brand**associated with the banner.
- Select **HTML5**as the media type.
- Upload the **.zip archive**containing your banner.
- Upload a **preview image**for the banner.
 
- Choose whether the banner is intended for 
- Submit the form.

A banner in the **Shared** state is accessible to all affiliates and can be used in any campaigns of the brand it belongs. A banner in the **Personal** state is private and will not be available to affiliates until you explicitly assign it to them.

Once the banner is uploaded and shared with affiliates, they can simply select the HTML5 Banner during campaign or promo creation. On the promo details page, the system will provide a script that must be embedded on the website where the banner should appear.

 

A user visits a website where the provided script is embedded.`<script type="text/javascript" src="https://reflink.com/sources/promocode.js"></script>`

The script sends a request to our system. In response, the system returns JavaScript code, that embeds into the page an iframe pointing to HTML5 banner index page URL that resides on our CDN. Banner URL will have a reflink= parameter included, which allows to retrieve the referral link in banner's JavaScript code.

Iframe loads and renders HTML5 banner, which is displayed to the user.

To pass dynamic parameters, simply append them to the link included in our system’s script. When the system returns the JavaScript code, the `reflink` parameter will contain the full referral link along with all previously added parameters.`<script type="text/javascript" src="https://reflink.com/sources/promocode.js?click_id=i1234ji&sub_id=13"></script>`

- Must be in **.zip**format
- File size must **not exceed 1 MB**
- The archive must contain an **index.html**
 

To improve traffic quality analysis, we’ve introduced two new metrics in the **Partner Statistics** report (`/casino/report`) that can serve as MAU (Monthly Active Users) indicators: **Casino Active Players** and **Sportsbook Active Players**.

These metrics track the number of players who placed at least one bet within the selected period—using the `bets_sum_cents` API parameter for casino activity and the `sb_bets_sum_cents` API parameter for sportsbook activity.

You can enable and view these metrics on the **Partner Statistics** page under the Columns section. These columns are also available via the **Customer API.**

By default, **Casino Active Players** and **Sportsbook Active Players** are disabled for affiliates. To make them available, adjust the visibility settings in **Partner Report → Partner Statistics** (`/casino/settings/partner_report`).

 

To support deeper player behavior analysis and fraud detection, we’ve added a new "Player" **filter** and **grouping option** to the **Traffic Report** (`/casino/traffic_report`). This enhancement allows you to inspect non-unique visits per player and review the associated device type, user agent, visit IP, referrer, and more.

To use this feature, go to the **Traffic Report** page and either enter a player’s ID in the Player IDs filter or select Player in the Group by section. Player-based filtering and grouping is also available via the **Customer API**.

**Please note** that all available data will be grouped by player. Any visits not associated with a player will appear under **Player N/A** in the Player grouping.

The **Player filter** and **Player grouper** are not enabled by default for affiliates. To activate them, adjust the visibility settings under **Partner Report → Traffic Report** (`/casino/settings/partner_report`).

 

New **Traffic Source** filter is now available on the **Partner Statistics** (`/casino/report`) and **Cohort Analysis** (`/casino/cohort_report`) pages. This filter allows you to view visits, registrations, and player activity based on a specific traffic source, making traffic analysis more convenient and providing clearer insight into the conversion performance of particular acquisition channels.

The filter applies to data created **from October 1, 2024** onward, and is also accessible via the **Customer API**.

Please note that the system attributes visits, players, and their activities to the traffic source that the player was originally redirected from. For example, if a player arrives via a referral link associated with a promo where the traffic source is set to **SEO**, then their visit, registration, and all future activity will be attributed to the **SEO** source.

Traffic Source filtering is not enabled by default for affiliates. To activate it, update the visibility settings under **Partner Report → Partner Statistics** (`/casino/settings/partner_report`).

 

We've implemented new entities which are supported via our Customer API:

- The **Campaigns**page (`/casino/campaigns`) is now available through the`/api/customer/v1/casino/campaigns`endpoint.
 API documentation can be found under**API → Customer Operator → Campaigns →****“Campaigns list”****.**
- The **Requested Reports**page (`/casino/requested_reports`) is accessible via`/api/customer/v1/casino(partner)/requested_reports`for**both affiliates and operators**.
 This endpoint allows you to automatically export reports generated via queues—such as ZIP or XLSX files—directly into your BI systems.
 For operator API documentation is available under:**API → Customer Operator → Requested Reports →****“Requested report list”****.**For affiliate:**Partner****API → Requested Reports →****“Requested report list”**.
 - We have also improved the behavior of the `/api/customer/v1/casino(partner)/report`endpoint. When sending the parameter`async: true`and the report generation is delayed, the response will include a**report_id**. You can use this ID to later download the report via`/api/customer/v1/casino/requested_reports`.
 
- We have also improved the behavior of the 
- The **Traffic Report**page (`/partner/traffic_report`) is now supported via the`/api/customer/v1/partner/traffic_report`endpoint.
 Documentation is available in the affiliate interface under**Partner API → Traffic Reports →****“Traffic report in inline JSON”****.**
 

- User session cookie is renamed from "_affiliate_system_session" to "_session_id".
- Promo name is displayed for "Partner Statistics", "Traffic Report" and "Subaffiliate report" while "Promo" grouper is enabled.
- Performance optimisation: "Partner Statistics" report calculation via queues should be improved.
- New system emails design. This update should decrease cases of getting emails to spam.
- "Payments" page (`/casino/payments`): "Kind" and "Original payment ID" columns are added for CSV export.
- "ZAR" currency is now supported by "bank transfer", "crypto", "other" payment systems.
- "MATIC" cryptocurrency is no longer supported by our product due to its renewal to "POL".
- BUG FIX: User sessions are back on the partner and operator user detailed page.
- BUG FIX: "Brand" filter fix on the "Quick charts" section.
- BUG FIX: "Postback action" filter with "First deposit" value fix on the "Postbacks logs" page.
- BUG FIX: Partner, Campaign, Promo ID reflects correct players data during player reassignment.
- BUG FIX: "Traffic source" filter can be used via "Traffic report" customer API.
- BUG FIX: Data grouper by Date is fixed for affiliate "Traffic report".