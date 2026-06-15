# ORDER_RES_APPTS

> This table stores appointments scheduled for a recommendation.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the finding record corresponding to this result. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APPT_LINK_MTHD_C_NAME` | VARCHAR |  | The method category ID for the method used to create the link between the recommendation and the appointment. A null value indicates that the link was created manually. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

