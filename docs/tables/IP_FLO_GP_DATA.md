# IP_FLO_GP_DATA

> This table contains generic information about flowsheet groups/rows.

**Primary key:** `FLO_MEAS_ID`  
**Columns:** 3  
**Joined by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FLO_MEAS_ID` | VARCHAR | PK | The unique ID of the flowsheet group/row. |
| 2 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 3 | `DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (11)

| From | Column | Confidence |
|------|--------|------------|
| [IP_FLOWSHEET_ROWS](IP_FLOWSHEET_ROWS.md) | `FLO_MEAS_ID` | high |
| [IP_FLWSHT_EDITED](IP_FLWSHT_EDITED.md) | `FLO_MEAS_ID` | high |
| [IP_FLWSHT_MEAS](IP_FLWSHT_MEAS.md) | `FLO_MEAS_ID` | high |
| [IP_LDA_NOADDSINGLE](IP_LDA_NOADDSINGLE.md) | `FLO_MEAS_ID` | high |
| [SEP1_AUTOPOP_INIT_HYPOTN](SEP1_AUTOPOP_INIT_HYPOTN.md) | `FLO_MEAS_ID` | high |
| [SEP1_AUTOPOP_ORGAN_DSFX](SEP1_AUTOPOP_ORGAN_DSFX.md) | `FLO_MEAS_ID` | high |
| [SEP1_AUTOPOP_PERS_HYPOTN](SEP1_AUTOPOP_PERS_HYPOTN.md) | `FLO_MEAS_ID` | high |
| [SEP1_AUTOPOP_RE_ASMT](SEP1_AUTOPOP_RE_ASMT.md) | `FLO_MEAS_ID` | high |
| [SEP1_AUTOPOP_SIRS](SEP1_AUTOPOP_SIRS.md) | `FLO_MEAS_ID` | high |
| [V_EHI_FLO_MEAS_EDITED](V_EHI_FLO_MEAS_EDITED.md) | `FLO_MEAS_ID` | high |
| [V_EHI_FLO_MEAS_VALUE](V_EHI_FLO_MEAS_VALUE.md) | `FLO_MEAS_ID` | high |

