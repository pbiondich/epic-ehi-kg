# DENTAL_FINDING_HX

> This table contains the history of edits for a dental finding record.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENTAL_PATIENT_CSN` | NUMERIC |  | Stores the patient encounter in which a particular contact of the record was modified if it was available. |
| 4 | `DENTAL_MOD_USER_ID` | VARCHAR |  | Stores the user who modified a piece of dental data in the finding record. |
| 5 | `DENTAL_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DENTAL_MOD_INSTANT_DTTM` | DATETIME (Attached) |  | Stores the date and time when a piece of dental data in the finding record was modified |
| 7 | `DEN_FIND_STAT_HIS_C_NAME` | VARCHAR |  | The history of the finding's status (unaddressed, resolved, removed, etc.) |
| 8 | `TOO_FIND_TYPE_H_C_NAME` | VARCHAR |  | Stores the history of the finding type of a tooth-level finding |
| 9 | `DENT_CHRON_INSTANT_DTTM` | DATETIME (Attached) |  | This is the date and time the documentation was made for, such as when documenting past historical data. |
| 10 | `CARIES_CLASS_HIST_C_NAME` | VARCHAR | org | The history of the finding's caries classification |
| 11 | `CARIES_DEPTH_HIST` | NUMERIC |  | The history of the finding's caries depth |
| 12 | `DENT_FUR_CLASS_HX_C_NAME` | VARCHAR | org | This item stores the history of the severity of furcation documented on a tooth. |
| 13 | `DENT_MOB_CLASS_HX_C_NAME` | VARCHAR | org | This item stores the history of a tooth's mobility classification, which is its severity of mobility. |
| 14 | `CARIES_INCIP_HX_C_NAME` | VARCHAR | org | The history of whether a caries finding is incipient |
| 15 | `DENT_PERIFIND_SEVERITY_C_NAME` | VARCHAR | org | This item tracks the history of the level of severity for a periodontal finding. It contains the periodontal finding severity category ID for the finding. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

