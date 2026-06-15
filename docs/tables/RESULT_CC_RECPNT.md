# RESULT_CC_RECPNT

> Stores information about recipients to be CCd on results for an orders only encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `RSLT_ORD_CC_RCP_MOD` | VARCHAR |  | Stores Result Orders section CC recipient modifier. |
| 5 | `RSLT_ORD_CC_RCP_INI` | VARCHAR |  | The record type of the CC'ed recipient for the result orders, for example SER for provider, DEP for department, etc. |
| 6 | `RSLT_ORD_CC_RCP_ID` | VARCHAR |  | The unique ID of the CC'ed recipient for the result orders. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

