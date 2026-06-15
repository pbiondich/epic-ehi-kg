# MC_PRICER_REMIT

> This table contains information about the remittance codes that explain differences between billed charges and Medicare reimbursements.

**Primary key:** `PRICER_MSG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the pricer message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MC_PRICER_REASON_CODE` | VARCHAR |  | The claim adjustment reason code (CARC) associated with the discount from the billed charges to the Medicare payment determined by the Pricer. |
| 4 | `MC_PRICER_GROUP_CODE` | VARCHAR |  | The claim adjustment group code associated with the discount from the billed charges to the Medicare payment determined by the Pricer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

