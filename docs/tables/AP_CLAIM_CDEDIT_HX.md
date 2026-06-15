# AP_CLAIM_CDEDIT_HX

> The AP_CLAIM_CODEEDIT_HX table contains the code edit history of an accounts payable claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | The line count of the change on the claim. |
| 3 | `EDIT_DATE` | DATETIME |  | The date that code editor was run on the claim. |
| 4 | `EDITOR_CLAIM_NUM` | VARCHAR |  | The ID of the claim sent to the code editor. |
| 5 | `EDIT_RESULT_C_NAME` | VARCHAR |  | Indicates the result of the code edit. |
| 6 | `RESPONSE_SUMMARY` | VARCHAR |  | The response summary of the code edit. |
| 7 | `RESPONSE_NOTE_ID` | VARCHAR |  | The unique ID of the response note for the code edit. |
| 8 | `EDIT_USER_ID` | VARCHAR |  | The unique ID of the user doing the code edit. |
| 9 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EDIT_DATETIME` | DATETIME (Local) |  | The code edit date and time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

