# ENC_METRIC_ENGINE_CALC

> Contains calculation data used for flowsheet metrics in this encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `METRICS_FLO_MET_DATA_CONTEXT_C_NAME` | VARCHAR |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the data context. |
| 7 | `METRICS_START_INST_UTC_DTTM` | DATETIME (UTC) |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the start instant for the reporting range of the corresponding metrics. |
| 8 | `METRICS_END_INST_UTC_DTTM` | DATETIME (UTC) |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the end instant for the reporting range of the corresponding metrics. |
| 9 | `METRICS_CALC_INST_UTC_DTTM` | DATETIME (UTC) |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the calculation instant of the corresponding metrics. |
| 10 | `METRICS_SOURCE_FLO_MEAS_ID` | VARCHAR |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the source FLO of the corresponding metrics. |
| 11 | `METRICS_SOURCE_FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 12 | `METRICS_FLO_MET_POPULATION_C_NAME` | VARCHAR |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the population of the corresponding metrics. |
| 13 | `METRICS_FLO_MET_STATUS_C_NAME` | VARCHAR |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the status of the corresponding metrics, which is either Active, Historical, or Erroneous. |
| 14 | `METRICS_SOURCE_ORDER_ID` | NUMERIC |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the ID of the ORD that was used to request and populate these metrics. |
| 15 | `METRICS_SOURCE_SUBID` | VARCHAR |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the Result Sub-ID of this piece of the ORD that was used to request and populate these metrics. |
| 16 | `METRICS_TRIGGER_C_NAME` | VARCHAR |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the trigger for this calculation, indicating why this calculation was performed. |
| 17 | `METRICS_INITIATING_USER_ID` | VARCHAR |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the EMP ID of the user that initiated this calculation. |
| 18 | `METRICS_INITIATING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `METRICS_SOURCE_ORD_DAT` | NUMERIC |  | This related group stores information about metrics that are calculated from the flowsheet metrics engine. The metrics are stored in SI EPT 87750 where I EPT 87755 is the line number in this group for the corresponding metadata. This item stores the contact on the ORD that created this set of metrics, if these originated from an ORD. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

