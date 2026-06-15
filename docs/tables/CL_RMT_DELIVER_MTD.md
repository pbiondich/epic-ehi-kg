# CL_RMT_DELIVER_MTD

> This table contains information on the remittance delivery method when the funds are transferred independently from the remittance.

**Primary key:** `IMAGE_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | The unique identifier for the image record. |
| 2 | `RPT_XMISSION_CODE_C_NAME` | VARCHAR |  | Information about how the report and related funds were transmitted |
| 3 | `THIRD_PARTY_NAME` | VARCHAR |  | Holds the name of the third party processing entity |
| 4 | `COMM_NUM` | VARCHAR |  | The communication number of the third party processing entity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

