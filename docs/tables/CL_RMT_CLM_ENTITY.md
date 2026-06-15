# CL_RMT_CLM_ENTITY

> Contains identifying information for entities (persons or organizations) from an electronic remittance payment. This information is sent in the NM1 segment of an ANSI 835 Health Care Claim Payment/Advice file. This information is stored in the remittance image record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | ID for the remittance image record containing the claim related entity information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ID_CODE_C_NAME` | VARCHAR | org | The entity identifier code for the claim related entity. This is a standard code that indicates what type of individual or organization is being identified. |
| 4 | `ENT_QUAL_C_NAME` | VARCHAR |  | Code indicating whether this information is for a person or a non-person entity. |
| 5 | `LAST_NAME_ORG_NAME` | VARCHAR |  | This is the individual last name or organization name. |
| 6 | `FIRST_NAME` | VARCHAR |  | The individual first name. |
| 7 | `MIDDLE_NAME` | VARCHAR |  | The individual middle name or initial. |
| 8 | `NAME_SUFFIX` | VARCHAR |  | The suffix to individual name. |
| 9 | `IDEN_CODE_QUALF_C_NAME` | VARCHAR |  | The identification code qualifier. This is a standard code that indicates what type of ID is used to identify the specific individual or organization. |
| 10 | `IDEN_CODE` | VARCHAR |  | The ID associated with the specific individual or organization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

