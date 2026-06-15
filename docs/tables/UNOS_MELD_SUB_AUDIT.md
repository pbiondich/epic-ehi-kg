# UNOS_MELD_SUB_AUDIT

> This table stores auditing information about the MELD/PELD lab submission workflow.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UNOS_MELDSUB_DATA` | VARCHAR |  | Audit item tracking MELD/PELD lab submissions via Epic. This item stores the submitted lab values. |
| 4 | `UNOS_MELDSUB_USER_ID` | VARCHAR |  | Audit item tracking MELD/PELD lab submissions via Epic. This item stores the submitting user. |
| 5 | `UNOS_MELDSUB_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `UNOS_MELDSUB_INST_UTC_DTTM` | DATETIME (UTC) |  | Audit item tracking MELD/PELD lab submissions via Epic. This item stores the submission instant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

