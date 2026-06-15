# CL_SCD_SCHED_CODE

> The CL_SCD_SCHED_CODE table contains data on visit type scheduling codes. Scheduling Codes is a system designed to provide flexible decision support for complex scheduling requirements at the point of visit type selection. Once a visit type is entered, a form will display which will allow you to enter the scheduling codes. Depending on the setup, the scheduling codes have the ability to replace the current visit type with another. Scheduling codes allow you to simplify appointment entry for schedulers, even when they must deal with complicated appointment instructions and orders, cutting down on both scheduling time and error rates. It also allows you to use information for recordkeeping, billing and other purposes.

**Primary key:** `SCD_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCD_ID` | VARCHAR | PK | The unique ID assigned to the scheduling code record. |
| 2 | `SCD_ID_SCHED_CODE_NAME` | VARCHAR |  | The name of the scheduling code. |
| 3 | `SCHED_CODE_NAME` | VARCHAR |  | The name of the scheduling code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [OR_LOG_LN_SCD](OR_LOG_LN_SCD.md) | `SCD_ID` | high |

