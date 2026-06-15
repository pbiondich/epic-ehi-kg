# CAL_COMM_HX_PAT_CSN

> Stores the history of patient contacts referenced by a communication (i.e. the history of CAL_REFERENCE_PAT.REF_PAT_CSN). Each GROUP_LINE corresponds to a line in CAL_COMM_HX for a COMM_ID.

**Primary key:** `COMM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier for the communication record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `REF_PAT_CSN` | NUMERIC | FK→ | Stores the unique identifier of a patient contact referenced by this communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REF_PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

