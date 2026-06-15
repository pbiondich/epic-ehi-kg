# ORD_AUD_PROTCL_ANSWERS

> This table contains audit information about the imaging protocol answers.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROTOCOL_ANS_IDS` | VARCHAR |  | This audit trail item stores the imaging protocol answers (HQA or HLV IDs). The values are delimited by "^". The source item is located at PROTOCOL_INFO.PROTOCOL_ANSWER_ID or ORDER_CONCEPT_INDEX.CONCEPT_HLV_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

