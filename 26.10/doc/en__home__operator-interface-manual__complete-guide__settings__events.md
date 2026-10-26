You can reach this page via the **/casino/events** link.

Here you can track events that happened in your Affiliate Program and you can also subscribe to these events and receive email notifications once the event has occurred.

Email subscription is available right under the filter pane.

By clicking on the event ID in the table you’ll be able to see more details on the event (if such details are available).

The events available are:

- **2fa disabled:**whenever someone disables 2fa on your own account, this event will be logged and an automatic email notification will be sent to you. This case requires no subscription. It is also possible for the Operators to subscribe to receiving an email whenever such an event occurs on other Operator's or Affiliate's account.
- **2fa**- **enabled**: whenever someone enables 2fa, this event will be logged and an automatic email notification will be sent to those Operators on whose account 2fa is enabled. It is also possible for the Operators to subscribe to receiving an email whenever such an event occurs on other Operator's or Affiliate's account.
- **Balance correction made:**notifies you whenever an Operator changes affiliate account balance;
- **Bill approved:**notifies you whenever an Operator approves a Bill;
- **Bill cancelled:**notifies you whenever an Operator cancels a Bill;
- **Business health check alert:**notifies you on irregularities, positive or negative, in the activities and player imports compared to the previous period. At the moment we check the following metrics: registrations, FTDs, deposits count, and activities/players imports frequency. We compare the data received with the data from the previous week. If the data differs by 50% upward or downward, the “Business Health Check Alert” is triggered. The detailed event page contains the info on the performed business health checks.
- **CSV export requested:**notifies you whenever an Operator requests a CSV export from some page; The event contains the info on: who requested the export and when, what page the export was made from (payments, bills, partners, report, etc) and the details of the export, if any, in an event pop-up window (click on its id to see more).
- **Cashout requested:**notifies you whenever an Affiliate makes a cashout request;
- **Cashout accepted:**notifies you whenever a cashout request acquires "success" state (after an Operator accepts it and it is successfully processed within the payment system);
- **Cashout cancelled:**notifies you whenever an Affiliate or an Operator cancels a cashout request;
- **Cashout stuck:**notifies you whenever a cashout is stuck (e.g. you processed the payment, but for some reason it never acquired "success" state because there was some fault with the payment system and the cashout got stuck and never reached its destination);
- **Casino settings change:**notifies you whenever an Operator changes the global report visibility settings on the “All settings” > "Partner Report" page (/casino/settings/partner_report).
- **Comment created:**notifies you whenever an Affiliate or an Operator or a Superadmin adds a comment to some document/payment or partner page;
- **Commission**- **archived**: notifies you whenever an operator archives a commission.
- **Commission**- **assigned**: notifies you whenever an operator assigns a commission to a partner. The detailed event card contains the information on the commission which was assigned, the operator who assigned the commission, the time when the commission was assigned and the partner the commission was assigned to.
- **Commission**- **expired**: notifies you whenever a commission assigned to a partner expires. This happens either automatically by schedule or is done manually by some operator. The detailed event card contains the information on the commission which expired, the operator who expired the commission (if the commission expired automatically, the “Actor” will be “System”), the time when the commission expired and the partner associated with the commission.
- **Commission will expire:**notifies an operator 2 days prior to commission expiration. If you assigned a specific deal for your affiliate for a duration of 3 months, you will get an advance email notification that this commission will expire in 2 days for this affiliate. Thus you can schedule a new commission for them on time. Or do nothing;
- **Document approved:**notifies you whenever an Operator approves an Affiliate document;
- **Document archived:**notifies you whenever an Affiliate archives some document;
- **Document declined:**notifies you whenever an Operator denies document approval;
- **Document uploaded:**notifies you whenever an Affiliate uploads a document to their account;
- **Operator signed in as Partner:**notifies you whenever an Operator signed in as an Affiliate to act on their behalf;
- **Partner blocked:**notifies you whenever an Operator blocked some Affiliate account;
- **Partner settings change:**notifies you whenever an Operator changes the individual report visibility settings for a specific partner on the Partner Report Settings page (/casino/partners/:partner_id/settings/partner_report).
- **Partner unblocked:**notifies you whenever an Operator unblocked some Affiliate account;
- **Partner verified:**notifies you whenever an Operator verified some Affiliate account;
- **Payment method added:**notifies you whenever an Affiliate or an Operator acting on their behalf adds new payment details to their wallet; The event contains the info on what psp was changed, who changed it and when and how cashout details were changed.
- **Payment method deleted:**notifies you whenever an Affiliate or an Operator acting on their behalf deletes some previously used payment details from affiliate wallet. The event contains the info on what psp was deleted, who deleted it and when as well as the exact cashout data which was deleted.
- **Payment method verified:**notifies you whenever an Operator verifies an affiliate payment method and contains data about the affiliate and his payment method that was verified, as well as information about the Operator who performed the action.
- **Refund made:**if there is a refund of an affiliate cashout (e.g. affiliate's bank cannot accept the transaction), it returns to the affiliate balance, this event is logged on the Events page. On a detailed event page you can see the amount and the original transaction on which the refund was made.
- **Registration done:**notifies you whenever a new Affiliate registered with your Affiliate program.
- **Subaffiliate assigned:**notifies you whenever a sub-affiliate is attached to a parent affiliate.
- **Sync health check alert:**The Sync Health Check Alert runs every 2 hours at the 20th minute. It will trigger if, during the previous 2 hours, any import log on players or their activities has a status of- **Partial Success**,- **Failed**, or- **Failed Schema**. The event pop-up will include direct links to the specific Activities or Players import logs with the relevant statuses.

You can filter and find events by:

- **Event IDs:**the filter supports multiple values. You can type several IDs here separated by a comma, “Space” or “Enter” key. The filter will find all the events with the indicated IDs.
- **Event action:**the action type of the logged event (e.g. refund made, activities sync failed, etc).
- **Subject:**the subject/object of the action, the receiver of the action, something/someone affected by the action in question. You can choose the Subject type (e.g. Bill, Commission, Document, Partner, etc) and also indicate the specific Subject ID to narrow down your search.
- **Actor:**someone/something who performs the action. You can choose the Actor type (Administrator, Partner, Operator, System) and also indicate the specific Actor ID to narrow down your search.
- **Created at:**the date when a specific event happened (from…to date range).