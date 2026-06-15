# AUTH_UM_STATUS_HX

> This table contains the authorization decision history for service authorizations.

**Primary key:** `AUTH_ID`, `LINE`  
**Columns:** 46  
**Org-specific columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK FK→ | The unique identifier for the authorization record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UM_STATUS_C_NAME` | VARCHAR |  | The status assigned to the service by the associated user on the specified date/time. |
| 4 | `UM_APPROVED_RSN_C_NAME` | VARCHAR | org | The authorized reason assigned to the service by the associated user on the specified date/time. |
| 5 | `UM_PART_APRV_RSN_C_NAME` | VARCHAR | org | The partial authorization reason assigned to the service by the associated user on the specified date/time. |
| 6 | `UM_DENIED_RSN_C_NAME` | VARCHAR | org | The denied reason assigned to the service by the associated user on the specified date/time. |
| 7 | `UM_DISMISSED_RSN_C_NAME` | VARCHAR | org | The dismissed reason assigned to the service by the associated user on the specified date/time. |
| 8 | `UM_NOT_REQUIRED_RSN_C_NAME` | VARCHAR | org | The no auth required reason assigned to the service by the associated user on the specified date/time. |
| 9 | `UM_PENDING_RSN_C_NAME` | VARCHAR | org | The pending reason assigned to the service by the associated user on the specified date/time. |
| 10 | `UM_CANCELED_RSN_C_NAME` | VARCHAR | org | The canceled/withdrawn reason assigned to the service by the associated user on the specified date/time. |
| 11 | `CHANGED_DTTM` | DATETIME (Local) |  | The date and time (local) the associated change (for ex, setting the status and status reason) happened on the service. |
| 12 | `CHANGED_BY_USER_ID` | VARCHAR |  | The user that made the change (for ex., assigned the status and status reason) to the service. |
| 13 | `CHANGED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `NUM_SVCS_APPROVED` | INTEGER |  | The number of services, units, or visits approved as of the associated user's edit as of the specified date/time. |
| 15 | `NUM_SVCS_REQUESTED` | INTEGER |  | The number of services, units, or visits requested as of the associated user's edit as of the specified date/time. |
| 16 | `REV_CODE_ID` | NUMERIC |  | The procedure revenue code assigned to the authorization record as of the specified date/time. This column can be used to link to the CL_UB_REV_CODE table. |
| 17 | `REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 18 | `PROC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 19 | `PROC_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 20 | `INTER_NUM_SVCS_APRV` | INTEGER |  | The number of services approved for each interval as of the specified date/time. |
| 21 | `INTER_NUM_SVCS_REQ` | INTEGER |  | The number of services requested for each interval as of the specified date/time. |
| 22 | `INTER_APRV_FREQ_ID` | VARCHAR |  | The ID of the associated Frequency Record for the approved recurring authorization as of the specified date/time. |
| 23 | `INTER_APRV_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 24 | `INTER_REQ_FREQ_ID` | VARCHAR |  | The ID of the associated Frequency Record for the requested recurring authorization as of the specified date/time. |
| 25 | `INTER_REQ_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 26 | `INTER_NUM_APRV` | INTEGER |  | The number of times the interval has been approved to repeat as of the specified date/time. |
| 27 | `INTER_NUM_REQ` | INTEGER |  | The number of times the interval has been requested to repeat as of the specified date/time. |
| 28 | `UM_STATUS_CHANGE_SRC_C_NAME` | VARCHAR |  | When the status changes on a service authorization, this item indicates if the change was manual or done automatically by ASA. |
| 29 | `UM_CLOSED_RSN_C_NAME` | VARCHAR | org | The closed reason assigned to the service by the associated user on the specified date/time. |
| 30 | `PROC_FREE_TEXT` | VARCHAR |  | Audits changes made to AUT-1115 in UM AUTs. |
| 31 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 32 | `NDC_ID` | VARCHAR | FK→ | Audits changes to the NDC associated with the service. |
| 33 | `NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 34 | `REQ_RX_QTY` | NUMERIC |  | The history item containing the requested quantity limit for the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 35 | `REQ_RX_DISP_QTYUNIT_C_NAME` | VARCHAR | org | The history item containing the requested quantity limit unit for the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 36 | `REQ_RX_DAYS` | NUMERIC |  | The history item containing the requested quantity limit number for days of the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 37 | `REQ_UM_MED_TIER_C_NAME` | VARCHAR | org | The history item containing the requested tier for the selected medication. |
| 38 | `APRV_RX_QTY` | NUMERIC |  | The history item containing the approved quantity limit for the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 39 | `APRV_RX_DISP_QTYUNIT_C_NAME` | VARCHAR |  | The history item containing the approved quantity limit unit for the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 40 | `APRV_RX_DAYS` | NUMERIC |  | The history item containing the approved quantity limit number for days of the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 41 | `APRV_UM_MED_TIER_C_NAME` | VARCHAR |  | The history item containing the approved tier for the selected medication. |
| 42 | `FORMULARY_QL_QUANTITY` | NUMERIC |  | The history item containing the formulary quantity limit for the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 43 | `FORMULARY_QL_DISP_QTYUNIT_C_NAME` | VARCHAR |  | The history item containing the formulary quantity limit for the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 44 | `FORMULARY_QL_DAYS` | NUMERIC |  | The history item containing the formulary quantity limit number for days of the selected medication. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 45 | `FORMULARY_UM_MED_TIER_C_NAME` | VARCHAR |  | The history item containing the formulary tier for the selected medication. |
| 46 | `UM_WORKFLOW_STAGE_C_NAME` | VARCHAR |  | The workflow stage category for the authorization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |
| `NDC_ID` | [RX_NDC](RX_NDC.md) | sole_pk | high |

