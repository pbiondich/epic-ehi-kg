# HH_EPSD_ANC_PROV

> This table contains Home Health episode-level ancillary providers information. This information is entered in the Episode Info 2 form as part of an Intake encounter in the Ancillary Providers table.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `ANC_PROV_CMT` | VARCHAR |  | Ancillary provider comment text entered by a user. |
| 5 | `RECV_PLAN_OF_CARE_FYI_YN` | VARCHAR |  | Flag for determining whether a provider should be included on FYI messages when new supplemental orders are added to the plan of care. |
| 6 | `ANC_PROV_UNQ_ADR_ID` | VARCHAR |  | This item stores the unique ID of the address that should be used for this provider in the ancillary provider table. |
| 7 | `ANC_PROV_REL_C_NAME` | VARCHAR | org | The ancillary provider's relation to the patient. |
| 8 | `ANC_PROV_START_DATE` | DATETIME |  | The date on which the ancillary provider began care of the patient. |
| 9 | `ANC_PROV_END_DATE` | DATETIME |  | The date on which the ancillary provider ended care of the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

