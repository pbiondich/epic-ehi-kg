# ENC_METRIC_ENGINE_RSLT

> Contains metrics for a patient, typically calculated from FLO data.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `METRIC_FLO_MET_DATA_CONTEXT_C_NAME` | VARCHAR |  | This related group stores metrics that are calculated by the flowsheet metrics engine. This item contains the data context for this line, which represents a single metric in this data context. |
| 7 | `METRIC_FLO_MET_METRIC_C_NAME` | VARCHAR |  | This related group stores metrics that are calculated by the flowsheet metrics engine. This item contains the metric ID for this line, which represents a single metric in this data context. |
| 8 | `METRIC_VALUE` | NUMERIC |  | This related group stores metrics that are calculated by the flowsheet metrics engine. This item contains the value of the metric for this line, which represents a single metric in this data context. |
| 9 | `METRIC_DISPLAY_NAME` | VARCHAR |  | This related group stores metrics that are calculated by the flowsheet metrics engine. This item contains the display name of the metric for this line, which represents a single metric in this data context. |
| 10 | `METRIC_LPP_ID` | NUMERIC |  | This related group stores metrics that are calculated by the flowsheet metrics engine. This item contains the LPP used to calculate the metric for this line, which represents a single metric in this data context. |
| 11 | `METRIC_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 12 | `METRIC_CALC_LN` | INTEGER |  | This related group stores metrics that are calculated by the flowsheet metrics engine. This item contains the corresponding line in SI EPT 87730 on this patient contact for this metric, which contains information about how this metric was calculated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

