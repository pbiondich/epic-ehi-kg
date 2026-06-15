# CL_OTL_2

> This table contains information about order template records. It is a continuation of the CL_OTL table.

**Overflow of:** [CL_OTL](CL_OTL.md)  
**Primary key:** `OTL_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTL_ID` | VARCHAR | PK | The unique identifier (.1 item) for the template record. |
| 2 | `USES_TOD_IN_PAT_SIG_C_NAME` | VARCHAR |  | If the patient sig contains time of day indicators like "morning", "noon", "evening", or "bedtime". 1 if yes it does and I OTL 7661 will contain which times are included. 2 if no it doesn't, and that was determined either from an unsupported frequency or explicitly marking "no" when placing the composer. Null if the order was placed prior to this item, and therefore it isn't known. |
| 3 | `DENTAL_TEETH_NOTATION_C_NAME` | VARCHAR |  | The tooth notation system category ID for the order template record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

