# PRE_AR_CHG_DOC

> This table stores information about charges documented by providers. Note: temporary accounts receivables (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the charge session record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `FUNCTION_C_NAME` | VARCHAR | org | The function of the charge's documentation provider, such as performed or supervised. |
| 5 | `PROCEDURE_LIST` | VARCHAR |  | The list of line numbers associated with the procedures that the documentation physician provided the specified function for. Cross-reference using the PRE_AR_CHG table, TAR_ID and CHARGE_LINE columns for more information about these charges. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

