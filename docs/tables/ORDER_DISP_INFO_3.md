# ORDER_DISP_INFO_3

> This table contains dispense information for orders.

**Overflow of:** [ORDER_DISP_INFO](ORDER_DISP_INFO.md)  
**Primary key:** `ORDER_MED_ID`, `CONTACT_DATE_REAL`  
**Columns:** 33  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `RX_FILL_NOTE_ID` | VARCHAR |  | Prescription fill level note from the requesting source. |
| 4 | `ACQ_COST_CODE_C_NAME` | VARCHAR | org | Cost code used when calculating acquisition cost for the order. |
| 5 | `CHARGING_CSN` | NUMERIC |  | Contains the patient contact serial number (CSN) of the pharmacy visit contact to use for charge and payment posting. |
| 6 | `EMRG_FILL_YN` | VARCHAR |  | Is the current fill an emergency fill. An emergency fill is a short term refill that is approved by a pharmacist so that a patient can stay on their therapy while waiting for a refill authorization request (RAR) to be approved. |
| 7 | `EMERG_FILL_RSN_C_NAME` | VARCHAR | org | The discrete reason the user gave for creating an emergency fill. |
| 8 | `EMERG_FILL_NOTE_ID` | VARCHAR |  | Stores the ID for a note (HNO) containing the free text additional details given for why it is necessary to create an emergency fill. |
| 9 | `TAX_DUE_TOTAL` | NUMERIC |  | This column holds the rounded value for the total amount due in taxes when the medication was sold. |
| 10 | `FILL_START_DATE` | DATETIME |  | Indicates the date the patient is expected to begin taking a particular dispense of a prescription. |
| 11 | `TAX_EXEMPT_YN` | VARCHAR |  | The column holds whether the tax was exempted when the medication was sold. |
| 12 | `ADJUD_REVERSE_ONLY_YN` | VARCHAR |  | This indicates that an adjudication with a failed reversal should not be resubmitted once the reversal failure is corrected. This will only ever be set for adjudications from Hyperspace. It is not used for Willow Ambulatory. |
| 13 | `RX_FILL_NAME_BRAND` | VARCHAR |  | The brand name for the prescription fill. E.g. in the name "TYLENOL (acetaminophen) 325 mg tablets", this would be "TYLENOL". |
| 14 | `RX_FILL_NAME_GENERIC` | VARCHAR |  | The generic name for the prescription fill. E.g. in the name "TYLENOL (acetaminophen) 325 mg tablets", this would be "acetaminophen". |
| 15 | `RX_FILL_IS_BRAND_YN` | VARCHAR |  | Is the fill for a brand medication. This helps determine how the medication name for the fill should be displayed. E.g. if it's a fill for a brand medication, the name would be "TYLENOL (acetaminophen) 325 mg tablets". If it's a fill for a generic medication, the generic medication name would display first. The default is No. |
| 16 | `RX_FILL_NAME_DOSAGE` | VARCHAR |  | The dosage for the prescription fill. E.g. in the name "TYLENOL (acetaminophen) 325 mg tablets", this would be "325 mg tablets". |
| 17 | `RX_TAX_ROUNDING_METHOD_C_NAME` | VARCHAR |  | This column contains the rounding method used to calculate the total taxes for a medication sold within a transaction in an outpatient pharmacy. |
| 18 | `TAX_EXEMPTED_TOTAL` | NUMERIC |  | This column contains the rounded value for total amount of taxes exempted when the medication was sold. |
| 19 | `FILL_END_DATE` | DATETIME |  | Indicates the date the patient is expected to end taking a particular dispense of a prescription. |
| 20 | `FILL_EPISODE_ID` | NUMERIC |  | Which therapy episode does this order fill correspond to |
| 21 | `FILL_THERAPY_TYPE_C_NAME` | VARCHAR | org | The therapy type for this order's fill |
| 22 | `FILL_LINE_TYPE_C_NAME` | VARCHAR | org | The line type for this order's fill |
| 23 | `FILL_DELIVERY_TYPE_C_NAME` | VARCHAR | org | The delivery type for this order's fill. Delivery type refers to the type of infusion pump, not which shipping carrier |
| 24 | `FILL_DOSES_NUM` | INTEGER |  | The number of doses included in the fill. Typically calculated from the fill start and end date, but can be manually changed |
| 25 | `SCHEDULED_FILL_YN` | VARCHAR |  | Specifies whether this is a scheduled fill. |
| 26 | `OVERRIDE_SERVICE_DATE` | DATETIME |  | The override date of service for a prescription fill |
| 27 | `RX_REFILL_REQ_SER_ADDRESS_ID` | VARCHAR |  | This column stores the unique ID for the receiving provider's address on the refill request. It is used to identify an address using I SER 21000. |
| 28 | `FILL_WASTED_QTY` | NUMERIC |  | The amount of a dispense that was wasted in a home infusion shipment. |
| 29 | `HX_RX_FILL_YN` | VARCHAR |  | If set to Yes [1], then this is a historical fill on a prescription. |
| 30 | `HX_RX_FILL_DISP_UTC_DTTM` | DATETIME (UTC) |  | The dispense instant for a historical prescription fill. |
| 31 | `RX_FILL_NAME_PREFIX` | VARCHAR |  | The medication name prefix for the prescription fill. |
| 32 | `RX_TRANSFER_ELECTRONIC_YN` | VARCHAR |  | This item is used during electronic prescription transfers between two pharmacies. This indicates whether it's an electronic transfer. This is not used for integrated transfers. |
| 33 | `RX_TRANSFER_DOCUMENT_ID` | NUMERIC |  | This item is used during electronic prescription transfers between two pharmacies. This is a link to the document (DXR) containing the RxTransfer information associated with this transfer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

