# ORDER_DISP_INFO_2

> This table contains dispense information for orders.

**Overflow of:** [ORDER_DISP_INFO](ORDER_DISP_INFO.md)  
**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`  
**Columns:** 40  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `RX_TO_PHRM_DEA` | VARCHAR |  | The transfer to pharmacy's Drug Enforcement Administration (DEA) number captured during a prescription transfer. A DEA number is assigned by the Drug Enforcement Administration to providers to allow them to write prescriptions for controlled substances. |
| 4 | `RX_XFER_PHARMACY_ID` | NUMERIC |  | Stores the pharmacy that performed the prescription transfer. |
| 5 | `RX_XFER_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 6 | `RX_XFR_LAST_DISP_DT` | DATETIME |  | Date the prescription was last dispensed from the previous non-integrated pharmacy captured during a prescription transfer. |
| 7 | `RX_FROM_PHRM_DEA` | VARCHAR |  | The transfer from pharmacy's Drug Enforcement Administration (DEA) number captured during prescription transfer. A DEA number is assigned by the Drug Enforcement Administration to providers to allow them to write prescriptions for controlled substances. |
| 8 | `RX_BILL_GUAR_ACC_ID` | NUMERIC |  | This item is used to contain the guarantor account ID to bill the remaining balance of the prescription if the patient will not be paying with cash. |
| 9 | `RX_BILL_HOSP_ACC_ID` | NUMERIC |  | This item is used to contain the hospital account ID to bill the remaining balance of the prescription if the patient will not be paying with cash. |
| 10 | `PAT_PAY_AMOUNT_CALC` | NUMERIC |  | When the prescription patient pay amount is overridden, this item is populated with the calculated patient pay amount. When the patient pay amount is not overridden, the calculated patient pay amount is stored in the patient pay amount (I ORD 47380). For cash prescriptions, the calculated patient pay amount is the cash price calculated by ambulatory pharmacy. For prescriptions using coverage, it's the patient pay amount determined by the processor. |
| 11 | `PAT_PAY_AMT_REAS_C_NAME` | VARCHAR | org | The reason why the user overrode the prescription patient pay amount. |
| 12 | `RX_XFR_FRST_DISP_DT` | DATETIME |  | The date the previous non-integrated pharmacy first dispensed the prescription to the patient. |
| 13 | `RX_FRM_PHR_ADDR` | VARCHAR |  | A prescription can be transferred in from a non-integrated pharmacy that is not built in the system (a free-text pharmacy). That pharmacy's address can be entered during the transfer in and stored here. |
| 14 | `RX_TO_PHR_ADDR` | VARCHAR |  | A prescription can be transferred out from an ambulatory pharmacy to a non-integrated pharmacy that is not built in the system (a free-text pharmacy). That pharmacy's address can be entered during the transfer out and stored here. |
| 15 | `CASH_PRICE_REAS_C_NAME` | VARCHAR | org | The reason the user overrode the cash price. |
| 16 | `RX_XFER_QTY_XFER` | NUMERIC |  | This is the quantity that was transferred during a prescription transfer. |
| 17 | `RX_XFR_QTY_UNIT_C_NAME` | VARCHAR | org | This is the unit associated with the quantity that was transferred during a prescription transfer. |
| 18 | `COMP_FILL_YN` | VARCHAR |  | Stores if this is a completion of a partial fill. For non-partial fills, it will always store a null. If this is a partial fill that does not complete the fill, then it will store a No. Otherwise, it will store a Yes. |
| 19 | `PAT_PAY_AMT_ESTIMAT` | NUMERIC |  | The patient pay amount estimated for the patient when requesting the fill. For example, this displays to the patient when requesting fills on the web with their credit card. If no estimate is shown to the patient, nothing will be stored. |
| 20 | `PAT_PAY_AMT_POSTED` | NUMERIC |  | The total amount paid by the patient for this order. |
| 21 | `PAT_PAY_AMT_APPRVD` | NUMERIC |  | The maximum allowed amount to charge the patient. This is used if an estimated price is shown to the patient while requesting the fill. For example, if an estimated price was shown to the patient this would initially be the estimated price plus a buffer. If blank, there is no maximum. |
| 22 | `PRES_DISP_CUST_ID` | VARCHAR |  | This item contains the government issued ID of the customer picking up the corresponding prescription fill. |
| 23 | `RX_FILL_DC_USER_ID` | VARCHAR |  | The unique ID of the user who filled a discontinued prescription. Normally this user is a pharmacist. |
| 24 | `RX_FILL_DC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 25 | `RX_BILL_PAYMENT_ID` | NUMERIC |  | In table ORDER_DISP_INFO_2, the column RX_BILL_PAYMENT_ID (I ORD 47815) has been deprecated. This column has been replaced by column RX_TAR_ID (I ORD 47816) in the table RX_ORDER_DISP_PAT_PMTS. The deprecated column's data is no longer available because it is no longer populated in Chronicles. |
| 26 | `RX_REFILL_REQ_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 27 | `PROD_EXP_DATE` | DATETIME |  | This item tracks the expiration date of the product, which is the date on which the drug needs to be discarded due to spoilage. |
| 28 | `RX_ACTIVE_PHR_ID` | NUMERIC |  | The pharmacy that is currently processing this fill request. |
| 29 | `RX_ACTIVE_PHR_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 30 | `CONTINUE_FILL_ON_DC_DTTM` | DATETIME (UTC) |  | This item stores the most recent instant the continuation of the fill on a reordered prescription was approved. |
| 31 | `FILL_DAY_SUP_THPY` | INTEGER |  | This item stores the number of days that the patient will be taking the medication that was dispensed. |
| 32 | `RX_PART_FILL_PAT_CHARG` | NUMERIC |  | Stores the partial fill patient pay amount at the time of dispense, if the partial was reversed after it was dispensed for the rebilling on completion fill. |
| 33 | `RX_TRANSITION_OVRIDE_STAT_C_NAME` | VARCHAR |  | This item stores whether or not a medication transition in place for the prescription has been overridden on the fill-level. |
| 34 | `RX_TRANSITION_OVRIDE_RSN_C_NAME` | VARCHAR | org | This item stores the reason that the medication transition was overridden on the fill-level. |
| 35 | `RX_TRANSITION_OVRIDE_CMT` | VARCHAR |  | This item stores a free-text comment explaining why the medication transition was overridden on the fill-level. |
| 36 | `RX_TRANSITION_OVRIDE_USR_ID` | VARCHAR |  | This item stores the user that overrode the medication transition on a fill-level. |
| 37 | `RX_TRANSITION_OVRIDE_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 38 | `RX_TRANSITION_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | This item stores the Coordinated Universal Time (UTC) instant that the user overrode the medication transition. |
| 39 | `OTH_PAY_COV_AMT` | NUMERIC |  | The total dollar amount of any payment from another source including coupons. |
| 40 | `PAT_PAY_CHA_APPROVE` | NUMERIC |  | When the Patient Charge Amount Changed flag is acknowledged by the user, this will store what Patient Charge (ORD 47380) amount they approved. It is used to make sure we don't re-add the flag unless the Patient Charge amount differs from this value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

