By default, all transactional emails to affiliates are sent via **Sendgrid account** (belongs to and is managed by AFFILKA). Such a setup renders email customisation and email marketing impossible. The Operator needs to set up an account with customer.io to be able to send marketing emails to partners and to customise email layouts as well as the content.

**!IMPORTANT! **If your iGaming brand is powered by the SOFTSWISS platform,please, note that this integration has nothing to do with your iGaming brand's back-office. You need to have either separate Customer.io accounts or different spaces within 1 account for your iGamin brand and affiliate program. Each of these accounts/spaces has their own integration keys, events, attributes and users. They do not overlap. A new space can be created by clicking on the selector with current space name in the top left corner of your customer.io account. Make sure that you're always in the correct space when editing emails or account info. 

1. When creating a workspace, specify the domain that will be used for your affiliate program and the sender’s address for sending the emails.

**Please NOTE! **The domain must be verified in customer.io for it to be set up correctly. To verify the domain, you need to copy the DNS-records found on the **Workspace Settings / Journey Settings / Email page / Sending domains tab**. Click ‘Verify domain’ and copy all MX, SPF, DKIM record data. Enter these data (type, hostname, value, priority) in the DNS settings of your domain. If your domain is administered by Affilka, provide your manager with the records. If the domain is administered by the SOFTSWISS platform, pass the records to the casino manager.

After the records are transferred, you need to wait for some time (from several hours to several days), then go to the **Workspace Settings / Journey Settings / Email page / Sending domains tab** again, and click on the ‘**Verify domain**’ button.

2. Once the domain is verified, you can start customizing your emails. First, you need to download the layouts (email template). Go to Customer.io, expand **‘Create content’ **in the left side menu, and select ‘**Email Layouts**’. On the page that opens, click ‘**Create layout**’ in the upper right corner. Set the name of the layout.

3. In the window that opens, select and delete all default code. Paste the code of your layout into the window.

4. Locate the part of the code where the email text will be placed and add {{content}}. Save your layout.

5. Now you can move on to customizing the email. Go to the **‘Campaigns’ **section. Click ‘**Create campaign**’ and name your first email. For convenience, we recommend naming your emails the same way the triggers are named. 

6. Select ‘**When someone performs an event**’ as the trigger for sending the email. Proceed to the next step.

7. In this step, type the trigger in the ‘**Trigger conditions**’ block. Leave all other conditions unchanged and proceed to the next step. 

8. In the ‘**Subscription preference**’ block, you need to select ‘**All subscribed and unsubscribed**’ in the drop-down menu. 

9. In the ‘**Goal**’ step, select the ‘**No goal**’ option. 

10. In the **‘Workflow’ **step, select the ‘Email’ block from the left side menu and drag that block to the ‘Drag your first block here’ area. 

11. Click on the added block and select ‘**Add Content**’  and in the left side menu, then choose the ‘**Code**’ option.

12. On the page that opens, expand the top menu where the sender's address is given. Here you need to add the subject line of the email and select a layout.

13. In the workspace, paste the text of the email. A preview of your email will be displayed on the right after clicking **“Save changes”** button. You can send a test email to yourself by clicking ‘**Send test…**’ button in “Actions” dropdown in the upper right corner. 

14. Make sure everything is set up correctly, save your changes and click on the ‘**Back to workflow**’ link in the top right corner.

15. Next, in the left menu of your email settings, be sure to change the status of the email in the ‘**SENDING BEHAVIOR**’ field to ‘**Send automatically**’. Without this setting, the email will not be sent.

16. Go to the final ‘**Review**’ step and in the upper right corner of the page, click ‘**Start Campaign**’.

17. Set up the emails for each of the triggers in the same manner.

To integrate customer.io. account with the affiliate program the Operator should provide the following integration data to their Account Manager:

**site id**

**API key**

This info is available within the corresponding customer.io account or space in the **"Integrations > Customer.io API"**** section.**

Customer Attributes, Events, and Event Attributes. Email Creation

