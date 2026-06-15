# HSP_TX_NAA_DETAIL

> This table contains the not allowed amount (NAA) calculation details for an insurance payment transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NAA_DTL_STEP` | VARCHAR |  | This column stores the calculation step to be shown in the not allowed amount calculation detail on the transaction detail form. It may include other characters for aid in display formatting. |
| 4 | `NAA_DTL_DESC` | VARCHAR |  | This column stores the description of a calculation step to be shown in the not allowed amount calculation detail on the transaction detail form. |
| 5 | `NAA_DTL_VAL` | VARCHAR |  | This column stores the value calculated or used in a calculation step to be shown in the not allowed amount calculation detail on the transaction detail form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

