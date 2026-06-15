# FIN_ASST_CASE_FLAG_UPD_HX

> This table contains the updates made to case flags of a financial assistance case record. Whenever any of the following columns are changed, one or more rows are added to this table based on the number of case flags present on the financial assistance case record. 1. Case status 2. Case flags 3. Assigned user 4. Follow up date 5. Application provided date 6. Application signed date.

**Primary key:** `FIN_ASST_CASE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated update made to one of the following columns in financial assistance case record. 1. Case status 2. Case flags 3. Assigned user 4. Follow up date 5. Application provided date 6. Application signed date Together with FIN_ASST_CASE_ID, this forms the foreign key to table FIN_ASST_CASE_UPDATE_HX. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple case flags associated with a financial assistance case after one of the following have been changed: 1. Case status 2. Case flags 3. Assigned user 4. Follow up date 5. Application provided date 6. Application signed date |
| 4 | `UPDATE_FLAG_C_NAME` | VARCHAR | org | The category ID of the one of the case flags that were on the financial assistance case when they were added to update history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

