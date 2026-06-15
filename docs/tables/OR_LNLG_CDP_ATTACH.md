# OR_LNLG_CDP_ATTACH

> This table contains the CDP Attachment Method information for the Surgical Log (ORL). CDP stands for Catheter, Drains, and Packings which has been replaced by LDAs (Lines, Drains, and Airways) post Summer 2009.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CDP_ATTACH_METHD_C_NAME` | VARCHAR | org | The attachment method of the CDP. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

