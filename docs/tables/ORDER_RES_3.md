# ORDER_RES_3

> The ORDER_RES_3 table contains result finding information for an order. Result findings include mammography pathology results, cardiovascular palette findings, and other result findings.

**Overflow of:** [ORDER_RES](ORDER_RES.md)  
**Primary key:** `FINDING_ID`  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LUNG_SEC_HIST_C_NAME` | VARCHAR |  | Determines the type of cancer that was found in the secondary cell type of the tissue sample. |
| 3 | `LUNG_SEC_NONSMALL_C_NAME` | VARCHAR |  | If secondary histology is "Non Small Cell Lung Cancer", then this item specifies the type of the cancer. |
| 4 | `LUNG_SEC_NS_COMM` | VARCHAR |  | If Secondary histology - Non-Small Cell Lung Cancer is Other, Specify, then this item holds a free text description of the cancer. |
| 5 | `FIRST_DOCUMENTED_UTC_DTTM` | DATETIME (UTC) |  | The date and time when this lesion was first documented. |
| 6 | `FOLLOWUP_CUR_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `FINDING_HIDDEN_YN` | VARCHAR |  | Indicates whether a finding in the image documentation section in study review for a breast imaging study is hidden. 'Y' indicates that a finding has been hidden. 'N' or NULL indicate that a finding has not been hidden. |
| 8 | `FINDING_SUP_MOPS_YN` | VARCHAR |  | Indicates whether a finding in the image documentation section in study review for a MOPS breast imaging study is suppressed. 'Y' indicates that a finding has been suppressed. 'N' or NULL indicate that a finding has not been suppressed. |
| 9 | `LUNG_HISTOLOGY_OTHER` | VARCHAR |  | If RES 52271 - LUNG HISTOLOGY contains Other, this item contains a free text description of the cancer. |
| 10 | `LUNG_SECONDARY_HISTOLOGY_OTHER` | VARCHAR |  | If RES 52283 - LUNG SECONDARY HISTOLOGY contains Other, this item contains a free text description of the secondary cancer. |
| 11 | `ANAT_LOC_CODE_SYS` | VARCHAR |  | The terminology system used to specifiy the anatomic location of the observation. |
| 12 | `ANAT_LOC_CODE` | VARCHAR |  | The anatomic location of the observation. This code is part of the anatomic location code system (stored in I RES 52560). |
| 13 | `ANAT_LOC_NAME` | VARCHAR |  | The display name of the observation's anatomic location code (I RES 52561). |
| 14 | `OBS_CODE_SYS` | VARCHAR |  | The terminology system that the observation code (I RES 52566) belongs to. |
| 15 | `OBS_CODE` | VARCHAR |  | The element set (observation) that this record represents. This code is part of the observation code system (stored in I RES 52565). |
| 16 | `OBS_NAME` | VARCHAR |  | The display name of the observation code (I RES 52566). |
| 17 | `FINDING_MNLY_EXCLD_YN` | VARCHAR |  | This item indicates whether a finding was excluded from the result. 'Y' indicates that a finding is excluded from the result. 'N' or NULL indicate that a finding has not been excluded. |
| 18 | `RSLT_TRK_RULE_ID` | VARCHAR |  | Stores the .1 of the CER rule which was evaluated to create this finding. |
| 19 | `RSLT_TRK_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 20 | `LUNG_HIST_SM_C_NAME` | VARCHAR |  | Lung cancer histology for a small cell cancer pathology finding. |
| 21 | `LUNG_SEC_HIST_SM_C_NAME` | VARCHAR |  | Lung cancer histology of the secondary cell type for a pathology finding when the histology is "Small Cell Lung Cancer". |
| 22 | `LUNG_T_PREFIX_C_NAME` | VARCHAR |  | Lung cancer histology T status prefix for a pathology finding. |
| 23 | `LUNG_N_PREFIX_C_NAME` | VARCHAR |  | Lung cancer histology N status prefix for a pathology finding. |
| 24 | `LUNG_M_PREFIX_C_NAME` | VARCHAR |  | Lung cancer histology M status prefix for a pathology finding. |
| 25 | `ENDO_PROC_SRC_IDENT` | VARCHAR |  | Stores the reference ID of the endoscopy procedure this finding is related to. |
| 26 | `ENDO_PROC_DDP_IDENT` | VARCHAR |  | Stores the deduplicated reference ID of the endoscopy procedure this finding is related to. |
| 27 | `RSLT_TRK_REV_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant when this actionable finding was reviewed by a reading provider in Study Review. |
| 28 | `OUTDATED_REV_FND_YN` | VARCHAR |  | Flag indicating that this reviewed finding no longer evaluates to true for its rule |
| 29 | `RULE_REVIEW_USER_ID` | VARCHAR |  | Stores the user who reviewed this rule-based finding in Study Review. |
| 30 | `RULE_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

