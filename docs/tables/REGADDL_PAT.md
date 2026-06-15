# REGADDL_PAT

> The additional registration items are used to store organization specific patient data which is captured during Prelude or ADT workflows. The REGADDL_PAT table contains all of the patient level items where a user may enter only a single value.

**Primary key:** `PAT_ID`  
**Columns:** 23  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `REGADDL_PAT_1_C_NAME` | VARCHAR | org | First of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 3 | `REGADDL_PAT_2_C_NAME` | VARCHAR | org | Second of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 4 | `REGADDL_PAT_3_C_NAME` | VARCHAR | org | Third of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 5 | `REGADDL_PAT_4_C_NAME` | VARCHAR | org | Fourth of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 6 | `REGADDL_PAT_5_C_NAME` | VARCHAR | org | Fifth of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 7 | `REGADDL_PAT_6_C_NAME` | VARCHAR | org | Sixth of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 8 | `REGADDL_PAT_7_C_NAME` | VARCHAR | org | Seventh of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 9 | `REGADDL_PAT_8_C_NAME` | VARCHAR | org | Eighth of eight additional registration patient level category columns. The usage of this data element is defined by your organization. |
| 10 | `REGADDL_PAT_1_DT` | DATETIME |  | First of three additional registration patient level date columns. The usage of this data element is defined by your organization. |
| 11 | `REGADDL_PAT_2_DT` | DATETIME |  | Second of three additional registration patient level date columns. The usage of this data element is defined by your organization. |
| 12 | `REGADDL_PAT_3_DT` | DATETIME |  | Third of three additional registration patient level date columns. The usage of this data element is defined by your organization. |
| 13 | `REGADDL_PAT_1_TM` | DATETIME (Local) |  | First of three additional registration patient level time columns. The usage of this data element is defined by your organization. |
| 14 | `REGADDL_PAT_2_TM` | DATETIME (Local) |  | Second of three additional registration patient level time columns. The usage of this data element is defined by your organization. |
| 15 | `REGADDL_PAT_3_TM` | DATETIME (Local) |  | Third of three additional registration patient level time columns. The usage of this data element is defined by your organization. |
| 16 | `REGADDL_PAT_1_NUM` | NUMERIC |  | First of three additional registration patient level numeric columns. The usage of this data element is defined by your organization. |
| 17 | `REGADDL_PAT_2_NUM` | NUMERIC |  | Second of three additional registration patient level numeric columns. The usage of this data element is defined by your organization. |
| 18 | `REGADDL_PAT_3_NUM` | NUMERIC |  | Third of three additional registration patient level numeric columns. The usage of this data element is defined by your organization. |
| 19 | `REGADDL_PAT_1_STR` | VARCHAR |  | First of five additional registration patient level string columns. The usage of this data element is defined by your organization. |
| 20 | `REGADDL_PAT_2_STR` | VARCHAR |  | Second of five additional registration patient level string columns. The usage of this data element is defined by your organization. |
| 21 | `REGADDL_PAT_3_STR` | VARCHAR |  | Third of five additional registration patient level string columns. The usage of this data element is defined by your organization. |
| 22 | `REGADDL_PAT_4_STR` | VARCHAR |  | Fourth of five additional registration patient level string columns. The usage of this data element is defined by your organization. |
| 23 | `REGADDL_PAT_5_STR` | VARCHAR |  | Fifth of five additional registration patient level string columns. The usage of this data element is defined by your organization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

