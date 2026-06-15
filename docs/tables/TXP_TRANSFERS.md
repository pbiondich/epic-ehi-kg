# TXP_TRANSFERS

> Table of transfer of patient care from one transplant center to another.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRANSFER_TOFROM_C_NAME` | VARCHAR | org | Whether the transplant patient has transferred to or from another facility. |
| 4 | `TRANSFER_CENTER_C_NAME` | VARCHAR | org | The center where the patient's care was transferred to or from if the center is a member of the United Network of Organ Sharing. |
| 5 | `TRANSFER_CENTER_OTH` | VARCHAR |  | The center where the patient's care was transferred to or from if the center is not a member of the United Network of Organ Sharing. |
| 6 | `TRANSFER_PHONE` | VARCHAR |  | The transfer center's phone number. |
| 7 | `TRANSFER_FAX` | VARCHAR |  | The transfer center's fax number. |
| 8 | `TRANSFER_DATE` | DATETIME |  | The date of the transfer of patient care from one center to another. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

