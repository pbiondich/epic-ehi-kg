# MANUAL_LINK_EXT_ENC_EVENT

> This table holds lines for each external encounter that was manually linked to a claim coding record.

**Primary key:** `CODING_RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the coding record record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOC_ENC_EVENT_IDENT` | VARCHAR |  | The encounter event ID of external encounters manually linked to the claim for the purpose of coding. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

