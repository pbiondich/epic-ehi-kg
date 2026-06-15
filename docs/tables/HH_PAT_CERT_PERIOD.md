# HH_PAT_CERT_PERIOD

> This table contains information about Home Health and Hospice contacts, including the contact's visit set and certification period.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | FK→ | Unique identifier for the patient. |
| 2 | `CONTACT_DATE_REAL` | FLOAT |  | Unique identifier for this contact for this patient. |
| 3 | `CARE_PLAN_ID` | VARCHAR |  | The care plan to which the contact is linked. Links to table CARE_INTEGRATOR. |
| 4 | `CERT_PERIOD` | INTEGER |  | The cert period to which the contact is linked. |
| 5 | `VISIT_SET` | INTEGER |  | The visit set of which the contact is a part. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 7 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 8 | `POC_ENC_NUM` | INTEGER |  | The serial number of the plan of care encounter that the contact created. |
| 9 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 10 | `REPORTING_DISC_C_NAME` | VARCHAR |  | This item stores the reporting discipline of the provider who completed the encounter. |
| 11 | `POC_ENC_DEL_YN` | VARCHAR |  | Stores if the Plan of Care encounter's certification period has been deleted. |
| 12 | `IS_SPOC_CERT_ENC_YN` | VARCHAR |  | Whether this encounter created a certification period that is associated with a plan of care. |
| 13 | `VISIT_SET_ID` | NUMERIC | FK→ | The unique ID of the visit set this encounter is part of. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

