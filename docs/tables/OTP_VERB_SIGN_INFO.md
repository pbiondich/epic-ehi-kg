# OTP_VERB_SIGN_INFO

> The verbal order signing history of an order template.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to a verbal signing of the order template in this row. |
| 3 | `VERB_ORD_TYPE_HX_C_NAME` | VARCHAR | org | The type of verbal order for the order template in this row. |
| 4 | `VERB_ORD_COMM_HX_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `VERB_ORD_SIGN_HX_ID` | VARCHAR |  | The user ID of the verbal order signer for the order template in this row. |
| 6 | `VERB_ORD_SIGN_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VERB_ORD_RCP_HX_ID` | VARCHAR |  | The verbal order message recipient for the order template in this row. |
| 8 | `VERB_ORD_RCP_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `VERB_ORD_MSG_HX_ID` | VARCHAR |  | The verbal order message ID for the order template in this row. |
| 10 | `VERB_ORD_INST_HX_TM` | DATETIME (Local) |  | The date/time in external format of the verbal signing of the order template in this row. |
| 11 | `VERB_ORD_MODE_HX_C_NAME` | VARCHAR | org | The verbal order mode for the order template in this row. |
| 12 | `ORD_PROV_HX_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `AUTH_PROV_HX_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `VERB_ORD_CMT_HX` | VARCHAR |  | The comment on a verbal order for the order template in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

