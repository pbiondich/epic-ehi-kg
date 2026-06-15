# CL_PAT_EDU_HISTORY

> Patient Education History items.

**Primary key:** `PED_ID`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `LINE` | INTEGER | PK | Line count for the Patient education history data. |
| 3 | `PAT_HX_KEY` | VARCHAR |  | The education key for patient education history. The education key is a string of Title^Topic^Point |
| 4 | `PAT_HX_TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 5 | `PAT_HX_POINT_ID` | VARCHAR |  | Unique identifier for the patient education history point. |
| 6 | `PAT_HX_STATUS_C_NAME` | VARCHAR |  | Category item that that specifies the status of title, topic, or point in education history. |
| 7 | `PAT_HX_INS` | DATETIME (Local) |  | Date/Time stamp for the instance when the title/topic/point was added, resolved, reactivated or deleted. |
| 8 | `PAT_HX_USER_ID` | VARCHAR |  | Unique identifier for the user that added, resolved, reactivated or deleted the title/topic/point for the patient education. |
| 9 | `PAT_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `PAT_HX_RSN_C_NAME` | VARCHAR | org | Category item specifying the reason for resolving title/topic |
| 11 | `PAT_HX_EPTCSN` | NUMERIC |  | The contact serial number for the patient contact to which this patient education record is associated to. |
| 12 | `HX_POINT_IED_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 13 | `HX_MY_POINT_HNO_ID` | VARCHAR |  | The unique identifier for the note record associated for a My point in patient education record history. My point is a patient education point created on the fly and does not have an education (IED) record associated with it. |
| 14 | `HX_MY_POINT_HNO_DA` | VARCHAR |  | The contact date for the note record associated for a My point in patient education record history. My point is a patient education point created on the fly and does not have an education (IED) record associated with it. |
| 15 | `PAT_HIST_TITLE_DAT` | INTEGER |  | The contact date (DAT) where the patient education history title was documented. |
| 16 | `PAT_HIST_TOPIC_DAT` | INTEGER |  | The contact date (DAT) where the patient education history topic was documented. |
| 17 | `PAT_HIST_POINT_DAT` | INTEGER |  | The contact date (DAT) where the patient education history point was documented. |
| 18 | `HX_FIRST_DOSE_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

