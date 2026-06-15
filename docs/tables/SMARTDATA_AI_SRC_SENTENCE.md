# SMARTDATA_AI_SRC_SENTENCE

> AI source sentence for a SmartData result.

**Primary key:** `HLV_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AI_SOURCE_SENTENCE` | VARCHAR |  | Source sentence for an HLV that was selected by an AI model. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

