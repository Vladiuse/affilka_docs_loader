Here you can view all the API docs you might need to work with the Affilka app. You can reach the docs via the API tab from the navigation menu.

This documentation is intended for creating a customized user website for your affiliate program with a unique design for the login and registration forms, as well as the operator and affiliate interfaces. Several requests from the Frontend API are actively used when customizing the affiliate landing page to connect the registration and login forms with the affiliate system. Specifically, these are the following requests: Registrations, Sessions, Info and Passwords, Current Casino, and Send Stag.

The Frontend API can also be used to export reports and lists that are not specified in the Customer Operator section, as well as those reports that can only be exported from the affiliate program in .csv format by downloading the file. However, this functionality is not officially supported. Affilka cannot be held responsible for the stability of data export through it.

Soon, the Customer API will be refined, and using the Frontend API for unintended purposes will become less relevant.

The documentation is divided into the following sections:

- Frontend Anonymous (for unauthorised users) – reachable via the **/casino/api_docs/client/anonymous/index.md**link
- Frontend Operator (for the Operator Interface) – reachable via the **/casino/api_docs/client/casino/index.md**link
- Frontend Partner (for the Affiliate Interface and affiliate registration/login/reset password forms) – reachable via the **/casino/api_docs/client/partner/index.md**link

To export this type of report, you need to:

- Perform a POST request for "Success session creation".
- After successful session creation, you can send GET requests to retrieve lists, using the documentation available in the api_docs/client/casino section.

Requests to perform any available actions in the operator interface (such as POST, PUT, DELETE) are executed additionally after performing the "Logged in Operator" GET request. Thus, the order of operation will be as follows:

- Perform a POST request for "Success session creation".
- Perform a GET request for "Logged in Operator":- Check the request URL (the domain to which the request is sent must be the BO domain of the affiliate program + the request path);
- Send the request by clicking the SEND button, and *ensure that a 200 response is received*.
- **In the response field, go to the Cookies section and copy the value of the CSRF-TOKEN parameter.**
 

Send the POST (PUT or DELETE) request specifying all necessary Headers indicated in API documentation and the token copied during the previous request in the Headers section as X-CSRF-TOKEN – value

*Please remember that the documentation may be changed or access to it may be restricted by the Affilka team.*

*In cases where you with your own frontend send us an empty value for the default_currency field, we will set the base fiat currency of the first created brand with the 'enabled' status by default. If there are no brands, EUR is set by default – the same applies to unverified brands.*

This documentation describes the process of connecting an affiliate landing page to the Affilka back office (BO).To implement login and registration requests, the Affilka BO domain must be located in the same domain zone as the landing page. For example:

- Affiliate landing page - affprogramexample.com
- Affiliate BO domain - backoffice.affprogramexample.com

Also, to connect the affiliate program landing page to the Affilka BO via API, the following is required:

- Configure CORS and cookies on the domain - this task is handled by the Affilka team.
- Ensure that the field settings in casino/settings/profile_fields correspond to the information that will be sent to Affilka via API during partner registration.
- Add the parameter withCredentials: true to the affiliate login request in Affilka, and upon a successful login, redirect the partner to /partner/dashboard.

**IMPORTANT! **If **manual partner verification is enabled** in the affiliate program, the partner will not be logged into Affilka after registration. At this stage, the partner can be informed on the affiliate landing page that their application is being processed and further instructions will be sent by email. If manual verification is not required, a redirect to /partner/dashboard is necessary. Also, note that making requests from localhost is incorrect.


The affiliate program landing page can also act as a sub-affiliate landing page, meaning master affiliates can refer subaffiliates who register for the affiliate program on the affiliate program's landing page. If the affiliate landing page is connected to the Affilka BO via API, sub-affiliate registration is implemented as follows:

- The Parent affiliate provides the sub-affiliate with a referral link for registration in the affiliate program. This link directs the player to the registration form located on the affiliate landing page.
- If a stag is generated in the URL, an immediate request to "Send valid stag" should be made – the response to this request will set a special cookie that must be sent with the sub-affiliate registration request.
- Meanwhile, the subaffiliate fills out the registration form and clicks the "Sign up" button (by this time, the response to the request from step 2 will have arrived), and then a request to create the partner must be sent.
- After successful registration, the subaffiliate logs into the Affilka BO, and the system automatically assigns them to the correct master affiliate.

This documentation is used to obtain statistical data from the Affilka affiliate program. Authorization is performed using a unique statistic token. Partners in the affiliate interface also have access to the Partner API, which allows statistical data to be exported via API. The documentation covers the following sections:

- **Balance Corrections:**positive and negative balance corrections that were applied to affiliate accounts. The same data is available in the operator interface on the /- **casino/balance_corrections**page- **.**
- **Bankroll Transactions**– a list of positive and negative transactions applied to your bankroll. The same data is available in the operator interface on the /casino/bankroll_transactions page.
- **Bills:**all bills issued to affiliates as a reward for their marketing activities. The same data is available in the operator interface on the /- **casino/bills**page- **.**
- **Campaigns**– a list of campaigns created by partners. The same data is available in the operator interface on the- **/casino/campaigns**page.
- **Partners:**a list of partners registered in your affiliate program. The same data is available in the operator interface on the /- **casino/partners**page- **.**
- **Payments:**all cash-outs requested by your affiliates. The same data is available in the operator interface on the /- **casino/payments**page- **.**
- **Players:**a list of players referred to your brands by your affiliates. The same data is available in the operator interface on the /- **casino/players**page- **.**
- **Reports:**your general partner statistics report that showcases all player activities as well as partner rewards. The same data is available in the operator interface on the /- **casino/report**page (Reports>Partner Statistics tab)
- **Requested report**– a list of reports requested in Affilka. This endpoint automatically exports queued reports (e.g., ZIP or XLSX) straight to your BI system. The same data is available in the operator interface on the- **/casino/requested_reports**page.
- **Traffic Reports:**the traffic report that allows you to view and analyse clicks in more detail. The same data is available in the operator interface on the /- **casino/traffic_report**page (Reports>Traffic Report tab)- **.**

