This page can be reached via the** casino/traffic_report** link.

This report allows you to view and analyse the flow of traffic from affiliate websites via affiliate referral links to their iGaming brands.

The data on clicks in the Traffic report is updated almost in real-time. Whereas the info on player registrations and deposits is updated as soon as the activities data is sent from your iGaming platform to Affilka via API (every 15 minutes, every hour, etc).

The data in the report is available from January 1, 2023.

This is the complete list of all available metrics that can be found in the report:

| Metric/Parameter | Description | 
|---|---|
| All clicks | the total number of clicks for a specified period (both unique and duplicated) which were made on the referral links of an affiliate program. | 
| Unique clicks | the total number of unique clicks for a specified period which were made on the referral links of an affiliate program. The uniqueness of a click depends on visit cookie lifespan. Do not confuse a visit cookie with an affiliate attribution cookie. The visit cookie defines whether a user click was unique or duplicated, whereas the affiliate attribution cookie is responsible for attributing a player to a specific affiliate. The default visit cookie lifespan is set at 30 days for the affiliate program. It means that if the same player clicks 20 times on a referral link within 30 days, only 1 click will be counted as a unique one, and 19 as non-unique. You can set different visit cookie lifespans for your brand(s) and/or set an individual visit cookie lifespan for specific affiliate promos. The more granular setting will always overwrite the default one. | 
| Registrations | the total number of player registrations for a specified period. | 
| FTDscount | the total number of first deposits for a specified period. | 
| Depositscount | the total number of first deposits for a specified period. | 
| Clicks to regs % | a conversion ratio from unique clicks to registrations calculated as `(Registrations ÷ Unique Clicks) x 100%` | 
| Clicks to FTDs % | a conversion ratio from unique clicks to first deposits calculated as `(FTDs count ÷ Unique Clicks) x 100%` | 
| Clicks to Deposits % | a conversion ratio from unique clicks to deposits calculated as `(Deposits count ÷ Unique Clicks) x 100%` | 
| Regs to FTDs % | a conversion ratio from registrations to first deposits calculated as `(FTDs count ÷ Registrations) x 100%` | 

**Please, note! **The Traffic Report contains only those registrations and player activites that are associated with a click. If a player is tied to an affiliate not as a result of their clicking on a referral link, but through entering a bonus code or via data migration, such players and deposits will not be reflected in the traffic report.

This is the complete list of all available filters that can be found in the report:

| Filter | Description | 
|---|---|
| Date range | indicate the time period you’d like to analyze here.  E.g. 3 months, from June 1, 2020 to August 31, 2020. | 
| Brands | you may choose one or several iGaming brands from the dropdown selector. If a brand is not specified, you will see cumulative statistics on all of your brands taken together. | 
| Partner IDs | unique IDs of those affiliates you want to analyze. | 
| Campaign IDs | unique IDs of those affiliate campaigns you want to analyze. | 
| Promo IDs | unique IDs of those affiliate promos you want to analyze. | 
| Promo codes | unique promo codes of those affiliate promos you want to analyze. | 
| Traffic sources | filter by traffic sources indicated by affiliates on their Promos. Here you may choose one or several traffic sources for the analysis from the dropdown selector. Please keep in mind that you will be able to group and filter the data that was received after November 12, 2024. | 
| Landing IDs | filter by any of the specified landing ID's or URLs (supports multiple values, will autosuggest ready values from the drop-down menu). Note! We don't track landing URLs history change. So if you edit the URL of landing id: 46 from "example.com/bonus" to "test.com/freespins", the data in the report on all historical visits, registrations and activities will be grouped under "test.com/freespins" URL, but the landing id: 46 will remain the same. | 
| Player IDs | unique IDs of those players you want to analyze. | 
| Stag visits | filter the traffic report to include only the specific Stags provided. You can enter multiple Stags simultaneously. To find a player’s individual Stag, navigate to the Player Detailed page and locate the STAG Visit field. | 
| Dynamic tag keys | name of the dynamic tag (e.g.clickid, webid etc.) | 
| Dynamic tag values | value in response according to a dynamic tag (e.g. 15dgjsy527 etc.) | 
| Referrer URL | filter by any of the specified referrer URLs (single input field which supports partial search). | 
| Device types | filter by the device types that was recorded on a user's visit. The data is received from the visit's user agent data, the possible options include Computer, Tablet, Phone, Console, Wearable, TV, Unknown. | 
| User agent | filter by any of the specified user agents (dropdown selector, supports multiple values and an autosuggest feature). | 
| OS | filter by any of the specified operating systems (will autosuggest ready values from the drop-down menu). | 
| Visit Countries | filter by any of the specified click countries (will autosuggest ready values from the drop-down menu). Please, note! Visit countries might be different from actual countries indicated by players at registration or during profile editing. This setting filters all data by the country in which the click occurred. For example: a user clicked a link in Germany, but registered and deposited from Sweden, indicating Sweden as their profile country. If you filter the report by visit country = Germany, the click, the player and their deposits will appear in the report. | 
| Dedicated operator emails | filter the report by the emails of partners’ dedicated operators. Here you can choose the emails of operators from the autosuggested dropdown. | 
| Visit IP | filter by any of the Visit IPs (single input field which supports "starts with" search). | 

