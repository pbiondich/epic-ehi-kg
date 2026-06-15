# CLP_ATTACHMENTS

> This table stores claim-level attachment information.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTACHMENT_ROI_ID` | VARCHAR |  | The attachment record ID containing claim-level attachment information. |
| 4 | `ATTACHMENT_CONTROL_NUM` | VARCHAR |  | The attachment control number for the attachment. |
| 5 | `ATTACHMENT_GENERATED_YN` | VARCHAR |  | The indicator that the attachment was generated. |
| 6 | `ATTACH_REMOVED_YN` | VARCHAR |  | The indicator that the attachment was removed by a user from a workqueue. |
| 7 | `ATTACH_EDITED_YN` | VARCHAR |  | The indicator that the attachment was edited by a user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

