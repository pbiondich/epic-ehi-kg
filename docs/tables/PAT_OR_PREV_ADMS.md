# PAT_OR_PREV_ADMS

> This table stores contact serial numbers (CSNs) of the admission contacts to which this OR contact was linked and then later got unlinked.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | OR Contact Serial Number |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The community ID of the owner of this encounter. |
| 5 | `OLD_LINKED_CSNS` | NUMERIC |  | This column will store CSNs of the admission contacts to which this OR contact was linked and then later got unlinked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

