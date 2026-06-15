# PR_EST_EXTERNAL_PROC

> This table contains procedure level information for external procedures.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTEXT_LINE` | INTEGER |  | Contains a pointer to the external context line which can be referenced via the table PR_EST_EXTERNAL_CXT. |
| 4 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `MODIFIERS` | VARCHAR |  | Procedure modifiers associated with the service for which the estimate was made. |
| 6 | `QUANTITY` | INTEGER |  | The procedure quantity associated with the estimated service. |
| 7 | `CHARGE_AMOUNT` | NUMERIC |  | The charge amount associated with the estimated service. |
| 8 | `ALLOWED_AMOUNT` | NUMERIC |  | The allowed amount associated with the estimated service. |
| 9 | `SELF_PAY_AMOUNT` | NUMERIC |  | The self-pay amount for the estimated service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

