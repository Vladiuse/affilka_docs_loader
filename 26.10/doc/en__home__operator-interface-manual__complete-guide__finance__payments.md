This page can be reached via the **/casino/payments** link.

Here you can view and manage affiliate payments. Payments are represented by 2 types: cashouts and refunds.

- Cashouts are affiliate withdrawal requests. An affiliate can only request a cashout if there are enough funds on their account and if their payment request meets the min/max transactional limits set in the affiliate program (e.g. min 100 EUR and max 10000 EUR via Bank Transfer).
- Refunds represent refunded affiliate cashouts which were returned to the affiliate balance after processing (e.g. if an affiliate's bank wasn't able to accept the transaction). Affiliate refunds are displayed on the Payments page in the "Refunds" tab.

In order to manage Partner Payments, you need to have either full SuperOperator access without exclusions for Payments Processing or a role with “Payments process” permission enabled.

When you approve the payment, it is sent to the affiliate account in the payment system. *E.g. an affiliate requests a cashout via Skrill, after you approve it and the affiliate system receives a callback from Skrill that the transaction was a success, the payment lands in the affiliate’s Skrill account. *

If a specific payment system isn't integrated with Affilka, you will need to process such payments manually outside of the Affilka interface. You can approve these payments in your affiliate program, they will immediately receive “Success” state. However, since there is no API integration, you will need to log into your account with a selected payment system and process those affiliate payments you marked as Successful in Affilka manually.

You can approve and cancel payments in a batch by ticking off the checkboxes and applying the corresponding action, but we strongly recommend that you process them one by one and verify affiliate payment details each time. Especially, if payment details are used for the first time. You'll see an attention grabbing icon next to those payment requests where the cashout data is used for the first time and requires double-checking.

**Please, note!** If you're using Affilka merchant accounts to process payments to affiliates, you will be able to accept affiliate payments only if you have enough funds on your affiliate program bankroll. If some of your payment systems are rented via Affilka, while others are your own, only those cashouts requested via Affilka payment systems will affect the affiliate program bankroll. If you don't use Affilka merchant accounts, the affiliate program bankroll will be empty.

Payments can be exported in CSV.

At the bottom of Payments table, you will find the info on the total amounts of Payments and Payment Systems Commissions in money equivalent. This section contains both Page totals and Overall Totals. For instance, you can filter Payment requests created during a specific month and see the Total Payments Amount and Payment Systems Commissions Amount in fiat and crypto currencies for the whole month as well as specific Page Totals.

To approve/cancel payments in a batch, select the payments you want to process and press "Batchactions" at the top of the list. Choose the action ("Approve" or “Cancel”) and confirm/cancel your action in the pop-up window. You will also see the total transactions sum.

You can indicate a reason for cancelling a payment in a pop-up window that appears after you choose a payment and press "Cancel". The field is not obligatory, so you can leave it empty. All comments that you leave when cancelling payments will be visible to other operators on a detailed payment page in the comments section at the bottom.

Please, note that batch actions are applied to 1 page only. To process more payments, you need to move to next pages following the pagination trail.

You can filter the payments by:

- **IDs**: type Payment IDs you want to find. This filter supports multiple values.
- **Partner IDs**: type Partner Identifiers here. The filter will find payment requests initiated by specific partners. The filter supports multiple values.
- **Partner emails**: type partners' email addresses here. This filter supports multiple values. Once you start typing the email, you will see a hint with autosuggested emails in the dropdown selector.
- **Partner names:**type partners' names here. This filter supports multiple values. Once you start typing the name, you will see a hint with autosuggested names in the dropdown selector.
- **Partner tags:**this filter supports multiple values and an autosuggest feature. Start typing the name of the tag and it will appear in the dropdown selector. You can select several tags and the filter will find all payments requested by those partners who have any of the indicated tags. Use this filter to find and process payments of specific partners united by the same tags faster.
- **Dedicated operator emails**filter supports multiple values and an autosuggest feature. You can use the filter to search for payments of those affiliates for which dedicated operators are assigned. You can select several dedicated operators from the drop-down selector and filter the payments by them.
- **Currency and amount (from…to):**choose the currency and indicate payment amount in money equivalent. If you need to find all payment requests over, say, 1000 EUR, choose EUR in the “Currency” filter and type 1000 in the “Amount:from” filter.
- **Payment systems:**choose payment systems via which a cashout is requested. Supports multiple values.
- **Created at and Finished at dates:**indicate the date range when a payment was requested and/or processed.

With this sorting, you can select your mostly used filters on the Payments and thereby optimize the space of the page you are viewing.

In order to set this, please do the following:

- Point a cursor on one of the filters and you'll see the PIN icon in front of the filter name.
- Click on the active PIN icon.
- After that filter will be sorted down to the “Show more” section.
- To pin the filter back you will need to click on the non - active PIN icon of the filter.

**NOTE!** Settings are applied for each account individually.

You can view a detailed payment page by clicking on the payment id in the payments table.

This page contains detailed information about the payment. From here you can approve or cancel the payment request. You can indicate a reason for cancelling a payment in a pop-up window that appears after you choose a payment and press "Cancel". The field is not obligatory, so you can leave it empty. All comments that you leave when cancelling payments will be visible to other operators on a detailed payment page in the comments section at the bottom.

If it's a refund you're looking at, there are no actions associated with this payment type - you can only view it. The detailed refund page contains a link to the Original transaction (cashout) on which the Refund was made.

If an affiliate uses some payment details that were never used before, you will see a notification on top of the payment request. Before approving the payment, please, double-check whether these payment details really belong to this partner.

On a detailed payment page you will see the payment ID, the Partner who requested the payment, when it was requested and processed, whether it is successful, stuck (on the detailed payment page, in the stuck reason field, you can see the error that occurred), processing, pending or cancelled; the amount and currency of payment, the payment system via which the payment was requested as well as affiliate payment details.

If the payment was not registered in the payment system and received the stuck status, you can cancel it in the operator interface.To do this, please open the detailed payment page and click “Cancel”, the funds will reach the affiliate's balance. The error is also available on the stuck payment detailed page. If there is no “Cancel” button on the stuck payment, please inform your account manager in order to check it.

Located at the bottom of the view, this section allows operators to review verification files uploaded by the partner for this specific transaction.

Operators and partners can view the following details in the table:

- **Preview:**A visual thumbnail of the uploaded image or document.
- **Title:**The clickable file name (allows downloading or viewing the file in full size).
- **State:**The current review status of the specific document (e.g.,- *Pending*).
- **Created at:**The timestamp showing when the document was uploaded.
- **Actions:**Functional button allowing you to- **Download**

Once the payment is approved, you will also see the full commission amount charged by the payment system for processing this transaction. This commission amount will be subtracted from your affiliate program bankroll. The “Commission amount” field will always be filled in in all payments that go through Affilka merchants. If you rely on your own merchants to process payments to affiliates, the “Commission amount” field will be empty.

If the payment details have not been used before or the affiliate requests a cashout for the first time, the system will let you know about it through notifications in the operator interface. You can see them on the payments page, on the detailed payment page, and when accepting the payment, you will also be notified in a pop-up window that the payment details of this cashout need to be double-checked to make sure that everything is correct here.

We strongly recommend you to pay attention to the system notifications for safe withdrawal of funds.