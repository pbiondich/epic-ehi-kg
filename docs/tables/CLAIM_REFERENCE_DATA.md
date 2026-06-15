# CLAIM_REFERENCE_DATA

> Table of Claim Reference Data collections, where each collection represents a single piece of received claim-related data.

**Primary key:** `REF_DATA_ID`  
**Columns:** 32  
**Org-specific columns:** 2  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REF_DATA_ID` | NUMERIC | PK | The unique identifier for the Claim Reference Data record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, and others). |
| 3 | `ORGANIZATION_ID` | NUMERIC | FK→ | The ID of the organization that sent the invoice. |
| 4 | `ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The Patient ID of the member in the Payer system for whom the invoice was sent. |
| 6 | `MEMBER_IDENT` | VARCHAR |  | The Member ID of the associated member for whom the invoice was sent. |
| 7 | `CRF_RECORD_TYPE_C_NAME` | VARCHAR |  | The type of Claim Reference Data record. This is determined by the claims-related record the Claim Reference Data record will link to (Claim, Referal, or other). |
| 8 | `LINKED_CLAIM_ID` | NUMERIC |  | The ID of the Claim record linked to the Claim Reference Data record. |
| 9 | `BILLING_PROV_NPI` | VARCHAR |  | The NPI of the Billing Provider / Vendor that sent the invoice. |
| 10 | `BILLING_PROV_TAX_IDENT` | VARCHAR |  | The Tax ID of the Billing Provider / Vendor that sent the invoice. |
| 11 | `BILLING_SYS_C_NAME` | VARCHAR |  | The type of the Billing System that sent the invoice. |
| 12 | `HOSPITAL_ACCT_IDENT` | VARCHAR |  | The external identifier of the Hospital Account associated with the invoice. This identifier should not be used to join to internal Hospital Account tables. |
| 13 | `CLAIM_INT_CONTROL_NUMBER` | VARCHAR |  | The Internal Control Number (ICN) for the claim. Each ICN points to a unique Claim record in the Payer system. |
| 14 | `INVOICE_NUMBER` | VARCHAR |  | The number of the invoice in the claim reference data set. |
| 15 | `CLAIM_FROM_DATE` | DATETIME |  | The minimum service date on the claim. |
| 16 | `CLAIM_TO_DATE` | DATETIME |  | The maximum service date on the claim. |
| 17 | `BILLED_AMOUNT` | NUMERIC |  | The total of the charges on the claim. |
| 18 | `ORIGINAL_INVOICE_NUMBER` | VARCHAR |  | The number of the original or previous invoice in a series of invoices where the previous invoice was canceled, replaced, resubmitted, or otherwise nullified. |
| 19 | `CANCEL_FLAG_C_NAME` | VARCHAR |  | Flag raised if the associated invoice is a Cancellation. |
| 20 | `REPLACE_FLAG_C_NAME` | VARCHAR |  | Flag raised if the associated invoice is a Replacement. |
| 21 | `RESUBMIT_FLAG_C_NAME` | VARCHAR |  | Flag raised if the associated invoice is a Resubmission. |
| 22 | `RECORD_NAME` | VARCHAR |  | The name of the Claim Reference Data record. |
| 23 | `PRIMARY_LINK_UTC_DTTM` | DATETIME (UTC) |  | The instant a Primary record was linked to the Claim Reference Data record. |
| 24 | `CANCELLED_BY_PROV_FLAG_C_NAME` | VARCHAR |  | Indicates whether the associated invoice has been cancelled by the submitter. |
| 25 | `PAT_MRN` | VARCHAR |  | The patient's medical record number. |
| 26 | `FILING_ORDER_C_NAME` | VARCHAR |  | Stores the providers claim filing order. |
| 27 | `REF_DATA_CLAIM_PRINT_ID` | NUMERIC |  | The claim print record for which the CRF record is generated from. This item is only populated on a shared instance implementation of CRF. |
| 28 | `ASSOCIATED_CLAIM_FORM_TYPE_C_NAME` | VARCHAR | org | The claim type associated with this Claim Reference Data record. |
| 29 | `ASSOCIATED_COVERAGE_ID` | NUMERIC |  | The coverage associated with this Claim Reference Data record. |
| 30 | `PROV_CLM_RECON` | VARCHAR |  | The Claim Reconciliation (CRD) record id in the provider system's Epic instance. This is not a networked item and does not link to a Claim Reconciliation record. |
| 31 | `SUBSCRIBER_IDENT` | VARCHAR |  | The Subscriber ID of the member in the Payer system associated with the claim reference data set. |
| 32 | `MEM_REL_TO_SUB_C_NAME` | VARCHAR | org | The relationship of the patient to the subscriber for the member in the Payer system associated with the claim reference data set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORGANIZATION_ID` | [ORG_DETAILS](ORG_DETAILS.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [CRF_ASSOCIATED_CSN](CRF_ASSOCIATED_CSN.md) | `REF_DATA_ID` | high |
| [CRF_ASSOCIATED_ENCS](CRF_ASSOCIATED_ENCS.md) | `REF_DATA_ID` | high |
| [CRF_ASSOCIATED_RELEASES](CRF_ASSOCIATED_RELEASES.md) | `REF_DATA_ID` | high |
| [CRF_AUDIT_HISTORY](CRF_AUDIT_HISTORY.md) | `REF_DATA_ID` | high |

