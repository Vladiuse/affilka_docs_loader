Here you can view and manage general affiliate program settings. The page is divided into 6 tabs: Profile Fields Management, Partner Reports, Available Locales, Dynamic Tags, Postbacks, System Management.

You can reach this page via the **/casino/settings/profile_fields** link.

As an Operator you can customise the fields which are required/optional/unnecessary during affiliate registration and which can be viewed/edited later on in the affiliate profile.

You can manage the following fields: Nickname, Full name, Address, Phone, Referral Source (how did affiliate find out about your affiliate program), Traffic sources (just a text field where they can indicate their traffic sources in a free format), Contact Email, Microsoft Teams account, Telegram account, Security Question and Security Answer, Receive Newsletters options, Language settings (an affiliate can type their language of communication and language will be sent to Customer.io as user attribute).

- **Hidden**– the field will not be visible at Registration. Please, note that you cannot hide “Receive newsletters” option from registration;
- **Optional**– the field will be visible at registration but isn’t required to be filled in. Set this status for “Received newsletters” option;
- **Required**– the field will be visible and required at registration.

- **View only**– the field will be visible in the affiliate profile but cannot be edited;
- **Editable can be blank**– the field will be visible in the affiliate profile; it can be edited and can be left blank;
- **Editable can’t be blank**– the field will be visible in the affiliate profile; it can be edited but cannot be left blank.

**Please, note!****  Email, company name and password/password confirmation are always required at registration and therefore must be submitted and cannot be edited.**

The Affiliate can reach their profile info by clicking on their email in the header of the Affiliate Interface (link **/partner/profile**).

You can reach this page via the **/casino/settings/partner_report** link.

Here you can manage 2 report types and their visibility:

To switch between the two report types, click on the corresponding report name in the filter switch in the top right corner of the page.

Here you can manage what all of your partners will see in their reports under the** /partner/report **section. 

For instance, if you want to make your reports totally transparent and show GGR, bonuses, additional deductions and admin fees to your affiliates – you can do this. These are global report visibility settings. If you want to be more or less transparent with specific partners, you can manage their individual report settings from their profile from the “Settings” tab. The individual report visibility settings always override the global ones.

To apply the settings, select the "Partner Reports" tab and choose the “Partner statistics” type. Tick off the checkboxes next to filters, column names and data groupings you want to make visible.

By default the following is visible in partner reports:

- Filters: from…to date range; brand ids; commission strategies; commission ids; campaign ids; promo ids; promo codes; exchange rates date and conversion currency (if you remove the checkboxes from currency conversion options, the affiliates won’t be able to see quick stats and quick charts on their dashboard);
- Columns: visits count; registrations count; first deposits count; deposits sum; Casino NGR; Poker rounds count, Poker rake sum, Poker NGR.
- Groupings: by brand, strategy, campaign, promo, day-week-month-year;

Once you check the required checkboxes, press “Submit”.

If you want to roll back to default settings, press “Reset to default” and “Submit”.


here you can manage whether your partners will see the Traffic report **/partner/traffic_report** and which parameters of the Traffic Report will be available to them. These are global traffic report visibility settings. If you want to be more or less transparent with specific partners, you can manage their individual traffic report settings from their profile from the “Settings” tab. The individual traffic report visibility settings always override the global ones.

To apply the settings, select the "Partner Reports" tab and choose the “Traffic report” type.

By default, the Traffic Report is enabled for all partners. If you want to switch it off completely, remove the “Enable traffic report” checkbox. If you want to keep it visible for all, keep the “Enable traffic report” switched on.

Tick off the checkboxes next to filters, column names and data groupings you want to make visible.

By default the following is visible in Traffic report:

- Filters: from…to date range; brand ids; campaign ids; promo ids; promo codes; traffic sources; Dynamic tag keys; Dynamic tag values*;*Visit IP; Visit countries.
- Columns: Unique clicks, Registrations, FTDs count, Clicks to Regs, Clicks to FTDs, Regs to FTDs.
- Groupings: by brand, campaign, promo, Visit IP, Visit country, Traffic source, day-week-month-year, Tags;

