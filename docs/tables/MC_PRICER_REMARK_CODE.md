# MC_PRICER_REMARK_CODE

> Remittance advice remark codes (RARC) associated with the discount from billed to allowed amount based on Medicare pricing.

**Primary key:** `PRICER_MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the pricer message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MC_PRICER_REMARK_CODE` | VARCHAR |  | The remittance advice remark codes (RARC) associated with the discount from the billed charges to the Medicare payment determined by the Pricer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

