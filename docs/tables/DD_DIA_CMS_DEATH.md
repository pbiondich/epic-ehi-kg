# DD_DIA_CMS_DEATH

> This table contains data elements submitted for CMS ESRD death forms (CMS-2746).

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 35  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `FORM_IDENTIFIER` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It stores a dialysis patient's form 2746 ID. |
| 3 | `ADMISSION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 4 | `PAT_FIRST_NAME` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's first name. |
| 5 | `PAT_MIDDLE_INITIAL` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's middle name initial. |
| 6 | `PAT_LAST_NAME` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's last name. |
| 7 | `DLYS_NAME_SUFFIX_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores a dialysis patient's name suffix. |
| 8 | `DLYS_PAT_SEX_C_NAME` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's sex assigned at birth. |
| 9 | `PAT_BIRTH_DATE` | DATETIME |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's date of birth. |
| 10 | `PAT_SSN` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's Social Security Number. |
| 11 | `PAT_HICNUM` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's Medicare health insurance claim number. |
| 12 | `PAT_MBI_NUM` | VARCHAR |  | It stores a dialysis patient's Medicare Beneficiary Identifier number for dialysis regulatory reporting. |
| 13 | `PHYSICAL_ADDRESS_STATE_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores the state from a dialysis patient's physical address. |
| 14 | `DIA_CMS_DEATH_MODALITY_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It stores a dialysis patient's treatment modality at the time of death. |
| 15 | `DIA_CMS_DEATH_PLACE_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It stores a dialysis patient's location at the time of death. |
| 16 | `PRIMARY_DIA_CMS_DEATH_CAUSE_C_NAME` | VARCHAR | org | This item is used in CMS death form 2746 reporting. It stores a dialysis patient's primary cause of death. |
| 17 | `SEC_1_DIA_CMS_DEATH_CAUSE_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It stores a dialysis patient's secondary cause of death. |
| 18 | `SEC_2_DIA_CMS_DEATH_CAUSE_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It indicates the second secondary cause of death of an expired dialysis patient. |
| 19 | `SEC_3_DIA_CMS_DEATH_CAUSE_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It indicates the third secondary cause of death of an expired dialysis patient. |
| 20 | `SEC_4_DIA_CMS_DEATH_CAUSE_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It indicates the fourth secondary cause of death of an expired dialysis patient. |
| 21 | `OTHER_DEATH_CAUSE` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It stores a dialysis patient's cause of death if primary or secondary cause of death indicates other cause of death. |
| 22 | `WAS_DIA_TREAT_DISCON_YN` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It indicates whether or not renal therapy was discontinued prior to a patient's death. |
| 23 | `DLYS_TRT_DISCH_RSN_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It stores the reason for discontinuing renal therapy prior to a patient's death. |
| 24 | `LAST_TREATMENT_DATE` | DATETIME |  | This item is used in CMS death form 2746 reporting. It stores the date of last dialysis treatment if renal therapy was discontinued prior to a patient's death. |
| 25 | `DIA_CMS_DISC_REQUEST_C_NAME` | VARCHAR | org | This item is used in CMS death form 2746 reporting. It stores whether or not the discontinuation of renal therapy occurred after patient or family request. |
| 26 | `TRANSPLANT_DATE_UKNWN_YN` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It indicates whether the date of an expired patient's most recent kidney transplant is unknown. |
| 27 | `LAST_KIDNEY_TRANSPLANT_DATE` | DATETIME |  | This item is used in CMS death form 2746 reporting. It stores an expired dialysis patient's most recent kidney transplant date. |
| 28 | `DIA_CMS_DEATH_TXP_TYPE_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It stores the most recent kidney transplant type that a dialysis patient received before death. |
| 29 | `GRAFT_FUNC_DEATH_DIA_CMS_YNU_C_NAME` | VARCHAR | org | This item is used in CMS death form 2746 reporting. It indicates whether or not a functioning graft was present at the time of a patient's death. |
| 30 | `WAS_TRT_RESUMED_DIA_CMS_YNU_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It indicates whether an expired patient, prior to death, resumed renal therapy after receiving a transplant. |
| 31 | `RECV_HOSPIC_CARE_DIA_CMS_YNU_C_NAME` | VARCHAR |  | This item is used in CMS death form 2746 reporting. It indicates whether or not a dialysis patient was receiving hospice care prior to death. |
| 32 | `TREATMENT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 33 | `PAT_HAD_TRANSPLANT_C_NAME` | VARCHAR |  | Indicates whether the patient ever received a kidney transplant for this form. 'Y' indicates the patient received at least one kidney transplant. 'N' indicates the patient did not receive a kidney transplant. 'UNKNOWN' or NULL indicates that it is not known whether the patient received a kidney transplant prior to death. |
| 34 | `WAS_ACUTE_DIALYSIS_RECEIVED_C_NAME` | VARCHAR |  | Indicates whether the patient received a short-term (acute) course of dialysis prior to death for this form. 'Y' indicates that the patient received a short-term (acute) course of dialysis prior to death. 'N' indicates that the patient did not receive a short-term (acute) course of dialysis prior to death. 'UNKNOWN' or NULL indicate that it is not known whether the patient received a short-term (acute) course of dialysis prior to death. |
| 35 | `DIAL_DISC_HOSPICE_REL_YN` | VARCHAR |  | Indicates whether the patient's dialysis treatment was discontinued related to hospice care for this form. 'Y' indicates that the patient's dialysis treatment was discontinued related to hospice care. 'N' or NULL indicate that the patient's dialysis treatment was not discontinued or treatment was discontinued, but not related to hospice care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

