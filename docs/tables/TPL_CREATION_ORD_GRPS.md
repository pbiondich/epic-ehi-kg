# TPL_CREATION_ORD_GRPS

> A list of the order groups used to create this treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_GROUP_ID_ORDERSET_NAME` | VARCHAR |  | The SmartGroup record name. This is different from the display name, which is stored in CL_OSQ_OT.DISPLAY_NAME. |
| 4 | `ORDER_GROUP_CSN` | NUMERIC |  | Contains the contact serial number (CSN) of order groups included in the protocol from which this treatment plan was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

