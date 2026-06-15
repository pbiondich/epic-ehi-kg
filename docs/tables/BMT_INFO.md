# BMT_INFO

> Table for cellular therapy episode information.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 44  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `TX_DISCHARGE_DT` | DATETIME |  | Date transplant patient is discharged. |
| 3 | `TX_EVAL_DT` | DATETIME |  | The start date of the transplant evaluation. |
| 4 | `TX_REV_DT` | DATETIME |  | Stores the date when the transplant case was reviewed by the evaluation committee. |
| 5 | `TX_EPSD_TYPE_C_NAME` | VARCHAR |  | Indicates whether the patient is a donor or a recipient for the transplant. |
| 6 | `ADMISSION_DT` | DATETIME |  | Date of the admission for the transplant. |
| 7 | `TX_DT` | DATETIME |  | Stores the date the transplant was performed. If used with donors, it will instead store the donation/collection date. |
| 8 | `MOB_START_DT` | DATETIME |  | The start date of the process to increase the number of immature hematopoietic cells in the blood. |
| 9 | `CND_START_DT` | DATETIME |  | The start date of the regimen that will eliminate the individual's ability to make blood cells. |
| 10 | `HCT_TYPE_C_NAME` | VARCHAR |  | The category number for the hematopoietic cell transplantation type. |
| 11 | `PRIMARY_DX_C_NAME` | VARCHAR | org | The category number for the blood and marrow transplant diagnosis |
| 12 | `CELL_PRODUCT_C_NAME` | VARCHAR | org | The category number for the planned blood and marrow transplant product type. The product type is the source of the cells used in treatment. |
| 13 | `DONOR_SELECTION_C_NAME` | VARCHAR |  | The donor's selection status. |
| 14 | `DONOR_ELIGIBILITY_C_NAME` | VARCHAR |  | The donor's eligibility. |
| 15 | `DONOR_PREGNANCIES_NUM` | INTEGER |  | The number of pregnancies the donor had at time of collection. |
| 16 | `BMT_CARE_PATH_ID` | NUMERIC |  | The ID of the child care path associated with this clinical episode. |
| 17 | `TRANSPLANT_NUM` | INTEGER |  | Stores the transplant number. |
| 18 | `DONOR_SUITABILITY_C_NAME` | VARCHAR |  | The donor suitability. |
| 19 | `DONOR_AVAILABILITY_C_NAME` | VARCHAR |  | The donor's availability for transplant. |
| 20 | `PRIMARY_DX_OTHER` | VARCHAR |  | This diagnosis details when the user selects "other" as the diagnosis. |
| 21 | `CELL_PRODUCT_OTHER` | VARCHAR |  | This product details when the user selects "other" as the product type. |
| 22 | `CURRENT_PHASE_C_NAME` | VARCHAR |  | Current stage of the transplant. |
| 23 | `CURRENT_STATUS_C_NAME` | VARCHAR | org | Status of the current stage of the transplant. |
| 24 | `EPISODE_NOTE_ID` | VARCHAR |  | The episode note ID |
| 25 | `CURRENT_STATUS_DATE` | DATETIME |  | Date of the last transplant stage update. |
| 26 | `EPISODE_RECORD_STATUS_C_NAME` | VARCHAR |  | The episode status. |
| 27 | `BMT_PLAN_ID` | NUMERIC |  | Stores the ID of the blood and marrow transplant plan. |
| 28 | `RECIPIENT_DAY_0_DATE` | DATETIME |  | On donor episodes, this column contains the planned or actual Day 0 for the recipient to whom this patient is donating cells. On recipient episodes, this column contains the planned infusion date as of when the plan was verified. |
| 29 | `BMT_DNR_WORKUP_C_NAME` | VARCHAR |  | Whether the donor is the primary donor for workup, the backup donor, or neither |
| 30 | `BMT_DEFERRAL_C_NAME` | VARCHAR | org | Why the donor is deferred |
| 31 | `BMT_DEFERRAL_OTHER` | VARCHAR |  | Free text entry for why the donor is deferred |
| 32 | `ANC_OVRIDE_DATE` | DATETIME |  | Stores override absolute neutrophil count recovery date |
| 33 | `ANC_NO_REC_YN` | VARCHAR |  | Stores an override to indicate explicitly that the absolute neutrophil count did not recover. |
| 34 | `PLT_OVRIDE_DATE` | DATETIME |  | Stores override platelet recovery date |
| 35 | `PLT_NO_REC_YN` | VARCHAR |  | Stores an override to indicate explicitly that the platelet count did not recover. |
| 36 | `RECIPIENT_IDENT` | VARCHAR |  | The ID of the recipient to whom this patient is donating cells. Can hold a CRID. Valid values for an EPT IIT for ICX 110 for subject Recipient are valid values for this item. Note that this item is only used for donor episodes where the recipient is anonymous/unknown. |
| 37 | `IEC_THERAPY_TYPE_C_NAME` | VARCHAR | org | Immune effector cell therapy type. |
| 38 | `IEC_PRODUCT_C_NAME` | VARCHAR | org | Immune Effector Cell (IEC) product name, like from a specific manufacturer or a research product. |
| 39 | `IEC_INF_DATE_TYPE_C_NAME` | VARCHAR |  | The infusion date type for the IEC product. |
| 40 | `IEC_PRODUCT_TYPE_C_NAME` | VARCHAR |  | Indicates the IEC product's investigational status as either 1 - No or 2 - Yes. If the product has not been approved by an oversight body, it is investigational. |
| 41 | `INFUSION_CENTER_C_NAME` | VARCHAR | org | Cell Therapy Center responsible for a recipient's transplant or infusion procedure. For donors, it is the center responsible for collecting the donor's cells. |
| 42 | `CELL_THERAPY_CENTER_C_NAME` | VARCHAR |  | Determines which cell therapy center owns the patient episode. |
| 43 | `DNR_COLL_AGE_NUM` | NUMERIC |  | Age of the cell therapy donor at the time of collection. |
| 44 | `COLL_RC_AGE_UNITS_C_NAME` | VARCHAR |  | Units for the age of the cell therapy donor at the time of collection |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

