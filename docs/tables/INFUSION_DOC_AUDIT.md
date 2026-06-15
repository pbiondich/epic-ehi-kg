# INFUSION_DOC_AUDIT

> This table contains an audit of infusion documentation.

**Primary key:** `ALERT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the med alert record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOC_FILING_USER_ID` | VARCHAR |  | Tracks the user that filed documentation for an infusion |
| 4 | `DOC_FILING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `DOC_FILED_UTC_DTTM` | DATETIME (UTC) |  | The instant documentation was saved. If the user is back-charting for 1100 and the current time is 1258, this will be 1258. |
| 6 | `DOC_BASED_ON_TM` | DATETIME (Local) |  | The user setting for the filing user. The instant the intervals are based on. |
| 7 | `DOC_PARTIAL_INTERVAL_SELECT_C_NAME` | VARCHAR | org | The user setting for the filing user. Last partial Interval Selected or Not Selected. |
| 8 | `DOC_DEFAULT_SELECTION_C_NAME` | VARCHAR | org | The user setting for the filing user. Documentation Select All or Select None. |
| 9 | `DOC_INTER_SEL` | INTEGER |  | The interval selection for the filing user when filing infusion documentation from Infusion Verify |
| 10 | `DOC_UTC_DTTM` | DATETIME (UTC) |  | The instant infusion documentation is saving at. If the user is back-charting for 1100 and the current time is 1258, this will be 1100. |
| 11 | `DOC_USER_EXPAND_ALL_SEL_YN` | VARCHAR |  | Indicates whether the user has chosen to expand all infusion groups by default in Infusion Verify. 'Y' or NULL indicates that all infusion groups are expanded by default. 'N' indicates that only infusion groups with warnings are expanded by default. NULL indicates that the user's profile is not configured to collapse infusion groups without warnings by default. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

