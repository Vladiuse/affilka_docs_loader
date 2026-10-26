We are pleased to announce a significant update to our user management system, designed to provide granular control over brand-specific data and operations. This feature allows our users to restrict or grant access to specific brands for individual users, ensuring better data security and focused management.

 

**1. Granular Brand Permissions**

We have introduced a new "`Available brands"` section on the user's detailed page. This section enables operators to control brand data access to other operators.

- **Setting control:**Brand assignments for specific users can be configured on the user editing page (- `/casino/users/:id/edit`) using checkboxes and viewed on the user's detailed page under the "Brands" field as well as on the operators list.
- **Default State:**By default, all operators will have the- `All Brands`checkbox enabled upon release.
- **Interdependency:**If- `All Brands`is selected, individual brand checkboxes are automatically disabled. Conversely, selecting specific brands will automatically deactivate the- `All Brands`option.

**2. Impact on Data Visibility**

When an operator is restricted from a brand, all related entities and data points associated with that brand will be hidden or inaccessible to them. This includes, but is not limited to:

- **Reports & Statistics:**Data in Partner Statistics- `casino/report`, Traffic Report- `traffic_report`, Cohort Report- `cohort_report`, and Subaffiliate report- `subaffiliate_report`will only show information for accessible brands.
- **Partners:**Available landings, media, assigned/scheduled/archived commissions, balance corrections related to restricted brands will not be visible.
- **Financials:**Bills and balance corrections related to restricted brands will not be visible.
- **Marketing & Assets:**Media files, landing pages, landing domains, campaigns, and promos tied to restricted brands will be hidden.
- **Operations:**Access to bonus codes, postbacks, and events associated with restricted brands will not be visible.
- **Commissions:**Operators will still be able to view the full list of all created commissions (unless restricted by other permissions), but enabling or disabling a commission will only be possible for the brands assigned to them.

**Important Note:** Please keep in mind that brand access restrictions are currently enforced **ONLY** within the Operator Interface. They do not apply to the Partner Interface when utilizing the "Sign in as Affiliate" feature. We are already working on bringing this functionality to the Partner Interface in upcoming updates—stay tuned!

**3. Role-Based Control**

The ability to manage brand accessibility is restricted to users with the **"Brands Assign"** role. This ensures that only authorized team members can modify brand permissions for other operators.

This configuration is available on both the Role Creation (`/casino/roles/new`) and Role Editing (`/casino/roles/:id/edit`) pages. Here's how it works:

- If **"Brands Assign" role IS NOT enabled**, operators:- are not able to assign brands to other operators on the operator's detailed page.
- are not able to view assigned brands to other operators under the "Brands" column/field on the operator's list and operator's detailed page.
 

**Important Note:** Upon release, this role will be **granted exclusively to Superoperators** by default. Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

 

We are pleased to announce a significant upgrade to our payment system, designed to streamline document management and ensure compliance requirements are met efficiently. This update introduces the ability to link supporting documents directly to affiliate payments.

**Important Note: **Please keep in mind that payment document upload is not enabled for your payment systems by default. Please contact your Account Manager in order to enabled it.

 

**1. Payment Document Upload (Affiliate Interface)**

- **On Payment Creation:**Affiliate can now attach necessary documentation (e.g., invoices, agreements) directly during the payment request process. The flow is:- Click the **Withdraw**button to initiate a payment request.
- In the displayed pop-up, utilize the two new document fields:- **Select document:**Choose from previously uploaded files.
- **Upload document:**Drag and drop or browse to attach new files directly to this transaction.
 
- Click **Withdraw**to submit the form.
 
- Click the 
- **Post-Submission Upload:**If a payment is already in progress, affiliate can still add or manage documents on the specific payment detailed page. The flow is:- Navigate to the payment's detailed page by clicking on its **ID**.
- In the **Documents**section, click the**Add**button to attach new files.
- Fill in the required fields in the pop-up form.
- Click **Submit**to finalize and link the documents to the payment.
 
- Navigate to the payment's detailed page by clicking on its 

**2. New Payment Details Page (Affiliate Interface)**

- A dedicated **Payment Details page**is now available for every Affiliate by clicking on payment's "id" (`/partner/payments/:id`).
- This page provides a comprehensive overview of Affiliate payment, including transaction status, payment system details, and a new **Documents block**.
- Affiliate can view/delete/download all attached files, check their status, and manage document uploads directly from this page.

**3.Document Section On Payment Page (Operator Interface)**

- A new Document block is introduced on payment's detailed page (/`casino/payments/:id`).
- Operators can view, download all attached files by clicking on "Download" icon and check their status directly from this page.

**4. Flexible Configuration (System-wide)** Depending on the specific payment system requirements, document uploads will be configured in one of three ways:

- **None:**“Select document” & “Upload document” fields are hidden.
- **Optional:**Uploading documents is supported but not required.
- **Mandatory:**Document attachment is required to complete the payment request. If no document is attached, the system will prevent the payment creation.
 

- **Centralized Document Review:**Operators can now view all documents linked to specific payments directly within the operator interface.
- **Automatic Status Sync:**When an operator approves a payment, any documents associated with that payment will automatically transition to an "Approved" status.
 

We are excited to introduce a new feature that empowers clients to independently manage their balancer domains, ensuring greater control and flexibility over tracking links.

A new **Balancer Domains** page (`/casino/balancer_domains`) has been added to the operator interface, allowing operators to seamlessly replace active balancer domains. This self-service functionality is designed to help you act quickly during emergencies, such as domain blocks.

 

**1. Balancer Domains Management**

Head over to **Affiliate program ➔ Balancer domains** in the side menu. This dedicated page allows operators to seamlessly manage and replace active balancer domains right from the data table.

The flow is:

- Simply click the "Edit" button in the table to modify a specific domain.- Autosuggest: When changing a domain, an autosuggest consists of all active balancer domains on your affiliate program plus **backup balancer domains**.
 
- Autosuggest: When changing a domain, an autosuggest consists of all active balancer domains on your affiliate program plus 
- Click on "Save" button to apply changes.- A confirmation popup will appear, clearly stating the impact of the change (e.g., updating tracking links for a specific brand or sub-affiliate system) before you finalize the action.
 

Once a new domain is submitted, the system automatically updates all existing tracking links (or sub-affiliate referral links) in promos and commission associated with that domain.**Important Note:**Please let your Account Manager know if one of the balancer domains is no longer going to be used.

**2. Backup Balancer Domains**

To ensure operational continuity, we have introduced a Backup Balancer Domains.

- **Purpose:**Account managers can pre-add such domains upon operator’s request. These domains serve as a ready-to-use pool for quick replacements if your currently active domain is not working (f.e. blocked).
- **Validation:**All backup domains must follow a standard URL format (- `example.com`), be unique to the affiliate program.
 

To give you a better understanding of the replacement logic, here are two common scenarios (applying to brand balancer domains):

- **Scenario A: Replacing a current domain with a Backup Balancer Domain**- *Setup:*Your current active domain is- `test.com`. You have- `test1.com`saved in your Backup balancer domains.
- *Action:*You edit the active domain and replace- `test.com`with- `test1.com`. You confirm the change in the pop-up window.
- *Result:*All related commissions and promo materials will immediately start displaying the new- `test1.com`domain. Additionally,- `test1.com`will be removed from your Backup list and will no longer appear in the autosuggest dropdown for future replacements.
 
- **Scenario B: Replacing a domain with another domain already active on the brand**- *Setup:*You have two currently active balancer domains on the same brand:- `test.com`(ID 1) and- `test1.com`(ID 2).
- *Action:*You edit the first domain (ID 1) and replace- `test.com`with the already active- `test1.com`. You confirm the change in the pop-up window.
- *Result:*The tracking links and promo materials associated with ID 1 will update to show- `test1.com`. Visually, your interface will now display two identical domain names (- `test1.com`), but they will have different system IDs (ID 1 and ID 2).
 
 

We've added two new roles for managing this feature: "Balancer Domains Read" and "Balancer Domains Process". Here's how it works:

- If **"Balancer Domains Read"**and**"Balancer Domains Process"**roles**ARE NOT enabled**, operators:- are not able to view or edit balancer domains.
- don't see the "Balancer Domains" tab in the "Affiliate Program" section.
- don't have access to the "Balancer domains" page (`/casino/balancer_domains`).
 
- If **"Balancer Domains Read" IS enabled**and**"Balancer Domains Process" IS NOT enabled**: operator has access to the page and can view all information mentioned above**EXCEPT**editing balancer domains in the interface.
- If **"Balancer Domains Read"**and**"Balancer Domains Process" ARE enabled**: all information and actions mentioned above are available for operator.

If there is a need to (de-)activate these roles for the operators, please use the "Roles" page.**Important Note:** Upon release, this role will be **granted exclusively to Superoperators** by default. Please, contact your Account Manager if you want to limit the scope of action for some of your SuperOperators.

- **Security update:**To enhance account security, a mandatory confirmation pop-up has been added when disabling two-factor authentication (2FA) for a user.
- **Partner Statistics filter x General Manager:**"Dedicated operator emails" filter is now visible to regular operators who have other operators assigned to them.
- **Formula Constructor:**We have improved the cursor placement and interaction logic in the formula builder to ensure a more intuitive and predictable editing experience.
- **System Email Update:**The "Unlock Instructions" email has been migrated to our new design. All system emails have now been successfully updated.
 

- Commissions page (`/casino/commissions`)**:**
 - "Сurrency" filter is implemented which filters commissions by used currency in the commission constructor section.
- "Condition", "Qualifier", "Reward", and "Modifiers" filters are implemented to sort commissions by the specific entities used.
 - In addition, you can now filter by exact numerical criteria within these entities (e.g., finding qualifiers with more than 3 deposits or a Fixed reward exceeding 150 EUR).
- Important note: When filtering by currency-based metrics (such as deposit sums, casino NGR, etc.), you must first specify a currency in the "Commission currency" filter.
 
 
- Traffic Report (/casino/traffic_report):
- Traffic source list is updated with "SEO Exclusive bonus", "SEO Incentivized traffic", "SEO Special Promo", "SEO Deposit bonus".
- Deposit cache on the reassigned player is now resetting.
- BUG FIX: You can now upload several files on Media page (`/casino/media`).
- BUG FIX: Landing domain archiving pop-up now disappears after confirmation action.
- BUG FIX: Balancer corrections CSV are now exported with applied filters by reporting period and created at date.
- BUG FIX: The "Amount" field is now mandatory when editing a bill.
- BUG FIX: Subaffiliate report (`/casino/subaffiliate_report`) no longer resets columns and groupers order upon page refresh.
- BUG FIX: Tables are now supported for Affiliate Program Terms & Conditions.
- BUG FIX: Bill editing form is now scrollable if opened on screens with small resolution.
- BUG FIX: No longer possible to use "from_last_bill / from_last_issued_bill entities" with "period_from_registration" modifier while configuring commission.
- BUG FIX: Notification text message layout was fixed.