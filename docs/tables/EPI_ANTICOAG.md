# EPI_ANTICOAG

> This contains episode information pertaining to anticoagulation therapy. Most fields are accessed through the anticoagulation enrollment form. There is a corresponding encounter table, PAT_ENC_ANTICOAG. Do not assume that all patients on anticoagulation therapy have a record in this table. The best way to determine anticoagulation episodes is by using the SUM_BLK_TYPE_ID in the EPISODE table.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 13  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. NOTE: This table is filtered to include only non-inpatient episodes. Inpatient episode data can be found in the table IP_EPISODE_LINK (first released with system 2002). |
| 2 | `INR_GOAL_C_NAME` | VARCHAR | org | Data item to store the INR goal, which is a range, for this episode of anticoagulation |
| 3 | `RESPONSIBLE_HIP_ID` | NUMERIC |  | Responsible group for anticoagulation therapy |
| 4 | `RESPONSIBLE_HIP_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 5 | `TARGET_END_DATE` | DATETIME |  | Target end date of anticoagulation therapy |
| 6 | `LAB_LOCATION_C_NAME` | VARCHAR | org | Patient's preferred INR lab location |
| 7 | `PREFERRED_LAB_ID` | NUMERIC |  | The unique ID of the lab that is the patient's preferred lab for international normalized ratio (INR) tests. This column is frequently used to link to the CLARITY_LLB table. |
| 8 | `PREFERRED_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 9 | `WEEKLY_MAX_DOSE` | NUMERIC |  | Weekly maximum coumadin/warfarin dose |
| 10 | `DISCONT_REASON_C_NAME` | VARCHAR | org | Reason for discontinuing the anticoagulation therapy. |
| 11 | `NEXT_INR_DATE` | DATETIME |  | The date the patient should return for their next INR check. |
| 12 | `INDEFINITE_TREAT_YN` | VARCHAR |  | Specifies if the patient's treatment is indefinite. |
| 13 | `REFERRING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

