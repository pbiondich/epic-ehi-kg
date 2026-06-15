# PERFORMING_ORG_INFO

> Stores the performing organization information.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PERFORMING_ORG_NAME` | VARCHAR |  | The name of the performing organization. The phone number might be a part of the organizations name as labs might send it as a part of the name. |
| 4 | `PERFORMING_ORG_DIRECTOR` | VARCHAR |  | The name of the medical director of the performing organization. |
| 5 | `PERFORMING_ORG_CITY` | VARCHAR |  | The city where the performing organization is located. |
| 6 | `PERFORMING_ORG_STATE_C_NAME` | VARCHAR | org | The state where the performing organization is located. |
| 7 | `PERFORMING_ORG_ZIP_CODE` | VARCHAR |  | The zip code of the performing organization. |
| 8 | `PERFORMING_ORG_PHONE_NUM` | VARCHAR |  | Phone number of the performing organization. |
| 9 | `PERFORMING_ORG_CLIA_NUM` | VARCHAR |  | The Clinical Laboratory Improvement Amendment (CLIA) number of the performing organization. Any laboratory that is included in the CLIA legislation must obtain a CLIA certificate from the U.S. Department of Health and Human Services. The certificate will include a 10-digit number which is the CLIA number of that laboratory. |
| 10 | `PERFORMING_ORG_FORMAT_C_NAME` | VARCHAR |  | This item represents the format in which the performing organization medical director name is stored. |
| 11 | `PERFORMING_ORG_HOUSE_NUM` | VARCHAR |  | The housing number of the performing organization address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

