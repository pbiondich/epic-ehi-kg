# POC_BP_INFO

> Contains information concerning the benefit periods corresponding to the plan of care.

**Primary key:** `POC_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BP_START_DATE` | DATETIME |  | Benefit period start date |
| 4 | `BP_END_DATE` | DATETIME |  | Benefit period end date |
| 5 | `BP_MED_DIR_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `BP_ATT_PROV_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `BP_VCTI_DATE` | DATETIME |  | Benefit period verbal CTI date |
| 8 | `BENEFIT_PERIOD_NUM` | INTEGER |  | The number of this benefit period in the sequence of the patient's hospice care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

