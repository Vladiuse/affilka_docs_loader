Purpose

The previously existing subaffiliate module had one drawback: the "parent" affiliate reward was calculated based on their subaffiliates' bills within one brand only, despite the fact that several brands could have been presented in the affiliate program. This behavior was irrelevant for most clients who had 1+ brands presented within one affiliate program.

The purpose of this refactoring was to make subaffiliate rewards calculations take into account all the brands created within one affiliate program. This led to changes in previously created commissions, landings, media, campaigns and some minor interface changes.

During the subaffiliate system refactoring release we have automatically:

- Created new subaffiliate commissions based on the old commissions in which the setting *allow subaffiliates: true*was enabled, the settings of the old commission were taken into account when creating the new one. In the newly created commissions the word “Subaffiliate” was added in the beginning of the name and strategy.
- Created new subaffiliate campaigns and promos based on the old ones and linked new Subaffiliate commissions to them. Old promos that led to the subaffiliate landing page were transferred to new campaigns. The promo code for subaffiliate referral links remains unchanged, which allows your affiliates to bring subaffiliate traffic using the previously created referral links.
- Created balancer domain URL for subaffiliate commissions with a random balancer domain from the existing ones in your affiliate program. IF you need to change the subaffiliate balancer domain to another one, please contact your Account Manager.

During the subaffiliate system refactoring release the existing billing period remained unchanged, i.e. bills will be issued at the expected date for the expected reporting period.

If you have any questions regarding this block, don't hesitate to contact your Account Manager.

After the refactoring some minor interface changes took place. Here we provide the updated subaffiliate system creation flow. There are several steps:

1. First of all, you need to check if your affiliate program has subaffiliate landing and subaffiliate balancer domain, as they are used by affiliates during the subaffiliate campaign creation:

- Subaffiliate landing can be found on the “Landings” page *(/casino/landing)*by typing “subaffiliate” in “Name” filter.
- Subaffiliate balancer domain can be found during the commission creation *(/casino/commissions/new)*by ticking off “Subaffiliate” checkbox. You will see a dropdown with available balancer domains.

If you need to add a subaffiliate landing or a subaffiliate balancer domain, please contact your Account Manager.

2. Secondly, create a subaffiliate commission on “Commissions” page *(/casino/commissions/new)*, activate the Subaffiliate checkbox at the very bottom of the first block. By clicking on the checkbox, the usual field for selecting brands disappears, since subaffiliate commissions are taken out of the brand level and placed at the affiliate program level. After that you need to:

- Select the balancer domain to be used in the subaffiliate promos created based on this commission.
- If relevant, tick the Default checkbox; it is responsible for making the commission available to all partners, i.e. default.
- In the commission constructor, set the relevant Conditions and Rewards. The options in Conditions, Rewards, Modifiers are limited to those necessary for the subaffiliate commission.

3. In case the commission is Personal (not available to all partners by default), assign the created subaffiliate commission to the Partner. To assign a subaffiliate commission, you need to tick off the “Subaffiliate” checkbox, and you will see the list of commissions available for assignment.

4. Since the commission is assigned to the Partner, they can proceed with the campaign creation *(/partner/campaigns/new)*, by activating the “Subaffiliate” checkbox right under the “Campaign name”. The subaffiliate commission will not be tied to any specific brand, since subaffiliate commissions are taken out of the brand level and placed at the affiliate program level. Then the Partner needs to:

- Select a subaffiliate commission from the list of those available to them.
- Choose subaffiliate landings and media (landings and media for players are not available here).

5. Congratulations! Both the campaign and the promo are created. The Partner can take the referral link from the promo and start attracting subaffiliates. Also, on the campaign's detailed page, you can see that the “Brand” field is not filled in and the status is *Subaffiliate: true*.

 

**Other actions that can be performed when working with the subaffiliate module:**

- Adding a subaffiliate landing page *(/casino/landings/new)*:- Activate the Subaffiliate checkbox under the “Name” field. "Brand" selection field will be hidden.
- Under “Domain” field (you can only select domains related to the subaffiliate system).
- The rest of the settings remain unchanged. Please keep in mind that subaffiliate landing pages cannot be prioritized.
 
- Adding a subaffiliate media*(/casino/media/new)*:- Activate the Subaffiliate checkbox under the “Name” field. "Brand" selection field will be hidden.
- The rest of the settings remain unchanged.