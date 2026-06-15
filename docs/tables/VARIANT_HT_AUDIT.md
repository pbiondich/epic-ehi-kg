# VARIANT_HT_AUDIT

> This table contains information about changes to this variant record done as a result of Happy Together variant auto-reconciliation.

**Primary key:** `VARIANT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier for the variant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. Each line corresponds to a happy together action taken on this variant record. |
| 3 | `RESULT_KEY` | VARCHAR |  | The Reference ID of the result data to which this variant is linked. This can be used to link to result information for the result to which this variant is linked, for example, by linking to DOCS_RCVD_RSLTS and DOCS_RCVD_RSLT_VAR_INFO. |
| 4 | `VAR_INFO_DOCUMENT_CSN_ID` | NUMERIC |  | The CSN of the source DXR from which this variant was reconciled |
| 5 | `HT_VAR_AUDIT_ACTION_C_NAME` | VARCHAR |  | The action that was performed during variant auto-reconciliation |
| 6 | `HT_VAR_AUDIT_UTC_DTTM` | DATETIME (UTC) |  | The time instant in UTC when the action was performed |
| 7 | `HT_VAR_AUDIT_LOCAL_DTTM` | DATETIME (Local) |  | The time instant in local time when the action was performed |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

