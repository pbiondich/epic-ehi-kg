# ORD_SECOND_SIGN

> This table stores the information about second sign for orders.

**Primary key:** `ORDER_ID`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `SEC_SIGN_STATUS_C_NAME` | VARCHAR |  | This item stores the status of the second sign. |
| 3 | `SEC_SIGN_FIRS_DTTM` | DATETIME (Local) |  | This column contains the instant at which the first sign occurred. |
| 4 | `SEC_SIGN_MESSAGE` | VARCHAR |  | This is the message shown to the user. |
| 5 | `SEC_SIGN_REQUIRE_C_NAME` | VARCHAR |  | This is the second sign requirement that this order was signed with. |
| 6 | `SEC_SIGN_SIGNER_ID` | VARCHAR |  | The ID of the secondary signing user. |
| 7 | `SEC_SIGN_SIGNER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `SEC_SIGN_SEC_DTTM` | DATETIME (Local) |  | This column contains the instant at which the second sign occurred. |
| 9 | `SEC_SIGN_REJECT_C_NAME` | VARCHAR | org | The reason that this order was rejected. |
| 10 | `SEC_SIGN_COMMENT` | VARCHAR |  | This stores the comment for the rejection. |
| 11 | `SEC_SIGN_MESSAG_ID` | VARCHAR |  | The second sign message ID. |
| 12 | `SEC_SIGN_REJECT_ID` | VARCHAR |  | This is the ID of the rejection message that is sent. |
| 13 | `SEC_SIGN_INDIV_YN` | VARCHAR |  | Whether individual review was required for this order when second signing the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

