# ARPB_CHG_ENTRY_DX

> The table lists all diagnoses on a charge entry session in which the charge was posted.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique internal ID of the transaction record representing this charge. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `DX_QUALIFIER_C_NAME` | VARCHAR | org | Qualifier for the diagnosis on this line. Indicates if diagnosis is: 1 - Active 2 - Acute 3 - Chronic 4 - Inactive 5 - Temporary |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

