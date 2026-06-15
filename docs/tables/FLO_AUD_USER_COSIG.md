# FLO_AUD_USER_COSIG

> Stores the audit values for the requested cosigners or user that did cosign the data.

**Primary key:** `FSD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique ID of the flowsheet data record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUDIT_USER_COSIG_ID` | VARCHAR |  | This is the audit trail item for storing the user ID of the users that co-signed the data. |
| 5 | `AUDIT_USER_COSIG_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

