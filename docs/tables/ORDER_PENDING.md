# ORDER_PENDING

> This table contains information on pending orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the pended order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record |
| 3 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user pending the order. |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `PENDED_TIME` | DATETIME (Local) |  | The time an order was pended. |
| 6 | `PENDED_FOR` | VARCHAR |  | The reason an order was pended. |
| 7 | `RELEASED_USER_ID` | VARCHAR |  | The unique ID of the user releasing a pended medication. |
| 8 | `RELEASED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `PENDING_COMMENTS` | VARCHAR |  | Order pending comments. |
| 10 | `PEND_REASON_C_NAME` | VARCHAR | org | Order pending reason. |
| 11 | `SH_ORDR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `SH_AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `SH_ORDER_MODE_C_NAME` | VARCHAR | org | The verbal order mode category ID for the signed and held order, indicating the way the order was placed, e.g. telephone with readback. |
| 14 | `SH_VERB_ORD_COMMENT` | VARCHAR |  | The comment entered by a user when creating a signed and held order. |
| 15 | `SH_VRB_COMM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 16 | `SH_COSIGN_USER_ID` | VARCHAR |  | The unique identifier of the user responsible for providing a cosignature for the order. |
| 17 | `SH_COSIGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `SH_COSIGN_REQ_YN` | VARCHAR |  | Indicates whether this order required a cosignature. 'Y' indicates that the order required a cosignature. 'N' or NULL indicates that the order did not require a cosignature. |
| 19 | `SH_VBL_CSN_NO_REQ_N` | INTEGER |  | Indicates whether a rule was used to prevent generating a verbal signature requirement for the order record. |
| 20 | `SH_COS_REQ_RSN_C_NAME` | VARCHAR |  | The signature requirement creation source category ID for the order, indicating the reason a cosignature is required for this signed and held order. |
| 21 | `SH_COS_SRC_ENC` | VARCHAR |  | The DAT of the patient encounter where a cosign or verbal sign was created for a signed and held order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

