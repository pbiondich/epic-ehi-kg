# GUAR_PAT_BILL_INV_HX

> This table contains information about pending authorized user invitations to a guarantor account.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BILL_ACSS_INV_CODE` | VARCHAR |  | This item stores a unique code used to invite a user to become an authorized user on this guarantor. |
| 4 | `BILL_ACCS_INV_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when an authorized user invite was sent. |
| 5 | `BIL_ACS_INV_MYPT_ID` | VARCHAR |  | This item stores the WPR of the authorized user that is invited, if applicable. |
| 6 | `BILL_ACCS_ATMPT_CNT` | INTEGER |  | This items stores the number of times a user attempts to confirm an authorized user invite offer. |
| 7 | `BILL_ACSS_INV_NAME` | VARCHAR |  | This item stores the name of the person the guarantor invited to become an authorized user. |
| 8 | `BILL_ACSS_INV_EMAIL` | VARCHAR |  | This item stores the email of the person the guarantor invited to become an authorized user. |
| 9 | `BILL_ACSS_INV_PHONE` | VARCHAR |  | This item stores the phone number of the person the guarantor invited to become an authorized user. |
| 10 | `BILL_ACSS_INV_SYS_C_NAME` | VARCHAR |  | Stores the billing system of the guarantor account that the authorized user is invited to. |
| 11 | `BILL_ACCS_INV_REC_STMT_YN` | VARCHAR |  | This items stores whether the MyChart account with billing access to the guarantor account should receive paper copies of statements once the invited authorized user accepts the authorized user invite offer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

