# FINALIZE_PHYSICIAN

> This table contains information about the physician who finalized a study and when it was finalized.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINALIZE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `FINALIZING_INS_DTTM` | DATETIME (Local) |  | This item stores the instant that a study is finalized. |
| 5 | `FINALIZING_INST_UTC_DTTM` | DATETIME (UTC) |  | CAUTION: This item stores data that must be kept in sync with Order item 52269 - Finalizing Instant UTC, Bucketed. *This means you should never set this item without setting I ORD 52269 This item captures the date and time in the Universal Time Coordinated (UTC) format that the provider listed in the Finalizing Physician (I ORD 52265) item marked the study as Final. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

