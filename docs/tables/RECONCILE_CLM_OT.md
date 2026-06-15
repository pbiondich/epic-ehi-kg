# RECONCILE_CLM_OT

> This table contains over time single information for claim reconciliation records.

**Primary key:** `CLAIM_REC_ID`, `CONTACT_DATE_REAL`  
**Columns:** 55  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_REC_ID` | VARCHAR | PK FK→ | The unique ID of the claim reconciliation record. |
| 2 | `CONTACT_DATE` | DATETIME |  | The contact date of the claim, in external format. |
| 3 | `CONTACT_DATE_REAL` | NUMERIC | PK | The contact date of the claim, in internal format. |
| 4 | `CLM_STATUS_CODE_C_NAME` | VARCHAR | org | The status code of the claim being tracked over time. |
| 5 | `PAYR_CLM_AMT_SUBMT` | NUMERIC |  | The amount submitted by the payer on this claim. |
| 6 | `PAYOR_CLM_AMT_PAID` | NUMERIC |  | The amount paid by the payer on this claim. |
| 7 | `PAYOR_REF_NUM` | VARCHAR |  | The claim's payer reference number. |
| 8 | `PAYOR_NAME` | VARCHAR |  | The payer name of the payer on the claim. |
| 9 | `CH_REF_NUM` | VARCHAR |  | This is the claim's clearinghouse reference number. |
| 10 | `CH_NAME` | VARCHAR |  | This is the claim's clearinghouse name. |
| 11 | `CLAIM_STATUS_MSG` | VARCHAR |  | The claim's textual status message. |
| 12 | `STATUS_DATE` | DATETIME |  | The status date of the claim. |
| 13 | `FILE_NAME` | VARCHAR |  | This is the filename associated with this claim. |
| 14 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 15 | `CLM_CLOSED_REASON_C_NAME` | VARCHAR |  | The category value for the reason the claim was closed. This value can be used to link to the ZC_CLM_CLSD_REASON table to get more information on the category values. |
| 16 | `CLAIM_ST_CAT_CODE_C_NAME` | VARCHAR | org | The status category code of the claim being tracked over time. |
| 17 | `TRANSMIT_MEDIUM_C_NAME` | VARCHAR | org | If claim has been transmitted, this item stores the medium. |
| 18 | `ERR_FIELD` | VARCHAR |  | The field a claim error is reported in. |
| 19 | `ERR_ITEM` | VARCHAR |  | The item for which the claim error was reported. |
| 20 | `ERR_VAL` | VARCHAR |  | The claim value that caused the error. |
| 21 | `ERR_MSG` | VARCHAR |  | The error message received for a claim. |
| 22 | `CH_SENT_DATE` | DATETIME |  | Stores the date that the claim was sent out of the clearinghouse. |
| 23 | `PAYOR_RECV_DATE` | DATETIME |  | Stores the date that the payer received the claim. |
| 24 | `CLAIM_SEL_ACT_C_NAME` | VARCHAR |  | Stores the action that was selected to be performed on the invoice. |
| 25 | `CLAIM_ACT_INFO_C_NAME` | VARCHAR |  | Can store additional information on why a given action was selected. |
| 26 | `TRANSMIT_STATUS_C_NAME` | VARCHAR |  | Stores the system transmission status for the claim. |
| 27 | `EXTERNAL_REJECT_YN` | VARCHAR |  | Yes/No flag indicating that the claim has been rejected by the payor or clearinghouse. |
| 28 | `PERFORM_ACT_C_NAME` | VARCHAR |  | Will store the action that was performed on the invoice. |
| 29 | `PERFORM_ACT_RSN` | VARCHAR |  | Stores the reason for the action that was performed on the invoice. |
| 30 | `GROUP_CONTROL_NUM` | INTEGER |  | Stores the group control number (GS-06) value for an American National Standards Institute (ANSI) electronic claim file. |
| 31 | `TRANSMIT_TYPE_C_NAME` | VARCHAR |  | Records electronic claim transmission type. |
| 32 | `PAYOR_CONTACT_NAME` | VARCHAR |  | Name of contact person or department associated with an information request. |
| 33 | `CLAIM_BILL_TYPE` | VARCHAR |  | This is the bill type received in the claim reconciliation file. |
| 34 | `MRN` | VARCHAR |  | This is the medical record number (MRN) received in the claim reconciliation file. |
| 35 | `INTERMEDIARY_IDENT` | VARCHAR |  | This is the transmission identifier received in the claim reconciliation file. |
| 36 | `AGENCY_CLAIM_NUM` | VARCHAR |  | This is the claim number received in the claim reconciliation file. |
| 37 | `CASE_REF_IDENT` | VARCHAR |  | This is the case reference identifier received in the claim reconciliation file. |
| 38 | `INFO_REQ_NUM` | VARCHAR |  | This is the attachment request tracking number received in the claim reconciliation file. |
| 39 | `PRIOR_INFO_REQ_NUM` | VARCHAR |  | This is the prior attachment request tracking number received in the claim reconciliation file. |
| 40 | `INFO_REQ_DUE_DATE` | DATETIME |  | Stores the date the requested information is to be returned. |
| 41 | `RESP_CONTACT_NAME` | VARCHAR |  | Name used by the payer for routing the requested information within their system. |
| 42 | `RESP_CONTACT_CITY` | VARCHAR |  | City of the mailing location for the return of attachment data. |
| 43 | `RESP_CONTACT_STATE` | VARCHAR |  | State of the mailing location for the return of attachment data. |
| 44 | `RESP_CONTACT_ZIP` | VARCHAR |  | Postal Code of the mailing location for the return of attachment data. |
| 45 | `RESP_CONTACT_CNTRY` | VARCHAR |  | Country of the mailing location for the return of attachment data. |
| 46 | `RESP_CONTACT_SUBDIV` | VARCHAR |  | Subdivision of the mailing location for the return of attachment data. |
| 47 | `SUPPORTED_ACTIONS_C_NAME` | VARCHAR |  | The claim actions supported by the interface profile at the time a claim status update is received from an external entity. |
| 48 | `TX_DEST_TYPE_C_NAME` | VARCHAR |  | The destination type when the claim is transmitted. |
| 49 | `PAYER_CHECK_DATE` | DATETIME |  | Holds the payer check date from claim reconciliation. |
| 50 | `PAYER_CHECK_NUM` | VARCHAR |  | Holds the payer check number from claim reconciliation. |
| 51 | `STATUS_RESP_TYPE_C_NAME` | VARCHAR |  | This type of status response this contact represents. |
| 52 | `CLAIM_RECON_CSN_ID` | NUMERIC |  | The contact serial number (CSN) of the contact. |
| 53 | `HAS_REJ_SVC_LN_YN` | VARCHAR |  | Yes/No flag indicating that the claim contains service lines that were rejected by the payer or clearinghouse. |
| 54 | `EXPRESS_IMAGE_ID` | VARCHAR |  | This item is set with the invoice level IMD created from a payer's interface message data when responding to an Express claim. |
| 55 | `MA_MAO002_ICN_IDENT` | VARCHAR |  | The ICN received on the MAO-002 for Medicare Advantage encounter reporting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_REC_ID` | [RECONCILE_CLM](RECONCILE_CLM.md) | sole_pk | high |

