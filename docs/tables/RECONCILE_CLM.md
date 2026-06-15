# RECONCILE_CLM

> This table contains basic information for claim reconciliation records.

**Primary key:** `CLAIM_REC_ID`  
**Columns:** 42  
**Org-specific columns:** 1  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_REC_ID` | VARCHAR | PK | The unique ID of the claim reconciliation record. |
| 2 | `CLAIM_INVOICE_NUM` | VARCHAR |  | The invoice number of the claim. |
| 3 | `CUR_EPIC_STATUS_C_NAME` | VARCHAR | org | This is the system status of the claim: opened or closed. |
| 4 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 5 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 6 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `BUCKET_ID` | NUMERIC | shared | The hospital liability bucket ID for the claim. This column is populated only for Hospital Billing claims. |
| 9 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The hospital account ID for the claim. This column is populated only for Hospital Billing claims. |
| 10 | `SERVICE_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 11 | `EPIC_CLM_STS_C_NAME` | VARCHAR |  | This column stores the status of the claim that created the reconciliation record. This column will indicate whether the claim has been accepted, processed, or rejected in Epic. |
| 12 | `CLAIM_RUN_ID` | VARCHAR |  | This column stores the claim run ID for the reconciliation record. This column will be populated for records created in the 2010 version and beyond. |
| 13 | `TOTAL_BILLED` | NUMERIC |  | This column stores the billed amount for the reconciliation record. |
| 14 | `EXT_STS_RCV_YN` | VARCHAR |  | This column indicates whether at least one external status update has been received for the reconciliation record. |
| 15 | `CROSSOVER_CLAIM_YN` | VARCHAR |  | Indicates whether the associated claim is a crossover claim. |
| 16 | `RECORD_TYPE_C_NAME` | VARCHAR |  | This item indicates whether the record is Interchange Control Header (ISA), Transaction Set Header (ST), or Claim data. |
| 17 | `ISA_CONTROL_NUM` | INTEGER |  | This item holds a unique value used for tracking an interchange for records of type Interchange. |
| 18 | `GS_CONTROL_NUM` | INTEGER |  | This item holds a unique value used for tracking a transaction set for records of type Transaction Set. |
| 19 | `NUM_OF_CLAIMS` | INTEGER |  | This item holds the number of claims submitted. It is set for records of type Interchange and Transaction Set. |
| 20 | `PRINT_USER_ID` | VARCHAR |  | This item holds the user associated with the print event. Set only for records of type Interchange. |
| 21 | `PRINT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `BHT_REF_NUM` | INTEGER |  | The reference identifier (BHT-03) value from the electronic claim file generated out of Epic. This acts as a link to the receiver level reference identifier (TRN-02) in the claim reconciliation (277CA) response file. |
| 23 | `POST_ACK_STATUS_YN` | VARCHAR |  | This item indicates whether at least one external status update has been received on or after either four days post claim acceptance or the predicted payment response date if earlier. Claim acknowledgements are generally posted before then. |
| 24 | `AP_CLAIM_IMPORT_SOURCE_C_NAME` | VARCHAR |  | Used to define the type of source a claim is imported from to drive reporting on the different use cases a single workflow type may have. |
| 25 | `SOURCE_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 26 | `MC_PROV_ACCT_NUM` | VARCHAR |  | This item stores the provider account number (invoice number) of the rejected claim. |
| 27 | `REJ_CLM_SVC_DATE` | DATETIME |  | This item stores the service date of the rejected claim. This column will be deprecated in Aug 27. The same information is stored in CLM_SVC_DATE. |
| 28 | `REJ_CLM_MEMBER_ID` | VARCHAR |  | This item stores the matched member of the rejected claim, if one was identified during claim load. This column will be deprecated in Aug 27. The same information is stored in CLM_PAT_ID. |
| 29 | `REJ_CLM_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 30 | `REJ_CLM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 31 | `REJ_CLM_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 32 | `CLAIM_CLOSED_DATE` | DATETIME |  | This item holds the contact date the CRD was marked closed. |
| 33 | `CLM_PAT_ID` | VARCHAR | FK→ | Contains the patient associated with the claim. Currently this is only populated for claims loaded through Tapestry EDI. |
| 34 | `CLM_SVC_DATE` | DATETIME |  | This item stores the service date of the claim. Currently this is only populated for claims loaded through Tapestry EDI. |
| 35 | `CLM_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 36 | `CLM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 37 | `CLM_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 38 | `CR_CODING_RECORD_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the coding record that led to this chart review submission. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 39 | `CR_SUBMISSION_TYPE_C_NAME` | VARCHAR |  | The chart review record submission type category ID for the chart review submission. This is used to indicate if the submission is linked to an encounter claim. |
| 40 | `CR_SUBMIT_CHANGE_TYPE_C_NAME` | VARCHAR |  | The chart review record submission change type category ID for the chart review submission. This is used to indicate information about the purpose of the submission. |
| 41 | `CR_PRIOR_SUBMIT_CLAIM_RECON_ID` | VARCHAR |  | The unique ID of the claim reconciliation (CRD) record that represents the chart review record this submission is updating, when this is a void or replacement submission. |
| 42 | `CR_ORIGINAL_SUB_CLAIM_ID` | NUMERIC |  | The unique ID of the claim (CLM) record that was submitted previously for risk adjustment, which this chart review submission is linked to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLM_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [RECONCILE_CLM_OT](RECONCILE_CLM_OT.md) | `CLAIM_REC_ID` | high |
| [RECONCILE_CLSD_TX](RECONCILE_CLSD_TX.md) | `CLAIM_REC_ID` | high |
| [RECONCILE_SVC_LINE](RECONCILE_SVC_LINE.md) | `CLAIM_REC_ID` | high |

