# POC_MEDICATIONS

> This table contains medication information for the Plan of Care (POC) master file.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 26  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_MED_ID` | NUMERIC | FK→ | The unique identifiers for order records associated with current medications that appear in the plan of care. |
| 4 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 5 | `DISPLAY_NAM` | VARCHAR |  | This item contains the medication display name at time the POC was created. |
| 6 | `ORDER_CLASS_C_NAME` | VARCHAR | org | This item contains the medication order class. |
| 7 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `FREQ_ID` | VARCHAR | FK→ | This item contains the medication frequency. |
| 9 | `FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 10 | `MEDICATION_DOSE` | VARCHAR |  | This item contains the medication dose. |
| 11 | `MEDICATION_ROUT_C_NAME` | VARCHAR | org | This item contains the medication route. |
| 12 | `MEDICATION_QTY` | VARCHAR |  | This item contains the medication quantity dispensed. |
| 13 | `MEDICATION_REFIL` | VARCHAR |  | This item contains the number of refills. |
| 14 | `MEDICATION_SIG` | VARCHAR |  | This item contains the medication sig. |
| 15 | `MEDICATION_LONG_SIG` | VARCHAR |  | This item contains the medication long sig. |
| 16 | `MEDICATION_START_DT` | DATETIME |  | This item contains the medication start date. |
| 17 | `MEDICATION_END_DT` | DATETIME |  | This item contains the medication end date. |
| 18 | `MEDICATION_CMT` | VARCHAR |  | This item contains the medication comments. |
| 19 | `MEDICATION_TAKING_DIFF_LINE` | INTEGER |  | The line to show in the plan of care if a medication on the plan of care is documented as being taken differently than prescribed. |
| 20 | `ORDER_MODE_C_NAME` | VARCHAR |  | This will store whether the medication is ordered as an inpatient or an outpatient med |
| 21 | `PRN_REASONS` | VARCHAR |  | For medications on the hospice plan of care that were ordered PRN, the reason documented for taking the medication. |
| 22 | `INDICATIONS` | VARCHAR |  | Indications for a medication on a hospice plan of care. |
| 23 | `HOSPICE_CVG_C_NAME` | VARCHAR |  | This column indicates the hospice coverage status of medications which are pulled to the hospice plan of care. |
| 24 | `DISCON_UTC_DTTM` | DATETIME (UTC) |  | This item stores the discontinued instant (UTC) of medications which are pulled to the hospice plan of care. |
| 25 | `HSPC_NONCVRD_MED_RSN_C_NAME` | VARCHAR | org | The reason a patient's medication is not covered by the hospice benefit. This appears on the Hospice Plan of Care. |
| 26 | `HSPC_NONCVRD_MED_RSN_C_CMT` | VARCHAR |  | The comment for the reason a patient's medication is not covered by the hospice benefit. This appears on the Hospice Plan of Care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FREQ_ID` | [IP_FREQUENCY](IP_FREQUENCY.md) | sole_pk | high |
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

