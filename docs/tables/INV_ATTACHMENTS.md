# INV_ATTACHMENTS

> This table stores invoice-level attachment information.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INV_ATTACH_INV_NUM` | VARCHAR |  | Invoice number for the related group. |
| 4 | `INV_ATTACH_ROI_ID` | VARCHAR |  | The request for information record for the invoice. |
| 5 | `INV_ATTACHMENT_CONTROL_NUM` | VARCHAR |  | The attachment control number. |
| 6 | `INV_ATTACHMENT_GENERATED_YN` | VARCHAR |  | Identifies if an attachment was generated. |
| 7 | `INV_ATTACH_EDITED_YN` | VARCHAR |  | Identifies if an attachment was edited. |
| 8 | `INV_ATTACH_REMOVED_YN` | VARCHAR |  | Identifies if a user removed the attachment from a workqueue. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

