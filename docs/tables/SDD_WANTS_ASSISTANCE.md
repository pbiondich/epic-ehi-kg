# SDD_WANTS_ASSISTANCE

> Stores information about whether the patient would like resource recommendations for SDOH domains.

**Primary key:** `SDOH_DATA_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SDOH_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the social driver data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WANTS_ASSISTANCE_YN` | VARCHAR |  | Tracks whether the patient was documented as wanting assistance with needs in an SDOH domain. |
| 4 | `WANTS_ASST_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant a patient was documented as wanting or not wanting assistance. This instant stores when the data was written to SDD. If the data was filed via a flowsheet, it may not match the taken or recorded instant. The intent of this item is to indicate when a user could have first viewed this status in SDOH views for the patient. To find when the flowsheet was filed, items 904 and 905 can be used to find the linked flowsheet data. |
| 5 | `WANTS_ASST_USER_ID` | VARCHAR |  | The user who documented a patient as wanting assistance |
| 6 | `WANTS_ASST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `WANTS_ASST_TYPE_C_NAME` | VARCHAR |  | How a patients decision on whether they want assistance was documented |
| 8 | `WANTS_ASST_FSD_ID` | VARCHAR |  | The FSD record where flowsheet data that indicated a patient would or would not like assistance was documented |
| 9 | `WANTS_ASST_FSD_LINE` | INTEGER |  | The FSD line where flowsheet data that indicated a patient would or would not like assistance was documented |
| 10 | `WANTS_ASST_PAT_REP_YN` | VARCHAR |  | Whether documentation that a patient would like assistance was patient reported. This item tracks whether the information was collected via MyChart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SDOH_DATA_ID` | [SDD_DATA](SDD_DATA.md) | sole_pk | high |

