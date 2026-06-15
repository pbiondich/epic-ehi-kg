# POC_DME

> This table contains durable medical equipment (DME) information for the Plan of Care (POC) master file.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `POC_DME_TYPE_C_NAME` | VARCHAR | org | This item contains the DME type. |
| 4 | `POC_DME_START_DT` | DATETIME |  | This item contains the start date of episode DMEs as of the time the POC was saved. |
| 5 | `POC_DME_END_DT` | DATETIME |  | This item contains the end date of episode DMEs as of the time the POC was saved. |
| 6 | `POC_DME_CMT` | VARCHAR |  | This item contains the comments for episode DMEs as of the time the POC was saved. |
| 7 | `POC_DME_DELETED_YN` | VARCHAR |  | This item contains the deleted status for episode DMEs as of the time the POC was saved. |
| 8 | `HSPC_COVERED_C_NAME` | VARCHAR |  | The durable medical equipment - hospice coverage category ID for the plan of care. |
| 9 | `HSPC_NONCVRD_RSN_C_NAME` | VARCHAR | org | The durable medical equipment - hospice not covered reason category ID for the plan of care. |
| 10 | `HSPC_NONCVRD_RSN_C_CMT` | VARCHAR |  | The durable medical equipment - hospice not covered reason category comment for the plan of care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

