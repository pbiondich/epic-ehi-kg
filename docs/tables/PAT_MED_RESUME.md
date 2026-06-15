# PAT_MED_RESUME

> This table contains information on suspended medications on discharge. The status of the resumed order, reason for discontinuing or resuming the medication, along with the unique ID of the order is stored.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `MED_RESUME_ORD_ID` | NUMERIC |  | The unique ID of the medication order that is resumed or discontinued on discharge. |
| 4 | `MED_RESUME_STAT_C_NAME` | VARCHAR |  | The status of the suspended medication that is resumed on discharge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

