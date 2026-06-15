# UCL_TOOTH

> This table contains tooth numbers for a Universal Charge Line (UCL) record.

**Primary key:** `UCL_ID`, `TOOTH_LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique identifier for the charge line record. |
| 2 | `TOOTH_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TOOTH_NUM_C_NAME` | VARCHAR |  | The tooth number category ID for the universal charge line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

