# HSP_CLP_UB_OTH_BKT_TX

> This table contains information about charges pulled from buckets other than the one associated with the claim when creating UB claim lines in Hospital Billing.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLP_GRP_200_LN` | INTEGER |  | Stores the line number of the CLP 200 group. |
| 4 | `UB_OTH_BKT_HB_TX_ID` | NUMERIC |  | Stores the HTR IDs of the charges pulled from other buckets in the UB line group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

