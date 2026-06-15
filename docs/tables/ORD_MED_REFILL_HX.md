# ORD_MED_REFILL_HX

> This table shows Medication Refill History Information.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 26  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the refill medication order. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `RFL_HX_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 4 | `RFL_HX_NDC_CODE` | VARCHAR |  | NDC code for each refill. |
| 5 | `RFL_HX_ACTION_C_NAME` | VARCHAR |  | Action taken, such as Dispense or Refill. |
| 6 | `RFL_HX_FILL_REMAIN` | INTEGER |  | Number of refills remaining. |
| 7 | `RFL_HX_FILL_USED` | INTEGER |  | Number of refills used. |
| 8 | `RFL_HX_REFILL_NUM` | INTEGER |  | Refill number. This is the number of refills used so far. It counts sequentially up from 1. |
| 9 | `RFL_HX_CANCELLED_C_NAME` | VARCHAR |  | Refill cancellations. |
| 10 | `RFL_HX_SIG` | VARCHAR |  | The description of how a refill medication is to be administered (sig). |
| 11 | `RFL_HX_LONG_SIG` | VARCHAR |  | Long sig for refill. This is a longer version of the sig, and is only populated by the interface in the case where a longer sig needs to be stored. |
| 12 | `REFILL_SUBSTITU_YN` | VARCHAR |  | Was the refill substituted? |
| 13 | `RFL_HX_PERSON` | VARCHAR |  | Refill person, this is a free text field that will depend on interface setup. |
| 14 | `RFL_HX_PHARMACY_ID` | NUMERIC |  | PHR ID of pharmacy that refilled the medication. |
| 15 | `RFL_HX_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 16 | `RFL_HX_DATE` | DATETIME |  | The date the refill medication order was placed. |
| 17 | `RFL_HX_TIME` | DATETIME |  | The time the refill medication order was placed. |
| 18 | `RFL_HX_COMMENT` | VARCHAR |  | The comments entered by the user who placed the refill medication order. |
| 19 | `REFIL_HX_DIS_NDC_ID` | VARCHAR |  | This item will hold the NDC related to the dispensed medication that comes through the interface sent from the pharmacy. This item will only be populated through the interface. This item will be networked to the NDC master file. |
| 20 | `REFIL_HX_DIS_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 21 | `REFIL_HX_DIS_MED` | VARCHAR |  | This item will hold the dispensed medication name that comes through the interface from the pharmacy. This item will only be populated by the interface. |
| 22 | `REFIL_HX_DISP_QTYUNIT_C_NAME` | VARCHAR | org | This item will hold the dispense unit quantity for the medication that comes through the interface from the pharmacy. It will only be populated through the interface. |
| 23 | `REFIL_HX_DIS_DUR` | NUMERIC |  | This item will hold the duration of the dispense for the medication sent through the interface from the pharmacy. This item will only be populated from the interface. |
| 24 | `REFIL_HX_DUR_UNT_C_NAME` | VARCHAR | org | This item will hold the duration unit for the medication sent through the interface from the pharmacy. This item will only be populated through the interface. |
| 25 | `REFILL_HX_ACTION_MOD_C_NAME` | VARCHAR |  | Adds an additional classification to the Refill Hx Action, eg. 'Remediation' |
| 26 | `REFILL_HX_QUANTITY_DISPENSED` | NUMERIC |  | Quantity dispensed for refill. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

