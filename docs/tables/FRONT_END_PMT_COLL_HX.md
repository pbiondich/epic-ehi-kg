# FRONT_END_PMT_COLL_HX

> This table stores information about front-end collection actions taken through point of sale (POS) payment posting or refund workflows.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 33  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `COLL_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant that this event occurred. |
| 5 | `COLL_WORKFLOW_TYPE_C_NAME` | VARCHAR |  | The workflow in which this event took place. |
| 6 | `LOGIN_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `ENC_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `RSN_NON_COLL_AMT_C_NAME` | VARCHAR | org | The non-collection reason category ID for this event. |
| 9 | `RSN_NON_COLL_AMT_COMMENT` | VARCHAR |  | The free text non-collection comment explaining why some portion of a due amount was not collected. |
| 10 | `GUARANTOR_ACCOUNT_ID` | NUMERIC |  | The unique ID of the guarantor who is associated with this event. |
| 11 | `EVENT_TYPE_C_NAME` | VARCHAR |  | The event type category ID that defines the type of payment event data that is stored in this row. |
| 12 | `PB_COPAY_COLL` | NUMERIC |  | The amount of professional billing copay that a user collected during this event. |
| 13 | `PB_COPAY_PAID` | NUMERIC |  | The amount of professional billing copay that had already been paid towards an encounter at the time of this event. |
| 14 | `PB_COPAY_DUE` | NUMERIC |  | The total amount of professional billing copay that is required for this visit at the time of this event. |
| 15 | `HB_COPAY_COLL` | NUMERIC |  | The amount of hospital billing copay that a user collected during this event. |
| 16 | `HB_COPAY_PAID` | NUMERIC |  | The amount of hospital billing copay that had already been paid towards an encounter at the time of this event. |
| 17 | `HB_COPAY_DUE` | NUMERIC |  | The total amount of hospital billing copay that is required for this visit at the time of this event. |
| 18 | `PB_PREPAY_COLL` | NUMERIC |  | The amount of professional billing prepayment that a user collected. |
| 19 | `PB_PREPAY_PAID` | NUMERIC |  | The amount of professional billing prepayment that had already been paid towards an encounter at the time of this event. |
| 20 | `PB_PREPAY_DUE` | NUMERIC |  | The total amount of professional billing prepayment that is required for this visit at the time of this event. |
| 21 | `HB_PREPAY_COLL` | NUMERIC |  | The amount of hospital billing prepayment that a user collected during this event. |
| 22 | `HB_PREPAY_PAID` | NUMERIC |  | The amount of hospital billing prepayment that had already been paid towards an encounter at the time of this event. |
| 23 | `HB_PREPAY_DUE` | NUMERIC |  | The total amount of hospital billing prepayment that is required for this visit at the time of this event. |
| 24 | `PB_PREV_BAL_COLL` | NUMERIC |  | The amount of professional billing previous balance that a user collected during this event. |
| 25 | `PB_PREV_BAL_PAID` | NUMERIC |  | The amount of professional billing previous balance that had already been paid towards this guarantor's outstanding balance during the day of this event. |
| 26 | `PB_PREV_BAL_DUE` | NUMERIC |  | The amount of self-pay professional billing outstanding balance that a guarantor owed at the time of this event. |
| 27 | `HB_PREV_BAL_COLL` | NUMERIC |  | The amount of hospital billing previous balance that a user collected during this event. |
| 28 | `HB_PREV_BAL_PAID` | NUMERIC |  | The amount of hospital billing previous balance that had already been paid towards this guarantor's outstanding balance during the day of this event. |
| 29 | `HB_PREV_BAL_DUE` | NUMERIC |  | The amount of self-pay hospital billing outstanding balance that a guarantor owed at the time of this event. |
| 30 | `PREPAY_DISCOUNT_OFFERED` | NUMERIC |  | The total amount of the prepay discount that was offered for this visit at the time of this event. |
| 31 | `VIS_BAL_COLL` | NUMERIC |  | The amount of visit balance that a user collected during this event. |
| 32 | `VIS_BAL_PAID` | NUMERIC |  | The amount of the visit balance that had already been paid towards an encounter at the time of this event. |
| 33 | `VIS_BAL_DUE` | NUMERIC |  | The total amount of the visit balance that is required for this visit at the time of this event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

