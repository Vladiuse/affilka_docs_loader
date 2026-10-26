This page can be reached via the **/casino/deep_links** link

**PLEASE NOTE!** Contact your Account Manager to enable the Dynamic Deep Linking feature and get access to the page. 

The **Deep Link Whitelist** is a safety control that limits where users can be redirected when a referral link includes a * dplnk* parameter.

Only URLs/domains that you add to the whitelist are available to be used as redirect endpoints.

The page shows a table of whitelisted items within your affiliate program, that are allowed to users to be redirected to. 

The list of whitelisted URLs/domains is divided into 2 tabs: active and archived.

- **Active:**contains all active items that are visible to your partners during a promo or campaign creation/editing.
- **Archived:**contains all archived items that are no longer available to your partners when they create or edit their promos and campaigns.

To create a landing, press **“Create”**

- Add a **name**of your deep link - Free text (for your internal reference).
- **Brand**- pick a brand from the dropdown.
- **Deep Link URL**- enter the base domain manually.
- Choose options in the checkboxes if necessary:

**“Allow subdomains”** - allows a redirect to any subdomain of the entered domain. E.g. subdomain.example.com”

**“Allow paths”** - allows a redirect to any URL path after the domain. E.g. /tournaments/vip”

**Default state** of the deep link, if neither of the checkbox options are chosen: 

**Allow subdomains:** false**Allow paths:** true

- Click **Submit**to save, or**Cancel**to discard.

**IMPORTANT! **

**www.**example.com is a subdomain of example.com. If you add only example.com with “Allow subdomains” = false, redirects to www.example.com will not be allowed.

To allow both example.com and www.example.com but no other subdomains, add two entries:

- example.com with “All subdomains” unticked.
- www.example.com with “All subdomains” unticked.

Archiving performs a deletion from the active whitelist.

Once archived:

- Redirects will no longer be allowed to that domain.
- You can create a new item with the same domain.
- You will not be able to unarchive a deep link

To archive an item, press **“Archive”** in the “Actions” column next to a deep link in the list and confirm in the popup.

Buttons: Confirm / Cancel

Edit a deep link.

To edit an item, press **“Edit”** in the “Actions” column next to a deep link in the list.

You are able to **edit the “Name” of an item only**.

If the URL itself was created incorrectly, archive it and create a new deep link.

**Partners using deep links must add the parameter ****dplnk=**** followed by the specific URL where a player should be redirected. ****Example: **

The referral link will look like this: __https://reflink.com/abcde?dplnk=https://www.example.com/events/event-id-12345__

Player in the end will redirected to: __https://www.example.com/events/event-id-12345__ is the redirect page

Unlike static embedded landing pages (which operators must update for every new event), deep links let affiliates, streamers, and tipsters craft event-specific destinations themselves. That means:

- Players land on timely, relevant, and personalized pages leading to higher conversion and engagement.
- Operators avoid the constant issue of maintaining thousands of landing pages.**Other parameters can be included with dplnk**

When a user is redirected to the URL defined in the *dplnk* parameter, our system **reorders** all parameters before sending the user to the destination page.

**Priority order**

- STAG (essential attribution)
- Deep-link-related parameters (parameters appended **to the deep-link URL**itself)
- All remaining parameters in their original order

If **duplicate parameters** exist, **all values** are forwarded.

To let the system correctly detect which parameters belong to the deep-link domain, place dplnk **at the very end** of the referral link and append deep-link parameters **after it**, starting with question mark “?”.

**Referral link**

`https://reflink.com/abcde?utm_campaign=123&clickid=12345&trsrc=adult&dplnk=https://www.example.com/events/event-id-12345?betcode=XYZ&clickid=67890`

- `betcode=XYZ&clickid=67890`are- **deep-link–related**because they appear after the deep-link domain.- **After redirect:**

`https://www.example.com/events/event-id-12345?stag=1111_111111111&betcode=XYZ&clickid=67890&utm_campaign=123&clickid=12345&trsrc=adult`

- stag - first position
- betcode=XYZ, clickid=67890 - second group (deep-link-related)
- utm_campaign=123, clickid=12345, trsrc=adult - remaining parameters

**The fallback mechanism is set to prevent traffic loss when deep link cannot be applied. **

The system will automatically redirect a player to promo’s landing page in the following cases:

- Deep-links setting is not enabled on your brand
- Deep-link URL is not whitelisted
- Deep-link URL is brand’s balancer domain
- *dplnk*parameter is empty