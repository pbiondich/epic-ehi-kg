# PAT_INDICATOR_INFO

> The PAT_INDICATOR_INFO table contains information about your patient genomic indicator records.

**Primary key:** `PAT_IND_CSN_ID`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | FK→ | This column contains the unique identifier (.1 item) for the pt indicators record. |
| 2 | `CONTACT_DATE` | DATETIME |  | This column contains the date of this contact in calendar format. |
| 3 | `PAT_IND_CSN_ID` | NUMERIC | PK | This column contains the contact serial number (CSN) of the contact. |
| 4 | `UPDATE_USER_ID` | VARCHAR |  | This column contains the EMP ID of the user that has made an update to this PGI record. |
| 5 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `INSTANT_OF_ENT_DTTM` | DATETIME (Local) |  | This column contains the instant of entry when the genomic indicator record is edited. |
| 7 | `HIDDEN_FROM_PAT_YN` | VARCHAR |  | This column contains whether the genomic indicator is hidden from the patient. If null, the default is No. |
| 8 | `REMOVAL_REASON_C_NAME` | VARCHAR | org | This column contains the reason why a patient's genomic indicator was marked as "removed" from the patient's genomic indicators list. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_INDICATOR_ID` | [PAT_INDICATOR](PAT_INDICATOR.md) | sole_pk | high |

