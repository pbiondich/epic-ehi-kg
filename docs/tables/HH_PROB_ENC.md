# HH_PROB_ENC

> This table no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). This table contains Home Health care plan problems overtime single items information. This information is entered in the Care Plan task on the Home Health Remote Client.

**Primary key:** `PROBLEM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the PROB_CONTACT column in the PROB_CONTACT table to report on this item instead. Unique identifier for the care plan problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the CONTACT_DATE_REAL column in the PROB_CONTACT table to report on this item instead. Unique identifier for this contact for this patient. |
| 3 | `CONTACT_NUMBER` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the CONTACT_NUMBER column in the PROB_CONTACT table to report on this item instead. The serial number of the contact on the care plan problem record. |
| 4 | `CONTACT_DATE` | DATETIME |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the CONTACT_DATE column in the PROB_CONTACT table to report on this item instead. The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the CM_CT_OWNER_ID column in the PROB_CONTACT table to report on this item instead. The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 6 | `USER_ID` | VARCHAR | FK→ | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the PROB_CONTACT column in the PROB_CONTACT table to report on this item instead. Unique identifier of the user who created the contact. Links to table CLARITY_EMP. |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `LAST_EDIT_INST` | DATETIME (Local) |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the LAST_EDIT_TIME column in the PROB_CONTACT table to report on this item instead. Instant at which care plan problem was last edited. |
| 9 | `IS_RESOLVED_C_NAME` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the IS_RESOLVED_C column in the PROB_CONTACT table to report on this item instead. Indicates whether the care plan problem is resolved. 'Y' indicates that the care plan problem is resolved. 'N' or NULL indicate that the care plan problem is not resolved. Links to category list ZC_LPB_IS_RESOLVED. |
| 10 | `PRIORITY_C_NAME` | VARCHAR | org | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the CP_PRIORITY_C column in the PROB_CONTACT table to report on this item instead. Care plan problem priority. Links to category list ZC_CP_PRIORITY. |
| 11 | `PROB_START_DT` | DATETIME |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the START_DATE column in the PROB_CONTACT table to report on this item instead. Care plan problem start date. |
| 12 | `PROB_RESOLV_DT` | DATETIME |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the RESOLVED_DATE column in the PROB_CONTACT table to report on this item instead. Care plan problem resolved date. |
| 13 | `CARE_PLAN_CSN` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the CAREPLAN_CSN_ID column in the PROB_CONTACT table to report on this item instead. The unique contact serial number of the care plan problem contact that is associated with the care plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

