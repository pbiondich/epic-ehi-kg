# BDC_ASSOC_REMARK_CODES

> This table lists the remark codes associated with a Denial/Correspondence (BDC) record.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | The unique identifier for the denial/correspondence record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REMARK_CODE_ID` | VARCHAR |  | Remark codes associated with the denial reason code. |
| 4 | `REMARK_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