To perform this type of request, the following steps must be followed:

The operator exporting the report from Affilka needs to go to the /casino/users section, navigate to their individual page, and copy the unique *Statistic Token* that will be used when sending the API request.

**IMPORTANT! **For full access to data, the operator must have the status of **Superoperator**. Ensure your account has this status to avoid restrictions when working with the API.

To export any available information from Affilka, **a GET type API request must be sent. **

The domain where the affiliate program's back office is located must be specified in the request URL. 

Next, place a "/" and specify the request path to the data location. The request path is indicated in the API documentation **in the "Route" and cURL** sections. After the "?" sign, specify the data that needs to be exported.

**IMPORTANT!  **All requests for exporting data from the affiliate program **must be sent to the domain of your affiliate program**, not the server on which it is located. In the Customer Operator section of the API documentation, the request URL is indicated as  https://youraffiliatesystemdomain.com - this means that the domain of your affiliate program must be specified in the URL string to send the API request.


Next, proceed to fill in the Headers field: 

The main parameters required for sending the request are described in the documentation in the "Headers" section - it is important to remember that they may be different for each request. It is also mandatory to specify the Authorization parameter, where the unique *Statistic Token* is indicated in the value.

All hidden parameters in the Headers are also necessary for the correct sending of the request.

As for your affiliates, they can also view Report API docs within the Affiliate Interface in the API tab in the navigation menu. They can rely on these docs to get their own performance reports within your affiliate program. The API authorisation is done via the unique statistic token assigned to an affiliate. Their unique statistic token can be found on the Account Info page. Affiliates have an option to expire statistic token for themselves or their teammates. Please, note that the statistic token is unique for each team member. Affiliates can also find their tokens in their XML/JSON report feed URLs.

This documentation is used for integrating casino and sportsbook platforms. The main goal of this API block is to transfer players and their activities from the casino platform to the affiliate program for detailed traffic analysis and interaction with Partners (affiliates) in the framework of campaign building, reward calculation, and other activities.

- To ensure the correct operation of the integration request, you must first create an environment.

On the environment settings page, enter the 4 main variables necessary for the correct operation of the environment and sending requests:

- **authorizationKey**- this is the API key that the Affilka team manager must provide to the operator's team.
- **secret_key**- this is the API secret, which the Affilka team manager must also provide to the operator's team.
- **host_api_v1**- this is the server domain where the operator's affiliate program is located—this can also be requested from the Affilka team manager.
- **authorizationSign**- this is the unique X-Authorization-Sign parameter for request authentication. It is important to note that it must be new for each request

2. Select the created environment to work with.

3. Next, proceed to create a request:

- Select the request type and enter the server domain in the URL where the request will be sent, as well as the path for this request – remember that this information can be found in the documentation in the affiliate program (in the API section) and from the Affilka team manager.
- Fill in the Headers block according to the example in the screenshot below:

The API key and X-Authorization-Sign can be obtained from the Environment information section (Environments) on the right. Next, go to the Body section: the request body is formed here.

Here you can specify the input format for the request body parameters, for example, specifying parameters as "Key-Value," JSON, XML, file submission, or even a plain text format.

5. Be sure to select the RAW input method for the data being sent in JSON format, and the request body can be copied from the API documentation and adjusted for the specific request. After filling in all the necessary blocks of the request, you need to click the SEND button.

6. Upon successful submission of the request, the **201 Created response** should be displayed (server responses are shown just below the request).

An HTTP response (status) code indicates whether a specific HTTP request has been successfully completed. The codes are grouped into 5 classes:

- *100 - 199:*Informational
- *200 - 299:*Successful
- *300 - 399:*Redirection
- *400 - 499:*Client Error
- *500 - 599:*Server Error

**400 Bad Request** - The server cannot process the request due to a syntax error in the request.

Possible reasons:

- Malformed URL.
- Incorrect data in the request body.
- Missing required parameters.

**401 Unauthorized** - This error indicates authorization issues. It usually occurs for the following reasons:

- Incorrectly entered API keys.
- Expired API keys.
- The operator is blocked or locked.
- The Statistic token is outdated/irrelevant.
- The domain from which the request is sent is incorrectly specified.
- The affiliate program's back office domain has additional verification from Cloudflare.

**403 Forbidden** - The server understands the request but refuses to fulfill it due to access restrictions.

Possible reasons:

- The user lacks access rights.
- Incorrectly entered API keys.
- Expired API keys.
- The operator is blocked or locked.
- The Statistic token is outdated/irrelevant.

**404 Not Found** - The server cannot find the requested resource.

Possible reasons:

- Incorrect URL (you must use your affiliate URL, not the example URL);
- Server routing error.

**422 Unprocessable Entity** - This error means the server understands the request but cannot process it due to problems with the transmitted data.

Possible reasons:

- Incorrect request structure;
- Missing mandatory fields;
- Invalid or conflicting data (e.g., incorrect date format or values outside the allowed range).
- Incorrect request syntax

**429 Too Many Requests** - The operator has sent too many requests in a short period. Possible reasons:

- Exceeding the API request limit;
- The server is defending against DDoS attacks or abuse.

**500 Internal Server Error** - The server encountered an unexpected error while processing the request. In this case, the request should be repeated, or repeated a little later.

**503 Service Unavailable** - The server is unavailable because it is overloaded or undergoing technical maintenance. In this case, you should contact your Affilka account manager for information on when the server will resume operation.