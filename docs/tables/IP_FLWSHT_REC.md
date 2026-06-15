# IP_FLWSHT_REC

> This table contains linking information associated with flowsheet records.

**Primary key:** `FSD_ID`  
**Columns:** 5  
**Joined by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK | The unique ID for the flowsheet data record. |
| 2 | `INPATIENT_DATA_ID` | VARCHAR | shared | The unique ID of the inpatient record associated with this flowsheet reading. |
| 3 | `RECORD_DATE` | DATETIME |  | The date these flowsheet readings were taken. |
| 4 | `DAILY_NET` | NUMERIC |  | The daily net Intake/Output total for this date. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (18)

| From | Column | Confidence |
|------|--------|------------|
| [FLOWSHEET_METAEDIT_LOOSE](FLOWSHEET_METAEDIT_LOOSE.md) | `FSD_ID` | high |
| [FLOWSHEET_METAEDIT_STRICT](FLOWSHEET_METAEDIT_STRICT.md) | `FSD_ID` | high |
| [FLOWSHEET_METAEDIT_VAL](FLOWSHEET_METAEDIT_VAL.md) | `FSD_ID` | high |
| [FLOWSHEET_META_LOOSE](FLOWSHEET_META_LOOSE.md) | `FSD_ID` | high |
| [FLOWSHEET_META_STRICT](FLOWSHEET_META_STRICT.md) | `FSD_ID` | high |
| [FLOWSHEET_META_VAL](FLOWSHEET_META_VAL.md) | `FSD_ID` | high |
| [FLOWSHEET_NOTES](FLOWSHEET_NOTES.md) | `FSD_ID` | high |
| [FLOWSHT_NOTE_AUDIT](FLOWSHT_NOTE_AUDIT.md) | `FSD_ID` | high |
| [FLO_AUD_INST_COSIG](FLO_AUD_INST_COSIG.md) | `FSD_ID` | high |
| [FLO_AUD_USER_COSIG](FLO_AUD_USER_COSIG.md) | `FSD_ID` | high |
| [FLO_INST_COSIGNED](FLO_INST_COSIGNED.md) | `FSD_ID` | high |
| [FLO_USER_COSIGNED](FLO_USER_COSIGNED.md) | `FSD_ID` | high |
| [FLWSHT_SINGL_COL](FLWSHT_SINGL_COL.md) | `FSD_ID` | high |
| [IP_FLWSHT_EDITED](IP_FLWSHT_EDITED.md) | `FSD_ID` | high |
| [IP_FLWSHT_MEAS](IP_FLWSHT_MEAS.md) | `FSD_ID` | high |
| [IP_LDA_NOADDSINGLE](IP_LDA_NOADDSINGLE.md) | `FSD_ID` | high |
| [V_EHI_FLO_MEAS_EDITED](V_EHI_FLO_MEAS_EDITED.md) | `FSD_ID` | high |
| [V_EHI_FLO_MEAS_VALUE](V_EHI_FLO_MEAS_VALUE.md) | `FSD_ID` | high |

