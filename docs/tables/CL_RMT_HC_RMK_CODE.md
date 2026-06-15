# CL_RMT_HC_RMK_CODE

> Contains health care remark code information from the service line level of an electronic remittance file. This information is sent in the LQ segment of an ANSI 835 Health Care Claim Payment/Advice file. This information is stored in the remittance image record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | ID for the remittance image record containing the health care remark code information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LQ_SERVICE_LINE` | VARCHAR |  | The service line associated with the health care remark code. |
| 4 | `CODE_LST_QUAL_C_NAME` | VARCHAR |  | The code list qualifier code. This is a standard code which indicates which code set the remark code belongs to. |
| 5 | `INDUSTRY_CODE` | VARCHAR |  | The specific health care remark code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

