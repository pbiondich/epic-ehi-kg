# RT_ORDER_SITE_AND_TECHNQ

> Contains body sites and radiation therapy techniques planned to treat them.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RAD_THP_BODY_SITE_C_NAME` | VARCHAR |  | This item stores the body sites that are planned to be treated with radiation therapy. |
| 4 | `RAD_THP_BODY_SITE_LATERALITY_C_NAME` | VARCHAR |  | This item stores the laterality of the body site documented in item 38150. |
| 5 | `RAD_THP_TECHNIQUE_C_NAME` | VARCHAR |  | This item stores the radiation therapy techniques used to treat the associated body sites documented in item 38150. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

