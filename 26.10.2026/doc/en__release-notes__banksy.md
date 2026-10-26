Keeping your affiliates informed about the latest updates of your affiliate program can be one of the most important steps in building your affiliate partnership. 

We've added a news creation feature which should simplify the process of notifying your partners. 

In order to create news you need:

- Go to the "News" section in the Operator Interface (under the "Affiliate Program" tab).
- Click on the "Create" button on the News page (/casino/news).
- Fill in the form on the News creation page (all the fields are required):
 Name - the news name will be displayed only in the Operator Interface.
 Preview banner - the preview banner which will be reflected on the Affiliate's Dashboard, News list and News detailed page.*Recommended banner's aspect ratio is 16:9.*
 Header - the news header will be displayed in the Affiliate Interface.
 Content - a WYSIWYG text editor where you create the news content.
- Click on "Save as a draft" button in order to create news.

After the news creation there are 3 actions which can be performed on the news detailed page:

- Publish - by clicking this button the news will be published and can be seen by all your affiliates in their interfaces.
- Archive - by clicking on this button after the news is published, it will be deleted from the partner interface and can't be seen by affiliates. This action is irreversible.
- Edit - if you want to change or modify news you need to use this action. You can edit news even if the news is published the changes will be applied immediately.

Once the news is published, the affiliates can see it on the Affiliate Dashboard under the "Latest news" section and on the "News" list page (/partner/news) under the "Affiliate program" tab where they can see news header, banner and text preview. By clicking on the news an affiliate will be redirected to the news detailed page where they can read the main news content.

We've also implemented filters on the News list page (/casino/news) which should help you easily find a desired news.

The field where the news text will be entered directly is presented as a WYSIWYG text editor, meaning that the way the text is presented during its creation is the same way it will look in the Affiliate Interface on the news detailed page. You can find a text editor control panel just under "Content" field. With its help of which you can set text headings, alignments, colours, font styles, create lists, add links and upload images, etc. We believe that these settings will be enough for you to be able to create your very first news.

Due to the large number of landing pages, when creating a campaign or promotion, an affiliate may choose the wrong landing page, which can lead to traffic losses. 

We have added a feature that will prioritise the desired landing page and place it above the rest. 

To prioritise a landing you need to go the Edit page page of the particular landing, activate the "Priority landing" checkbox, press Submit button to apply settings. The setting can also be activated during the landing creation. Keep in mind that the "Priority landing" setting can be applied only for landings with "Shared" state. 

After applying the priority setting to the landing, it will be placed above other "Shared" landings during a campaign/promo creation. If a partner has “Personal” or “Dedicated” landing pages, they will be given a higher priority, than the "Shared" landing pages.

So the priority funnel during campaign/promo creation is: Personal or Dedicated landings - Shared landings with Priority flag - Shared landings without Priority flag.

Landings pages within the same priority are sorted by the date of their creation.

There is no limit for landing pages with the "Priority landing" setting applied, but we recommend that you have no more than 2-3 of those within one brand.

We have added "Pix for individuals" and "Pix for business" as **external** payment systems to Affilka settings. Those payment systems are not integrated into Affilka via an API. It is a manual payment system that allows you to easily collect affiliate payment details for "Pix" system  to perform payouts on your side.

What is the difference between "Pix for individuals" and "Pix for business"?

The first payment system for making transfers to individuals, and the second to corporate entities. In practice, the difference is in the data to be filled in. 

For the "Pix for individuals" an affiliate must enter CPF number, email, full name, Pix Key Type and Pix Key. For the "Pix for business" only CNPJ Number is required. 

When "Pix for individuals" or "Pix for business" are enabled, your affiliates will see it among the available payment options in their wallet on /partner/wallet page.

Contact your Account Manager to get this Payment System enabled for your affiliate program, or to get more details as to how external PSPs workflow is organised.

In the future, we expect that "Pix for individuals" will be integrated into Affilka via an API.

In order for you to export your players' information via the API, we have created a separate endpoint for the "Players" page, available via **/api/customer/v1/casino/players**. When making requests to the Customer API, you need to send your user’s unique statistic token in the authorisation header. Your unique statistic token can be found on your operator’s detailed page: /casino/users/:user_id page.

When getting a request for a list of players, the system takes into account all the existing roles that limit access to certain information of the player.

You can find new API documentation following the API tab - Customer Operator - Players section - click on "Precise filtered players list".

Before the affiliate program set-up, an operator may choose how admin fee will be calculated: eithier as a percent of Sportsbook GGR or as a percent of Sportsbook NGR. Once the setting is configured, it cannot be changed. Thus, all operators who currently working with admin fees calculated as a percent of Sportsbook NGR will continue to work this way. New operators have a chance to choose how admin fee will be calculated.

- "Partner Statistics" report will no longer be sent to the operator's or partner's email. It will be possible to download the report only from the requested reports page (/casino/requested_reports).
- New Field for Partner Registration form: Tax Identification number. The partner can indicate their identification number as a taxpayer in their country. This can be done during registration or while editing their profile later. You can enable the field in the "All settings" tab under the "Profile fields management" section.
- We've implemented a possibility to edit SuperOperator in the Operator Interface. Please keep in mind that SuperOperator can only be edited only by another SuperOperator. Your contact information can only be edited by yourself.
- "Failed" state is implemented for requested reports.Now if the report fails to generate, the page will show a "Failed" state on the report.
- "Sign in as Affiliate" action no longer affects "Last seen at" date on a partner user.
- Payments performed via payment systems "bank transfer", "other", "player_account", "webmoney", "capitalist", "Pix for individuals", "Pix for business", that are not handled automatically via API calls, will be automatically get "Success" status right after approval.
- "Processed at" column is added to the "Bills" page in the Affiliate Interface.