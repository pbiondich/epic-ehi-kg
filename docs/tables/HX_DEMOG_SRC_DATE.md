# HX_DEMOG_SRC_DATE

> Historical external system identifer bundles (ID Bundles) for the claim over time.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SRC_FILE_DATE` | DATETIME |  | The source file dates that this claim has previously been loaded with. Used to track the most recent historical External System Identifier Bundle (ID Bundle) for each source file date. |
| 4 | `HX_DEMOG_ID` | NUMERIC |  | The historical External System Identifier Bundles (ID Bundles) that this claim has previously been loaded with. Used to track the unique sets of demographics and identifiers that the claim was received with from the external system. This list represents a history of the ways in which the claim has previously been linked into External System Identifier Bundles (ID Bundles) for patient matching purposes. Only the most recent REQ per source file date is tracked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

