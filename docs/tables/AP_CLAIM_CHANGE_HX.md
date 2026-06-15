# AP_CLAIM_CHANGE_HX

> The AP_CLAIM_CHANGE_HX table contains the change history of an accounts payable claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_TIME` | DATETIME (Local) |  | The date and time of change to the claim. |
| 4 | `ACTION_C_NAME` | VARCHAR |  | The Change History Action category ID for the claim record. Indicates the item changed on the claim (i.e. workflow, workflow other status, etc.). |
| 5 | `CHANGE_HX_CMT` | VARCHAR |  | The comment associated with the change. |
| 6 | `CHANGE_HX_USER_ID` | VARCHAR |  | The unique ID of user making the change. |
| 7 | `CHANGE_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CHANGE_HX_CODEEDIT` | VARCHAR |  | The code edit reason associated with the change. |
| 9 | `CHANGE_HX_TX_ID` | NUMERIC |  | The transaction ID associated with change. |
| 10 | `CHANGE_HX_PREV_REC_OR_CAT` | VARCHAR |  | The record or category ID stored in the item before changes were made. This column will contain the translated record or category CID if CID translation is enabled. |
| 11 | `CHANGE_HX_NEW_REC_OR_CAT` | VARCHAR |  | The record or category ID stored in the item after changes were made. This column will contain the translated record or category CID if CID translation is enabled. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

