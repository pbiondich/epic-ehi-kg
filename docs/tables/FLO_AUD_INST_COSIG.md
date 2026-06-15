# FLO_AUD_INST_COSIG

> This table stores the flowsheet audit instants that cosigners cosigned the data.

**Primary key:** `FSD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique ID of the flowsheet data record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUDIT_INST_COSIG_TM` | DATETIME (Local) |  | This is the audit trail item to store the instants the users co-signed the data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

