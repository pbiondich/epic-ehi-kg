# CLARITY_UCL_FRMCHG

> Stores the original charge from which a charge was reposted.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID of the charge line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REPOSTED_FRM_UCL_ID` | VARCHAR |  | The original charge from which this charge was reposted |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

