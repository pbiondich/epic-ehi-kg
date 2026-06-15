# HSP_CLP_CLAIM_HX

> This table contains the claim action histories for the claim print records associated with the hospital account/liability bucket.

**Primary key:** `CLAIM_PRINT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The ID of the claim record associated with a single hospital account. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date for the creation of the record in internal format. (There is only one contact date per claim print record.) |
| 3 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `CLM_ACTION_HIST_C_NAME` | VARCHAR |  | The type of claim action that was taken. |
| 5 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the hospital account with which this claim record is associated. |
| 6 | `CM_PHY_OWN_ID` | VARCHAR |  | ID of the physical deployment owner for this record. Physical owners will be where the data is hosted, either on the cross-over server or the owner deployment. |
| 7 | `CLM_HIST_USER_ID` | VARCHAR |  | The user ID who performed claim action for the claim record. |
| 8 | `CLM_HIST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `CLM_HIST_CMT_PTR` | VARCHAR |  | The pointer to the comments for the claim action for the claim record. |
| 10 | `CLM_HIST_DTTM` | DATETIME (Attached) |  | The date and time the claim action was performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

