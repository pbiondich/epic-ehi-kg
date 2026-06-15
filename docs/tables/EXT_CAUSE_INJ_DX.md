# EXT_CAUSE_INJ_DX

> All values associated with a claim are stored in the Claim External Value record. The EXT_CAUSE_INJ_DX table holds the diagnoses that document any accidents or other external causes for the patient's injury.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `EXT_CAUSE_INJ_QUAL` | VARCHAR |  | This item holds the qualifier identifying the code set for the external cause of injury diagnoses. |
| 4 | `EXT_CAUSE_INJ_DX` | VARCHAR |  | This item holds the external cause of injury diagnoses for the claim. |
| 5 | `EXT_CAUSE_INJ_POA` | VARCHAR |  | This item identifies if the external cause of injury diagnosis was present when the patient was admitted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

