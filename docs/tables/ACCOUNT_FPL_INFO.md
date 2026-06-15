# ACCOUNT_FPL_INFO

> This table contains Federal Poverty Level information from EAR masterfile.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 25  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique ID for the account record. This ID number could be encrypted if you have elected to implement enterprise reporting’s encryption security function. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FPL_EFF_DATE` | DATETIME |  | The date from which this line of Federal Poverty Level information is effective. |
| 4 | `FPL_INCOME` | NUMERIC |  | Total income for use in calculating Federal Poverty Level information. |
| 5 | `FPL_FAMILY_SIZE` | INTEGER |  | Family size for use in calculating Federal Poverty Level information. |
| 6 | `FPL_PERCENTAGE` | NUMERIC |  | Calculated percentage of the Federal Poverty Level for this guarantor. |
| 7 | `FPL_STAFF_TYPE_C_NAME` | VARCHAR | org | The type of staff category ID for the person who collected this Federal Poverty Level information. |
| 8 | `FPL_INCOME_PRF_C_NAME` | VARCHAR | org | The category ID for the method used by the guarantor to prove their income level. |
| 9 | `FPL_STATUS_CODE_C_NAME` | VARCHAR | org | The category ID for the financial assistance status of a guarantor account. This only applies to guarantors that have their Federal Poverty Level form filled out. |
| 10 | `FPL_REASON_CODE_C_NAME` | VARCHAR | org | The category ID for the financial assistance reason code associated with this row. |
| 11 | `FPL_EXP_DATE` | DATETIME |  | The date until which this line of Federal Poverty Level information is effective. |
| 12 | `FPL_ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user that collected this line of Federal Poverty Level information. |
| 13 | `FPL_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `FPL_USER_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 15 | `FPL_INST_OF_ENTRY` | DATETIME (Local) |  | The date and time at which this line of Federal Poverty Level information was collected. |
| 16 | `INCOME_INTDIV` | NUMERIC |  | Gross monthly income from interest and dividends. |
| 17 | `INCOME_PENSION` | NUMERIC |  | Gross monthly income from pension. |
| 18 | `INCOME_ALIMONY` | NUMERIC |  | Gross monthly income from alimony/child support. |
| 19 | `INCOME_SSI` | NUMERIC |  | Gross monthly supplemental security income. |
| 20 | `INCOME_GOVT` | NUMERIC |  | Gross monthly income from government assistance. |
| 21 | `INCOME_NON_WAGE` | NUMERIC |  | Other gross monthly non-wage income. |
| 22 | `INCOME_HRLY_WAGE` | NUMERIC |  | Hourly wage for gross monthly income calculation. |
| 23 | `HOURS_WORKED_WEEK` | INTEGER |  | Number of hours worked per week. |
| 24 | `OTHER_WAGES` | NUMERIC |  | Other wages for use in calculating gross monthly income for use in calculating Federal Poverty Level information. |
| 25 | `SALARY` | NUMERIC |  | Salary earned for use in calculating gross monthly income for use in calculating Federal Poverty Level information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

