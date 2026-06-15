# RX_EREFILL_RQST

> This table contains information about e-refill requests.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`  
**Columns:** 29  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID for the order with which the electronic refill is associated. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 5 | `EREFILL_APP_RX_NAME` | VARCHAR |  | This is the prescription name. |
| 6 | `EREFILL_APP_ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 7 | `EREFILL_APP_RX_QTY` | INTEGER |  | The prescription quantity approved. |
| 8 | `EREFILL_APP_RX_UNIT` | VARCHAR |  | The units associated with the quantity of the refill when the request was approved. |
| 9 | `EREFILL_APP_RX_SIG` | VARCHAR |  | The signature on the e-refill approval. |
| 10 | `EREFILL_APP_RFL_NUM` | VARCHAR |  | This column is the number of e-refills approved. |
| 11 | `EREFILL_APP_END_DT` | DATETIME |  | The end date for the e-refill prescription. |
| 12 | `EREFILL_APP_PROVIDE` | VARCHAR |  | This is the provider associated with the e-refill approval. |
| 13 | `EREFILL_APP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `EREFILL_ENT_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. |
| 15 | `EREFILL_ENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `EREFILL_PR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `EREFILL_APP_DATE` | DATETIME (Local) |  | This is the date and time the e-refill was acted on (approved or refused). |
| 18 | `EREFILL_APP_INSTANT` | DATETIME (Local) |  | The instant that e-refill was approved or refused. |
| 19 | `EREFILL_APP_COMMENT` | VARCHAR |  | Stores the ID of an General Use Notes record that stores the comments to the support staff. |
| 20 | `EREFILL_ACTION_C_NAME` | VARCHAR | org | The e-refill action; examples include "refuse","approve", etc. |
| 21 | `EREFILL_COMP_YN` | VARCHAR |  | This column tells whether the e-refill has been completed. |
| 22 | `ERFLL_FOL_UP_STAT_C_NAME` | VARCHAR |  | The e-refill authorization request follow-up status. |
| 23 | `ERFLL_FOL_UP_MSG_ID` | VARCHAR |  | The unique identifier of an In Basket message record, which is a message sent to the provider to follow up on an electronic refill request. |
| 24 | `EREFILL_DENY_REAS_C_NAME` | VARCHAR | org | If the refill is refused, the reason will be stored here. |
| 25 | `ERFLL_APP_RFL_PRN_C_NAME` | VARCHAR |  | This item stores the PRN value (for example PRN-2Yr or PRN-1Yr, referring to the length of time the 'as needed' medication can be refilled) approved in the e-refill. |
| 26 | `EREFILL_MSG_PHM_ID` | VARCHAR |  | The unique ID of a note record that stores the comments entered in the message to pharmacy field. |
| 27 | `EREFILL_COS_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 28 | `ERFLL_PREPRV_INST_X` | VARCHAR |  | The prescribing provider's ID and the instant at which he acted on the order, separated by a caret. This item is used for indexing. |
| 29 | `ERFLL_ACTPRV_INST_X` | VARCHAR |  | The acting provider's ID and the instant at which he acted on the order, separated by a caret. This item is used for indexing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

