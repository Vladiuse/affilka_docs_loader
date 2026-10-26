You can reach this page via the **/casino/users** link.

On this page you can view, manage, create affiliate program operators. You can filter and find Operators by their IDs, Names, Roles, Emails as well as their status – Blocked or Active.

**Please, note** that SuperOperators with full access to the Operator Interface can only be added by the Affilka team. Only SuperOperators with a special role can edit other Operators.

Only ordinary operators can be created in Affilka by SuperOperators. **Ordinary Operators** can only see **partners they are assigned as dedicated operators** **to**. 

To create them, please click the **“New”** button on the “Operators” page. 

1. Fill in all the information required:

Full name 

Email 

Roles (should be pre-created on casino/roles page) 

2. Additionally, you can add operator contact information, such as:

Email

Phone

Microsoft Teams 

Telegram

In the bottom of the page you can assign **all brands visibility for the operator or to the specific ones only**. Please tick the necessary checkbox.

To view operator details, press on their ID.

On a detailed Operator page you will see their ID, email, statistic token feed (which you can expire if you do not want the Operator to have access to the statistics feed in JSON/XML), name, role, whether they are blocked or active, when they were created/updated, the date/time of their last sign in, their sign in count, whether locked due to failed login attempts or not, whether 2fa is enabled on their account. You can also see their contact details.

At the top of the page you will find 4 links: media, commissions, landings and partners.

- **Media**: here you can assign dedicated media to an operator. You can assign Media in “Dedicated” state only to those operators who have no "Media" permissions in their Role, otherwise all media in all states will be available to them.
- **Landings**: here you can assign dedicated landings to an operator. You can assign Landings in “Dedicated” state only to those operators who have no "Landings" permissions in their Role, otherwise all landings in all states will be available to them.
- **Commissions**: here you can assign commissions to an operator. You can assign Commissions only to those operators who have no "Commissions" permissions in their Role, otherwise all commissions will be available to them.
- **Partners**: by clicking on this link, you will be taken to- **/casino/partners**page filtered by this dedicated operator in question. If there are no partners associated with this operator, then the list of partners will be empty.

If you click “**Edit**” next to the operator name or in the upper tabs list, you will be able to edit their Role, Status (Blocked/Active), and set default currency for reports.

Only SuperOperators with a special role can edit other Operators. As for editing other SuperOperators, they can only edit their status (Blocked/Active), set default currency for reports, and assign specific brands to operators.

During operator editing, you can select the default currency that will be used in Partner Statistics and in Quick stats/Quick charts on the Dashboard. After you set it, all values in the specified sections will be shown in the selected currency by default.

**In order for the setting to be applied:**

- Click on the dropdown
- Choose currency
- Press “Submit”.

**NOTE!** The default currency setting only affects the currency in which reports and Quick stats/charts will be shown. Commissions, bills and payments are calculated in brands' base currencies.

Please keep in mind that "Report Favorites" templates overrides the "Default currency for reports" setting. This means that if USD is selected as the default currency, but the "Report Favorites" template was saved in EUR, then after the changes in the selected field are applied, the "Report Favorites" templates still will be shown in EUR. In order to change the currency in the "Report Favorites", you'll need to create a new template.

Assigned operators functionality builds a hierarchical system of operators.

The scheme involves creating a system which assigns one or more operators to another operator accountable for them. It gives a parent operator access to their assigned operators’ partners’ data and statistics.

Meanwhile, the parent operator could also be an assigned operator of another parent operator. 

Overall, it builds a management pyramid.

**Example: **

Operator A is a parent operator of operators B and C. Operator A has access to B and C operators partners. 

Operator D is a parent operator of A. Operator D has access to A, B and C operators partners. 

**IMPORTANT! **

The scheme is not applicable to **Superoperators**. If one of the operators in the hierarchy gets a Superoperator role, all Assigned operators will be unassigned.

**ASSIGNED OPERATOR ACTIONS.**

To assign an operator:

- Open the detailed page of an operator you would like to be a parent operator.
- Find **“Assigned operators”**field (under Role field).
 If the field is empty, you’ll see “Assign” button.
- **Click Assign**- a selection field appears.
- Click the field to open the dropdown with available operators.
- Select one or more operators from the dropdown.
- Click Assign to confirm (or Cancel to discard)

When one or more operators are already assigned, you can find two buttons next to them: **Edit/Unassign**

**Edit:** replace that specific operator using the dropdown; click Assign to confirm or Cancel.**Unassign:** remove the connection between operators.

You can terminate an active session if you have identified a login from an unfamiliar device among your active sessions. After you terminate the session, the user who is currently logged in using this device will log out.

**To force the termination of user sessions for operators:**

- On the "Operators" page find the required operator
- Scroll down to the "Active sessions" section
- Press "Terminate" next to the session you wish to expire.

**To force the termination of user sessions for affiliates:**

- On the "List of Partners" page find the required affiliate
- Open "Users" tab and select required user
- Scroll down to the "Active sessions" section
- Press "Terminate" next to the session you wish to expire