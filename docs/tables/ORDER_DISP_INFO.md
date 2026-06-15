# ORDER_DISP_INFO

> This table contains dispense information for orders.

**Overflow family:** [ORDER_DISP_INFO_2](ORDER_DISP_INFO_2.md), [ORDER_DISP_INFO_3](ORDER_DISP_INFO_3.md), [ORDER_DISP_INFO_4](ORDER_DISP_INFO_4.md)  
**Primary key:** `ORDER_MED_ID`, `CONTACT_DATE_REAL`  
**Columns:** 38  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the order that these actions were taken on. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `FILL_PHR_ID` | NUMERIC |  | The fill pharmacy for prescription being filled from Integrated pharmacy for each fill. A prescription could be filled multiple times and each fill will have a fill pharmacy saved. A fill request is a contact on the order record recording information about the specific dispense of the order. |
| 4 | `FILL_PHR_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 5 | `FILL_AUTHPHRMCST_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `FILL_SERVICE_DATE` | DATETIME |  | The date of service for a prescription fill. The date of service can be entered by a user during the filling process. If no service date was entered by the user, then the date of service is the date of the first successful adjudication. If the prescription fill was not adjudicated, then the date of service is the date the fill was dispensed. |
| 7 | `FILL_NUMBER` | NUMERIC |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. The value is used in adjudication to indicate what fill we are adjudicating. The fill numbers are sequential with the first fill set to 0 and all refills numbered 1-99. |
| 8 | `FILL_SUPPLY_DAYS` | NUMERIC |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This is the number of days this fill will supply. For example, this fill dispensed enough to cover a 30-day supply. |
| 9 | `FILL_DISP_QTY` | NUMERIC |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This is the actual amount the pharmacy is dispensing. This may be different from the intended quantity, which is what the prescriber intended the patient to receive. The two numbers may be different if the patient can only pay for a smaller days supply, or the pharmacy may only have a small amount of the medication left to dispense. |
| 10 | `FILL_INT_SUP_DAYS` | NUMERIC |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. If the fill is a partial fill, this is the number of days the supply that is dispensed will cover. For example, I have a partial fill of 15 tabs for a Daily medication. The intended days supply would be 15. |
| 11 | `FILL_IS_PARTIAL_YN` | VARCHAR |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This item indicates if the fill is a partial one. If the patient can only pay for a smaller supply or the pharmacy may only have a small amount of the medication left to dispense, then the actual amount dispensed will be different from the intended amount, which is what the prescriber intended the patient to receive. For example, if the patient has a fill of 30 tabs for a Daily medication for 30 days of supply, a partial fill of 15 tabs will cover 15 days of supply; and the patient can receive the rest of the fill later when the patient can pay or the pharmacy has more to dispense. This flag is also used in adjudication to let the insurer know that a fill is a partial one and the insurance company will adjust the payment amount accordingly. |
| 12 | `FILL_SOURCE_C_NAME` | VARCHAR |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This item saves the information about where/how the fill was initiated. For example, if the patient walks in the pharmacy and hands a paper script to the pharmacist, then the source will be Walk-in; if the prescription is routed from EpicCare order entry, then the source will be EpicCare; and if the patient requests a refill through MyChart, then the source will be MyChart. |
| 13 | `FILL_TYPE_C_NAME` | VARCHAR |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This item saves the type of the fill. The first fill on the new prescription will have the type of New; a refill will have the type of Refill; and refill requests will have the type of EpicCare Refill Request or Non-EpicCare Refill Request, depending on whether the authorizing provider is an EpicCare provider. |
| 14 | `FILL_STATUS_C_NAME` | VARCHAR | org | When a order is placed in an integrated pharmacy, a contact is created in the order and all order information is saved to this order contact. This item saves the current status of the order. An order could have different status. For example, when it's being reviewed, the status will be marked as Reviewed; when it's being filled, its status will be marked as Filled. |
| 15 | `FILL_DISP_QTYUNT_C_NAME` | VARCHAR | org | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This is the actual amount unit the pharmacy is dispensing. The actual amount dispensed from the pharmacy could be different from the intended quantity, which is what the prescriber intended the patient to receive. The two numbers may be different in the case the patient can only pay for a smaller supply, or the pharmacy may only have a small amount of the medication left to dispense. |
| 16 | `FILL_INT_QTY` | NUMERIC |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This is the amount the prescriber intended the patient to receive. In the case of a partial fill, the patient can only pay for a smaller supply or the pharmacy may only have a small amount of the medication left to dispense, and this actual dispense amount is saved in the dispense quantity. |
| 17 | `FILL_INT_QTYUNT_C_NAME` | VARCHAR |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This is the amount unit the prescriber intended the patient to receive. In the case of a partial fill, the patient can only pay for a smaller supply or the pharmacy may only have a small amount of the medication left to dispense, and this actual dispense amount is saved in the dispense quantity. |
| 18 | `CHG_STATUS_C_NAME` | VARCHAR |  | When a prescription is filled in an integrated pharmacy, a fill contact is created in the order and all fill information is saved to this fill contact. A prescription can have multiple fills. This item indicates the current charging status of the fill. It is used to track if the payor has agreed to pay the pharmacy for this fill. |
| 19 | `CASH_PRICE` | NUMERIC |  | The cash price for this order. |
| 20 | `RX_TO_PHRM_USER_ID` | VARCHAR |  | This is the user that authorized the incoming prescription transfer (typically a pharmacist) when the user exists in the User (EMP) master file. |
| 21 | `RX_TO_PHRM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `RX_TO_PHRM_USERNAM` | VARCHAR |  | This is the name of the user that authorized the incoming prescription transfer (typically a pharmacist) when the user does not exist in the User (EMP) master file. |
| 23 | `RX_FRM_PHRM_USER_ID` | VARCHAR |  | This is the user that authorized the outgoing prescription transfer (typically a pharmacist) when the user exists in the User (EMP) master file. |
| 24 | `RX_FRM_PHRM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 25 | `RX_FRM_PHRM_USERNAM` | VARCHAR |  | This is the name of the user that authorized the outgoing prescription transfer (typically a pharmacist) when the user does not exist in the User (EMP) master file. |
| 26 | `RX_FRM_PHRM_ID` | NUMERIC |  | This is the pharmacy from which the prescription was transferred when the pharmacy exists in the Pharmacy (PHR) master file. |
| 27 | `RX_FRM_PHRM_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 28 | `RX_FRM_PHRM_NAM` | VARCHAR |  | This is the name of the pharmacy from which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| 29 | `RX_FRM_PHRM_PHNUM` | VARCHAR |  | This is the phone number of the pharmacy from which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| 30 | `RX_TO_PHRM_NAM` | VARCHAR |  | This is the name of the pharmacy to which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| 31 | `RX_TO_PHRM_PHNUM` | VARCHAR |  | This is the phone number of the pharmacy to which the prescription was transferred when the pharmacy does not exist in the Pharmacy (PHR) master file. |
| 32 | `RX_TRANSFER_COMMENT` | VARCHAR |  | These are the comments that are entered along with the prescription transfer. |
| 33 | `PAT_PAY_AMOUNT` | NUMERIC |  | This is the expected payment amount for this order. This can be calculated by the system and optionally overridden by the user. If the patient pay amount was overridden, then the override amount is stored here. |
| 34 | `FILL_PKG_DISPQTY` | NUMERIC |  | The number of packages dispensed for this fill. |
| 35 | `FILL_NDC_CSN` | VARCHAR |  | This column stores the package (NDC) contact serial number (CSN) for the dispensed medication. |
| 36 | `DISP_WHOLE_PKG_YN` | VARCHAR |  | Is the medication order dispensed in whole packages or not. This item is set to Yes when the order is dispensed as a whole package and does not apply for the orders merely dispensed in multiple packages. |
| 37 | `HAS_RX_FLAGS_YN` | VARCHAR |  | This indicates whether the fill request currently has any flags. Fill requests with flags appear in the flagged orders queue in Ambulatory Pharmacy. |
| 38 | `DAW_REASON_C_NAME` | VARCHAR | org | The category number for dispense as written (DAW) reason. It can be specified when dispensing a brand package (NDC) for a prescription fill. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

