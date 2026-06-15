# PATIENT_HMT_STATUS

> This table contains information on the due status of health maintenance topics.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `HMT_PPN_UNTL_DT` | DATETIME |  | The date until which a Health Maintenance topic is postponed. |
| 4 | `HMT_PPN_RSN_C_NAME` | VARCHAR | org | The postpone reason category number for a Health Maintenance topic which was postponed. |
| 5 | `HMT_LAST_UPDATE_DT` | DATETIME |  | The last completion date for the patient's Health Maintenance topic. |
| 6 | `HM_ORDER_STATUS_YN` | VARCHAR |  | This item indicates if the Health Maintenance (HM) topic has been addressed by signing an order. If an appropriate active order was found during the HM update, this will be set to yes. |
| 7 | `ACTIVE_SUBTOPIC_ID` | NUMERIC |  | Stores the active subtopic for a combination topic |
| 8 | `ACTIVE_SUBTOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 9 | `ACTIVE_HM_PLAN_ID` | NUMERIC |  | Stores the Health Maintenance plan that is currently active for the topic |
| 10 | `ACTIVE_HM_PLAN_ID_HM_PLAN_NAME` | VARCHAR |  | The name of the Health Maintenance Plan record. |
| 11 | `HM_TENTATIVE_YN` | VARCHAR |  | Boolean value indicating whether the Health Maintenance topic's next follow-up is tentative and requiring review. |
| 12 | `HM_ACTIVE_SERIES_C_NAME` | VARCHAR | org | Stores the active immunization series the patient is currently on. |
| 13 | `HM_NEW_ATTEST_YN` | VARCHAR |  | This item indicates if the Health Maintenance (HM) topic has a patient attestation that needs review. If an active attestation was found during the HM update, this will be set to yes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

