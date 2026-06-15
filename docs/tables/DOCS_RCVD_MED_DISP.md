# DOCS_RCVD_MED_DISP

> This table stores external medication dispense history received from outside sources.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 51  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `MDH_REF_ID` | VARCHAR |  | This item stores the medication dispense reference identifier. |
| 4 | `MED_DISP_MED_NAME` | VARCHAR |  | This item stores the medication dispense medication name. |
| 5 | `MED_DISP_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 6 | `MED_DISP_MED_SIG` | VARCHAR |  | This item stores the medication dispense medication directions. |
| 7 | `MED_DISP_MED_DOSE` | VARCHAR |  | This item stores the medication dispense medication dose. |
| 8 | `MED_DISP_DIS_DOSE` | NUMERIC |  | This item stores the medication dispense medication discrete dose. |
| 9 | `MED_DISP_UNIT` | VARCHAR |  | This item stores the medication dispense medication dose unit. |
| 10 | `MED_DISP_UNIT_ID_C_NAME` | VARCHAR | org | This item stores the medication dispense mapped medication dose unit. |
| 11 | `MED_DISP_ROUTE` | VARCHAR |  | This item stores the medication dispense medication dose route. |
| 12 | `MED_DISP_ROUTE_ID_C_NAME` | VARCHAR | org | This item stores the medication dispense mapped medication dose route. |
| 13 | `MED_DISP_FREQ` | VARCHAR |  | This item stores the medication dispense medication dose frequency. |
| 14 | `MED_DISP_FREQ_ID` | VARCHAR |  | This item stores the medication dispense mapped medication dose frequency. |
| 15 | `MED_DISP_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 16 | `MED_DISP_FORM` | VARCHAR |  | This item stores the medication dispense medication form. |
| 17 | `MED_DISP_FORM_ID_C_NAME` | VARCHAR | org | This item stores the medication dispense mapped medication form. |
| 18 | `MED_DISP_STRN` | NUMERIC |  | This item stores the medication dispense medication strength. |
| 19 | `MED_DISP_STRN_UNT_C_NAME` | VARCHAR |  | This item stores the medication dispense mapped medication strength units. |
| 20 | `MED_DISP_REFILLS` | NUMERIC |  | This item stores number of refills allowed for this medication. |
| 21 | `MED_DISP_AS_WRIT_YN` | VARCHAR |  | This item stores whether the medication was dispensed as written. |
| 22 | `MED_DISP_DATE` | DATETIME |  | This item stores the medication dispense date. |
| 23 | `MED_DISP_QTY_DISP` | NUMERIC |  | This item stores the medication quantity dispensed. |
| 24 | `MED_DISP_UNIT_C_NAME` | VARCHAR |  | This item stores the mapped medication dispense units. |
| 25 | `MED_DISP_DAYS_SUPL` | NUMERIC |  | This item stores the day supply for this medication. |
| 26 | `MED_DISP_WRTN_DATE` | DATETIME |  | This item stores the medication written date. |
| 27 | `MED_DISP_AUTH_QUA_C_NAME` | VARCHAR |  | This item stores the medication prior authorization qualifier. |
| 28 | `MED_DISP_AUTH_DATA` | VARCHAR |  | This item stores the prior authorization data. |
| 29 | `MED_DISP_PHARM_ID` | VARCHAR |  | This item stores the pharmacy Identifier. |
| 30 | `MED_DISP_PROV_ID` | VARCHAR |  | This item stores the provider identifier. |
| 31 | `MED_DISP_ORD_ID` | NUMERIC |  | This item stores the Epic Order identifier associated with this prescription. |
| 32 | `MED_DISP_PRESC_NUM` | VARCHAR |  | This item stores the medication prescription number. |
| 33 | `MED_DISP_PRIM_DX` | VARCHAR |  | The primary diagnosis code for the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface. This column is being replaced by table MED_DISP_ALL_DX_CODES. |
| 34 | `MED_DIS_PRIM_DX_SYS` | VARCHAR |  | The coding system used for the primary diagnosis code for the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface. This column is being replaced by table MED_DISP_ALL_DX_CODE_SYS. |
| 35 | `MED_DISP_PRIM_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 36 | `MED_DISP_SEC_DX` | VARCHAR |  | The secondary diagnosis code for the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface. This column is being replaced by table MED_DISP_ALL_DX_CODES. |
| 37 | `MED_DIS_SEC_DX_SYS` | VARCHAR |  | The coding system used for the secondary diagnosis code for the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface. This column is being replaced by table MED_DISP_ALL_DX_CODE_SYS. |
| 38 | `MED_DISP_SEC_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 39 | `MED_DISP_LASTFIL_DT` | DATETIME |  | The date on which the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface, was last filled. |
| 40 | `MED_DISP_DEA_CODE_C_NAME` | VARCHAR |  | The DEA schedule for the medication in the medication dispensed segment of the external e-prescription received through the incoming e-prescribing interface. |
| 41 | `MED_DISP_EAR_FIL_DT` | DATETIME |  | The first or earliest date on which the medication in the medication dispensed segment of the external e-prescription can be filled. |
| 42 | `MED_DISP_IS_MIX_YN` | VARCHAR |  | This column indicates whether the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface, is a mixture. |
| 43 | `MED_DISP_IS_SUPP_YN` | VARCHAR |  | This column indicates whether the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface, is a medication supply (for example, a test strip). |
| 44 | `MED_DISP_DUR_UNIT_C_NAME` | VARCHAR |  | The unit for the duration of therapy for the medication associated with the medication dispensed segment of the external e-prescription. |
| 45 | `MED_DSP_ADM_UNIT_C_NAME` | VARCHAR |  | The unit of measurement for the admin amount of the medication dose in the medication dispensed segment of the external e-prescription. |
| 46 | `MED_DIS_TTLDOSUNT_C_NAME` | VARCHAR |  | The unit for the total amount for a unit dose of a medication that uses a patient's clinical measurement (for example, weight or BSA) for dosing in the medication dispensed segment of the external e-prescription. |
| 47 | `MED_DISP_DOSE_TYP_C_NAME` | VARCHAR | org | The dosing type, based on the patient's clinical measurement, used for determining the unit dose amount of the medication in the medication dispensed segment of the external e-prescription. |
| 48 | `MED_DISP_DURATION` | VARCHAR |  | The duration of therapy for the medication associated with the medication dispensed segment of the external e-prescription. |
| 49 | `MED_DISP_ADMIN_AMT` | VARCHAR |  | The admin amount for a unit dose of the medication associated with the medication dispensed segment of the external e-prescription. |
| 50 | `MED_DISP_TTL_DOSE` | VARCHAR |  | The total amount for a unit dose of a medication that uses a patient's clinical measurement (for example, weight or BSA) for dosing in the medication dispensed segment of the external e-prescription. |
| 51 | `MED_DISP_DOSE_VALUE` | VARCHAR |  | The value of the patient's clinical measurement used for dosing a unit dose of the medication in the medication dispensed segment of the external e-prescription. For weight-based dosing, the value is stored in kilograms and for BSA-based dosing, the value is stored in square meters (m2). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

