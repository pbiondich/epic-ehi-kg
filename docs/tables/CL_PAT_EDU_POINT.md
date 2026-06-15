# CL_PAT_EDU_POINT

> Enterprise reporting table for patient education point items in the Patient Education (PED) master file.

**Primary key:** `PED_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `LINE` | INTEGER | PK | Line count for the Patient education point data. |
| 3 | `PAT_POINT_ID` | VARCHAR |  | Unique identifier for the patient education points. |
| 4 | `PAT_PNT_TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 5 | `PAT_PNT_TITLE_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 6 | `PAT_PNT_STATUS_C_NAME` | VARCHAR |  | A category item that specifies each point's status. |
| 7 | `PAT_POINT_KEY` | VARCHAR |  | The education point key for patient education record. This is a string of Title^Topic^Point |
| 8 | `POINT_IED_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 9 | `MY_POINT_HNO_ID` | VARCHAR |  | The unique identifier for the note record associated for a My Point. My Point is a patient education point created on the fly and does not have an IED record associated with it. |
| 10 | `MY_POINT_HNO_DAT` | VARCHAR |  | The contact date for the note record associated for a My Point. My Point is a patient education point created on the fly and does not have an IED record associated with it. |
| 11 | `POINT_FIRST_DOSE_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

