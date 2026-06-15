# HSP_ACCT_PX_LIST

> This table contains hospital account final procedure list information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID number of a hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Since multiple coded procedures can be stored in one hospital account, each procedure will have a unique line number. |
| 3 | `FINAL_ICD_PX_ID` | VARCHAR |  | A coded procedure stored in the hospital account. |
| 4 | `FINAL_ICD_PX_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 5 | `PROC_DATE` | DATETIME |  | The date associated with a coded procedure stored in the hospital account. |
| 6 | `PROC_PERF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `PROC_EVENT_NUMBER` | INTEGER |  | The event number associated with a coded procedure stored in the hospital account. Event numbers are used to associate coded procedures with CPT™ codes. |
| 8 | `PX_AFCT_ROM_YN` | VARCHAR |  | Indicates whether the procedure has an impact on the DRG's Risk of Mortality. |
| 9 | `PX_EXCLD_RPT_YN` | VARCHAR |  | Indicates whether the procedure was marked to be excluded from clinical reporting. |
| 10 | `PX_AFCT_SOI_YN` | VARCHAR |  | Indicates whether the procedure has an impact on the DRG's Serverity of Illness. |
| 11 | `AFFECTS_DRG_YN` | VARCHAR |  | Indicates whether the procedure has an impact on the DRG. |
| 12 | `INTERVENTION_TYPE_C_NAME` | VARCHAR |  | The intervention type for the ICD procedure. |
| 13 | `PX_AU_PERF_LOC_C_NAME` | VARCHAR |  | This item stores where the procedure was performed, and is used in Australian Coding workflows. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

