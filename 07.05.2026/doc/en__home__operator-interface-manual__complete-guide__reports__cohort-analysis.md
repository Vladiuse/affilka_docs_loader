Cohort analysis is a powerful tool that helps you track and evaluate players behavior over time. By grouping players into cohorts based on shared characteristics or actions (e.g., cohort based on registration date, FTD date, deposit date), this report allows you to analyze trends, measure performance, and understand the long-term impact of your strategies.

**Why It’s Useful:**

- **Track Retention:**Monitor how player groups engage with your product over time.
- **Evaluate Campaigns:**Measure the effectiveness of marketing efforts and promotional activities.
- **Make Data-Driven Decisions:**Identify patterns and trends to optimize your business strategies.

**Where to Find It:**

You can find the "Cohort Analysis" report at the bottom of the "Reports" section or go directly to `/casino/cohort_report`.

The Cohort Analysis report is presented in a table format for easy interpretation:

- The first column displays the cohort type (registration date, FTD date, deposit date) along with the cohort period size (e.g., week, month, etc.).

- The second column (Players count) shows the size of each cohort, representing the number of users or entities in that group.

- The remaining columns, combined with the rows, illustrate the behavior or performance of each cohort over time.

By default, the report shows the data for the past 2 months (last month+current month). It represents how players who registered within a span of these 2 months deposit over the set period. The data is grouped by week. It shows cumulative data of all partners and brands. The report is converted into a default report currency set for your user. The exchange rate for the report is set at the current day.

**Cell colour distribution.**

The report uses 5 color values as an indication of relative metric values: the darkest color represents the highest metric values, and the lightest color represents the lowest metric values. Each color represents the same relative range of values.

For example, if the highest value in the table is 100, then each color represents a range of 20 (100/5); if the highest value in the table is 50, then each color represents a range of 10 (50/5).

The Cohort filters section allows you to determine the cohort you wish to analyze.

- **Cohort type –**indicate the type of action by which the players will be grouped. The available cohort types (actions) are: Player registration date, Player FTD date, Player deposit date.
- **Cohort size –**indicate the period by which the cohort will be grouped. The available options are Day, Week, Month.

In the Filter section you can indicate the action you wish to analyze, set the period for analysis, indicate how player activities should be grouped as well as filter the report by specific Brands, Partners, Campaigns, Countries, etc.

- **Metric**– choose the activities you wish to analyze. For example: Casino bets sum, Deposits sum, Casino NGR. The metrics presented here are the same as in the Partner Statistics report excluding Visits, Casino active players, Sportsbook active players, Partner Income, Reward-type columns and Payable Casino NGR.
- **Period range**– indicate the period for which the data will be analyzed.
- **Period size**– choose how the data in the report will be grouped period-wise. The available options are Day, Week, Month.
- Use filters such as Partner IDs, Brands, Campaign/Promos IDs, Dynamic tag include/exclude, Traffic sources etc. if you want to limit the scope of the report to specific entities.

Please note that the **Period Range** defines both the cohort selection and the period for analyzing metrics. For example:

If the **Period Range** is set to **01.01.2024 - 31.03.2024**, the cohort type is **Player Registration Date**, the analyzed metric is **Casino NGR**, the cohort and period size is set to **month**:

- The report will include players who registered between **01.01.2024 – 31.03.2024**, grouped by their registration month.

It will display how much **Casino NGR** those players generated during the same period (**01.01.2024 – 31.03.2024**), also grouped by month.

The Cohort Analysis report can be exported in **XLSX**, **XML**, or **JSON** formats using the **"Export Report" **button. For exports in **XLSX format**, the report will be sent to your email or can be downloaded at any time from the **Requested Reports** page (`/casino/requested_reports`).

To get a report in XLSX format, first, apply the required filters and data groupings and choose the fields you want to see in the report, and press “Filter”. After that, click “Report export” and choose “XLSX**”. **As soon as the report is ready, you will be notified via email. 

The email will contain an attached XLSX file, in case you want to view the report straight away. The email will also contain a link to the detailed page of the requested report in the Affilka interface where you can download the report via browser.

When you want to extract the report in XLSX format, you will be prompted to give a name to your requested report.

If you haven't indicated a name for your report when requesting it or you hit a time-out limit and didn't have a chance to indicate the report name, you can give the name to it on the detailed requested report page by clicking the “Edit” button.

Choose something that reflects the contents of the report so that you could easily navigate among your requested reports once they're ready.

The requested report will have a “cohort analysis” type assigned to it.

You can extract Cohort report in XML/JSON formats. To retrieve the statistics feed link, press "Export report" button and choose the desired format. Every link can be copied and opened outside an active session off site thanks to individual statistic tokens assigned to each operator. The statistic token remains static so that you could fetch data across different months without having to log in.

If an Operator is no longer working with the affiliate program and is removed from the team or their access to the operator interface is compromised, you can always expire the statistic token for this operator email. To block access to the statistic feed for a specific operator email, find the Settings>Operators tab (/casino/users), find the Operator's email, click on their ID and press “expire” next to the statistic token on a detailed Operator page.

- If you want to analyze how many FTDs were made by players who registered during the week of 01.12.2024–07.12.2024 and you want to see their daily performance, you need to configure the following settings: **Cohort type**– Player Registration Date;**Cohort size**– Day;**Period range**– 01.12.2024–07.12.2024;**Period size**– Day,**Metric**– FTD count.
- If you want to analyze how much Casino NGR was generated for the 2024 year by players who made their first deposit in 2024, and you want to see their monthly performance,  you need to configure the following settings: **Cohort type**– Player FTD Date;**Cohort size**– Month;**Period range**– 01.01.2024–31.12.2024;**Period size**– Month,**Metric**– Casino NGR.

The choice of grouping depends on your analysis goals and the length of the period being analyzed. For shorter periods, grouping by day is more appropriate, while for longer periods, such as months, grouping by month is recommended.