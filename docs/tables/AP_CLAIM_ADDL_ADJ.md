# AP_CLAIM_ADDL_ADJ

> Clarity table that stores the Additional Adjustments for a service.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_ADJ_SRC_TYPE_C_NAME` | VARCHAR |  | The type of positive adjustment that will be applied to the service's allowed amount. |
| 4 | `ADDL_ADJ_AMT` | NUMERIC |  | Stores the monetary additional adjustment amount that applies to the allowed amount of a service. |
| 5 | `ADDL_ADJ_OVR_AMT` | NUMERIC |  | Stores the override monetary amount for an additional adjustment that applies to the allowed amount of a service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

