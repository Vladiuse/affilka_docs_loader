The Geo-Distributed Redirect feature intelligently routes users to destination landing pages via regional clusters closest to their location. This geo-optimised infrastructure minimises redirect times, increasing successful website visits from referral links. The feature is designed for seamless scalability across multiple regions and enhances performance globally, wherever needed.

With the new feature, we reduced redirect duration **by** **2.5 to 5 times**. At one of the regions, for example, extensive simulated tests showed a decrease in redirect times for users from 1.5 seconds to 300-500 milliseconds – this is one of the fastest responses available in the market. As a result, the feature implementation leads to a **3.5% to 7% growth** in users successfully reaching casino sites. This increase in site traffic, in turn, directly contributes to more registrations and deposits.

We would be delighted to help you implement this feature and boost your user engagement. If you are interested and want to enable this feature or have questions regarding this topic, please contact your Account Manager if you have any questions.

In order to enhance the affiliates' data security we have implemented the "Personal partner details" role for operators. Here's how it works:

- If an operator doesn't have access to the "Personal partner details" role: they don't see partners' "Tax identification number", "Address", "Phone" and partner user's "Email", "Nickname", "Contact email", "Full name", "Skype", "Telegram", "Security question", "Security answer". The related filters are removed (f.e. "Partner emails", "Skype", "Telegram" from the "List of partners" (/casino/partners) page). This data cannot be seen under the "Sign in as affiliate" feature, it is unavailable via CSV and Customer API.
- If an operator has access to the "Personal partner details" role: the listed changes above are disabled. The operator is able to see partner's personal data.

The "Personal partner details" role will be activated automatically to all users. If there is a need to (de-)activate these roles for the operators, please use the "Roles" page.

You can also limit which SuperOperators can have access to this role. Please contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

We've improved the existing "Personal player details" role for SuperOperator that enhances the security of player's personal data. SuperOperators without this role are not able to see the following data on the player's detailed page:

- Player's "Nickname" is removed "Overview" tab.
- Information about "email", "first_name", "last_name", "nickname" fields under the "Changes history" tab. The fields are masked.
 

We've implemented the "My Promos" page (/partner/promos) to streamline interaction with created promos. Affiliates can now easily locate their desired promos and perform quick actions, such as copying the referral link, adding a postback, or editing the promo. This page simplifies promo management and enhances efficiency for affiliates.

In addition, we've implemented the following filters on this page: Promo IDs, Promo names, Promo codes, Campaign IDs, Brands, Commission titles, Subaffiliate, Created at. Multiple input is supported.

 

We've made a revision of our existing filters and implemented new ones on different pages across our product to enhance usability of our product. Here is what was changed:

- **Operator Interface**- **Operators page (/casino/users)**
 Operator IDs, Names, Role IDs , Blocked - all filters are new, multiple input is supported.
- **Bills page**(/casino/bills)
 IDs - new filter, supports multiple input, filters by bill id.
 Strategies, Commission IDs, Partner IDs, Partner Emails - multiple input is supported.
- **Payments page**(/casino/payments)
 IDs - new filter, supports multiple input, filters by payment id.
 Partner IDs, Partner emails, Partner names, Payment systems - multiple input is supported & autosuggest is implemented.
 "Bill created at" and "Bill finished at" were renamed to "Created at" and "Processed at" respectively.
- **Commissions page**(/casino/commissions)
 Strategies, Schedule plans - multiple input is supported & autosuggest is implemented.
- **Promos page (/casino/promos)**
 Commission IDs - multiple input is supported.
- **News page (/casino/news)**
 Author IDs - autosuggest is implemented.
- **Landings page (/casino/landings)**
 Countries, Languages, Tags - multiple input is supported & autosuggest is implemented.
- **Media page (/casino/media)**
 Countries - multiple input is supported & autosuggest is implemented.
 
- **Partner Interface**- **My campaigns page (/partner/campaigns)**
 Promo IDs, Promo codes - multiple input is supported.
- **My postbacks page (/partner/postbacks)**
 Postback Actions, Postback URLs, Campaign IDs, Promo IDs, Postback Scope - all filters are new and all of them support multiple input.
- **Postbacks log page (/partner/postbacks_log)**
 Response codes - multiple input is supported.
- **Bills page (/partner/bills)**
 Brand, Fiat amount currency + Issued fiat amount + Fiat amount to be paid, Crypto amount currency + Issued coin amount + Coin amount to be paid, Created at, Processed at - all filters are new.
- **Events page (/partner/events)**
 Event IDs, Event action, Created at - all filters are new.
 

We've implemented a new, smooth way to apply filters: in addition to click on the "Filter" button, users can now simply press the "Enter" key after entering their filter criteria. This enhancement speeds up the filtering process, offering a faster, more intuitive product experience.

Here is the list of our small enhancements that should make your user experience with our product better.

