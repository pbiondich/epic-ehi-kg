# PAT_ENC_5

> This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, and PAT_ENC_4 tables. It contains additional information related to patient encounters or appointments.

**Overflow of:** [PAT_ENC](PAT_ENC.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 34  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `PUBLIC_HOUSING_YN` | VARCHAR |  | This item tracks whether or not a patient lived in public housing at the time of a given encounter. |
| 4 | `PVT_HOSP_ENC_C_NAME` | VARCHAR | org | The category value corresponding to the private encounter setting for this patient contact. |
| 5 | `LINK_INS_TYPE_C_NAME` | VARCHAR | org | The lab insurance type category ID for the insurance type used with the ordering encounter in EpicCare Link. |
| 6 | `PAT_VER_HCA_C_NAME` | VARCHAR |  | Contains the patient's response on the Health Care Agent Verification screen in Welcome; either "Patient indicated data was correct" or "Patient indicated they want to discuss care decisions with a clinician." |
| 7 | `EXT_GRP_IDNT` | VARCHAR |  | This column holds appointment group identifiers assigned by external systems. If two appointments have the same external group identifier, they were checked in as a group, and they will be treated as a group in Epic. |
| 8 | `EXT_GRP_SRC_C_NAME` | VARCHAR | org | Holds the source of an external group identifier in EXT_GRP_IDNT. If two rows have the same value for their external group source, the same external system grouped the appointments. |
| 9 | `PREPAY_SET_BY_USER_YN` | VARCHAR |  | This item will be set to Yes if the prepay due for this visit was manually set by a user. |
| 10 | `PREPAY_UPDATE_USER_ID` | VARCHAR |  | User who last updated the prepay due amount. |
| 11 | `PREPAY_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `PREPAY_UPDATE_INST_DTTM` | DATETIME (UTC) |  | The last instant the prepay due for the visit was updated. |
| 13 | `PREPAY_CALC_SCENARIO` | VARCHAR |  | Stores the scenario/reason why the corresponding payment needs to be collected upfront from the patient. |
| 14 | `AUTHCERT_ID` | NUMERIC |  | The unique ID of the auth/cert associated with the patient contact. |
| 15 | `ED_REF_CALLBAK_YN` | VARCHAR |  | Whether a referring provider requests a call back from the ED physician at the end their visit |
| 16 | `ED_REF_CALLBAK_P_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `ED_REF_CALLBAK_C_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 18 | `ED_REF_CALLBAK_NUM` | VARCHAR |  | Phone number to contact the referring provider at after ED visit |
| 19 | `IS_ON_DEMAND_VV_YN` | VARCHAR |  | Denotes whether this contact is an on-demand video visit. |
| 20 | `ATTR_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 21 | `PAT_DTREE_ANSWER_ID` | VARCHAR |  | Stores the decision tree that was completed by the patient which resulted in this encounter being created. |
| 22 | `PREPAY_DISCNT_AMT` | NUMERIC |  | Stores the total amount that was discounted because a patient paid early. |
| 23 | `PREPAY_DISCNT_PCT` | NUMERIC |  | Stores the percent that was used to calculate the prepay discounted amount. |
| 24 | `PREPAY_PROPOSED_DISCNT_AMT` | NUMERIC |  | Stores what the prepay discount would be if it applied. |
| 25 | `PREPAY_DISCNT_CALC_RULE_ID` | VARCHAR |  | Stores the rule that was used to determine the prepay discount percent. |
| 26 | `PREPAY_DISCNT_CALC_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 27 | `PREPAY_DISCNT_CALC_PCT` | NUMERIC |  | Stores the system calculated percent for a prepay discount. |
| 28 | `PREPAY_DISCNT_OVRIDE_AMT` | NUMERIC |  | If a user overrides the prepay discount amount, the override will be stored here and we will no longer use rules to determine the prepay discount. |
| 29 | `PREPAY_DISCNT_OVRIDE_PCT` | NUMERIC |  | If a user overrides the prepay discount percent, the override will be stored here and we will no longer use rules to determine the prepay discount. |
| 30 | `PREPAY_DISCNT_OVRIDE_USER_ID` | VARCHAR |  | If a user overrides the prepay discount, this will store the user who made the override. |
| 31 | `PREPAY_DISCNT_OVRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `PREPAY_DISCNT_OVRIDE_CMT` | VARCHAR |  | If a user overrides the prepay discount and adds a comment about why they did so, the comment will be stored here. |
| 33 | `PREPAY_DISCNT_OVRIDE_DTTM` | DATETIME (Local) |  | If a user overrides the prepay discount, this will store the instant it was overridden. This item is mainly used for reference purposes. |
| 34 | `EVISIT_STATUS_C_NAME` | VARCHAR |  | The current status of the e-visit encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PAT_ENC](PAT_ENC.md).

