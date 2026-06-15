# CL_PAT_EDU_NS

> Enterprise reporting table for no add single items in Patient Education (PED) records.

**Primary key:** `PED_ID`  
**Columns:** 6  
**Org-specific columns:** 2  
**Joined by:** 25 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK | The Unique ID for the Patient Education Record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | Patient Identifier to for which the Education record is created. Stored in internal format and can be used to link to patient record. |
| 3 | `METHOD_CAT_C_NAME` | VARCHAR | org | Category item that specifies method of education. |
| 4 | `RESPONSE_CAT_C_NAME` | VARCHAR | org | Category item that specifies learner's response to the education. |
| 5 | `INSTANT_NOADD_EDIT` | DATETIME (Local) |  | Date/Time stamp for the instance when the patient education record was last edited. |
| 6 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category number for the patient education record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (25)

| From | Column | Confidence |
|------|--------|------------|
| [CL_PATEDU_CNTCT_PT](CL_PATEDU_CNTCT_PT.md) | `PED_ID` | high |
| [CL_PATEDU_CNT_TITL](CL_PATEDU_CNT_TITL.md) | `PED_ID` | high |
| [CL_PATEDU_CT_HIST](CL_PATEDU_CT_HIST.md) | `PED_ID` | high |
| [CL_PATEDU_CT_TOPIC](CL_PATEDU_CT_TOPIC.md) | `PED_ID` | high |
| [CL_PAT_EDU_HISTORY](CL_PAT_EDU_HISTORY.md) | `PED_ID` | high |
| [CL_PAT_EDU_LEARNER](CL_PAT_EDU_LEARNER.md) | `PED_ID` | high |
| [CL_PAT_EDU_NM](CL_PAT_EDU_NM.md) | `PED_ID` | high |
| [CL_PAT_EDU_OS](CL_PAT_EDU_OS.md) | `PED_ID` | high |
| [CL_PAT_EDU_POINT](CL_PAT_EDU_POINT.md) | `PED_ID` | high |
| [CL_PAT_EDU_TITLE](CL_PAT_EDU_TITLE.md) | `PED_ID` | high |
| [CL_PAT_EDU_TOPIC](CL_PAT_EDU_TOPIC.md) | `PED_ID` | high |
| [IP_EDU_HANDOUT_TRACKING](IP_EDU_HANDOUT_TRACKING.md) | `PED_ID` | high |
| [IP_EDU_HANDOUT_TRACK_HX](IP_EDU_HANDOUT_TRACK_HX.md) | `PED_ID` | high |
| [IP_EDU_HNDT_VWED_USERS](IP_EDU_HNDT_VWED_USERS.md) | `PED_ID` | high |
| [PAT_EDU_HNDT_DURATION](PAT_EDU_HNDT_DURATION.md) | `PED_ID` | high |
| [PAT_EDU_HNDT_LOCAL_INST](PAT_EDU_HNDT_LOCAL_INST.md) | `PED_ID` | high |
| [PAT_EDU_HNDT_MAX_PROG](PAT_EDU_HNDT_MAX_PROG.md) | `PED_ID` | high |
| [PAT_EDU_HNDT_PROG_TRACK](PAT_EDU_HNDT_PROG_TRACK.md) | `PED_ID` | high |
| [PAT_EDU_HNDT_UTC_INST](PAT_EDU_HNDT_UTC_INST.md) | `PED_ID` | high |
| [PAT_EDU_HNDT_VWED_USERS](PAT_EDU_HNDT_VWED_USERS.md) | `PED_ID` | high |
| [PAT_EDU_POINT_LEARNER](PAT_EDU_POINT_LEARNER.md) | `PED_ID` | high |
| [PAT_EDU_POINT_LEARNER_DAT](PAT_EDU_POINT_LEARNER_DAT.md) | `PED_ID` | high |
| [PAT_EDU_POINT_LEARNER_LN](PAT_EDU_POINT_LEARNER_LN.md) | `PED_ID` | high |
| [PAT_EDU_POINT_REVWD_INST](PAT_EDU_POINT_REVWD_INST.md) | `PED_ID` | high |
| [PAT_EDU_POINT_REVWD_USER](PAT_EDU_POINT_REVWD_USER.md) | `PED_ID` | high |

