# CL_RMT_SVCE_LN_INF

> This table contains service line information from the remittance image.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with remittance service line information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each instance of service line information will have its own line. |
| 3 | `SERVICE_LINE` | VARCHAR |  | Service line information for claim remittance. |
| 4 | `PROC_IDENTIFIER` | VARCHAR |  | The composite medical procedure identifier to identify a medical procedure by its standardized codes for service line information. |
| 5 | `LINE_ITEM_CHG_AMT` | NUMERIC |  | Monetary amount for submitted service line item charge. |
| 6 | `PROV_PAYMENT_AMT` | NUMERIC |  | Monetary amount for the service line item provider payment amount. |
| 7 | `NUBC_REV_CD` | VARCHAR |  | National uniform billing committee revenue code for service line information. |
| 8 | `UNITS_PAID_CNT` | NUMERIC |  | Count of the Units of Service Paid for service line information. |
| 9 | `SUBM_PROC_IDENT` | VARCHAR |  | Submitted composite medical procedure identifier information if that was different from adjudicated procedure for service line information. |
| 10 | `ORIG_UNITS_CNT` | NUMERIC |  | Original units of service count for service line information. |
| 11 | `SVC_LINE_CHG_PB_ID` | NUMERIC |  | ID for professional billing service line charge. |
| 12 | `SVC_LINE_CHG_HB_ID` | NUMERIC |  | ID for hospital billing service line charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

