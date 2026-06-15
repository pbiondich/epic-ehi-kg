# TX_DIAG

> This table contains information about the diagnoses associated with transactions. Since one transaction may be associated with multiple diagnoses, each row in this table represents one diagnosis and is identified by the transaction ID and line number. The first six diagnosis IDs associated with a transaction are recorded in the CLARITY_TDL table in the columns DX_ ONE_ID through DX_ SIX_ID. This table allows you to easily identify transactions with a specific diagnosis code or range of diagnosis codes. The data for this table is extracted using a KB_SQL query.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique accounts receivable transaction record ID. |
| 2 | `LINE` | INTEGER | PK | Line number to identify each row of diagnosis data associated with an individual transaction. Line 1 identifies the primary diagnosis of the charge. |
| 3 | `POST_DATE` | DATETIME |  | The post date of the charge transaction |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `DX_QUALIFIER_C_NAME` | VARCHAR | org | Diagnosis Qualifier for the diagnosis associated with this charge |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

