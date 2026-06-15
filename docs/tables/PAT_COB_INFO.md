# PAT_COB_INFO

> This table contains a list of coordination of benefits savings bucket (COB) coverages to which a member belongs, and information specific to that COB coverage, such as insurance company and subscriber name.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 29  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | Unique patient ID associated with the Coordination of Benefits (COB) information. |
| 2 | `LINE` | INTEGER | PK | Line number of Coordination of Benefits (COB) information on patient. |
| 3 | `COB_INS_CO_NAME` | VARCHAR |  | Name of the insurance company for Coordination of Benefits (COB) information. |
| 4 | `COB_INS_CO_ADDR` | VARCHAR |  | Address of insurance company for Coordination of Benefits (COB) information. |
| 5 | `COB_INSURED_NAME` | VARCHAR |  | Name of subscriber on Coordination of Benefits (COB) coverage. |
| 6 | `COB_GRP_POLICY_NUM` | VARCHAR |  | Group/policy number on Coordination of Benefits (COB) coverage. |
| 7 | `COB_GRP_NAME_EMPR` | VARCHAR |  | Group/employer name on Coordination of Benefits (COB) coverage. |
| 8 | `COB_STATUS_C_NAME` | VARCHAR | org | Status of information for a member/Coordination of Benefits (COB) coverage. |
| 9 | `COB_INS_PHONE` | VARCHAR |  | Phone number of contact at Coordination of Benefits (COB) insurance company. |
| 10 | `COB_INS_CONTACT` | VARCHAR |  | Contact at Coordination of Benefits (COB) insurance company. |
| 11 | `COB_INSURED_DOB` | DATETIME |  | Date of birth for subscriber on a Coordination of Benefits (COB) coverage. |
| 12 | `COB_MEM_RELX_C_NAME` | VARCHAR | org | Relationship of member to the subscriber on a Coordination of Benefits (COB) coverage. |
| 13 | `COB_MEM_EFF_DATE` | DATETIME |  | Effective date of member on a Coordination of Benefits (COB) coverage. |
| 14 | `COB_MEM_TERM_DATE` | DATETIME |  | Termination date for a member on a Coordination of Benefits (COB) coverage. |
| 15 | `COB_MEM_COMMENT` | VARCHAR |  | Free-text comment for a member on a Coordination of Benefits (COB) coverage (member-level). |
| 16 | `COB_COMMENT` | VARCHAR |  | Free-text comment associated with a Coordination of Benefits (COB) coverage (coverage-level). |
| 17 | `COB_MEM_PRI_YN` | VARCHAR |  | Indicates if the Coordination of Benefits (COB) coverage should be considered primary for the member (Y=COB coverage is primary, N=COB coverage is not primary). |
| 18 | `COB_MEMBERS` | VARCHAR |  | Returns internal member IDs associated with Coordination of Benefits (COB) coverage. |
| 19 | `COB_PART_D_RX_BIN` | VARCHAR |  | The Beneficiary Identification Number (BIN) used for Part D Coordination of Benefits |
| 20 | `COB_PART_D_RX_PCN` | VARCHAR |  | The Processor Control Number (PCN) used for Part D Coordination of Benefits |
| 21 | `COB_PART_D_RX_GRP` | VARCHAR |  | The group used for Part D Coordination of Benefits |
| 22 | `COB_PART_D_RX_ID` | VARCHAR |  | The ID used for Part D Coordination of Benefits |
| 23 | `COB_COVERAGE_ID` | NUMERIC |  | The ID of the indemnity coverage that is associated with this Coordination of Benefits (COB) coverage. |
| 24 | `COB_SUB_EMPLOYMENT_STATUS_C_NAME` | VARCHAR | org | The employment status of the subscriber on this Coordination of Benefits (COB) coverage. |
| 25 | `COB_MEM_COURT_DECREE_C_NAME` | VARCHAR | org | The court decree for the member on this Coordination of Benefits (COB) coverage. |
| 26 | `COB_MEM_SUB_CUSTODY_C_NAME` | VARCHAR | org | The subscriber custody for the member on this Coordination of Benefits (COB) coverage. |
| 27 | `COB_SUBSCRIBER_NUM` | VARCHAR |  | The identifier for Coordination of Benefits (COB) coverages that is shared by all members on the same coverage. |
| 28 | `COB_MEMBER_NUM` | VARCHAR |  | Coordination of Benefits (COB) member identification number. |
| 29 | `MCARE_IS_SEC_PAYER_RSN_C_NAME` | VARCHAR |  | The Medicare is Secondary Payer (MSP) reason category ID for the COB coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

