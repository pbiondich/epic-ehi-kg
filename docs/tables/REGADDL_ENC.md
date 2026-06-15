# REGADDL_ENC

> The additional registration items are used to store organization specific patient data which is captured during Prelude or ADT workflows. The REGADDL_ENC table contains all of the encounter level items where a user may enter only a single value.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 25  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `REGADDL_ENC_1_C_NAME` | VARCHAR | org | First of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 5 | `REGADDL_ENC_2_C_NAME` | VARCHAR | org | Second of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 6 | `REGADDL_ENC_3_C_NAME` | VARCHAR | org | Third of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 7 | `REGADDL_ENC_4_C_NAME` | VARCHAR | org | Fourth of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 8 | `REGADDL_ENC_5_C_NAME` | VARCHAR | org | Fifth of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 9 | `REGADDL_ENC_6_C_NAME` | VARCHAR | org | Sixth of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 10 | `REGADDL_ENC_7_C_NAME` | VARCHAR | org | Seventh of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 11 | `REGADDL_ENC_8_C_NAME` | VARCHAR | org | Eighth of eight additional registration encounter level category columns. The usage of this data element is defined by your organization. |
| 12 | `REGADDL_ENC_1_DT` | DATETIME |  | First of three additional registration encounter level date columns. The usage of this data element is defined by your organization. |
| 13 | `REGADDL_ENC_2_DT` | DATETIME |  | Second of three additional registration encounter level date columns. The usage of this data element is defined by your organization. |
| 14 | `REGADDL_ENC_3_DT` | DATETIME |  | Third of three additional registration encounter level date columns. The usage of this data element is defined by your organization. |
| 15 | `REGADDL_ENC_1_TM` | DATETIME (Local) |  | First of three additional registration encounter level time columns. The usage of this data element is defined by your organization. |
| 16 | `REGADDL_ENC_2_TM` | DATETIME (Local) |  | Second of three additional registration encounter level time columns. The usage of this data element is defined by your organization. |
| 17 | `REGADDL_ENC_3_TM` | DATETIME (Local) |  | Third of three additional registration encounter level time columns. The usage of this data element is defined by your organization. |
| 18 | `REGADDL_ENC_1_NUM` | NUMERIC |  | First of three additional registration encounter level numeric columns. The usage of this data element is defined by your organization. |
| 19 | `REGADDL_ENC_2_NUM` | NUMERIC |  | Second of three additional registration encounter level numeric columns. The usage of this data element is defined by your organization. |
| 20 | `REGADDL_ENC_3_NUM` | NUMERIC |  | Third of three additional registration encounter level numeric columns. The usage of this data element is defined by your organization. |
| 21 | `REGADDL_ENC_1_STR` | VARCHAR |  | First of five additional registration encounter level string columns. The usage of this data element is defined by your organization. |
| 22 | `REGADDL_ENC_2_STR` | VARCHAR |  | Second of five additional registration encounter level string columns. The usage of this data element is defined by your organization. |
| 23 | `REGADDL_ENC_3_STR` | VARCHAR |  | Third of five additional registration encounter level string columns. The usage of this data element is defined by your organization. |
| 24 | `REGADDL_ENC_4_STR` | VARCHAR |  | Fourth of five additional registration encounter level string columns. The usage of this data element is defined by your organization. |
| 25 | `REGADDL_ENC_5_STR` | VARCHAR |  | Fifth of five additional registration encounter level string columns. The usage of this data element is defined by your organization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

