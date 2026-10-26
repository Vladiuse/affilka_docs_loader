*  Бунгало, бунгало**  В ньому димно і сонячно**  Де ти була, де ти була**  Моя вовчиця**  І де ти вже випила?**  Та ти шо, та ти шо.**  Ти цілуєш перша.**  Тобі тут нравиться.*

In the Traffic Report, you can now break down clicks by Landings to which players get redirected. To do that, group the report by "Landing". As a result, you will see how many visits each Landing gained within a specified timeframe.

You can also filter the report by specific Landing IDs. The "Landing IDs" filter supports multiple values, and also automatically suggests the values based on the IDs or Landing URLs you start typing.

We have also added Landing IDs into CSV exports from the Traffic Report page. When you group the data by Landings and download a CSV file, the information on Landing IDs will be under the "foreign_landing_id" column name.

Traffic report is available to affiliate program operators via an API. It is available via the ** /api/customer/v1/casino/traffic_report **endpoint. When making requests to the Customer API, you need to send your user’s unique statistic token in the authorisation header (the principle is the same as with our main activities report).

You can find Traffic Report API documentation in the "API" section of the Operator Interface, under the "Customer Operator" tab.

When an affiliate bill amount is being disputed for some reason (e.g. fraud, incorrect commission settings, etc) , it is important to keep track of such bills and notify affiliates that their bill is being investigated. Specifically for such cases we have introduced a new bill state – "On hold".

You can put any pending bill "On hold". To do that, go to a detailed bill page and press the "Put on hold" button. As soon as you do that, the Bill will transition to an "On hold" status. While the bill is on hold, you cannot process it: neither approve the bill, nor cancel it.

As soon as you're finished with analysing the bill, commission, or affiliate activities that caused the hold, you can "Remove a Hold" by pressing on the same-name button on a detailed bill page, thus, unlocking the "Approve" and "Cancel" bill actions.

All bills that are currently "On hold" will appear under the "On hold" tab on the **/casino/bills** page. The affiliate will also see that the bill is put "On hold" within the affiliate interface on the** /partner/bills** page.

The action of putting a bill on hold or removing a hold from the bill, is available to only those operators who have a "Bills Process" role.

We've split the "Bills" role into two separate ones: "Bills Read" and "Bills Process". Here's how it works:

- If an operator doesn't have access to the "Bills Read" and "Bills Process" roles, they don't have access to the "Bills"(/casino/bills) page, they don't see the "Latest issued bills" section on the Operator's Dashboard, they aren't able to process Bills.
- If an operator has access to the "Bills Read" role, but doesn't have to the "Bills Process" role, it means that they have access to the "Bills"(/casino/bills) page, they see the "Latest issued bills" section on the Operator's Dashboard, but they are still not able to process bills.
- If an operator has access to both "Bills Read" and "Bills Process" roles, it means that they have access to the "Bills"(/casino/bills) page, they see the "Latest issued bills" section on the Operator's Dashboard and they are able to process bills.

The roles "Bills Read" & "Bills Process" will be activated automatically to all users which have previously had access to the "Bills" page. If there is a need to (de-)activate these roles for the operators, please use the "Roles" page.

You can also limit which SuperOperators can have access to this page by using the SuperOperator exclusions "Bills Read" and "Bills Process". Please, contact your account manager if you want to limit the scope of action for some of your SuperOperators.

The new column “Net Deposits” shows the difference between total deposits amount and total withdrawals amount of a player/group of players for a specified period of time. It is calculated according to the following formula: Net Deposits = Deposits - Cashouts.

You can enable this column for all of your affiliates by ticking off the corresponding checkboxes in the global report visibility settings or you can enable them for the selected affiliates only (available under the "Settings" tab on a detailed partner page).

Whenever an Operator verifies an affiliate payment method, this event is logged and can be accessed from the **/casino/events **page. You can filter and find the event by its type (Payment method verified) and subscribe to receive email notifications whenever such an event occurs. The event "Payment method verified" contains the info on the Partner whose payment method is verified, the Operator who performed the action as well as the actual cashout details which were verified.

You can see whether a player is verified on a detailed player page. The history of player attributes' changes is also reflected in the "Changes history tab". You can also filter players by "Verified" status (All, True, False) on the**/casino/players **page. Please, note, that the "Verified" player attribute is sent to Affilka by an iGaming platform within player imports/updates. Affilka does not assign "Verified" statuses by itself, we receive this data from you.

