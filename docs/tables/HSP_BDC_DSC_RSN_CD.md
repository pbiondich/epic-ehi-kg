# HSP_BDC_DSC_RSN_CD

> This table contains discrepancy reason code information for records in the Denial/Correspondence (DBC) master file.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record the discrepancy reason code information is associated with. |
| 2 | `LINE` | INTEGER | PK | Line number of discrepancy reason code information that is being extracted by enterprise reporting. |
| 3 | `DISCP_RMC_CODE_ID` | VARCHAR |  | The discrepancy reason code associated with the denial/correspondence record. |
| 4 | `DISCP_RMC_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 5 | `EXTL_DISCP_RSN_CD` | VARCHAR |  | The external discrepancy reason code associated with the denial/correspondence record. |
| 6 | `DISP_GRP_CODE_C_NAME` | VARCHAR | org | This column stores the discrepancy reason group code associated with the discrepancy reason code associated with the denial correspondence record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

