# IMG_COMP_FILM_CHNG

> This stores comparison film change amounts. It relates to table IMG_COMP_FILMS and they can be joined using the ORDER_ID and LINE columns.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FILM_CHNG_AMT_C_NAME` | VARCHAR | org | Contains the amount of change from a comparison film. The actual film or chart record can be obtained by joining this table to IMG_COMP_FILMS using the ORDER_ID and LINE columns. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

