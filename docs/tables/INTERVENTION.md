# INTERVENTION

> This table contains data on intervention (LPI) records associated with a patient.

**Primary key:** `INTERVENTION_ID`  
**Columns:** 5  
**Joined by:** 38 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK | The unique ID for the intervention record. |
| 2 | `DISPLAY_NAME` | VARCHAR |  | The display name for this intervention. |
| 3 | `INTRV_TYPE_ID_INTRVNTN_TYPE_NAME` | VARCHAR |  | The name of the intervention type. |
| 4 | `INTRV_TYPE_CONTACT` | INTEGER |  | The intervention type contact for this intervention. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this intervention. This column is frequently used to link to the PATIENT table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (38)

| From | Column | Confidence |
|------|--------|------------|
| [FINDING_INTERVENTIONS](FINDING_INTERVENTIONS.md) | `INTERVENTION_ID` | high |
| [GOAL_INTRVNTN](GOAL_INTRVNTN.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_CONTACT](HH_INTVTN_CONTACT.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_DISC](HH_INTVTN_DISC.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_DISC_GROUP](HH_INTVTN_DISC_GROUP.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_ENC](HH_INTVTN_ENC.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_HX_CONT](HH_INTVTN_HX_CONT.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_INFO](HH_INTVTN_INFO.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_LINKED_LDA](HH_INTVTN_LINKED_LDA.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_POC_INFO](HH_INTVTN_POC_INFO.md) | `INTERVENTION_ID` | high |
| [HH_INTVTN_VARIANCE](HH_INTVTN_VARIANCE.md) | `INTERVENTION_ID` | high |
| [INTERVENTIONS_HISTORY](INTERVENTIONS_HISTORY.md) | `INTERVENTION_ID` | high |
| [INTERVENTION_FLO](INTERVENTION_FLO.md) | `INTERVENTION_ID` | high |
| [INTERVENTION_FSD](INTERVENTION_FSD.md) | `INTERVENTION_ID` | high |
| [INTERVENTION_READING_HX](INTERVENTION_READING_HX.md) | `INTERVENTION_ID` | high |
| [INTERV_SMARTTEXT](INTERV_SMARTTEXT.md) | `INTERVENTION_ID` | high |
| [INTVTN_CONTACT](INTVTN_CONTACT.md) | `INTERVENTION_ID` | high |
| [INTVTN_DOC_INFO](INTVTN_DOC_INFO.md) | `INTERVENTION_ID` | high |
| [INTVTN_OVRD_FREQ_DAYS](INTVTN_OVRD_FREQ_DAYS.md) | `INTERVENTION_ID` | high |
| [INTVTN_OVRD_FREQ_REL_INFO](INTVTN_OVRD_FREQ_REL_INFO.md) | `INTERVENTION_ID` | high |
| [INTVTN_OVRD_FREQ_TIME](INTVTN_OVRD_FREQ_TIME.md) | `INTERVENTION_ID` | high |
| [INV_TEMPLATE_INFO](INV_TEMPLATE_INFO.md) | `INTERVENTION_ID` | high |
| [INV_TEMP_INFO_2](INV_TEMP_INFO_2.md) | `INTERVENTION_ID` | high |
| [IP_WORKLIST](IP_WORKLIST.md) | `INTERVENTION_ID` | high |
| [LPI_WEBLINKS](LPI_WEBLINKS.md) | `INTERVENTION_ID` | high |
| [PROBLEM_INTERVENTION](PROBLEM_INTERVENTION.md) | `INTERVENTION_ID` | high |
| [RX_DEFERRAL_HISTORY](RX_DEFERRAL_HISTORY.md) | `INTERVENTION_ID` | high |
| [RX_INTERVENTION](RX_INTERVENTION.md) | `INTERVENTION_ID` | high |
| [RX_IVENT_DOC](RX_IVENT_DOC.md) | `INTERVENTION_ID` | high |
| [RX_IVENT_MEDS](RX_IVENT_MEDS.md) | `INTERVENTION_ID` | high |
| [RX_IVENT_NOTES](RX_IVENT_NOTES.md) | `INTERVENTION_ID` | high |
| [RX_IVENT_ORDERS](RX_IVENT_ORDERS.md) | `INTERVENTION_ID` | high |
| [RX_IVENT_OUTCOMES](RX_IVENT_OUTCOMES.md) | `INTERVENTION_ID` | high |
| [RX_IVENT_TYPES](RX_IVENT_TYPES.md) | `INTERVENTION_ID` | high |
| [RX_IVENT_USERINFO](RX_IVENT_USERINFO.md) | `INTERVENTION_ID` | high |
| [SSC_GEN_ENC_INFO](SSC_GEN_ENC_INFO.md) | `INTERVENTION_ID` | high |
| [VARIANCE](VARIANCE.md) | `INTERVENTION_ID` | high |
| [VISIT_SET_CARE_PLAN_ELEM](VISIT_SET_CARE_PLAN_ELEM.md) | `INTERVENTION_ID` | high |

