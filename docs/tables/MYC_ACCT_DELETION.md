# MYC_ACCT_DELETION

> Details about a MyChart account's impending deletion.

**Primary key:** `MYPT_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MYPT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the account record. |
| 2 | `DEL_ACCT_ON_DATE` | DATETIME |  | The date this MyChart account should be deleted. |
| 3 | `DEL_ACCT_DELETION_REASON_C_NAME` | VARCHAR |  | The reason that this MyChart account should be deleted. |
| 4 | `DEL_ACCT_LST_NOTICE_UTC_DTTM` | DATETIME (UTC) |  | The date/time we last notified the patient that we were going to delete their account. |
| 5 | `DEL_ACCT_ERROR_STATUS_C_NAME` | VARCHAR |  | This is a flag to indicate this account cannot be deleted. It will also show if the account has tried to be deleted, or if we've just checked whether or not it can. |
| 6 | `DEL_ACCT_DEL_REPORT_FILE` | VARCHAR |  | The file name/location of the report generated when we run the Patient Deletion Utility on a MyChart Account that will be deleted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

