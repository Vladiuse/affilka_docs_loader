You can reach this page via the **/casino/roles **link.

Here you can view and manage Roles assigned to various Operators.

In order to manage the actions permitted to specific operators the SuperOperator needs to create roles for such operators with the corresponding permissions. Here's how it's done:

1) Go to the **/casino/roles** and press "New".

2) Set the name for this role and choose permissions for the role out of the available ones:

- **API Docs**– allows the Operator to view Integration, Report, Frontend API documentation located within the Operator Interface.
- **Balance Corrections Read**- allows the Operator to view a history of balance adjustments for specific partners and retrieve this data via the Customer Operator API. The Balance Correction page (/casino/balance_corrections) is accessible.
- **Balance Corrections Process**- allows the Operator to both view and manually adjust a partner's balance. This is performed by clicking the "Change" button within the Accounts block on the partner’s detailed page.
- **Bankroll transactions**- allows the Operator to view Bankroll and its amount as well as Bankroll transactions page.
- **Balancer Domains Read**- allows the Operator to view balancer domains. The Balancer Domains tab within the Affiliate Program section and the corresponding page (/casino/balancer_domains) are accessible in read-only mode.
- **Balancer Domains Process**- allows the Operator to both view and manage balancer domains via the interface, granting full access to the Balancer Domains tab and page.
- **Bills Read**– allows the Operator to view bills, but not process them.
- **Bills Process**– allows the Operator to view, approve, cancel, put bills on hold or remove it.
- **Brands Assign**– allows the Operator to view and manage brand assignments for Casino Users. When enabled, this permission allows editing and viewing which specific brands are accessible to a particular affiliate program operator. The corresponding "brands assign" checkbox is available on the role creation and editing pages in the Operator interface.
- **Casino**- **Users**– allows the Operator to view other Affiliate Program Operators.
- **Commissions Read**– allows the Operator to view commissions and all the events related to Commissions. Without this permission, the Operator will not be able to see any sections related to commissions. This permission alone will not give the Operator the ability to assign/expire commissions for affiliates or to modify commissions (edit, publish, set tags, etc). If you want the Operator to be able to assign/expire/modify commissions, you need to grant them the abilities “Commissions Assign” and “Commissions Process” as well.
- **Commissions Assign**– allows the Operator to manage which operators can assign and expire commissions for affiliates. This permission alone will not give the Operator the ability to process commissions (edit, publish, set tags, etc). If you want the Operator to be able to modify commissions, you need to grant them the ability “Commissions Process” as well.
- **Commissions Process**– allows the Operator to view, create, edit, publish, archive, add tags to the commissions. Without this permission, the Operator will not be able to modify the commissions in any way. This permission will not give the Operator the ability to assign/expire commissions for affiliates. If you want the Operator to be able to assign and expire commissions, you need to grant them the ability “Commissions Assign” as well.
- **Data Export**– allows the Operator to export the data from all the pages in the Operator Interface via CSV, XML, JSON, API.
- **Deep Link Whitelist Read**– allows the Operator to view Deep Link Whitelist page
- **Deep Link Whitelist Process**– allows the Operator to view, create, edit, archive domains on Deep Link Whitelist page
- **Events**–allows the Operator to view the events tied to their Affiliates.
- **Interface**– allows the Operator to configure the colour theme of the Affiliate Program interface both for operators and affiliates.
- **Landings**– allows the Operator to view, create, edit, assign and archive all Landings in the Operator Interface. Without this permission, the Operator can only see their Dedicated Landings (=landings assigned to them by SuperOperators) and assign these landings to their affiliates.
- **Media**– allows the Operator to view and manage all Media in the Operator Interface. Involves media uploading, editing, archiving. Without this permission, the Operator will only be able to see their Dedicated Media (=media assigned to them by SuperOperators) and assign these media to their affiliates.
- **News Items Read**– allows the Operator to view the News: on the Dashboard, in the “News” section (/casino/news) as well as in the Affiliate Interface when signed in as an affiliate.
- **News Items Process**– allows the Operator to create, edit, publish and archive News.
- **Operator Assign Read**- allows the Operator to view Assigned operators list on other operators’ detailed page
- **Operator Assign Process**- allows the Operator to perform “Assign”, “Unassign” and “Edit” actions with the “Assigned operators” field (Operator detailed page)
- **Payment Methods Verification**– allows the Operator to verify the payment methods of affiliates on casino/payment_methods page.
- **Partner Report Settings**– allows the Operator to change individual report visibility settings for those partners that are tied to them. Users with such a role can view active report settings on a partner's detailed page in their Settings tab (/casino/partners/:id/settings/partner_report page), view all the events related to the report settings change on the /casino/events page and are able to modify report settings only individually for affiliates. Ordinary operators, even with this ability enabled, cannot change global report visibility settings which are applied to the whole affiliate program.
- **Partners**– allows the Operator to view, create and manage Partners, Partner Users and their profiles. The Operator will only see the affiliates whom they've invited via Referral Links or to whom they were attached as Dedicated Operators by the SuperOperator.
- **Personal partner details**– allows the Operator to view the Affiliate's personal data such as "Tax identification number", "Address", "Phone" as well as partner user's "Email", "Nickname", "Contact email", "Full name", "Skype", "Telegram", "Security question", "Security answer". If this permission is not assigned to the Operator, the data becomes unavailable, it's impossible to filter partners by these parameters, impossible to view them when signing in on behalf of the affiliate, and this data cannot be extracted in any form.
- **Payments Read**– allows the Operator to view payments, but not process them.
- **Payments Process**– allows the Operator to view, approve and cancel payments requested by their affiliates.
- **Players Read**– allows the Operator to view players invited by this Operator's Affiliates.
- **Player Reassign**– allows the Operator to reassign a player to a different partner/campaign/promo
- **Roles**– allows the Operator to create new roles and edit existing ones.
- **Subaffiliate assign**– allows the Operator to assign subaffiliates to the parent affiliate.

**Please, note! **If the ability with "... process" name is enabled, the "... read" ability will be enabled automatically – because it is impossible to grant somebody the right to processing something without granting them the right to view something.

3) Press “Submit”.