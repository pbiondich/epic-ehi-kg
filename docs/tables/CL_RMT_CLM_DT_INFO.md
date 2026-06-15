# CL_RMT_CLM_DT_INFO

> Contains claim level date information from the electronic remittance payment. This information is sent in the DTM segment in Loop 2100 of an ANSI 835 Health Care Claim Payment/Advice file. This segment is used to send specific dates associated with the claim being paid. This information is stored in the remittance image record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with related claim date information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_DATE_QUAL_C_NAME` | VARCHAR |  | The date qualifier code for the claim date information. This is a standard code that indicates what the date represents. |
| 4 | `CLAIM_DT` | DATETIME |  | Claim related date sent in the remittance file. The specific meaning of this date is indicated by the associated date qualifier code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

