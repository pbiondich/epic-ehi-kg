# PR_EST_PX_CVG_ADDL_INFO

> Contains additional coverage related information for each procedure in a price estimate.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PX_CVG_ADDL_LINE_NUM` | INTEGER |  | This item holds a line number of the additional charge info items related group. |
| 4 | `PX_CVG_FO_NUM` | INTEGER |  | The coverage level associated with the corresponding coverage (I PES 168). |
| 5 | `IS_NON_COVERED_YN` | VARCHAR |  | This indicates whether a line of an estimate is covered/non-covered. |
| 6 | `INS_ALLOW_AMT` | NUMERIC |  | This is the insurance allowed amount of the current service line. |
| 7 | `INS_PAID_AMT` | NUMERIC |  | This is the insurance paid amount of the current service line. |
| 8 | `DENTAL_DGRADE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `DENTAL_DGRADE_ALLW_AMT` | NUMERIC |  | The allowed amount of the downgraded procedure for a given procedure line and coverage. |
| 10 | `SYS_INS_PAID_AMT` | NUMERIC |  | This item stores the system-calculated insurance paid amount of the current service line. |
| 11 | `DENTAL_UPGRADE_AMOUNT` | NUMERIC |  | Upgrade charge amount for given procedure line and coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