Customer Attributes characterize partner users.

The following **partner user attributes** are sent to Customer.io:

| 
 | 
 | 
 | 
 | 
|---|---|---|---|
| `email` | john_doe@example.com | `partner_id` | 5437 | 
| `blocked` | true | `partner_tags` | ["test","kyc_verified","scandi"] | 
| `full_name` | John Doe | `receive_newsletter` | false | 
| `created_at` | 1575534068 | `partner_name` | John Doe Company Ltd | 
| `id` | PartnerUser_2305 | `nickname` | johndoenickname | 
| `locale` | en | `unsubscribe_token` | WdNLY22t8At9Z3PFRnG2Riwn | 

If you wish to use some customer attribute in an email, it should be preceded by the variable **customer**


Email Content ExampleDear {{customer.full_name}},

Text

If you wish to unsubscribe from receiving these newsletters, click the <a href="https://example.com/partner/unsubscribe-newsletter?unsubscribe_token={{customer.unsubscribe_token}}">Unsubscribe</a> link.


where https://example.com is your affiliate program **backend domain name.**

Events represent specific actions that happen to an affiliate account within the affiliate system. Event attributes are characteristic of specific events.

The following system events and event attributes are supported:

| 
 | 
 | 
 | 
|---|---|---|
| 
 
 | 
 
 | 1Psb9Rzh6ypRD9SkZk7r | 
| 
 
 | 
 
 | 99rHUT5AqVE3GRohygyN | 
| 
 
 | 
 
 | 4XY8Jeot9imaghL-34Td | 
| 
 
 | - | - | 
| 
 
 | - | - | 
| 
 
 | - | - | 
| 
 
 
 | 
 
 
 
 
 | 100 EUR 17/11/2020 09:12:03 Neteller 
 | 
| 
 
 
 | 
 
 
 
 
 | 100 EUR 17/11/2020 09:12:03 Neteller 
 | 
| 
 
 | 
 
 
 
 
 
 | 0.0001 BTC 100 EUR 17/11/2020 09:12:03 
 | 
| 
 
 
 | - | - | 
| 
 
 | - | - | 
| 
 
 | `event.сashout_data` | {"account_id"=>"A123456987", "area"=>"eea", "email"=>"example@softswiss.com"} | 
| `event.payment_method` | skrill | |
| 
 
 
 | `event.сashout_data` | {"account_id"=>"A123456987", "area"=>"eea", "email"=>"example@softswiss.com"} | 
| `event.payment_method` | skrill | |
| (will be sent when a refund is made to the affiliate by the payment system) | `event.payment.amount` | 100.00 | 
| `event.payment.currency` | EUR | |
| `payment.created_at` | 09/06/2022 09:22:06 | |
| `payment.id` | 31972 | |
| `event.payment.payment_system` | Bank transfer | |
| `event.refund.amount` | 90.00 | |
| `event.refund.currency` | EUR | |
| `event.refund.created_at` | 09/06/2022 11:16:06 | |
| `refund.id` | 31977 | |
| `refund.payment_system` | Bank transfer | 

**Several email examples for event triggered campaigns:**

**Event ****confirmation_instructions****:**


Email Content ExampleDear partner,

Please confirm your email address to complete your account setup by clicking the button below:

<a href="https://example.com/partner/confirmation?confirmation_token={{event.token}}">Confirm my email</a>


where https://example.com is your affiliate program **backend domain name.**

**Event ****created****:**


Email Content ExampleDear partner,

thanks for registering with our affiliate program. Please, confirm your account by following this link: <a href="https://example.com/partner/password/edit?token={{event.token}}">Confirm Account</a>


where https://example.com is your affiliate program **backend domain name.**

**Event ****reset_password_instructions****:**


Email Content ExampleDear partner,

someone has requested a link to change your password. You can change your password via this link: <a href="https://example.com/partner/password/edit?token={{event.token}}">Reset Password</a>

