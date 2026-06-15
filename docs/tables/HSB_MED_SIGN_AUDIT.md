# HSB_MED_SIGN_AUDIT

> Contains the list of all actions taken during the medication sign off process.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUD_MED_RVWR_ID` | VARCHAR |  | Contains the ID of the user who took the corresponding action (like signing off on the report) during the medication review process. |
| 4 | `AUD_MED_RVWR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `AUD_MED_RVW_STAT_C_NAME` | VARCHAR |  | Contains the action (such as updates sent or sign off received) that took place. |
| 6 | `AUD_ACTION_INS_DTTM` | DATETIME (UTC) |  | Contains the instant when this action occurred during the medication review process. |
| 7 | `AUD_MED_RVW_DEV_C_NAME` | VARCHAR | org | Stores the device used when the user signed off on the medications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

