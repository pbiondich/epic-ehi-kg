# EXPECTED_DISCHARGE_HX

> This is the expected discharge status history. It will track changes made to the patient's expected discharge throughout the encounter. This table contains data about the expected discharge date (I EPT 10442), approximate expected discharge time (I EPT 10443), exact expected discharge time (I EPT 10444), comments about the expected discharge (I EPT 10445), the date and time that the expected discharge was entered (I EPT 10446), the user that made the change (I EPT 10447), and whether the expected discharge date and time was unknown (I EPT 10454). Each time the information is entered or modified, it will add a line to this table.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `EXPECTED_DISCHARGE_APPROX_HX_C_NAME` | VARCHAR | org | Approximate time the patient is expected to be discharged. Each value in this column denotes a time range (e.g. Morning, Midday, Afternoon, Evening). If the approximate time is empty, the patient may have an associated exact time (check column EXPECTED_DISCH_DTTM_HX_TIME). |
| 5 | `EXPECTED_DISCH_DTTM_HX_TIME` | DATETIME (Local) |  | This column stores the date and exact time the patient is expected to be discharged (e.g. 10/16/2015 8:00AM). If an exact time is empty, the patient may have an associated approximate time (check column EXPECTED_DISCHARGE_APPROX_HX_C). |
| 6 | `EXPECTED_DISCHARGE_COMMENT_HX` | VARCHAR |  | This column stores the comment entered about the expected discharge. |
| 7 | `EXPECTED_DISCH_UPD_HX_UTC_DTTM` | DATETIME (UTC) |  | This column stores the date and time when the expected discharge items were updated. |
| 8 | `EXPECTED_DISCHARGE_UPD_SRC_C_NAME` | VARCHAR | org | The reason the expected discharge date and / or time was updated. |
| 9 | `EXPECTED_DISCHARGE_UNKNOWN_YN` | VARCHAR |  | Indicates whether the expected discharge date is unknown for this patient. 'Y' indicates that the expected discharge date is unknown and documented. 'N' indicates that the expected discharge date is known and documented. NULL should not be stored in the column. |
| 10 | `EXPECTED_DISCH_UPD_HX_LCL_DTTM` | DATETIME (Local) |  | Local instant when expected discharge date information was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

