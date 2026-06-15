# RXMA_SITE_OF_CARE

> Medication Access Site of Care documentation.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOC_LOCATION_C_NAME` | VARCHAR | org | Site of care location |
| 4 | `SOC_DETERMINATION_C_NAME` | VARCHAR |  | Outcome for this site of care investigation |
| 5 | `SOC_REJECT_RSN_C_NAME` | VARCHAR | org | Reason for a site not being approved |
| 6 | `AUTH_REFERRAL_ID` | NUMERIC |  | Auth referral with codes related to this site of care |
| 7 | `SOC_PAT_PREF_C_NAME` | VARCHAR | org | Patient's opinion on using the related site of care |
| 8 | `REQUIRED_PHARMACY_ID` | NUMERIC |  | If a restriction exists, the pharmacy the site of care is restricted to. |
| 9 | `REQUIRED_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 10 | `SITE_COMMENTS` | VARCHAR |  | Comments on additional site restrictions |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

