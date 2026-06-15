# HSP_BWQ_INFO

> This table contains information about hospital billing workqueues. Each row represents one workqueue in the Hospital Billing WQ (BWQ) master file.

**Primary key:** `WORKQUEUE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `WORKQUEUE_ID` | VARCHAR | PK shared | This column stores the unique identifier for the hospital billing workqueue record. |
| 2 | `WORKQUEUE_ID_WORKQUEUE_NAME` | VARCHAR |  | The name of the workqueue. |
| 3 | `WORKQUEUE_NAME` | VARCHAR |  | The name of the workqueue. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

