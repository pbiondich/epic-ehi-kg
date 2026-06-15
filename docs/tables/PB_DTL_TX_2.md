# PB_DTL_TX_2

> The PB_DTL_TX_2 table contains the detailed transactions associated with a billing account transaction.

**Overflow of:** [PB_DTL_TX](PB_DTL_TX.md)  
**Primary key:** `PB_TX_ID`  
**Columns:** 15  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TX_ID` | VARCHAR | PK | The unique identifier (.1 item) for the detail transaction record. |
| 2 | `INV_CLM_TYPE_C_NAME` | VARCHAR | org | Specify the source claim type associated with the detailed transaction. |
| 3 | `CLAIM_NUMBER` | VARCHAR |  | Specify the identifier of the source claim associated with the detailed transaction. |
| 4 | `SOURCE_CLAIM_ID` | NUMERIC |  | Specify the claim from which this transaction originates. |
| 5 | `SERVICE_DATE` | DATETIME |  | Specify the service date of the source claim associated with the detailed transaction. |
| 6 | `SELECTIVE_PLAN_GRP_ID` | VARCHAR |  | Used to find outstanding detail transactions that aren't batched quickly. Used in places such as payment computing. |
| 7 | `SELECTIVE_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 8 | `CLAIM_PAYEE_C_NAME` | VARCHAR |  | Specify the recipient type of the associated claim. |
| 9 | `VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 10 | `THIRD_PARTY_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 11 | `ASSOCIATED_REFUND_DTX_ID` | NUMERIC |  | Specify the associated vendor refund transaction (DTX). |
| 12 | `BALANCE_OFFSET_TRANSACTION_ID` | VARCHAR |  | Specify that it offsets a balance carried by another PDX. |
| 13 | `REALIZED_RCVRY_TRANSACTION_ID` | VARCHAR |  | Points to the realized recovery transaction (PDX). |
| 14 | `PREPAY_OFFSET_TRANSACTION_ID` | VARCHAR |  | This item appears on the refund prepayment recovery transaction (PDX) and points to the realized recovery transaction (PDX) created when the vendor refund or recoupment is posted. |
| 15 | `ASSOCIATED_VENDOR_CHECK_ID` | NUMERIC |  | Specify the associated vendor check (APC) of the recoupment transaction (PDX). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PB_DTL_TX](PB_DTL_TX.md).

