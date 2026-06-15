# AUTH_REQUEST_REC_STAT_HX

> This table contains information about changes to the Chronicles record status/soft-delete flag (SDFL item) of the authorization request record. Only records that have had their record status changed will be included in this table.

**Primary key:** `AUTH_REQUEST_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier for the authorization request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SDFL_EDIT_DTTM` | DATETIME (Attached) |  | The date and time that the record status of the authorization request record was changed. |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | The unique identifier of the user who changed the authorization request record status. |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTI_C_NAME` | VARCHAR |  | The edit action category ID for the change of the authorization request record status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

