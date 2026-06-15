# CL_REMIT

> This table stores information for each Image Database (IMD) record. This can be check-level or claim-level, and is indicated in column IMD_TYPE_C.

**Primary key:** `IMAGE_ID`  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record. A separate remittance image record is created for each invoice payment. |
| 2 | `CREATION_DATE` | DATETIME |  | The date when the remittance image record was created (i.e., when the electronic file was loaded and created). |
| 3 | `SERVICE_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `PAYMENT_METHOD_C_NAME` | VARCHAR |  | The posting method by which this remittance record was created (manual or through electronic remittance). |
| 5 | `PAYMENT_TYPE_C_NAME` | VARCHAR |  | The payment type for this remittance record (self-pay or insurance). |
| 6 | `PAYMENT_AMOUNT` | NUMERIC |  | Total amount paid by the payer in the remittance file. |
| 7 | `CREDIT_DEBIT_C_NAME` | VARCHAR |  | Code indicating whether payment amount is a credit or debit. |
| 8 | `PAYMENT_MTD_CODE_C_NAME` | VARCHAR |  | Code identifying the method for the movement of payment instructions. |
| 9 | `PAYMENT_FMT_CD_C_NAME` | VARCHAR |  | Code identifying the payment format used. |
| 10 | `SENDER_ID_QUAL_C_NAME` | VARCHAR |  | Sender ID qualifier. Code identifying the type of identification number of Depository Financial Institution (DFI). |
| 11 | `SENDER_IDN_NUM` | VARCHAR |  | Sender Depository Financial Institution (DFI) identification number from the remittance file. |
| 12 | `ISSUE_DATE` | DATETIME |  | Check issue date or Effective Entry Date for electronic fund transfers. |
| 13 | `TRACE_TYP_CD_C_NAME` | VARCHAR |  | Code identifying which transaction is being referenced. |
| 14 | `REF_IMG_ID` | VARCHAR |  | Reference remittance record for general remittance file information. A separate remittance image record is created for each invoice payment in the remittance file. The general check level information is stored in the first remittance image record and subsequent image records hold the image ID of that record in this item. |
| 15 | `GRP_REF_ID` | VARCHAR |  | Reference remittance image record for Provider Summary Information and Provider Supplemental Summary Information. A separate remittance image record is created for each invoice payment in the remittance file. Multiple invoice payments can share the same Provider Summary Information and Provider Supplemental Summary Information. This information is stored in the first remittance image record. Subsequent image records hold the image ID of the original remittance image in this item. |
| 16 | `PAT_ID` | VARCHAR | FK→ | The patient from the invoice to which the payment in the remittance image record is posted. |
| 17 | `CLM_START_DATE` | DATETIME |  | The starting date of the claim that was sent out to the payer. |
| 18 | `CLM_END_DATE` | DATETIME |  | The ending date of the claim that was sent out to the payer. |
| 19 | `CLP_ID` | NUMERIC | FK→ | Internal ID of the claim record (for Hospital Billing only). |
| 20 | `IMD_TYPE_C_NAME` | VARCHAR |  | Specifies the type of Remittance Image. 1 is Check Level and 2 is File Level. |
| 21 | `INTER_CTRL_NUM` | VARCHAR |  | Holds the Interchange Control Number from the electronic remittance file. |
| 22 | `GROUP_CTRL_NUM` | VARCHAR |  | Holds the Group Control Number from the electronic remittance file. |
| 23 | `EXPRESS_TYPE_C_NAME` | VARCHAR |  | This item identifies records created from incoming payer interface messages in response to Express claims. Records with this item set are not linked to transactions, but can be viewed from the Claim Status section in Inquiry or WQ. |
| 24 | `REPETITION_SEPARATOR` | VARCHAR |  | Stores the Repetition Separator from the ISA segment. |
| 25 | `VERSION_NUMBER` | VARCHAR |  | Stores the Interchange Control Version Number from the ISA segment. |
| 26 | `ACKNOWLEDGMENT_REQUEST_C_NAME` | VARCHAR |  | Stores the Acknowledgment Requested flag from the ISA segment. |
| 27 | `USAGE_INDICATOR_C_NAME` | VARCHAR |  | Stores the Interchange Usage Indicator from the ISA segment. |
| 28 | `RESP_AGENCY_CODE_C_NAME` | VARCHAR |  | Stores the Responsible Agency Code from the GS segment. |
| 29 | `INDUSTRY_IDENTIFIER_CODE` | VARCHAR |  | Stores the Industry Identifier Code from the GS segment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLP_ID` | [CLM_EDIT_WQ_CLM](CLM_EDIT_WQ_CLM.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

