# HSP_ACCT_ICDPX_ALT

> This table contains the hospital account alternate ICD procedures from the hospital account (HAR) master file. Alternate ICD procedures will be specified if hospital accounts are coded with two sets of ICD codes.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ICD_PX_ALT_ID` | VARCHAR |  | The alternate ICD procedures stored in the hospital account. |
| 4 | `ICD_PX_ALT_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 5 | `ICD_PX_ALT_DATE` | DATETIME |  | The alternate ICD procedure service date. |
| 6 | `ICD_PX_ALT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `ICD_PX_ALT_EVNT_NUM` | INTEGER |  | The alternate ICD procedure event link number. |
| 8 | `ICD_PX_ALT_EXCLD_YN` | VARCHAR |  | The alternate ICD procedure exclude from clinical reporting data. |
| 9 | `ICD_PX_ALT_AFSOI_YN` | VARCHAR |  | The alternate ICD procedure affects severity of illness data. |
| 10 | `ICD_PX_ALT_AFROM_YN` | VARCHAR |  | The alternate ICD procedure affects risk of mortality data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

