# GNOM_INTPRT_HT_AUDIT

> Happy Together audit information for a genomic interpretation.

**Primary key:** `GNOM_INTPRT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GNOM_INTPRT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interpretation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `HT_AUDIT_RESULT_KEY` | VARCHAR |  | The Reference ID of the result data to which this interpretation is linked. |
| 5 | `HT_AUDIT_DOCUMENT_CSN_ID` | NUMERIC |  | The CSN of the source DXR from which this interpretation was reconciled. |
| 6 | `HT_AUDIT_ACTION_C_NAME` | VARCHAR |  | The action that was performed during auto-reconciliation. |
| 7 | `HT_AUDIT_INST_UTC_DTTM` | DATETIME (UTC) |  | The time instant in UTC when the action was performed. |
| 8 | `HT_AUDIT_LOCAL_DTTM` | DATETIME (Local) |  | The time instant in local time when the action was performed. |
| 9 | `HT_AUDIT_TIME_ZONE_C_NAME` | VARCHAR |  | The time zone the action was performed in. Stores the system default time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GNOM_INTPRT_ID` | [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | sole_pk | high |

