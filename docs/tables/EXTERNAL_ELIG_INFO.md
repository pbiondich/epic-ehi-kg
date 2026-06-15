# EXTERNAL_ELIG_INFO

> The EXTERNAL_ELIG_INFO table contains the external eligibility information returned by Rx Hub.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_ELIG_ID` | VARCHAR |  | The unique ID of the external eligibility that is returned by RxHub. |
| 4 | `EXT_ELIG_TYPE_C_NAME` | VARCHAR | org | The external eligibility type category number for the external eligibility information returned by RX Hub. |
| 5 | `EXTERNAL_ELIG_V_YN` | VARCHAR |  | Indicates whether external eligibility is active. |
| 6 | `EXTERNAL_ELIG_S_ID` | VARCHAR |  | This is the unique ID of the external eligibility source returned by RxHub. |
| 7 | `EXT_ELIG_MATCH_YN` | VARCHAR |  | Indicates whether external eligibility has been user verified. |
| 8 | `EXT_ELIG_NCPDP_ID` | VARCHAR |  | Stores NCPDP value from Rx Eligibility responses into EPT 42021: EXTERNAL_ELIGIBILITY NCPDP VALUE. |
| 9 | `EXT_ELIG_CH_ID` | VARCHAR |  | Cardholder ID for mail order |
| 10 | `EXT_ELIG_CH_NAME` | VARCHAR |  | Cardholder Name for mail order |
| 11 | `EXT_ELIG_GRP_ID` | VARCHAR |  | Group ID for mail order |
| 12 | `EXT_ELIG_PCN_NUM` | VARCHAR |  | Plan network ID returned from SureScripts |
| 13 | `EXT_ELIG_BIN_NUM` | VARCHAR |  | Bin number returned from SureScripts |
| 14 | `EXT_ELIG_DEP_YN` | VARCHAR |  | Whether member is a dependent of the coverage |
| 15 | `EXT_ELIG_PAYOR_NAME` | VARCHAR |  | Holds the PBM (Payor) name received on the e-prescribing eligibility response. |
| 16 | `EXT_ELIG_CH_LNAME` | VARCHAR |  | Holds the cardholder last name as received from the e-prescribing interface. |
| 17 | `EXT_ELIG_CH_FNAME` | VARCHAR |  | Holds the cardholder first name as received from the e-prescribing interface. |
| 18 | `EXT_ELIG_CH_MNAME` | VARCHAR |  | Holds the cardholder middle name as received from the e-prescribing interface. |
| 19 | `EXT_ELIG_CH_SUFFIX` | VARCHAR |  | Holds the cardholder suffix as received from the e-prescribing interface. |
| 20 | `EXT_ELIG_GRP_NAME` | VARCHAR |  | Holds the Group Name as received from the e-prescribing interface. |
| 21 | `EXT_ELIG_ENT_IDENT_C_NAME` | VARCHAR |  | Contains the entity identifier code as received from the e-prescribing interface. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

