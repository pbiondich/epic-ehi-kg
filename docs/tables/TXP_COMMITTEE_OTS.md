# TXP_COMMITTEE_OTS

> Transplant committee review over time single response items.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `TXP_COMM_DECISION_C_NAME` | VARCHAR | org | The transplant committee review decision on whether a patient can be listed for a transplant. |
| 6 | `TXP_COMMITTEE_DT` | DATETIME |  | The expected date the transplant committee will review the candidate. |
| 7 | `TXP_CHAIR_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `TXP_COMMITTEE_TYP_C_NAME` | VARCHAR |  | The type of committee review. |
| 9 | `TXP_ELIG_OTHER` | VARCHAR |  | Transplant waitlist eligibility other criteria for committee review. |
| 10 | `TXP_ABS_CIND_OTHER` | VARCHAR |  | Other absolute contraindications, which cause a transplant patient to be denied a transplant. |
| 11 | `TXP_REL_CIND_OTHER` | VARCHAR |  | Other relative contraindications, which either cause a transplant patient to be denied a transplant or require the patient to be re-evaluated later. |
| 12 | `TXP_CR_EPSD_PHASE_C_NAME` | VARCHAR |  | The phase of the transplant episode at the time of documenting the decision in the committee review encounter. |
| 13 | `TXP_CR_EPSD_STAT_C_NAME` | VARCHAR | org | The status of the transplant episode at the time of documenting the decision in the committee review encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

