# CAL_REFERENCE_CARE_GAPS

> The care gap type category IDs detailing what was discusssed during the outreach.

**Primary key:** `COMM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `REFERENCE_HM_CARE_GAP_TYPE_C_NAME` | VARCHAR |  | Care Gap Type referenced by this Communication Tracking record. This value is used to track what the topics the patient was called about. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

