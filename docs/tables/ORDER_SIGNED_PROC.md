# ORDER_SIGNED_PROC

> This table contains the users, providers, and messages related to procedure verbal orders and cosign orders.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 27  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID for the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for the table. |
| 3 | `SIGNED_TYPE_C_NAME` | VARCHAR | org | Indicates the type of order signing the row represents. Note: Any type can have cosigner data. |
| 4 | `VERB_COMM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `VERB_SGNER_USER_ID` | VARCHAR |  | The unique user record ID for the user signing the verbal order. |
| 6 | `VERB_SGNER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VERB_MSGRC_USER_ID` | VARCHAR |  | The unique user record ID for the recipient of the In Basket message for the verbal order. |
| 8 | `VERB_MSGRC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `VERB_MSG_ID` | VARCHAR |  | The unique In Basket message record ID of the In Basket message created by the verbal order. |
| 10 | `VERB_SIGNED_TIME` | DATETIME (Local) |  | The date and time the verbal order was signed. |
| 11 | `VERBAL_MODE_C_NAME` | VARCHAR | org | The mode associated with the verbal order. |
| 12 | `ORDER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `CSGN_MSGRC_USER_ID` | VARCHAR |  | The unique user record ID for the recipient of the cosigned In Basket message. |
| 15 | `CSGN_MSGRC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `CSGN_MSG_ID` | VARCHAR |  | The unique In Basket message record ID of the cosigned In Basket message. |
| 17 | `CSGN_SIGNED_TIME` | DATETIME (Local) |  | The date and time the order was cosigned. |
| 18 | `COSIGNER_ID` | VARCHAR |  | The unique user record ID for the order cosigner. |
| 19 | `COSIGNER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `IS_HOSPITALIST_YN` | VARCHAR |  | Indicates if the order was by a hospitalist. |
| 21 | `VERB_ORD_CMT` | VARCHAR |  | Verbal order comment. |
| 22 | `CSGN_CREATE_DTTM` | DATETIME (UTC) |  | When the cosign requirement was created (UTC Time). |
| 23 | `CSGN_RQRD_C_NAME` | VARCHAR |  | This item stores whether or not an order requires a cosign based on when a new line is added to the verbal order category type (I ORD 34800). |
| 24 | `SIG_REQ_CRT_USER_ID` | VARCHAR |  | If the order signature requirement was manually created, this item stores the ID of the user who created the requirement. |
| 25 | `SIG_REQ_CRT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `SIG_REQ_CRT_SRC_C_NAME` | VARCHAR |  | This column is the creation source for order signature requirements. |
| 27 | `SIG_REQ_CRT_ENC` | NUMERIC |  | This item stores the CSN of the patient encounter where a cosign or verbal sign requirement was created. This item is populated when a cosign or verbal signature requirement is generated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

