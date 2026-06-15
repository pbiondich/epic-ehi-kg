# ORGAN

> Table for general organ information about transplanted and native organs.

**Primary key:** `ORG_RECORD_ID`  
**Columns:** 65  
**Org-specific columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `TX_ORG_SRC_C_NAME` | VARCHAR | org | State of the body where organ came from |
| 3 | `ORG_DEATH_ID` | NUMERIC |  | Reasons for organ graft death |
| 4 | `ORG_NOTE_ID` | VARCHAR |  | Note about the organ |
| 5 | `ORG_STAT_C_NAME` | VARCHAR | org | Status of organ throughout the transplant procedure |
| 6 | `ORG_WT` | NUMERIC |  | Organ's weight in ounces. |
| 7 | `ANTIGEN_MATCHES` | NUMERIC |  | Number of antigen matches 0 - 6 |
| 8 | `ORG_PROCUREMENT_DT` | DATETIME |  | Procurement date of organ from donor |
| 9 | `ORG_PERFUSION_MIN` | NUMERIC |  | Perfusion time of organ minutes component |
| 10 | `ORG_WISCHEMIA_MIN` | NUMERIC |  | Time in warm ischemia minutes component |
| 11 | `ORG_CISCHEMIA_MIN` | NUMERIC |  | Time spent in cold ischemia minute component |
| 12 | `CLAMP_INST_ON_TM` | DATETIME (Local) |  | Instant when clamp was put on |
| 13 | `CLAMP_INST_OFF_TM` | DATETIME (Local) |  | Instant clamp taken off |
| 14 | `ORG_DONATION_CRIT_C_NAME` | VARCHAR | org | Stores if the organ is classified as a standard criteria donor or an expanded criteria donor. This is a donor classification. |
| 15 | `PRIMARY_WARM_ISCH` | NUMERIC |  | Minutes organ is in primary warm ischemia |
| 16 | `ORG_FAIL_DT` | DATETIME |  | Date which the transplanted organ failed |
| 17 | `ORG_FAIL_METHOD_C_NAME` | VARCHAR | org | Method by which organ failure date was determined |
| 18 | `ORG_MATCHTYPE_C_NAME` | VARCHAR | org | Stores what kind of match type the organ was |
| 19 | `ORG_PRESERVE_C_NAME` | VARCHAR | org | Technique used for preserving the organ |
| 20 | `ORG_PROCEDURE_TYP_C_NAME` | VARCHAR | org | Technique used for transplanting the organ |
| 21 | `FINAL_RESISTANCE` | NUMERIC |  | Final resistance at transplant if organ was on a pump |
| 22 | `FINAL_FLOW_RATE` | NUMERIC |  | Final flow rate at transplant if organ was on a pump |
| 23 | `ORGAN_REMOVAL_DT` | DATETIME |  | Date the organ was removed after it failed. |
| 24 | `UNOS_PRIMARY_FAIL_C_NAME` | VARCHAR | org | The primary reason for organ failure from the United Network for Organ Sharing (UNOS). |
| 25 | `UNOS_PRIMARY_OTHER` | VARCHAR |  | Free text entry listing the primary reason for organ failure. If no entry exists in the category list, this explains the reason for organ failure. |
| 26 | `ORGAN_NUM` | NUMERIC |  | The sequential number of the organ transplanted. |
| 27 | `ORGAN_SIZE` | NUMERIC |  | The volume of the organ in mL. |
| 28 | `UNOS_CONTRIB_OTHER` | VARCHAR |  | Free text entry listing a contributory cause of organ failure. If no entry exists in the category list, this explains the reason for organ failure. |
| 29 | `NATIVE_ORGAN_YN` | VARCHAR |  | Set flag to yes to indicate that the record is for a native organ |
| 30 | `NAT_PRIMARY_FAIL_C_NAME` | VARCHAR | org | Primary reason for native organ failure |
| 31 | `NAT_PRIMARY_OTHER` | VARCHAR |  | Other primary reason for native organ failure |
| 32 | `NAT_CONTRIB_OTHER` | VARCHAR |  | Other contributory reason for native organ failure |
| 33 | `ORG_RECEIVED_ON_C_NAME` | VARCHAR | org | Was the organ received on ice or pump |
| 34 | `ORGAN_STAYED_ON_C_NAME` | VARCHAR | org | If the organ was received on ice, did it stay on ice? If organ was received on pump, did it remain on pump? |
| 35 | `INDUCTION_USED_C_NAME` | VARCHAR |  | Was an induction technique used |
| 36 | `KIDNEY_BIOPSY_YN` | VARCHAR |  | Was a preimplantation kidney biopsy done |
| 37 | `PERIOP_TRANSFUSION` | NUMERIC |  | Number of perioperative blood transfusions. |
| 38 | `INTRA_OP_TRANSFUSN` | NUMERIC |  | Number of intra-operative blood transfusions |
| 39 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status |
| 40 | `PREOP_BLOOD_TRANS` | NUMERIC |  | The number of pre-operative blood transfusions. |
| 41 | `ANASTOMOSIS_ST_DTTM` | DATETIME (Local) |  | Indicates the anastomosis start time for the transplant. |
| 42 | `PORT_CLAMP_OFF_DTTM` | DATETIME (Local) |  | Indicates the portal clamp off time for the transplant. |
| 43 | `CDC_YN` | VARCHAR |  | Does the donor have risk factors for blood-borne disease transmission. |
| 44 | `MATCH_RUN` | VARCHAR |  | The match run ID for the organ. |
| 45 | `OPO_C_NAME` | VARCHAR | org | The organ procurement organization which procured the organ. |
| 46 | `OPO_RISK_YN` | VARCHAR |  | Whether the donor is considered high risk by the organ procurement organization. |
| 47 | `LINKED_ORGAN_ID` | NUMERIC |  | If the current organ is linked to another organ, this stores the ID of the linked organ. This linked organ provides the donor information for the current organ. |
| 48 | `EXT_TEAM_RECOVER_YN` | VARCHAR |  | Was the organ procured by an external team. |
| 49 | `RECOVERY_FAC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 50 | `REC_FAC_OTHER` | VARCHAR |  | The facility where the organ was recovered, if none is listed in the organ recovery facility. |
| 51 | `ORG_TISCHEMIA_MIN` | INTEGER |  | Total ischemia time in minutes. |
| 52 | `FAILURE_DT_EST_C_NAME` | VARCHAR |  | Indicates whether the failure date was estimated. |
| 53 | `DNR_RISK_PRF_PCT` | INTEGER |  | The percentage score of donor risk profile index. |
| 54 | `DNR_KI_EXTRACT_INST_DTTM` | DATETIME (UTC) |  | Indicates the donor organ extraction time. |
| 55 | `ORGAN_CLASS_C_NAME` | VARCHAR |  | The organ classification. |
| 56 | `A_MISMATCHES_NUM` | INTEGER |  | Indicate the number of A mismatches between the donor and the recipient. |
| 57 | `B_MISMATCHES_NUM` | INTEGER |  | Indicate the number of B mismatches between the donor and the recipient. |
| 58 | `DR_MISMATCHES_NUM` | INTEGER |  | Indicate the number of DR mismatches between the donor and the recipient. |
| 59 | `POSTOP_BLOOD_TRANS` | INTEGER |  | The number of post-operative blood transfusions. |
| 60 | `MACHINE_PERFUSION_ST_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the organ perfusion started. |
| 61 | `MACHINE_PERFUSION_END_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the organ perfusion ended during the transplant surgery. |
| 62 | `MACHINE_PERFUSION_TOTAL_MIN` | NUMERIC |  | The number of minutes the organ was perfused using a machine. |
| 63 | `ORGAN_RECORD_TYPE_C_NAME` | VARCHAR |  | The organ type category ID for the ORG. |
| 64 | `RAD_THP_VOL_DESCRIPTION` | VARCHAR |  | Description of the radiotherapy volume |
| 65 | `ALLOC_DNR_ABO_C_NAME` | VARCHAR |  | Specifies the blood type used for the allocation of the organ. This is only used for Living Donors. If blank, then the donor's blood type was used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

