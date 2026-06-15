# GUARANTOR_SCANNED_DOCS

> Information about documents that have been scanned for this guarantor account.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCAN_FILE_NAME` | VARCHAR |  | The name of the scan file for this guarantor's document. |
| 4 | `SCAN_DOC_TYPE_C_NAME` | VARCHAR | org | The document type category ID for the guarantor's scanned document. |
| 5 | `SCAN_DOC_DESC` | VARCHAR |  | A description of the guarantor's scanned document. |
| 6 | `SCAN_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `DOC_SCAN_DATE` | DATETIME |  | The date when the guarantor's document was scanned. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