By default the report represents the data for the current calendar month and is grouped by partner. You can decide how the data will be presented in the report by breaking it down into the following groupings:

| Grouper | Description | 
|---|---|
| Period | indicate the time period you’d like to analyze here.  E.g. 3 months, from June 1, 2020 to August 31, 2020. | 
| Brand | this grouping helps you to compare different brands with each other. | 
| Partner | you can use this grouping if you want to compare partners with each other. | 
| Campaign | this grouping allows you to compare campaigns with each other. | 
| Promo | you can break down the report by Promo to analyze how each referral link performs and compare it to others. | 
| Player | use this data grouping to analyze traffic on a player level. Any visits not associated with a player will appear under Player N/A in the Player grouping. | 
| Dedicated operator | allows you to group the report by dedicated operators to analyze and compare each operator’s partners’ performance | 
| Landing | allows you to compare and analyze visits of each landing page in a specified period. | 
| Traffic source | you can analyze the performance of various traffic sources. | 
| Referrer | allows you to analyze the resources from which the visit was made. (if you use this grouping and the referrer is blank for a visit, this means that the system or site, from which the redirect was made, hid this information or the redirect was made by pasting referral link into the browser's address bar). | 
| Device type | you can analyze performance on the device type level. | 
| User Agent | grouping allows you to analyze data on the user agent level. | 
| OS | you can use it to analyze and compare operating systems with each other. | 
| Visit Country | allows you to analyze clicks on country level. Please, note! Visit countries might be different from actual countries indicated by players at registration or during profile editing. This setting groups all data by the country in which the click occurred. For example: a user clicked a link in Germany, but registered and deposited from Sweden, indicating Sweden as their profile country. If you group the report by visit country, the click, the player and their deposits will appear under “Germany” visit country grouper. | 
| Visit IP | this grouping allows you to analyze clicks by their IPs. | 
| Various dynamic player tags | you can break down data by dynamic parameters sent to you by affiliates in their referral links to analyze and differentiate traffic statistics | 

You can also organize the report in the order that suits you by dragging and dropping data groups in “Group by” section. By clicking on "Filter", the data is grouped in the desired order. Also you can sort all data in the report in the ascending or descending order. Regardless of the size of the report pages, you can see amounts using the Sticky totals feature, which includes the Total values of each page. The amount of items per page is set as 100 by default. The Traffic report will show the default report view if you click on “Reset”.

Traffic report can be exported in CSV format. To get a report in CSV format you need to apply the required filters and data groupings, and press “Filter”. After that, click on the “Export in CSV” and you will receive a report by email.

Also report can be extracted in JSON format via unique statistic token, it can be found on your operator’s detailed page: **/casino/users. **

On the **/casino/api_docs** page you can find the “Customer Operator” API documentation, in which the Traffic Reports API section is available. Please find **Traffic report **page there to get information about how to receive the data via API.

Traffic report is available for operators via the** /api/customer/v1/casino/traffic_report **endpoint. To make requests, you need to send your user's unique statistic token in the authorization header. The Traffic Reports API documentation can be found under the “API” navigation tab in the “Customer Operator” API section and can be reached via the /**casino/api_docs/customer/casino/index.md** link in the Operator Interface.