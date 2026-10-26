The Formula Constructor is a tool that allows you to build custom metrics directly within your "Partner Statistics" report. By calculating parameters inside Affilka, you eliminate the need for manual exports to Excel, Google Sheets, or external BI systems.

To get started, navigate to: **Affiliate Program → Formulas (or go to /casino/formulas)**.

1. Click the **"New" **button in the upper-right corner.

2. Complete the following fields:

- **Name**(Required) - The display name for the metric in your reports.
- **API Identifier**(Required) - Unique ID for API exports. Use lowercase a–z only (no spaces) and underscores.
- **Description**(Optional) - Context on why the formula was created and what it solves.
- **Formula Constructor**- The workspace where you build your calculation logic.

3. Click "Save as a Draft."

**IMPORTANT! **Formulas are created at the Affiliate Program level. Once created, they apply to all operators within that specific program.

 

The Formula Constructor works similarly to Excel logic, allowing you to combine raw metrics with mathematical operations.

- **Supported Metrics:**Includes all raw metrics from Partner Statistics (e.g., Visits, Registrations, FTDs, Deposits, Bets).

**NOTE! **Excludes Partner Income, reward-based columns, and Payable Casino NGR.

- **Operations:**Addition (+), subtraction (-), multiplication (×), and division (÷). Use brackets ( ) to define the order of operations.
- **Constants:**Use whole numbers (1, 2) or decimals (1.5, 3.75).- **Note:**These can't be added to or subtracted from monetary metrics (e.g., FTD Sum + 100).
 

**Publication: **Once your draft is ready, click "Publish" to make it available in Reports, Dashboards (Quick Stats/Charts), and the Customer API.

**Editing:** Formulas can be edited at any time. Changes take effect across all reports immediately.

**Archiving: **You can archive both Drafts and Published formulas.

**WARNING! **Unarchiving is not possible. Once archived, the metric is removed from all reports, dashboards, and API endpoints.