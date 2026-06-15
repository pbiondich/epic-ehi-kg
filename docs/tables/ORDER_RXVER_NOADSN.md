# ORDER_RXVER_NOADSN

> The ORDER_RXVER_NOADSN contains medication order verification information that has one value per order.

**Primary key:** `ORDER_MED_ID`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. NOTE: This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `RX_DC_VRFY_USER_ID` | VARCHAR |  | The user ID who verifies discontinued order. |
| 3 | `RX_DC_VRFY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `RX_DC_VRFY_INSTANT` | DATETIME (Local) |  | The date and time the discontinued order was verified in calendar format. |
| 5 | `LAST_VERIFY_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. This is the most recent verification contact for an order. This column is frequently used to link to the CONTACT_DATE_REAL column of the ORDER_DISP_INFO table. |
| 6 | `MEDICATION_ACCESS_STS_C_NAME` | VARCHAR |  | This item holds the status of med access for the order. |
| 7 | `MEDAC_REL_RSN_C_NAME` | VARCHAR | org | If an order was released from medication access in the bulk release workflow, this item will document the reason. |
| 8 | `MED_SUPPLY_SOURCE_C_NAME` | VARCHAR | org | This item documents how the patient received their supply of medication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

