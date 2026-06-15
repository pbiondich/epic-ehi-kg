# HH_VO_INFO

> Contains Home Health verbal orders noadd single items information.

**Primary key:** `VERBAL_ORDER_ID`  
**Columns:** 23  
**Org-specific columns:** 3  
**Joined by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERBAL_ORDER_ID` | VARCHAR | PK | The unique identifier for the verbal order record. |
| 2 | `ORDER_DATE` | DATETIME |  | Local date for home care order. Since this a local date, it will not always match the date in ORDER_INSTANT_UTC_DTTM. |
| 3 | `PROVIDER_ID` | VARCHAR |  | Unique identifier for the provider who is the referring provider for the verbal order. Links to table REFERRAL_SOURCE. The unique ID associated with the provider record for this row. This column is frequently used to link to the REFERRAL_SOURCE table. |
| 4 | `PROVIDER_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 5 | `USER_RECEIVED_ID` | VARCHAR |  | User ID of the verbal order receiving user. Links to table CLARITY_EMP. |
| 6 | `USER_RECEIVED_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `CREATE_DATE` | DATETIME |  | Date on which the verbal order was created. |
| 8 | `PATIENT_ID` | VARCHAR |  | Patient ID of the patient for whom the verbal order is created. Links to table PATIENT. |
| 9 | `STATUS_C_NAME` | VARCHAR |  | Verbal order status. Includes: not submitted, submitted, signed, sent, responded. Links to category table ZC_LVO_STATUS. |
| 10 | `POC_CSN_ID` | NUMERIC |  | The unique contact serial number of the patient associated with the hospice plan of care that generated the order. |
| 11 | `PLAN_OF_CARE_ID` | NUMERIC |  | This item contains the hospice plan of care ID associated with this verbal order. |
| 12 | `COSIGN_PROVIDER_ID` | VARCHAR |  | This item stores the cosign provider. |
| 13 | `COSIGN_PROVIDER_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 14 | `IS_COSIGN` | INTEGER |  | This item contains whether the verbal order has been cosigned. |
| 15 | `ORDER_MODE_C_NAME` | VARCHAR | org | This item indicates how the order was communicated. This helps distinguish between orders sent in by the physician unsolicited, orders communicated verbally from the physician to the clinician, and orders sent to the physician by the clinician without prior verbal communication. |
| 16 | `AUTH_LAST_EVENT_C_NAME` | VARCHAR | org | The last event for the authorizing provider (in HH_VO_INFO.PROVIDER_ID). Use this column when an order is sent to multiple providers and to differentiate between orders that are signed electronically and manually. |
| 17 | `PHY_CERT_CHARGE_ID` | VARCHAR |  | The unique ID of the physician certification or recertification charge. |
| 18 | `AUTO_CREATION_SRC_C_NAME` | VARCHAR |  | This item stores how the home care order was automatically created. |
| 19 | `ORDER_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | UTC date and time at which a home care order was placed. For orders created before we captured order time explicitly, the time saved here is equivalent to midnight local time. |
| 20 | `FACE_TO_FACE_ENC_DATE` | DATETIME |  | This item stores the encounter date for Face to Face orders. It is not used for other order types. |
| 21 | `CODE_STATUS_C_NAME` | VARCHAR | org | Document the type of code status this order placed (Full Code, DNR, etc.). |
| 22 | `PLAN_OF_CARE_CSN_ID` | NUMERIC |  | The unique contact serial number of the hospice plan of care that generated the order. This is used to identify the version of the plan that was sent with the order. |
| 23 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | Record status flag. Used in conjunction with record archived flag for encounter archiving. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (10)

| From | Column | Confidence |
|------|--------|------------|
| [FACE_TO_FACE_ORDERS](FACE_TO_FACE_ORDERS.md) | `VERBAL_ORDER_ID` | high |
| [HH_VO_ADDL_PROV](HH_VO_ADDL_PROV.md) | `VERBAL_ORDER_ID` | high |
| [HH_VO_COMPONENTS](HH_VO_COMPONENTS.md) | `VERBAL_ORDER_ID` | high |
| [HH_VO_DEFICIENCY](HH_VO_DEFICIENCY.md) | `VERBAL_ORDER_ID` | high |
| [HH_VO_ENC](HH_VO_ENC.md) | `VERBAL_ORDER_ID` | high |
| [HH_VO_EVENTS](HH_VO_EVENTS.md) | `VERBAL_ORDER_ID` | high |
| [HH_VO_NOTES](HH_VO_NOTES.md) | `VERBAL_ORDER_ID` | high |
| [HH_VO_NOTIFY](HH_VO_NOTIFY.md) | `VERBAL_ORDER_ID` | high |
| [HOME_CARE_VISIT_SET_ORDER](HOME_CARE_VISIT_SET_ORDER.md) | `VERBAL_ORDER_ID` | high |
| [OCS_CODE_STATUS](OCS_CODE_STATUS.md) | `VERBAL_ORDER_ID` | high |

