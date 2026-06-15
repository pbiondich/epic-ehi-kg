# CAL_COMM_TRACKING_2

> The CAL_COMM_TRACKING_2 table contains information about your communication tracking records. This is a continuation of the CAL_COMM_TRACKING table.

**Overflow of:** [CAL_COMM_TRACKING](CAL_COMM_TRACKING.md)  
**Primary key:** `COMM_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `PAT_LOCATION` | VARCHAR |  | Free text information about the location of the patient during the communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

