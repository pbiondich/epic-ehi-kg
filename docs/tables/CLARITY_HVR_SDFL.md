# CLARITY_HVR_SDFL

> This table contains the audit history of the Soft delete/Record status (SDFL) flag of the verification records.

**Primary key:** `VERIFY_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERIFY_ID` | NUMERIC | PK FK→ | The unique ID of the verification record |
| 2 | `LINE` | INTEGER | PK | This column holds the line number corresponding to the line of the edit. Each edit's details (instant, user id and action) associated with the verification record will be stored on a separate line. |
| 3 | `SDFL_EDIT_INSTANT` | DATETIME (Attached) |  | The instant the verification record was edited. |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | The unique ID of the user who edited the verification record. |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | The category value representing the action which the user performed on the verification record. This value indicated whether the user deleted or hid the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERIFY_ID` | [CLARITY_HVR](CLARITY_HVR.md) | sole_pk | high |

