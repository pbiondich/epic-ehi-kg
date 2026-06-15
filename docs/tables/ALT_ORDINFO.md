# ALT_ORDINFO

> This table contains order or order template related information for all alerts. Link to ALERT to get patient, vendor, and alert type information for specific alert. Link to ALT_HISTORY to get alert history information. Link to specific alert table to get specific alert information for a given alert type.

**Primary key:** `ALT_CSN_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALT_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this contact. This number is unique across all alerts in the system. |
| 2 | `ORDER_ID` | NUMERIC | shared | The unique order ID for the order that triggered this alert, if it exists. This could be null if one of the following is true: 1. The alert was triggered and the new medication was removed in Order Entry before an order was created. 2. The alert was triggered when signing an order template. OTP_ID contains the unique order template ID. If the alert is for a medication, link this column to ORDER_MED.ORDER_MED_ID to get the medication order information. If the alert is for a procedure, link this column to the ORDER_PROC table to get the procedure order information. |
| 3 | `ORD_CNCT_DAT_REAL` | FLOAT |  | The contact date in internal, decimal format for the order. |
| 4 | `IS_PRIMARY_YN` | VARCHAR |  | For medication alert, the alert appears because new medication orders are entered, or some actions are taken for existing medication, or order templates are signed or released, etc. During such scenario, if the alert appears because of actions on some selected medication order or order template, the selected medication order or order template is the reason, and the value in this column is "Y". Otherwise, it is "N". Default is "N". |
| 5 | `MED_ALERTS_ACTN_C_NAME` | VARCHAR |  | The category value for action done for corresponding order or order template. Link it to ZC_MED_ALERTS_ACTN.MED_ALERTS_ACTC_C to get name, title, abbreviation. Empty or NULL means that is no action for corresponding order. |
| 6 | `LINE` | INTEGER | PK | The line number for involved order or order template. |
| 7 | `ALT_ID` | NUMERIC | FK→ | The unique alert ID for each alert. You could link it to ALERT.ALT_ID to get patient and vendor information in table ALERT. |
| 8 | `ORDER_STATUS_C_NAME` | VARCHAR |  | This column stores the order status if the order is Signed and Held. |
| 9 | `ORDERING_MODE_C_NAME` | VARCHAR |  | This column stores the ordering mode. |
| 10 | `ORDER_POC_C_NAME` | VARCHAR | org | The phase of care assigned to the order when interaction checking occurred. |
| 11 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 12 | `ON_MAR_HOLD_YN` | VARCHAR |  | Indicates whether an order was on Medication Administration Record (MAR) hold when this warning was displayed. |
| 13 | `MED_FROM_OUTSIDE_SRC_YN` | VARCHAR |  | This column indicates whether or not an order comes from reconciled data. If the order does come from outside data, it will contain the value Yes. If the order does not come from outside data, it will contain the value No. Additionally, this column will be blank for any warnings that fired before the system was keeping track of this. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_CSN_ID` | [ALT_HISTORY](ALT_HISTORY.md) | sole_pk | high |
| `ALT_ID` | [ALERT](ALERT.md) | sole_pk | high |

