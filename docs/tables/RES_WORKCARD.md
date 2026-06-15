# RES_WORKCARD

> This table contains information about workcard actions on microbiology results. Workcard actions are the building blocks used to create complete organism identification flows ("decision trees") for aiding the identification of organisms in microbiology tests.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WC_ACTION` | VARCHAR |  | The workcard action for the associated component. |
| 4 | `COMPONENT_ID` | NUMERIC | shared | Workcard component identifier |
| 5 | `COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 6 | `COMPONENT_RESULT` | VARCHAR |  | The workcard result for the associated component. |
| 7 | `COMPONENT_VALUE` | VARCHAR |  | The workcard value for the associated component. |
| 8 | `COMPONENT_CMT` | VARCHAR |  | The workcard comment for the associated component. |
| 9 | `COMPONENT_INST` | DATETIME (Local) |  | The workcard instant for the associated component. |
| 10 | `WORKCARD_BILL_SS` | VARCHAR |  | Values from column WORKCARD_USE_YN when this result was last processed by billing |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