The Landing IDs filter allows you to filter the Campaigns and Promos in which this specific Landing is used. The filter supports multiple values, so you can indicate several Landing IDs here.

Whenever you click on Promos Count or Campaigns Count on the** /casino/landings **page, you will get redirected to the **/casino/promos** or **/casino/campaigns** page filtered by the Landing ID in question regardless of its URL. 

We track the dates when every commission was published. These dates are now displayed in the "Published at" column on the** /casino/commissions** page. You can also filter and find specific commissions that were published on a specific date or within a specific timeframe by using the filter "Published at" and indicated the required "From...to" dates.

You can filter and find commissions that have a specific admin fee percentage indicated in their settings. There are 3 separate filters on the** /casino/commissions **page responsible for that: Casino Admin fee, Sportsbook Admin fee, and Poker Admin fee. 

You can apply various actions in a batch to a selected list of commissions. Go to the **/casino/commissions **page, filter and tick off the commissions you want to apply batch actions to, press "Batch actions" and choose the corresponding action. You can publish and archive commissions in a batch, you can add tags to or remove tags from the selected list of commissions. To add/remove tags, select/type the tags you want to assign/remove in the pop-up window. 

The payment methods verification page contains 4 tabs based on payment methods statuses: all (includes all payment methods regardless of their status), unverified (waiting for verification), verified and rejected. By default, you will be prompted to the "Unverified" tab.

You can also filter and find the payment methods by Payment methods IDs, Partner IDs, Payment systems, and verification request date.

Previously the exchange rates date in the report favorites was absolute, meaning, that if you created a report favorite with a relative timeframe, the exchange rates date always remained fixed in time. For example: you created a report favorite with a relative period of "Last month" on March 1, 2023. When you call this report favorite in August 2023, you expect the report to show the data for July 2023. However, the exchange rates date stays fixed on March 1, 2023 when you created the report favourite.

We've changed this behaviour. Now the exchange rates date in the report favorites adapts to the period indicated in the date range filter (be it an absolute or a relative period), and always shows the next day following the specified date range (billing period).

- Traffic Report now shows 100 rows per page instead of 20.
- Traffic Report: "User Agent" autosuggest filter improved. Previously the autosuggest searched for the first letters in a word that you type, right now the User Agent filter searches all matches regardless of their position in a word.
- Traffic Report: "Reset" button behaviour fixed. When you press "Reset", the Traffic Report shows default report view.
- Traffic Report: obligatory grouping by period removed.
- 2fa code lifetime increased to 180 seconds. Now every user will have 180 seconds to fill in the 2fa code from the moment it was generated. We hope this will fix the issue with devices time sync many users are experiencing.
- Stuck payments reason is displayed on a detailed payment page.
- Commission Tags are displayed on the **/casino/commissions**page.
- System emails: affiliate system domain name displayed as sender instead of affilka and softswiss domains.
- Payments and Bills pages: checkboxes aren't displayed if batch actions are unavailable.
- "Approved at" column added into CSV export on the **/casino/payments**page.
- Brand name added into CSV export from the**/casino/report**page.
- Events: whenever an Operator acts on behalf of a Partner, they are logged as an actor behind every event.
- Bonus codes page contains the information on players who registered with this bonus code. By clicking on the players count, you will be redirected to the **/casino/players**page filtered by this bonus code.
- Brand filter on the**/casino/media**page improved. Previously the filter was pre-filled with some brand, now it shows all media of all brands. If you need to find media belonging to a specific brand, you need to choose this brand from a dropdown selector.
- "Forgiven fiat/crypto debt amount since previous bill" field behaviour fixed. Previously it showed accrued forgiven debts accumulated throughout the partner's lifetime, whereas now it shows only the amount forgiven from the previous bill.
- “From-To” period filters removed from report settings and are now always available to partners. If this filter wasn't enabled, it created problems with access to the reports. Reports without this filter are not functional. So we decided to make the filter available to all partners by default with no possibility to change that.
- "Your account is blocked" message is now shown upon login for blocked operators.
- New event in Partner Interface: Bill Approved. Affiliates are now notified when their Bills are approved. They can find the corresponding event on the /partner/events page. The event contains the information about the approved Bill and its amount. The partner also receives a corresponding email notification following the event.