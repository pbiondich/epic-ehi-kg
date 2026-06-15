# ORD_PRFLST_TRK

> Tracking info for orders coming from a preference list or order template. For Beacon, the column ORDER_TEMPLATE_ID is used, which is the unique ID of the order template in the patient's treatment plan used to create the order.

**Primary key:** `ORDER_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `ORDER_TEMPLATE_ID` | NUMERIC |  | The unique ID of the order template (OTP) in the patient's treatment plan that was used to create the order. |
| 3 | `ORDER_TMPLTE_OTL_I_ORDER_DESC` | VARCHAR |  | Description of the procedure. |
| 4 | `MOD_FROM_OTL_YN` | VARCHAR |  | Flag whether this order is modified from its order template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

