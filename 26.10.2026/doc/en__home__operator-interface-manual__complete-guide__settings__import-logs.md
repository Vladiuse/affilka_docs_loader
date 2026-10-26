You can reach this page via the **/casino/import_logs** link or by navigating to the “Settings” > “Import logs” tab via the navigation menu.

Here you can track all players and activities imports from your iGaming brand(s) to your affiliate program via the Integration API.

This page presents a structured table listing all import attempts related to players and activities.

You can switch between activities/players import logs by clicking on the “Activities” or “Players” filter in the top right corner of the table.

Each row in the table represents a sync attempt and includes the following details:

- **Brand**– the brand associated with the import log (sync).
- **Status**– current import status:- **success:**all players/activities are imported successfully;
- **partial success:**only a part of players/activities are imported;
- **failed:**none of the players/activities are imported;
- **schema failed:**import request failed due to validation errors;
- **in progress:**players/activities are still being imported (in progress or queued);
- **empty:**import request contains no data (you can keep sending empty imports at regular intervals to confirm that the syncs are working).
 
- **Progress**– percentage of data import completion if the import is in progress.
- **From/To**(- *applicable only for activities imports*) – indicates the period to which activities are related. UTC timestamps are indicated here.
- **Activities/Players to import**– the total number of players/activities sent from your iGaming brand(s) to the affiliate program via the API.
- **Imported activities/players**– the total number of players/activities that were successfully imported into the affiliate program by Affilka.
- **Not imported activities/players**– the total number of players/activities that failed to import.
- **Created at**– the timestamp of when the import log was created.
- **Finished at**– the timestamp when the final status was assigned to the import log.

Quickly locate specific import logs using the filters on the left: "Status", "Brands", "Created at", "Finished at", "Period range" (from-to, you can also indicate specific timestamps in UTC here) filters. Use the tabs in the top-right corner to switch between **Activities** and **Players** views.

Every import log contains the information on the players and activities import attempts as well as any reasons of imports failure.

On each **Import Log page**, you can see exactly why certain players or activities weren’t imported. This visibility helps you quickly diagnose and resolve import issues.

| Reason | Applies to | Comment | 
|---|---|---|
| Not bound* | activities | The activity could not be linked to a player due to internal reasons. | 
| Visit not found | activities / players | The visit ID used in the import doesn’t exist in the Affilka Database. This is typically caused if you're using an invalid or non-existent stag visit (visit id). | 
| Brand mismatch | activities / players | The item you're trying to import is already linked to a different brand than the one specified in the current import. | 
| Currency invalid* | activities | The currency used for specific activities is blacklisted by Affilka (currently ony XTS). | 
| Other not imported* | activities / players | The item wasn’t imported due to other internal system reasons. | 
| Zero | activities | The activity contains only zero values in all fields. | 
| Duplicated | activities | The activity already exists for the same player, brand, period, and currency. | 
| Non-existing bonus code | players | The player wasn't imported because you tried to tie them to a non-existing bonus code. | 
| Tracktor error* | players | The system was unable to connect to the redirect click-tracking Affilka application (Tracktor), preventing the import. | 

* In any of these cases, please, contact your Account Manager for further assistance.

If an import log has a **"schema failed"** status, you’ll find validation errors in the **"Fail reason"** field displayed directly beneath the **"Status" **on the import's log detailed page.