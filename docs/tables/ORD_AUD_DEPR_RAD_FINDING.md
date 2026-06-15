# ORD_AUD_DEPR_RAD_FINDING

> The table contains that the audit information for the depreacted rad findings.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RAD_FINDINGS_IDS` | VARCHAR |  | This column stores auditing information in IDs pertaining to the image documentation functionality used by imaging physicians to document on this imaging study. This column contains data related to a legacy version of the image documentation activity and is no longer populated on imaging studies with image documentation. This column has values delimited by "^". The source item is located at ORD_OLD_RAD_FINDINGS. RAD_FINDING_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

