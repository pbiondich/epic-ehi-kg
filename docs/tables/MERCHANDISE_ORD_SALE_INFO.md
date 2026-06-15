# MERCHANDISE_ORD_SALE_INFO

> This table stores the sale level information of merchandise orders.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`  
**Columns:** 24  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the merchandise order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This column contains a unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | This column contains the date of this contact in calendar format. |
| 4 | `MERCH_UNIT_PR` | NUMERIC |  | This column contains the final sale price for a merchandise in an order. If the price was overridden, this column contains the override price, and the original price is stored in Merchandise Original Unit Price column. |
| 5 | `MERCH_RETURN_RSN_C_NAME` | VARCHAR | org | The merchandise return reason category ID for the order. |
| 6 | `QUANTITY` | NUMERIC |  | This column holds the quantity of merchandise sold in the sale contact. |
| 7 | `STATUS_C_NAME` | VARCHAR | org | The current status category ID for the sale contact. |
| 8 | `STATUS_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | This column contains the instant that sale contact moved to its current status. |
| 9 | `CHARGING_CSN` | NUMERIC |  | The unique contact serial number of the patient of the pharmacy visit contact to use for charge and payment posting. |
| 10 | `UNIT_ACQUISITION_COST` | NUMERIC |  | This column contains the acquisition cost for the merchandise. |
| 11 | `CASH_PRICE` | NUMERIC |  | This column contains the total cash price for the merchandise sale. |
| 12 | `CASH_PRICE_CALCULATED` | NUMERIC |  | This column holds the original total cash price for the merchandise sale when the cash price was overridden. |
| 13 | `CASH_PRICE_OVERRIDE_REASON_C_NAME` | VARCHAR | org | The reason category ID for the cash price override for a merchandise sale. |
| 14 | `CASH_PRICE_OVERRIDE` | NUMERIC |  | This column holds the user specified value for the cash price for the merchandise sale. |
| 15 | `TAX_DUE_TOTAL` | NUMERIC |  | This column contains the rounded value for total taxes due for the merchandise sale. |
| 16 | `PAT_PAY_AMOUNT` | NUMERIC |  | This column contains the total cost of the merchandise including any taxes applicable to the merchandise sale. |
| 17 | `TAX_EXEMPT_YN` | VARCHAR |  | Indicates whether the tax was exempted for the merchandise sale. |
| 18 | `RX_TAX_ROUNDING_METHOD_C_NAME` | VARCHAR |  | The rounding method category ID used to calculate the total taxes for a merchandise sale. |
| 19 | `TAX_EXEMPTED_TOTAL` | NUMERIC |  | This column contains the rounded value for total amount of taxes exempted for a merchandise sale. |
| 20 | `SALE_PHARMACY_ID` | NUMERIC |  | The unique identifier for the pharmacy record associated with the merchandise sale contact. |
| 21 | `SALE_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 22 | `RX_CHARGE_DROP_INST_UTC_DTTM` | DATETIME (UTC) |  | This column contains the latest instant the charge associated with this contact was dropped/credited. |
| 23 | `PHARMACY_SALE_ITEM_ID` | VARCHAR |  | The unique identifier for the fee or merchandise record for the pharmacy sale. |
| 24 | `PHARMACY_SALE_ITEM_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

