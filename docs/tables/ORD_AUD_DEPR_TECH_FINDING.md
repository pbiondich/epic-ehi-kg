# ORD_AUD_DEPR_TECH_FINDING

> This table contains the audit information for the deprecated tech findings.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TECH_FINDING_IDS` | VARCHAR |  | This column stores auditing information in IDs pertaining to the image documentation functionality used by imaging technologists to document on this imaging study. This column contains data related to a legacy version of the image documentation activity and is no longer populated on imaging studies with image documentation. This column has values delimited by "^". The source item is located at ORD_OLD_TECH_FINDINGS.TECH_FINDING_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

