The **Subaffiliate Module** in Affilka is a powerful multi-tier marketing tool that allows your existing partners to act as parent affiliates. In addition to driving player traffic, they can recruit new affiliates to your platform, scaling your network organically and boosting your brand's reach with minimal operational overhead.

Before diving into the technical setup, let’s clarify the core roles and mechanics of this system:

**Parent Affiliate:** An existing partner in your program who refers new affiliates to your platform. In reward for expanding your network, the Parent Affiliate receives a commission based on the performance or earnings of the partners they brought in.

**Sub-Affiliate:** A new affiliate who registered on your platform via a unique referral link provided by a Parent Affiliate. Operationally, they function just like regular affiliates—driving player traffic and earning standard commissions—but they are permanently linked to their Parent Affiliate.

The **Operator** sets up a Sub-Affiliate landing page and a specific commission structure.

The **Parent Affiliate** creates a dedicated Sub-Affiliate campaign and shares the referral link.

A **potential partner** clicks the link, registers, and automatically becomes a **Subaffiliate** linked to that Parent Affiliate.

As the Sub-Affiliate generates traffic and earnings, the system automatically calculates and pays a referral reward to the Parent Affiliate.

This guide will walk you through setting up, optimizing, and managing your Sub-Affiliate ecosystem in Affilka.

To enable your Parent Affiliates to acquire Sub-Affiliates, you (the Operator) must first create a dedicated Sub-Affiliate campaign. A Sub-Affiliate campaign requires a specific commission structure and a landing page assigned to the Parent Affiliate.

A dedicated Sub-Affiliate Landing page is typically pre-created within your Affilka platform.

- **Location:**Navigate to casino/landings.
- **Verification:**Filter the Landings page by- **“Subaffiliate - Yes”**to find the correct landing.
 By default, this landing page directs potential Sub-Affiliates to the Affilka partner registratraion page:- `/partner/register`.
 

In case it is not pre-created, please go to **Affiliate program – Landing domains** (/casino/landing_domains). Click “New” button, tick the “Subaffiliate” checkbox and insert your affiliate system domain. Please refer to Landing domains page. 

 

After that, please go to **Affiliate program – Landings**. Refer to Landings guide for its creation. While creating a Subaffiliate landing you should insert `/partner/register` path. 

 

For detailed guidance on configuring the commission structure, please refer to the __Sub-Affiliate Commissions__ page in our wiki.

You can set a commission using one of the following models:

- **Sub-Affiliate Earnings Percentage:**The Parent Affiliate receives a specified percentage of the Sub-Affiliate's total earnings for the period.
- **Sub-Affiliate NGR Percentage:**The Parent Affiliate receives a specified percentage of the Sub-Affiliate's Net Gaming Revenue (NGR) for the period.


By default, Subaffiliate commissions are processed *after* the Subaffiliate’s own bill is finalized. To avoid long delays for your Parent Affiliates, follow this scheduling logic:

- **The Case:**If both the Subaffiliate and the Parent Affiliate have a "Monthly" schedule (e.g., bill issued on February 1st), the system will not have the Subaffiliate’s final earnings ready to pay the Parent Affiliate on that same day. This often results in the Parent Affiliate waiting until the- *next*month (March 1st) to get paid for February's work.
- **The Solution:**When setting up the- **Schedule Plan**for the Subaffiliate commission, select the- **"Pick days: 2"**option.

**Result:** If the Subaffiliate’s bill is generated on February 1st, the Parent Affiliate’s reward will be processed on **February 2nd**. This significantly speeds up the payout process for your partners.

 

Once the commission and landing page are assigned, partners can proceed to create the Sub-Affiliate campaign.

- During campaign creation, ensure partners tick the **"Subaffiliate" checkbox**. This enables them to select the dedicated Sub-Affiliate commission and landing from the available lists.
- Refer to the Wiki for detailed steps on creating a __Campaign that will target sub-affiliates__.
 

The generated campaign link can be shared by Parent Affiliates with potential Sub-Affiliates. When a potential Sub-Affiliate clicks this link, they are automatically redirected to the Affilka registration page and assigned to the Parent Affiliate.

- **Viewing Sub-Affiliates:**As the Operator, you can view a Parent Affiliate's Sub-Affiliates by opening the- __Subaffiliates Tab__on their detailed page.
- **Manual Assignment:**If a Sub-Affiliate registers without using a campaign link, you can manually assign a Parent Affiliate. Instructions for this process are available- __here__.
- **Manual Unassignment:**If a parent affiliate was linked incorrectly, you can now unassign them.- **Please note:**Unassigning a parent breaks the subaffiliate hierarchy chain (for example, detaching a 2nd-level subaffiliate in a 5-tier structure). As a result, subaffiliate commissions will not be calculated, and the corresponding bills will not be issued for the affected tiers.
 

Parent Affiliates can view their own list of Sub-Affiliates within their interface __here__.

 

To analyze and view Sub-Affiliate performance, use the __Subaffiliate Report__. This report is accessible only to the Operator.