- We've added a "Report" button to the player's and bill's detailed pages that should speed up the process of data analysis. By clicking on the button:- On the player's page operator will be redirected to the report with pre-filtered "Player IDs" filter and the default report columns are enabled.
- On the bill's page operator will be redirected to the report with pre-filtered "Data range", "Partner IDs",  "Brands", "Commission IDs", "Exchange rates date", "Convert all currencies" filters.
 For the "Data range", "Exchange rates date", "Convert all currencies" we use the data from the bill's "Reporting period start date-Reporting period end date", "Billed at", "Billing fiat currency" fields respectively. If the "Reporting period start date" field is empty on the bill's page, the report will use the first day of the month from the "Reporting period end date" field.
 
- We've eliminated the cases when the progress bar of a requested report is 100% without the ability to download the report.
- On the Partner statistics page (/casino(partner)/report) user can easily deselect all default columns by clicking on the "Deselect all" button under the "Columns" section.
- We've reduced the scale of our product interface by 10%, which has added more usable space for information display.
- The locale name under locale selector is now displayed in its native language.
- On the role creation page (/casino/roles/new):- the abilities are now displays in alphabetical order with the "... Process" roles on the first place;
- if the ability with "... proccess" name is enabled, the "... read" ability is ticked off automatically.
 
- We've disabled case sensitive search while assigning commission to the partner that should increase the usability of commission search via autosuggest. In addition, the commission autosuggest block width is limited to 400px.

We've implemented county, language, tag assignment for the "Landings" page(/casino/landings) and country assignment for the "Media" page(/casino/media). Using those components offers operators opportunities for better landings/media segmentations. To assign those items you need:

- Go the Landings or Media page.
- Click on the "Edit" button:
 - From Landings page you will be redirected to the landing's edit page;
- A particular medium can be edited within the same page.
 
- Fill in the fields using keyboard or autosuggest with values needed.
- Press "Submit" or "Save" button, depending on the page.

We've implemented the next API validations to prevent time-consuming investigates and enhance the consistency of data imports:

- Players activities import (api/v1/activity)- We've implemented a validation check on **null**`must be an integer`" error in the response body.**Validation comes into effect after the release.**
- We've implemented a validation on sending players activities that are older than 32 days. If such activities are sent, the response will be "422 Unprocessable Entity" with "`must be not older than 32 days`" error in the response body.**Validation comes into effect after the release.**
 In case there is a need to reexport activities for older periods due to data migrations or technical issues on your side,**please contact your Account Manager**.
- We've implemented a validation check for deposit dates (`processed_at`) to ensure they align with the specified activity period (`from-to`). If the deposit’s "`processed_at"`date falls outside the defined activity period, the response will be "422 Unprocessable Entity" with "`must be within 'from' - 'to' range`" error in the response body.
 Validation**doesn't**come into effect after release, we will enable it gradually for all our clients with prior approval.
- We've added a new logic for duplicated activities: activities will be considered duplicates and not imported if they fall within the time range of already existing activities for the same player and currency. **This logic comes into effect after the release.**
 F.e. if an activity for a player and currency for 12:00-13:00 04.10.2024 range already exists, and a casino send a new activity for the same player and currency for the 12:01-12:59 04.10.2024 range, we will identify this activity as duplicated and won't import. But if a casino send a new activity for the same player and currency for the 12:01-13:01 04.10.2024 range, we won't identify them as duplicated and will import it.
 
- We've implemented a validation check on 
- Players import (api/v1/players)- We've implemented a validation check for the email field. If an email is submitted as **""****(empty)**or**null**`must be filled`" error in the response body.**Validation comes into effect after the release.**
 
- We've implemented a validation check for the email field. If an email is submitted as 

- "CoinsPaid" payment system is now renamed to "Crypto". The system's withdrawal limits or partner's credentials remained unchanged.
- The "Stuck" tab is added to the "Payments" page.
- Pagination is added on the bill's detailed page under the "Player qualifications" section.
- Fail reason is now displayed for each not imported player on the detailed pages of "Players sync done/failed" events. Possible fail reasons are "visit_not_found" and "non_existing_bonus_code".
- Billing & Partner income performance is improved due to:- processing the bills in multiple streams;
- the cross-rates caching.
 
- The report performance was improved due to requests optimisation for the Database.
- The "Partner report" settings on the partner's settings detailed page are filled with the global ones by default.
- The tooltips for "Prequalified" and "Qualified" columns are added to the Partner Statistics (/casino/report).
- Commission constructor validations: the values "must be greater than 0"/"can't be blank" under Qualifiers/Rewards and values "can't be blank" under Conditions component.
- "ZAR" currency support for "Other" payment system is implemented.
- On the "Activities sync done/failed" events' pop-up we've implemented two new sections for not imported activities: "visit_not_found_activities" and "brand_mismatch_acitivities".
- We've improved the credentials form for the "Pix for Individuals" payment system by adding data autofill and helpful hints.
- BUG FIX: parameters (filters) which are indicated in the link to the "Postback logs" page are now applied on the page while redirect.
- BUG FIX: "Can't assign commission to brand" error is displayed on the commission's detailed page while enabling default commissions on the brand which already has default commission of the same strategy.
- BUG FIX: the inability to assign commissions to a partner in some cases is fixed.
- BUG FIX: usual operator with the "Commission Process" role are now able to create and edit subaffiliate commissions.
- BUG FIX: roles are now can be created via /casino/roles/new page.
- BUG FIX: operators are now able to edit themself and his personal data via /casino/users/:id/edit.