This page can be reached via the **/casino/media** link. 

It contains a list of all media (banners) which affiliates can use to promote your iGaming brands.

The list of media is divided into 2 tabs: active and archived.

- **Active**: contains all active media that are visible to your partners during a promo or campaign creation/editing.
- **Archived**: contains all archived media that are no longer available to your partners when they create or edit their promos and campaigns. For every archived media, you can view the date it was archived.

You can filter the media by:

- **Brands**. It's a brand with which the media is associated. The filter supports multiple values and an autosuggest feature. You can select several brands from the drop-down selector and filter the media by them.
- **Title**. It's a name assigned to the media. It's a text input field that supports partial search.
- **Language**. It's a language used within the media. The filter supports multiple values and an autosuggest feature. You can select several languages from the drop-down selector and filter the media by them.
- **State**. Represents one of the 3 media states: personal, dedicated, shared. The filter supports multiple values and an autosuggest feature. You can select several states from the drop-down selector and filter the media by them.
- **Subaffiliate**- **(All/Yes/No):**If a banner is designed to attract subaffiliates, choose “Yes”. If the banner isn't designed for subaffiliates but for players, choose “No”.
- **Country:**a specific country for which the banner is designed. The filter supports multiple values.
- **Content type.**Here you can choose one of the supported media formats: png, gif, jpeg. The filter supports multiple values and an autosuggest feature. You can select several content type options from the drop-down selector and filter the media by them.
- **Tag**. These are various tags that are assigned to the media. The filter supports multiple values and an autosuggest feature. You can select several tags from the drop-down selector and filter the media by them.
- **Orientation**. Here you can choose the orientation of the banner: horizontal, vertical, or square. The filter supports multiple values and an autosuggest feature. You can select several orientation options and filter the media by them.
- **Image width.**Here you can indicate the width of a banner in pixels. You can indicate a range of values.
- **Image height.**Here you can indicate the heights of a banner in pixels. You can indicate a range of values.


**Banner download** – a download icon is located to the right of each banner, allowing you to save the media for further use.

1) Press the “Add” button in the top right corner of the screen.

2) If the banner is designed to attract subaffiliates to your affiliate program, tick off the checkbox “Subaffiliate”. If the banner is designed to attract players to your iGaming brand, leave this setting empty.

3) Choose the brand the banner is created for. This setting cannot be used with “Subaffiliate” media. Subaffiliate media are created in the context of the whole affiliate program, not a brand.

4) Choose a media type you would like to upload. Media types supported: JPEG, PNG, GIF/HTML5

5)Drag and drop the file or click for file upload. Press “Submit”.

Please, note, that you can upload multiple media simultaneously by dragging and dropping them in the upload area of the window.

By default, the media you upload will acquire “Personal” status.

An HTML5 banner is a modern, interactive digital ad built with HTML, CSS, and JavaScript. It works like a mini web page, so it can display dynamic content — animations, video, and clickable elements, rather than being a static image. HTML5 banners are also responsive, meaning they adapt smoothly to desktop, tablet, and mobile devices.

HTML5 banners help improve campaign performance by loading faster. With flexible customization (offers, languages, layouts), you can easily adapt banners to any GEO or audience segment while keeping consistent performance across major ad networks and devices.

- Go to Media: /casino/media.
- Click Add.
- Fill in the form:- Audience: choose who the banner is for — Players or Subaffiliates.
- Brand: select the casino brand the banner belongs to.
- Media type: select HTML5.
- File: upload the .zip archive with the banner.
- Preview: upload a preview image (used in the banner list/card).
 
- Click Submit.

Once the banner is uploaded and access is granted, affiliates can select HTML5 Banner when creating a Campaign or Promo.

On the promo details page, the system provides a script that must be embedded on the website where the banner should appear.

Example:

*<script type="text/javascript" src="https://reflink.com/sources/promocode.js"></script>*

- A user opens a webpage where the script is embedded.
- The script sends a request to the system.
- The system returns JavaScript that inserts an iframe into the page.
- The iframe loads the HTML5 banner (the index.html page) and displays it to the user.
- The banner URL includes the*reflink=... parameter*so the banner can retrieve the referral link (e.g., inside the banner’s JavaScript code).

To pass dynamic parameters (for example, click_id or sub_id), append them to the script URL:

*<script type="text/javascript" src="https://reflink.com/sources/promocode.js?click_id=i1234ji&sub_id=13"></script>*

When the system generates the final JavaScript code, the reflink parameter will include the full referral link together with all appended parameters.

- Format: .zip
- Max file size: 1 MB
- The archive must contain index.html in the root (not inside a nested folder)

to edit media, press the “Edit” button next to the media in the media list. Here you will be able to indicate the country and the language of the media, choose a tag for the media out of the preconfigured tags or create a new custom tag for the media, and change the accessibility state for the uploaded banner.

- **Personal**– visible only to specific affiliates.
- **Shared**– visible to all affiliates.
- **Dedicated**– visible to specific Operators. Only Operators without any "Media" permissions can be assigned Dedicated Media otherwise all media in all states will be available to them

To archive media, press “Archive” next to the media you want to archive. Upon archiving, affiliates will no longer be able to use them to create new referral links. Archived media cannot be edited, they are not available for new campaigns, and they are not visible to new affiliates. Nevertheless, such media will continue to be functional in those referral links they were already used in.

For every archived media, you can view the date it was archived.