# AP_CLM_PX_BENEFIT_ROUTING

> This table contains benefits routing information for adjudicated claim procedures.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REMITTANCE_CAT_C_NAME` | VARCHAR |  | The payment type of the benefit accumulation routing line. |
| 4 | `ROUTING_BEN_FUNCTION_C_NAME` | VARCHAR | org | The function of the benefit accumulation routing line. |
| 5 | `ROUTING_FUNCTION_ORDER` | INTEGER |  | The function order of the benefit accumulation routing line. |
| 6 | `ROUTING_AMOUNT` | NUMERIC |  | The amount of the benefit accumulation routing line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

