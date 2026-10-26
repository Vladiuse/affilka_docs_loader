We’re excited to introduce the **Cohort Analysis Report**, now available in our product. Cohort analysis is a powerful tool that helps you track and evaluate players behavior over time. By grouping players based on shared characteristics or actions (e.g., registration date, FTD date and any deposit date), this report allows you to analyze trends, measure performance, and understand the long-term impact of your strategies.

**Why It’s Useful:**

- **Track Retention:**Monitor how player groups engage with your product over time.
- **Evaluate Campaigns:**Measure the effectiveness of marketing efforts and promotional activities.
- **Make Data-Driven Decisions:**Identify patterns and trends to optimize your business strategies.

**Where to Find It:**

You can find the "Cohort Analysis" report at the bottom of the "Reports" section or go directly to `/casino/cohort_report`.

**Data representation and report configuration:**

The Cohort Analysis report is presented in a table format for easy interpretation:

- The first column displays the cohort type along with the cohort period size (e.g., week, month, etc.).
- The second column (Players count) shows the size of each cohort, representing the number of users or entities in that group.
- The remaining columns, combined with the rows, illustrate the behavior or performance of each cohort over time.

To configure the report you need to specify values using these essential filters:

- **Cohort type**- this filter configure player cohort by their actions. Available cohort types (actions) are: Player registration date, Player FTD date, Player deposit date.
- **Cohort size**- how the cohort will be grouped by period. Available options are Day, Week, Month.
- **Period range**- the period which limits the cohort and cohort analyzed period.
- **Period size**- how analyzed period will be grouped by period. Available options are Day, Week, Month.
- and finally, **Metric****-**the metrics are the same as on the Partner Statistics report excluding Visits, Partner Income, Reward-type columns and Payable Casino NGR.
- Common filters like Partner IDs, Brands, Campaign/Promos IDs, etc. are also available.

Please note that the **Period Range** defines both the cohort selection and the period for analyzing metrics. For example:

- If the **Period Range**is set to**01.01.2024 - 31.03.2024**, the cohort type is**Player Registration Date**, the analyzed metric is**Casino NGR**, the cohort and period size is set to**month**:- The report will include players who registered between **01.01.2024 and 31.03.2024**, grouped by their registration month.
- It will display how much **Casino NGR**those players generated during the same period (**01.01.2024 - 31.03.2024**), also grouped by month.
 
- The report will include players who registered between 

**Cell colour distribution:**

It uses 5 color values as an indication of relative metric values: the darkest color represents the highest metric values, and the lightest color represents the lowest metric values. Each color represents the same relative range of values. For example, if the highest value in the table is 100, then each color represents a range of 20 (100/5); if the highest value in the table is 50, then each color represents a range of 10 (50/5).

**Report export:**

This report can be conveniently exported in **XLSX**, **XML**, or **JSON** formats using the **"Export Report"**button. For exports in **XLSX format**, the report will be sent to your email or can be downloaded at any time from the **Requested Reports** page (`/casino/requested_reports`).

**Report configuration examples:**

- If you want to analyze how many FTDs was made during the 01.12.2024-07.12.2024 week by players registered in 01.12.2024-07.12.2024 you need to set:**Cohort type**- Player Registration Date;**Cohort size**- day;**Period range**- 01.12.2024-07.12.2024;**Period size**- day,**Metric**- FTD count.
- If you want to analyze how many Casino NGR was generated for the 2024 year by players who did FTD in 2024 you need to set:**Cohort type**- Player FTD Date;**Cohort size**- month;**Period range**- 01.01.2024-31.12.2024;**Period size**- month,**Metric**- Casino NGR.

The choice of grouping depends on your analysis goals and the length of the period being analyzed. For shorter periods, grouping by day is more appropriate, while for longer periods, such as months, grouping by month is recommended.

 

We've enriched our traffic report with new filters, groupers and metric to make our report even more robust and provide you with valuable insights about your traffic.

Filters and groupers:

- Traffic sources - you can filter and group the data by the "Traffic source" which is specified on the promos of your affiliates. Please keep in mind that you will be able to group and filter the data that was received after November 12, 2024.
- Device types - you can filter and group the data by the "Device type". The data is received from the visit's user agent data, possible options are Computer, Tablet, Phone, Console, Wearable, TV, Unknown. You will be able to group and filter the data that was received after January 1, 2023.

Metric:

- Regs to FTDs % - the metric is calculated by the next formula "(`FTDs count/ Registrations count) * 100%`" for a specified period.
 

We've implemented a feature that displays the bills which were used as a base to calculate the reward for parent affiliate. This data enhances transparency and simplifies the process of reviewing subaffiliate bills, making it easier to verify reward calculations.

The data can be found on the detailed page of subaffiliate bill under the "Partner data" section:

- Pay your attention on the "Extra" column where you can find the bills which were used during reward calculation.
- If the reward calculation includes both fiat and crypto bills, the associated bills with a link will be displayed in the corresponding rows.

We've also added the "Subaffiliate" filter on Bills page (`/casino/bills)` that will help you to easily find subaffiliate bills.

 

You can now require affiliates to provide traffic source information when creating campaigns or promos. By enabling this feature, you ensure your traffic is properly segmented, allowing for enhanced report analysis based on traffic sources.

To enable this feature you need:

- Navigate to **All Settings > System Management**or go directly to`/casino/settings/system_management`.
- Enable the **Traffic Source**checkbox.
- Click **Submit**to save your changes.

Once this feature is enabled, your affiliates will encounter a "can't be blank" error message if a traffic source field is left empty during campaign or promo creation.

 

We've added the "News Items Read" and "News Items Process" roles. Here's how it works:

- If an Operator doesn't have access to the "News Items Read" and "News Items Process" roles,  they don't have access to the "News"(`/casino/news`) section in the Operator/Affiliate Interface, the "Latest news" section on the affiliate dashboard isn't presented, they are not able to perform any actions to the news.
- If an operator has access to the "News Items Read" role, but doesn't have the "News Items Process" role, they have access to the "News"(`/casino/news`) section in the Operator/Affiliate Interface, the "Latest news" section on the affiliate dashboard is presented, BUT they are not able to perform any actions to the news.
- If an operator has access to the "News Items Read" and "News Items Process" roles, they have full access to the News feature.

Since the release, the roles "News Items Read" & "News Items Process" will be activated automatically to all SuperOperators, for usual operators the "News Read" roles will be activated.

You can also limit which SuperOperators can have access to this page by using the SuperOperator exclusions "News Items Read" and "News Items Process". Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

 

We've implemented a feature that should help the Affilka Team to notify you about upcoming releases, server works, etc.

Notifications will be displayed in the Operator Interface at the very top of the screen: 

- Green notifications will be used for normal, not urgent announcements (f.e. new release). You can hide them by clicking on "X" sign.
- Red ones will be used for announcements that you should pay special attention to (f.e. expected server downtime). You have no option to hide them.
 

- "Report" button is now present on bills in "Paid" and "Cancelled" statuses.
- The process of generating a report in csv/xlsx has been accelerated due to the simultaneous processing of rows and totals.
- BUG FIX: "NGR" postback action now includes "Casino taxes" parameter.
- BUG FIX: on partner's detailed page under Traffic source text field and during comment creation you can use several lines while typing the text.
- BUG FIX: Promo id is clickable on the reports page (`/partner/report`) in the Affiliate Interface.
- BUG FIX: the default campaigns should be automatically created during partner creation.