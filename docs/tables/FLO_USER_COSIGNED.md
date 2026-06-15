# FLO_USER_COSIGNED

> Users that were either requested to cosign the data or did cosign the data.

**Primary key:** `FSD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The flowsheet data ID that this data corresponds to. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `USER_COSIGNED_ID` | VARCHAR |  | This item stores the networked user id of the user that cosigned the entered data. Multiple people could co-sign the same data. |
| 5 | `USER_COSIGNED_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

