# PAT_OCCUPN_HX

> This table contains descriptive occupation history for patients recorded for a given encounter. Each row represents one line of text for occupation description and/or occupation comments for a single employer. If more than one occupation is commented on or described, each related line of descriptions/comments will have the employer ID field in that line populated with that occupation's employer ID.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique system identifier of the patient encounter. Contact serial number is unique across all patients and all contacts. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `HX_EMPLOYER_ID` | VARCHAR |  | The unique system identifier of the patient's employer. |
| 5 | `HX_EMPLOYER_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 6 | `HX_OCCUPN_COMMENT` | VARCHAR |  | Any comments listed regarding the patient's occupation. |
| 7 | `HISTORY_SOURCE_C_NAME` | VARCHAR | org | Stores the source of entry for this row of data (i.e. where this data came from). Some examples include: Provider Patient Parent |
| 8 | `HX_INDUSTRY_C_NAME` | VARCHAR | org | The category value that represents the occupation industry which a patient has worked in. |
| 9 | `HX_OCCUPN_START_DATE` | DATETIME |  | The date when a patient started working at an occupation. |
| 10 | `HX_OCCUPN_END_DATE` | DATETIME |  | The date when a patient stopped working at an occupation. |
| 11 | `HX_OCC_C_NAME` | VARCHAR | org | Category value for occupation. Similar to occupation description (I EPT 19300), but more discrete. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