If you haven't requested password change, please, ignore this email.


where https://example.com is your affiliate program **backend domain name.**

**Event ****payment_accepted****:**


Email Content ExampleDear partner,


your payment via {{event.payment_system}} has been approved. The approved payment amount is {{event.amount}} {{event.currency}}. Date of payment request: {{event.created_at}}. You will see funds appear in your account shortly.

where **{{event.created_at}}** signifies the date when an affiliate requested their payment, not the date when it was approved.

**Event ****payment_canceled****:**


Email Content ExampleDear partner,


your payment request via {{event.payment_system}} was canceled. The canceled payment amount is {{event.amount}} {{event.currency}}. Date of payment request: {{event.created_at}}. Please, contact your affiliate manager for more information.

where** {{event.created_at}}** signifies the date when an affiliate requested their payment, not the date when it was canceled.

**Event ****bill_accepted****:**


Email Content ExampleDear partner,


Your commission was approved and is ready for cash out. The reward sum is: {{event.coin_amount}} {{event.coin_currency}} and {{event.fiat_amount}} {{event.fiat_currency}}. Reward was originally issued on the following date: {{event.created_at}}

You can request the cash out of the available funds by logging into your affiliate profile.

where **{{event.created_at}} **signifies the date when a bill was issued, not the date when it was approved.

**Event ****payment_method_added****:**


Email Content ExampleDear partner,

New payment method

was added to your wallet.{{event.payment_method}}Cashout data:

{{event.cashout_data}}

The cashout data is to be displayed un JSON format in quotation marks. If you would like to change the display, please turn to the following Customer.io guide.

**Event ****refund_made****:**


Email Content ExampleDear partner,

The refund in the amount of

was returned to your affiliate account balance on{{event.refund.amount}} {{event.refund.currency}}{{event.refund.created_. The original transaction viaat}}{{event.paymenton which the refund was made amounted to.payment_system}}. You can view your refunds here https://example.com/partner/payments?state=refund{{event.payment.amount}} {{event.payment.currency}}

where

- https://example.com is your affiliate program **backend domain name;**
- {{event.refund.amount}} and {{event.refund.currency}} are the amount and currency of the refund;
- {{event.refund.created_at}} is the timestamp of the refund;
- {{event.payment.payment_system}} is the name of the payment system via which the original cashout request was processed;
- {{event.payment.amount}} and {{event.payment.currency}} are the amount and currency of the original transaction.

The **subscribed/unsubscribed **state displayed on the user is a default attribute that belongs to the customer.io. 


The attribute **receive_newsletter**** true/false** is an attribute of the AFFILKA platform that we pass to customer.io. This attribute is stored separately from the default states of customer.io.


The  customer.io `subscribed` state will not change if an affiliate unsubscribes in his/her affiliate profile, via the registration form, or through the affiliate system link with unsubscribe token. 

The  customer.io `subscribed` state can be changed only if the user unsubscribes via the customer.io link: *https://links.customer.io/unsubscribe/en. *

**How the affiliates with the attribute ****receive_newsletter****  set as “false” can be excluded from the mailing list?**

1) In Customer. io, add our attribute (`receive_newsletter` false) to the Segment `unsubscribed`.


2) When sending newsletters, always specify that the newsletter should be sent to those users who are not in the unsubscribed segment.


View-only access to the Affilka test account where transactional emails are created:

**login:** support+customer@affilka.com**password:** Affilka100500

Please, note: the account is secured with additional authentication, so to log in to the account, you will need a log-in link. This link will be sent to the Affilka team group email. Please, ask your account manager to provide you with the link right after you try to log in. This link will only be valid for 15 minutes since the log-in attempt and this link only works on the same device and browser you started logging in on.


1. There may be a need to verify your domain by adding some DNS records. 

2. Check that the trigger is typed correct (no empty spaces before or after the trigger; correct word, etc).

3. Doublecheck that the campaign is started.

4. Ensure that the sending behaviour is set as "Send automatically".