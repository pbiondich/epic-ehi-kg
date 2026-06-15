# ORDER_MED_4

> This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow of:** [ORDER_MED](ORDER_MED.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 69  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `E_PRES_EARLIEST_DAT` | DATETIME |  | This column stores the earliest date on which a prescription can be filled for a Schedule II controlled medication. The date must occur on or before the start date for the prescription. It can't be changed after the order is signed. |
| 3 | `ORDER_CONTEXT_ID` | NUMERIC | FK→ | The unique identifier of the order context record associated with the order, which contains additional information about when the order is intended to be used. |
| 4 | `PREV_ORD_CONTEXT_ID` | NUMERIC |  | The unique identifier of the order context record associated with the order, which contains additional information about when the order is intended to be used. |
| 5 | `PARENT_ORDER_ID` | NUMERIC |  | The unique ID of the parent order record for Home Health (HH) orders. An HH order is an order which represents documentation by a user whose scope of practice doesn't include editing prescription data. Furthermore, the child order created will not be an actual prescription, but merely represents new instructions to the patient regarding how to take a medication. |
| 6 | `LINKED_OP_MED_ID` | NUMERIC |  | The unique ID of the orders record. When Home Health and Hospice clinicians need to document a medication administration against an inpatient medication, a copy of the medication is created with an order mode of inpatient to document the administration. This column holds a link to the original outpatient medication. |
| 7 | `INTERFACE_STAT_C_NAME` | VARCHAR |  | This column stores the ID of the interface status of the order. |
| 8 | `PRESC_ORD_SIG` | VARCHAR |  | The originally prescribed medication instructions for an order. This will be null if the original and current medication instructions are identical or if the order is not for a controlled medication that was electronically prescribed. |
| 9 | `PRESC_ORD_MED_NAME` | VARCHAR |  | The originally prescribed medication name for an order. This will be null if the original medication name and current medication name are identical or if the order is not for a controlled medication that was electronically prescribed. |
| 10 | `PRESC_ORD_REFILLS` | VARCHAR |  | The originally prescribed refills for an order. This will be null if the original refills and current refills are identical or if the order is not for a controlled medication that was electronically prescribed. |
| 11 | `PRESC_ORD_QUANTITY` | VARCHAR |  | The originally prescribed quantity for an order. This will be null if the original quantity and current quantity are identical or if the order is not for a controlled medication that was electronically prescribed. |
| 12 | `TXT_AUTHPROV_EXT_YN` | VARCHAR |  | Indicates whether the order's authorizing provider is from an external provider database. 'Y' indicates that the provider does not have a provider record in this EHR system and is from an external provider database. 'N' or NULL indicates that the provider has a provider record in this EHR system. |
| 13 | `TXT_ORDPROV_EXT_YN` | VARCHAR |  | Indicates whether the order's ordering provider is from an external provider database. 'Y' indicates that the provider does not have a provider record in this EHR system and is from an external provider database. 'N' or NULL indicates that the provider has a provider record in this EHR system. |
| 14 | `WAS_FMLY_CHECKED_YN` | VARCHAR |  | Indicates whether the medication order was compared to a formulary during signing. 'Y' indicates that the medication was compared to a payor-plan formulary, external formulary, or hospital formulary. 'N' or NULL indicates that the medication was not compared to a formulary. This does not indicate that the medication is or is not on any formulary, only that a formulary was checked for the medication. |
| 15 | `SELECTED_CRCL_SRC_C_NAME` | VARCHAR |  | The selected CrCl source category ID for the order record, indicating the source of the creatinine clearance (CrCl) value. |
| 16 | `CRCL_ORD_SPEC_VAL` | NUMERIC |  | This column stores the creatinine clearance (CrCL) value in the order. |
| 17 | `SELECTED_SCR_SRC_C_NAME` | VARCHAR |  | The selected sCr source category ID for the order record, indicating the source of the serum creatinine (sCr) value. |
| 18 | `SCR_ORD_SPEC_VAL` | NUMERIC |  | The serum creatinine (sCr) value for the order record. |
| 19 | `TRANSIG_LANGUAGE_ID` | NUMERIC |  | The unique identifier of the language record used for translating patient-facing information in this order record. |
| 20 | `TRANSIG_LANGUAGE_ID_LANGUAGE_NAME` | VARCHAR |  | The language name. If the language is written and uses more than one script to represent it, the name will contain the script in parentheses after the language name. |
| 21 | `ORIG_DOSE_BEFORE_SWITCH` | VARCHAR |  | The original dose of the medication before the dose was adjusted. |
| 22 | `ORIG_DOSE_UNIT_BEFORE_SWITCH_C_NAME` | VARCHAR | org | The unit category ID for the order record. |
| 23 | `MAXDOSE_HARDSTOP_YN` | VARCHAR |  | Indicate whether the max dose limit is a hard stop for this order. If "Yes", the max dose is a hard stop. Otherwise, the max dose is not a hard stop. |
| 24 | `TXT_AUTHPROV_DIST_C_NAME` | VARCHAR | org | The district category ID associated with the authorizing provider for this order record. |
| 25 | `TXT_AUTHPROV_CTY_C_NAME` | VARCHAR | org | The county category ID associated with the authorizing provider for this order record. |
| 26 | `TXT_AUTHPROV_CTRY_C_NAME` | VARCHAR | org | The country category ID associated with the authorizing provider for this order record. |
| 27 | `TXT_ORDPROV_HOUSE` | VARCHAR |  | The house number of the ordering provider for this order record. |
| 28 | `TXT_ORDPROV_DIST_C_NAME` | VARCHAR |  | The district category ID associated with the ordering provider for this order record. |
| 29 | `TXT_ORDPROV_CNTY_C_NAME` | VARCHAR |  | The county category ID associated with the ordering provider for this order record. |
| 30 | `TXT_ORDPROV_CNTRY_C_NAME` | VARCHAR |  | The country category ID associated with the ordering provider for this order record. |
| 31 | `MAX_BSA` | NUMERIC |  | The maximum Body Surface Area (BSA) for an order, if the selected BSA is greater than this BSA then the selected BSA will be capped at this value. |
| 32 | `MAX_DAILY_DOSE` | NUMERIC |  | Max daily dose value entered by the provider or defaulted as the calculated daily dose |
| 33 | `MAX_DLY_DOSE_UNIT_C_NAME` | VARCHAR |  | The unit category ID for the orders record |
| 34 | `TXT_AUTHPROV_HOUSE` | VARCHAR |  | The house number of the authorizing provider for this order record. |
| 35 | `UNROUNDED_DOSE_MIN` | NUMERIC |  | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the lower end of the range. If the dose does not have a range, then this will store the dose. |
| 36 | `UNROUNDED_DOSE_MAX` | NUMERIC |  | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the upper end of the range. Otherwise, this is null. |
| 37 | `UNROUND_DOSE_UNIT_C_NAME` | VARCHAR |  | The med & dose unit category ID for the unrounded dose of this order record. |
| 38 | `ION_SPEC_AC_AMT` | NUMERIC |  | This column shows the amount of acetate that a provider entered in this order record. This column will be empty if a chloride:acetate ratio or maximize option was selected. |
| 39 | `ION_SPEC_AC_UNIT_C_NAME` | VARCHAR |  | The med & dose unit category ID for the acetate amount that a provider entered in this order record. This column will be empty if a chloride:acetate ratio or maximize option was selected. |
| 40 | `ION_MAXIMIZE_C_NAME` | VARCHAR |  | The ion maximize selection category ID for the order record. |
| 41 | `ION_RATIO` | VARCHAR |  | This column shows the chloride:acetate ratio option that was selected. This column is empty when a specified acetate amount was entered or when a maximize option was selected. |
| 42 | `ION_BASED_TPN_YN` | VARCHAR |  | This column indicates how users specify electrolyte amounts for a total parenteral nutrition (TPN) order. 'Y' indicates that users enter amounts for specific ions to add in the TPN. 'N' indicates that users enter amounts for specific salts to add in the TPN. |
| 43 | `CALC_CL_AC_RATIO` | NUMERIC |  | This column stores the calculated chloride:acetate ratio for an ion-based total parenteral nutrition (TPN). |
| 44 | `ION_PRI_CALC_AMT_C_NAME` | VARCHAR |  | This column indicates whether the primary calculated amount is a weight-based or non-weight-based value. |
| 45 | `USE_AUC_DOSE_YN` | VARCHAR |  | Indicates whether the system should automatically update the dose for the order based on the area under the curve (AUC) calculations. 'Y' indicates that the system updates the dose based on AUC calculations. 'N' or NULL indicates that the system does not update the dose based on AUC calculations. |
| 46 | `EPRES_PHARMACY_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 47 | `EPRES_PHARMACIST_ID` | VARCHAR |  | This column stores the ID of the pharmacist or pharmacy technician who accepted the prescription. |
| 48 | `EPRES_PHARMACIST_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 49 | `RX_ACCEPT_DTTM` | DATETIME (Local) |  | Stores the instant at which the prescription was accepted. |
| 50 | `RPTSIG_EXISTS_YN` | VARCHAR |  | Indicates whether the patient has indicated that they are taking this med differently from how it was prescribed to them for this order. If yes, the patient reported that they are taking the med differently. If no or null, the patient did not report that they are taking the med differently. |
| 51 | `HOLD_PENDING_PA_YN` | VARCHAR |  | This item indicates whether the order is waiting for a prior authorization request to be completed before being sent to its final destination. |
| 52 | `SEND_PA_REQ_YN` | VARCHAR |  | Indicates whether a prior authorization request should be sent for a medication order when it is signed. 'Y' indicates that a prior authorization request should be sent. 'N' indicates that a prior authorization request should not be sent. |
| 53 | `PA_ORG_ID` | NUMERIC |  | The unique ID of the data exchange organization associated with the order record, which specifies the payer that a prior authorization request should be sent to when a medication order is signed. |
| 54 | `PA_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 55 | `SCRIPT_SUP_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 56 | `ONE_STEP_MEDPROC_ID` | NUMERIC |  | The unique ID of the order record. This item points to a procedure order record for the procedure used to administer the medication. The item is populated when administering a medication that is documented as administered in an Ophthalmology or Orthopedic context. |
| 57 | `SPEC_DOSE_LMT_HR` | INTEGER |  | The number of hours the dosing limit represents. |
| 58 | `SPEC_MED_TYPE_C_NAME` | VARCHAR |  | The special medication type category ID for this order. This indicates whether the medication uses special dosing parameters, such as for patient-controlled analgesia orders. |
| 59 | `RX_TRANSITION_ID` | NUMERIC |  | The unique identifier for the patient follow-up tracking record, which stores information about how a patient is transitioning from one medication to another. |
| 60 | `RX_TRANSITION_STAT_C_NAME` | VARCHAR |  | The medication transition status category ID for the order record. |
| 61 | `RX_TRANSITION_STAT_RSN_C_NAME` | VARCHAR | org | The medication transition status change reason category ID for the order record. |
| 62 | `RX_TRANSITION_STAT_CMT` | VARCHAR |  | This item stores any additional comments about why the medication transition status was changed. |
| 63 | `RX_TRANSITION_STAT_USR_ID` | VARCHAR |  | The unique identifier of the user who changed the transition status of the medication. |
| 64 | `RX_TRANSITION_STAT_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 65 | `RX_TRANSITION_STAT_UTC_DTTM` | DATETIME (UTC) |  | The date and time the medication transition status of the order was changed. |
| 66 | `DISCON_LOCAL_TIME` | DATETIME (Local) |  | This item stores the instant in the patient's local time zone that an order was discontinued. |
| 67 | `RX_REQUEST_TYPE_C_NAME` | VARCHAR |  | The prescription request type category ID for the order record |
| 68 | `DISC_WAIT_PA_YN` | VARCHAR |  | This column indicates whether an order was discontinued while waiting for prior authorization. |
| 69 | `ERX_ORD_NAME` | VARCHAR |  | The name of an order that was electronically prescribed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_CONTEXT_ID` | [ODC_BASIC](ODC_BASIC.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [ORDER_MED](ORDER_MED.md).

