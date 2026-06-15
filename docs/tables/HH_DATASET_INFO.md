# HH_DATASET_INFO

> This table contains information for both OASIS Data Sets and Hospice Item Sets.

**Primary key:** `DATASET_ID`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `DATA_SET_STATUS_C_NAME` | VARCHAR | org | This item contains the current submission status of the OASIS dataset or Hospice item set. |
| 3 | `PAT_ID` | VARCHAR | FK→ | This item links to the patient record (EPT) of the patient associated with the Data Set. |
| 4 | `DATASET_TYPE_C_NAME` | VARCHAR |  | Stores what type of dataset the record is. Currently datasets can be OASIS or HIS. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item contains the CSN for the encounter associated with the OASIS or HOPE data set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

