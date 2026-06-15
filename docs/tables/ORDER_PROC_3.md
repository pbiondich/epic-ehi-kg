# ORDER_PROC_3

> The ORDER_PROC_3 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same basic structure as ORDER_PROC, but was created as a third table to prevent ORDER_PROC_2 from getting any larger.

**Overflow of:** [ORDER_PROC](ORDER_PROC.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 59  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `MAMMO_OUTCOME_C_NAME` | VARCHAR |  | This column stores the outcome (e.g. FP/FN/TP/FN/etc) for a mammography study. This column is used to link to the ZC_MAMMO_OUTCOME table. |
| 3 | `OLD_RAD_STAT_C_NAME` | VARCHAR |  | This stores the category ID for the imaging study status (e.g. technician ended the exam, reading physician finalized the exam) before the order was canceled. This will only be populated for canceled imaging orders. This column is used to link to the ZC_RADIOLOGY_STS table. |
| 4 | `TRANSCRIPTIONIST` | VARCHAR |  | The transcriptionist of an external order result coming through the transcription interface. |
| 5 | `ORDERING_MODE_C_NAME` | VARCHAR |  | This indicates whether an order is an inpatient or outpatient order. Note that Outpatient orders can be placed from an Inpatient encounter as discharge orders. This column might be blank for Outpatient orders placed prior to the creation of the IP module. This column is used to link to the ZC_ORDERING_MODE table. |
| 6 | `PROV_STATUS_C_NAME` | VARCHAR |  | The provider status category number for the order at the time of the extract. This item reflects the providers' viewed status of the order result message. The amount, frequency and type of data stored in this item depends on the programming point records entered into the results message type definition in use at each facility. This column is used to link to the ZC_PROV_STATUS table. |
| 7 | `RESULT_TYPE_C_NAME` | VARCHAR |  | The result type category number for the order, if noted. A null value indicates that it is normal order results. This column is used to link to the ZC_ORD_RESULT_TYPE table. |
| 8 | `RFL_PRIORITY_C_NAME` | VARCHAR | org | The priority level category number of a referral order, which is used to specify whether a referral order is routine, urgent, emergency or elective. This column is used to link to the ZC_RFL_PRIORITY table. |
| 9 | `REFLEX_ORDER_ID` | NUMERIC |  | The order ID from which this reflex order was created. |
| 10 | `ORD_TRANS_METHOD_C_NAME` | VARCHAR | org | This item holds the method of transmission for a given order. It should only be set from a property within an order transmittal rule. |
| 11 | `NUM_SIG_REQ` | INTEGER |  | The number of physician signatures required to move the study status to final within the procedural applications. |
| 12 | `DURATION` | INTEGER |  | Duration for this procedure. |
| 13 | `INTERVENTION` | VARCHAR |  | Intervention for this procedure. |
| 14 | `SIGN_ACTION_PEND_C_NAME` | VARCHAR |  | Sign action for pended order. |
| 15 | `STAT_COMP_USER_ID` | VARCHAR |  | The ID of the user who marked an inpatient procedure as 'Complete' |
| 16 | `STAT_COMP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `STAT_COMP_DTTM` | DATETIME (Local) |  | The time and date that an inpatient procedure was marked as 'Complete' |
| 18 | `IS_EXT_READ_YN` | VARCHAR |  | This item indicates whether this order is for an external read of an imaging study. A null value should be assumed to be No. |
| 19 | `PENDDC_STATUS_C_NAME` | VARCHAR |  | Status of an order if the order is pending discontinue. |
| 20 | `AUTOINTK_COMPL_YN` | VARCHAR |  | This item contains whether an auto-intake has been completed for the order. |
| 21 | `RESULT_LOCATION_C_NAME` | VARCHAR |  | This item indicates which order item the result is stored. |
| 22 | `STAND_EOW_ID` | VARCHAR |  | Holds the ID number of the Standing Status In Basket message associated with this Order. The In Basket message informs the user that a Standing/Recurring order exists. |
| 23 | `INPAT_DISC_INTER_ID` | VARCHAR |  | This item stores the interval at which a standing order should be released for inpatient orders. |
| 24 | `INPAT_DISC_INTER_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 25 | `INPAT_AUTO_RLSE_YN` | VARCHAR |  | This item indicates whether child instances of a standing order should be automatically released for inpatient orders. |
| 26 | `LAB_CRT_CNCT_CSN_ID` | NUMERIC |  | The unique contact serial number for the contact that was created from this order. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 27 | `LAST_OVERALL_ASMT_C_NAME` | VARCHAR | org | The most recent overall mammography assessment for the order. This should be the same as the most recent value for ORDER_RAD_ASMT.ASSESSMENT_C. This column is used to link to the ZC_ASSESSMENT table. |
| 28 | `REVENUE_CODE_ID` | NUMERIC |  | The revenue code associated with the service. |
| 29 | `REVENUE_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 30 | `UNITS_REQUESTED` | INTEGER |  | The number of units requested for the service. |
| 31 | `UNITS_APPROVED` | INTEGER |  | The number of units approved for the service. |
| 32 | `TOTAL_PRICE` | NUMERIC |  | The total price of the service. |
| 33 | `PATIENT_PORTION` | NUMERIC |  | The amount or portion the patient will have to pay for the service they are being referred for. |
| 34 | `AUTH_REQUIRED` | VARCHAR |  | This column stores whether or not authorization is required for the service. |
| 35 | `NET_PAYABLE` | NUMERIC |  | The net payable of the service. |
| 36 | `NOT_COVERED` | VARCHAR |  | This item indicates whether or not the service is covered. |
| 37 | `PROVIDING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 38 | `COMMENT_WITH_CANCEL` | VARCHAR |  | Comment entered while cancelling an order. |
| 39 | `SOFT_DEL_FLAG` | VARCHAR |  | Soft deletion flag for order records associated with order-based transcriptions, which were deleted by the transcription soft-deletion utility. |
| 40 | `RESULT_TRACK_STS_C_NAME` | VARCHAR |  | This stores whether follow-up with recipients is required, in progress, or completed. This status is the per-order, see RESULT_TRACK_RECIP for individual recipient result tracking statuses. |
| 41 | `ORD_PHASE_OF_CARE_C_NAME` | VARCHAR | org | This item will store the phase of care for which this order was created. Example: Pre-Op, Intra-Op, PACU. |
| 42 | `REQUESTED_DATETIME` | DATETIME |  | The requested date and time. The items extracted to this column are populated by the Cadence Orders Interface. |
| 43 | `ORX_ID` | NUMERIC |  | Contains an ID from Order Lookup Index. This may be populated if an order originates from an Order Panel. |
| 44 | `ORX_ID_ORDER_LOOKUP_NAME` | VARCHAR |  | The name (.2 item) for the order panel record. |
| 45 | `RELEASED_INSTA_DTTM` | DATETIME (Local) |  | Stores the scheduled instant of the child order. |
| 46 | `LAST_SCHE_INST_DTTM` | DATETIME (UTC) |  | This item stores the inpatient order's last scheduled instant. |
| 47 | `INTERACT_COMMENT` | VARCHAR |  | Interaction override comment. |
| 48 | `COPY_POINTER_ID` | NUMERIC |  | This object tracks order record links created when using the inpatient or ambulatory order mover utilities to move an order record. This item is populated on the source order record and points to the target order record(s) created. |
| 49 | `AFTER_ORDER_ID` | VARCHAR |  | This column contains the After Order ID for an order after Order Transmittal. |
| 50 | `BEFORE_ORDER_ID` | VARCHAR |  | This column contains the Before Order ID for an order before Order Transmittal. |
| 51 | `DIET_COMMENTS` | VARCHAR |  | This column contains the Diet Comments entered for an order. |
| 52 | `ORD_CONDITION_FLAG` | INTEGER |  | This column contains the a Condition Flag if this is an order created from certain condition. |
| 53 | `COR_AFTR_FINAL_DTTM` | DATETIME (Local) |  | The date and time when the study was corrected and finalized. |
| 54 | `IS_HELD_ORDER_C_NAME` | VARCHAR |  | This item stores 1 if the order is signed and held and active |
| 55 | `NOCHRG_EXT_RSLT_YN` | VARCHAR |  | This column returns whether the order is an external result that should not drop charges. A value of 1 returns Y. A value of 0 returns N. A null value will return null but is treated the same as 0 when dropping charges. |
| 56 | `PROTOCOL_STATUS_C_NAME` | VARCHAR |  | Contains the current status of the order's protocols. Will be used to determine how to populate the protocol work list. |
| 57 | `PROTCL_ASGN_POOL_ID` | VARCHAR |  | If an order's protocol has been assigned to a pool, this item contains the pool ID of the assigned pool. |
| 58 | `PROTCL_ASGN_POOL_ID_POOL_NAME` | VARCHAR |  | The name of the scheduling pool used when searching for available providers for an appointment. |
| 59 | `PROTCL_ASGN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_PROC](ORDER_PROC.md).

