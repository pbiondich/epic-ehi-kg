# OR_CASE_VENDOR_INFO

> Case vendor special needs table.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CASE_VENDOR_REQ` | VARCHAR |  | This item stores vendor request information. |
| 4 | `CASE_VENDOR_NAME` | VARCHAR |  | This item stores the vendor name. |
| 5 | `CASE_VENDOR_DATE` | DATETIME |  | This item stores the date on which the vendor was contacted. |
| 6 | `CASE_VENDOR_ARRANGE` | VARCHAR |  | This item stores information about who made arrangements with the vendor. |
| 7 | `CASE_VENDOR_COMMENT` | VARCHAR |  | This item stores vendor comments. |
| 8 | `CASE_VENDOR_STAT_C_NAME` | VARCHAR | org | This item stores the status of the vendor request. |
| 9 | `CASE_VENDOR_NAME_C_NAME` | VARCHAR | org | This item stores the vendor name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

