# ORD_EREFILL_REQ

> This table gives all the electronic refill information. The information covers details of ordered medications, who ordered them and from where they were ordered.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID for the order with which the e-refill is associated. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact (when the order was placed) in calendar format. |
| 4 | `EREFILL_REQ_RX_NAM` | VARCHAR |  | The name of the e-refill requested medication. |
| 5 | `EREFILL_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 6 | `EREFILL_REQ_RX_QTY` | NUMERIC |  | The quantity of the requested medication. |
| 7 | `EREFILL_REQ_RX_UNIT` | VARCHAR |  | Stores the units of the quantity of requested medication. |
| 8 | `EREFILL_REQ_RX_SIG` | VARCHAR |  | Stores the user signature for the requested e-refill. |
| 9 | `EREFILL_REQ_RFL_NUM` | NUMERIC |  | The number of refills requested in the e-refill. |
| 10 | `EREFILL_REQ_END_DT` | DATETIME |  | Refill request end date |
| 11 | `EREFILL_PHARM_ID` | NUMERIC |  | Stores the ID of the requesting pharmacy |
| 12 | `EREFILL_PHARM_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 13 | `EREFILL_REQ_PERSON` | VARCHAR |  | Stores the EMP ID of the person requesting the refill. |
| 14 | `EREFILL_REQ_DT` | DATETIME |  | Stores the date and time the e-refill was requested. |
| 15 | `EREFILL_REQ_COMMENT` | VARCHAR |  | Stores the ID of the Note (HNO) record that stores the pharmacy comments. |
| 16 | `ERFLL_REQ_RFL_PRN_C_NAME` | VARCHAR |  | Stores the As Needed (PRN) value for refills (for example PRN-2Yr or PRN-1Yr), referring to the length of time the 'as needed' medication can be refilled. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

