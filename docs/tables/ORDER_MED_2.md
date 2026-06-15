# ORDER_MED_2

> This table enables you to report on medications ordered in EpicCare or Ambulatory Pharmacy (Prescriptions). This table should be used with ORDER_MED.

**Overflow of:** [ORDER_MED](ORDER_MED.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 48  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this medication order. This is an internal unique identifier for order records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `TXT_AUTHPROV_NAME` | VARCHAR |  | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's name. |
| 3 | `TXT_AUTHPROV_DEA` | VARCHAR |  | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's Dynamic Epic Advisory Database (DEA) number. |
| 4 | `TXT_AUTHPROV_PHONE` | VARCHAR |  | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's phone number. |
| 5 | `TXT_AUTHPROV_FAX` | VARCHAR |  | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's fax number. |
| 6 | `TXT_AUTHPROV_STREET` | VARCHAR |  | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's street address information. |
| 7 | `TXT_AUTHPROV_CITY` | VARCHAR |  | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's city. |
| 8 | `TXT_AUTHPROV_ZIP` | VARCHAR |  | In ambulatory pharmacy, a prescription order could be authorized by a non-EpicCare provider. There is no provider record for this provider. This is used to store the non-EpicCare provider's zip code. |
| 9 | `RX_NUM_FORMATTED` | VARCHAR |  | The formatted prescription number for the order. |
| 10 | `RX_COMMENTS` | VARCHAR |  | In an ambulatory pharmacy, the person who enters the prescription into the system can add additional comments to the prescription. The comments are not part of the order and are used for pharmacy internal communication only. The comments do not affect the patient instructions, nor the dispense information. |
| 11 | `RX_WRITTEN_DATE` | DATETIME |  | Store the prescription written date, which is the date the prescription was entered into the system through EpicCare, or the date the prescription was written to the paper prescription. |
| 12 | `EFQ_OVRD_DAY_TYPE` | NUMERIC |  | Specifies what the numeric values in the frequency override days columns represent. If it is 1 then the listed days are relative days. If it is 2 then the listed days are weekdays. Any other value has no meaning. |
| 13 | `EFQ_OVRD_CYCL_LEN` | NUMERIC |  | If there is a frequency override specified, this item will contain the length of a relative specified type cycle. For all other specified types this value will be ignored (and should be empty). |
| 14 | `CHART_CORRECTION_ID` | NUMERIC |  | For chart corrections, links the order to a Chart Correction Audit (CCA) record. |
| 15 | `PARENT_CE_ORDER_ID` | NUMERIC |  | When a cross-encounter order is released, this item stores the ID of the parent order. |
| 16 | `TPL_WT_SRC_C_NAME` | VARCHAR | org | The weight source of the treatment plan for this order, as of the time the order is signed. |
| 17 | `OVERRIDE_LINKED_C_NAME` | VARCHAR |  | The linked override resolved category number for the medication order. The category indicates whether the admins in the override pull are all linked to pharmacy orders. |
| 18 | `CONDITIONAL_C_NAME` | VARCHAR |  | Identifies an inpatient order as "conditional". |
| 19 | `COND_STATUS_C_NAME` | VARCHAR |  | For a conditional order, indicates whether the conditions for the order have been satisfied yet. |
| 20 | `PEND_REF_REAS_COMM` | VARCHAR |  | Extracts the comment attached to the pend refusal reason (I ORD 7706) |
| 21 | `PRIORITIZED_INST_TM` | DATETIME (Local) |  | The time and date that is used as the prioritized date. |
| 22 | `ORDER_QUESN_LIST` | VARCHAR |  | The order specific questions that are listed in the order composer for the order. |
| 23 | `EXT_PHARM_MED_NAME` | VARCHAR |  | Medication display name received from an external pharmacy. |
| 24 | `PEND_MED_ACTIVE_YN` | VARCHAR |  | A flag to determine if this is an active pending medication or not. |
| 25 | `PEND_PREV_ORD_ID` | VARCHAR |  | The previous order ID for the pending medication. This item is NOT networked to orders. |
| 26 | `TXT_AUTHPROV_NPI` | VARCHAR |  | If the authorizing provider for a medication is not currently an Epic provider (no SER record for this provider), free text provider items are used to save information about this provider. This item stores the National Provider ID (NPI) of the provider. |
| 27 | `ORD_TRANS_METHOD_C_NAME` | VARCHAR | org | This item holds the method of transmission for a given order. It should only be set from within an order transmittal rule using the transmission method property (LRC 161). |
| 28 | `PROFILE_ONLY_RX_YN` | VARCHAR |  | This item specifies whether the medication order is intended to be filled by the pharmacy immediately or should be filled later when requested by the patient. This flag can be set in order entry based on the order class or by selecting the 'profile only' checkbox in pharmacy order entry. |
| 29 | `DISP_QTY_REM` | NUMERIC |  | Stores the remaining authorized quantity (in Written Dispense Quantity unit) that the pharmacist can dispense. It is used in Ambulatory Pharmacy to calculate the Refills Remaining. |
| 30 | `FREQ_UNSCHEDULED_C_NAME` | VARCHAR |  | If the frequency is unscheduled, this column will store a 1. If the frequency is not unscheduled, this column will be blank. |
| 31 | `DURATION` | INTEGER |  | Duration for this medication. |
| 32 | `INTERVENTION` | VARCHAR |  | Intervention for this medication. |
| 33 | `LAST_SUSPEND_DTTM` | DATETIME (Local) |  | Instant this medication was last suspended. |
| 34 | `SIGN_ACTION_PEND_C_NAME` | VARCHAR |  | Sign action for pended order. |
| 35 | `ORIG_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 36 | `ORIG_STRENGTH` | VARCHAR |  | Original prescription column; contains the medication order strength. |
| 37 | `ORIG_ROUTE_C_NAME` | VARCHAR | org | Original prescription column; contains the medication order route. |
| 38 | `ORIG_MED_SOURCE_C_NAME` | VARCHAR | org | Original prescription column; contains the medication order source. |
| 39 | `ORIG_DIS_DISP_QTY` | NUMERIC |  | Original prescription column; contains the medication order discrete dispense quantity. |
| 40 | `ORIG_DISP_UNIT_C_NAME` | VARCHAR | org | Original prescription column; contains the medication order discrete dispense unit. |
| 41 | `ORIG_START_DATE` | DATETIME |  | Original prescription column; contains the medication order start date. |
| 42 | `ORIG_END_DATE` | DATETIME |  | Original prescription column; contains the medication order end date. |
| 43 | `ORIG_DAW_YN` | VARCHAR |  | Original prescription column; contains the medication order 'dispense as written?' flag and is either yes or no. |
| 44 | `PENDDC_STATUS_C_NAME` | VARCHAR |  | Status of an order with regard to pending discontinue. |
| 45 | `MED_DISC_REFILLS` | INTEGER |  | Saves the discrete medication refills information for the order. |
| 46 | `BACK_DATED_YN` | VARCHAR |  | Indicates whether the order was back-dated at the time the start date was entered |
| 47 | `RX_CLINICALLY_RV_YN` | VARCHAR |  | This specifies whether the prescription has been clinically reviewed by a pharmacist. Clinical review can either be required to occur before a prescription is filled or after it is filled during fill verification. |
| 48 | `PRIORITIZED_UTC_DTTM` | DATETIME (UTC) |  | Stores the prioritized instant for the result in UTC |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_MED](ORDER_MED.md).

