# IVR_WEBLINKS

> This table displays the weblinks associated with variance (IVR) records.

**Primary key:** `VARIANCE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANCE_ID` | VARCHAR | PK FK→ | The unique identifier for the variance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WEBLINK_TEXT` | VARCHAR |  | The display text for the reference link used by this variance record. |
| 4 | `WEBLINK_ADDRESS` | VARCHAR |  | The reference link address used by this variance record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANCE_ID` | [VARIANCE](VARIANCE.md) | sole_pk | high |

