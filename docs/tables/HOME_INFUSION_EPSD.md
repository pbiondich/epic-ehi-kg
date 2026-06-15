# HOME_INFUSION_EPSD

> Home Infusion episode details.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `HI_SERVICE_PAUSED_YN` | VARCHAR |  | Whether or not the current service is paused |
| 3 | `HI_START_DATE` | DATETIME |  | Expected Therapy Start Date |
| 4 | `HI_END_DATE` | DATETIME |  | Last day of therapy for patient |
| 5 | `HI_LINE_TYPE_C_NAME` | VARCHAR | org | Patient's line type for this therapy |
| 6 | `HI_LUMENS_NUM` | INTEGER |  | Number of lumens for patient line. |
| 7 | `HI_LINKED_LINE_ID` | VARCHAR |  | The unique ID of the infusion line associated with an episode |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