Once you check the required checkboxes, press “Submit”.

If you want to roll back to default settings, press “Reset to default” and “Submit”.

Here you can define what languages the affiliate interface will be localised into. Currently the Affiliate Interface is available in several languages with English being the default localisation.

To enable some locale, e.g. Russian, go to the** /casino/settings/locales** page, open the"Available Locales" tab ,and tick off the Russian locale. If you want to submit translations into any other language, please, contact your account manager to get the keys for translation. Please, note, that the translations you provide will be available to all operators powered by our Affiliate Platform.


These are Interface Localisations only. The language spoken by your affiliate, stored in the "Language" field for this partner and sent as "Language" attribute to customer.io may be different from the locale they've chosen their interface to be in.

The Affiliate can choose what locale the interface will be in on the login/signup page and inside the affiliate profile. The System will remember their preferences and will show the Affiliate Interface in the corresponding localisation.


This setting allows to configure dynamic tracking parameters accepted within affiliate tracking links and stored as player attributes. Let's say your affiliates are sending clickID and webID within their tracking links. These are affiliates' own custom parameters which they may later use to analyze their traffic in their tracking systems. If you add clickID and webIDon the **/casino/settings/tags **page in "Dynamic tags"tab these parameters will be remembered by our system and stored for the referred players. 

- go tothe**/casino/settings/tags**page in the Operator Interface and choose the "Dynamic Tags" tab
- press "New Dynamic Tag"and fill in the required fields: Tag (this is the KEY for the value which will be sent in the tracking link) and its description (for your own use).
- submit the changes

When editing the tag, you can only edit its description.

If you do not want to store a specific tag any longer, press "Archive" next to the tag.

After you archive a tag, our system will no longer accept this tag in the referral links for all newly registered players (but will remember the tags for the old players). You will be able to filter the reports by these tags but you won't be able to group the data in the reports by these tags any longer.

If a specific dynamic tag is not configured in the "Dynamic tags" tab on the **/casino/settings/tags** page, a player who follows a referral link with some custom affiliate parameter will not be attached to such a parameter and you will not have an opportunity to analyse the reports on this player with this parameter.

To bind players who had registered with certain tags before these tags were created, create a tag on the **/casino/settings/tags** page and on the detailed page of this tag press the "Migrate" button. It will bind the tag to all players who already registered and you will be able to analyse the stats on these players. The "Migrate" button will only be available once. All new registrations with this parameter following the tag creation will be attached to this tag. 


You can reach this page via the **/casino/settings/postbacks** link.

Here you can manage what postbacks are available to your affiliates. For instance, if you want to send registration postbacks only, you can tick off the “Registration” checkbox, and leave all other empty.

Once postbacks are turned off, they will no longer be available in the affiliate interface during postbacks creation, and, if they were previously set and used by partners, we will stop sending these postbacks.

If you want a specific affiliate to have access to more or fewer postback events then the rest of your affiliates have, you can go to individual postbacks visibility settings on a detailed partner page**/casino/partners/:partner_id/settings/postbacks**. These individual settings will always override the global ones.

By default, all postbacks are available to your affiliates when the affiliate program is set up.

Once you check the required checkboxes, press “Submit”.

If you want to roll back to the default settings, press “Reset to default” and “Submit”.

You can reach this page via the **/casino/settings/system_management** link. Here you can manage various settings pertaining to your affiliate program.

You can require affiliates to provide traffic source information when creating campaigns or promos. By enabling this feature, you make the “Traffic source” field mandatory at promo creation. This ensures your traffic is properly segmented, allowing for enhanced report analysis based on traffic sources.

To enable this feature you need to tick off the checkbox next to the “Traffic source” setting and click “Submit”.

Once this feature is enabled, your affiliates will encounter a "can't be blank" error message if a traffic source field is left empty during campaign or promo creation.