# ORDER_MED_7

> This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow of:** [ORDER_MED](ORDER_MED.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 42  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `MED_DOSAGE_END_DATE` | DATETIME |  | Stores the calculated end date of the order when using the wide end date feature |
| 3 | `FIRST_DOSE_EDU_PATIENT_CSN_ID` | NUMERIC |  | The unique contact serial number of the patient encounter associated with first-dose education. |
| 4 | `PENDED_PREV_SIG` | VARCHAR |  | For a pended medication order, this holds the contents (if any) of the "Sig (Previous)" display item from the order composer. If populated, this is the sig (ORD 7055) of the source order at the time the reorder was created. |
| 5 | `DOSE_ADJ_ACCEPTED_YN` | VARCHAR |  | Stores whether the dose adjustment is accepted. |
| 6 | `MED_DOSE_CALCULATION_DESC` | VARCHAR |  | Stores medication dose override dose programming point calculation. |
| 7 | `NUM_DOSES_TO_SCHED` | INTEGER |  | Stores the number of doses that should actually be scheduled after reconciling a pre-existing OP order into an encounter which schedules OP meds |
| 8 | `DO_NOT_SCHED_PAST_DATE` | DATETIME |  | Stores the last date on which it is OK to schedule an OP order that has been reconciled into an encounter that schedules OP meds |
| 9 | `SCHED_FROM_PERIOD` | INTEGER |  | Stores the period to start scheduling from for an OP order that has been reconciled into an encounter that schedules OP meds |
| 10 | `SCHED_FROM_PERIOD_DURATION` | INTEGER |  | Stores the remaning number of days in the period to start scheduling from for an OP order that has been reconciled into an encounter that schedules OP meds |
| 11 | `SEND_TO_PHARM_REASON_C_NAME` | VARCHAR | org | Reasons for sending a prescription directly to a pharmacy. For Australia e-prescribing. |
| 12 | `RX_MOBILE_NUM` | VARCHAR |  | Patient's mobile phone number. For Australia e-prescribing. |
| 13 | `MED_PROV_ORDER_ID` | NUMERIC |  | Links to the shadow order containing provisional verify data |
| 14 | `TAPER_TRIMMING_INCOMPLETE_C_NAME` | VARCHAR |  | Set to Yes if the taper trimming UI's decision hasn't been made yet |
| 15 | `STARTED_TAKING_DATE` | DATETIME |  | The date the patient reports they started taking a medication |
| 16 | `RX_REQ_SUBTYPE_C_NAME` | VARCHAR | org | This item specifies the subtype of the external change request this order represents. It is only set on orders created by external pharmacies, and is used in conjunction with ORD 7499. |
| 17 | `RESCARE_REORDER_C_NAME` | VARCHAR |  | Response to a question that a user is shown when reordering or modifying an outpatient order while the patient is admitted to a residential care facility. |
| 18 | `DISCRETE_SIG_SOURCE_C_NAME` | VARCHAR |  | The discrete sig source category ID for the order. |
| 19 | `MED_ORIG_DOSAGE_END_DATE` | DATETIME |  | Stores the original dosage end date for a medication order when using the wide end date feature if it was changed after the order was signed |
| 20 | `SCHED_FIRST_DOSE_DTTM` | DATETIME (Local) |  | Stores the date and time that the first dose in an admission should be scheduled |
| 21 | `LAST_REFILL_REQUEST_UTC_DTTM` | DATETIME (UTC) |  | The datetime of when the patient last requested a refill for this medication order through MyChart. Used to determine when another refill can be requested for medications filled through non-integrated pharmacies. |
| 22 | `SCHEDULE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number of the Patient contact for when Low Acuity scheduling information is saved to an order (SI 34570). |
| 23 | `SOURCE_SCHED_IN_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the low-acuity admission contact if the source order is schedulable in that admission when the current order is signed or released. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 24 | `SCHEDULE_USING_METHOD_C_NAME` | VARCHAR |  | The schedule using method category ID for the order. This determines how the medication should schedule administration due times in an encounter that supports scheduling outpatient medications on the MAR. |
| 25 | `NEED_INTAKE_SCHED_YN` | VARCHAR |  | Stores whether the medication needs intake to be scheduled, even if it was ordered directly on the low acuity encounter. |
| 26 | `RX_WRITTEN_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant of when the prescription was written |
| 27 | `REMAINING_DOSES_BEFORE_INTAKE` | INTEGER |  | The system will track the number of doses remaining for the order prior to the most recent intake into a low acuity medication management encounter. |
| 28 | `MED_CHG_REPLACE_YN` | VARCHAR |  | Flag to determine if I ORD 7088 - Med change reorder ID is actually a replacement ID. |
| 29 | `USES_TOD_IN_PAT_SIG_C_NAME` | VARCHAR |  | If the patient sig contains time of day indicators like "morning", "noon", "evening", or "bedtime". 1 if yes it does, and I ORD 7661 will contain which times are included. 2 if no it doesn't, and that was determined either from an unsupported frequency or explicitly marking "no" when placing the composer. Null if the order was placed prior to this item, and therefore it isn't known. |
| 30 | `TREATMENT_IDENT` | VARCHAR |  | ID to track the treamtent group associated with this medication order. |
| 31 | `DISPENSE_REQUEST_IDENT` | VARCHAR |  | ID to track dispense request associated with this medication order. |
| 32 | `ADDL_WISH_MEDICATION_C_NAME` | VARCHAR |  | The additional wishes selection for the medication roll. Currently only used by the Netherlands. |
| 33 | `ADDL_WISH_DELIVER_YN` | VARCHAR |  | The additional wishes selection for deliver. Currently only used by the Netherlands. |
| 34 | `ERX_DISP_QTY_SUFFICIENT_YN` | VARCHAR |  | Whether or not a medication is to be dispensed as Quantity Sufficient. |
| 35 | `ERX_INP_WITH_LTC_YN` | VARCHAR |  | Whether or not an Inpatient e-prescribed order was signed with long-term care specific features enabled for the order. This does not include orders which used old long-term care e-prescribing. |
| 36 | `ORG_RX_QS_YN` | VARCHAR |  | Original Quantity Sufficient status. |
| 37 | `MEDICATION_ACCESS_REFERRAL_ID` | NUMERIC |  | The referral record used to request medication access. |
| 38 | `AUTO_ORD_REC_STATUS_C_NAME` | VARCHAR |  | The category ID indicating whether this order was created via automatic order reconciliation and whether it needs review, has been reviewed, or has otherwise been acted on. |
| 39 | `OMT_ORDER_YN` | VARCHAR |  | Only used in Norway currently. The term used in Norway for this treatment is 'LAR'. This item stores Yes if the order is for such treatment. |
| 40 | `FUTURE_MODIFY_STATE_C_NAME` | VARCHAR | org | If a future modify was signed, then this will contain the future modify state category ID for the order. |
| 41 | `FUTURE_MODIFY_LOCAL_DTTM` | DATETIME (Local) |  | If a future modify was signed, then this will contain the date of the future modify. Can be empty for pended and not yet signed orders. |
| 42 | `AUTO_SCHED_CSN_ID` | NUMERIC |  | Stores the low-acuity encounter where the medication is auto-scheduled based on department-level configurations. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHEDULE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `SOURCE_SCHED_IN_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in

Inbound joins are tracked on the logical base [ORDER_MED](ORDER_MED.md).

