# HH_CPLN_ENC

> This table no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). This table contains Home Health overtime single items from the LCP (care plan) master file.

**Primary key:** `CAREPLAN_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the CARE_INTG_ID column in the CARE_INTEGRATOR or CAREPLAN_INFO tables to report on this item instead. Unique identifier for the care plan. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the CONTACT_DATE_REAL column in the CARE_INTEGRATOR or CAREPLAN_CNCT_INFO tables to report on this item instead. Unique identifier for this contact for this patient. |
| 3 | `CONTACT_NUMBER` | VARCHAR |  | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the CONTACT_NUMBER column in the CAREPLAN_CNCT_INFO table to report on this item instead. Contact number linked to the care plan. |
| 4 | `CONTACT_DATE` | DATETIME |  | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the CONTACT_DATE column in the CAREPLAN_CNCT_INFO or CARE_INTEGRATOR tables to report on this item instead. The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the CM_CT_OWNER_ID column in the CARE_INTEGRATOR or CAREPLAN_CNCT_INFO tables to report on this item instead. The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 6 | `USER_ID` | VARCHAR | FK→ | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the USER_ID column in the CARE_INTEGRATOR table to report on this item instead. ID of the user who created the contact. Links to table CLARITY_EMP. |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `LAST_EDIT_INST` | DATETIME (Local) |  | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the LAST_EDIT_TIME column in the CARE_INTEGRATOR table to report on this item instead. Instance at which the care plan was last edited. |
| 9 | `CTCT_SERIAL_NUM` | NUMERIC |  | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the CTCT_SERIAL_NUM column in the CAREPLAN_CNCT_INFO table to report on this item instead. The contact serial number (CSN) of the contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

