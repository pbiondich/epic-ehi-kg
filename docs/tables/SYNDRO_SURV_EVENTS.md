# SYNDRO_SURV_EVENTS

> Contains syndromic surveillance event information.

**Primary key:** `SYNDRO_SURV_EVENT_ID`  
**Columns:** 10  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SYNDRO_SURV_EVENT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the syndromic surveillance event record. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc.). |
| 3 | `SYNDRO_REGISTRY_ID` | NUMERIC |  | The unique ID of the syndrome (HFR) for the syndromic surveillance event. |
| 4 | `SYNDRO_REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the registry record. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient for the syndromic surveillance event. |
| 6 | `CONTRIBUTING_EVENT_DATE` | DATETIME |  | The date that the syndromic surveillance event contributes to the syndrome count. |
| 7 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `POSTAL_CODE_RAW` | VARCHAR |  | The raw postal code that the syndromic surveillance event contributes to in the syndrome trend. |
| 9 | `HOSPITAL_ONSET_YN` | VARCHAR |  | Indicates whether the syndromic surveillance event is considered hospital onset. 'Y' indicates that the event is considered hospital onset. 'N' or NULL indicate that the event is not considered hospital onset. |
| 10 | `RECORD_CREATION_DATE` | DATETIME |  | The date the record was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [SYNDRO_SURV_EVENT_ENCS](SYNDRO_SURV_EVENT_ENCS.md) | `SYNDRO_SURV_EVENT_ID` | high |
| [SYNDRO_SURV_EVENT_FLOS](SYNDRO_SURV_EVENT_FLOS.md) | `SYNDRO_SURV_EVENT_ID` | high |
| [SYNDRO_SURV_EVENT_INFS](SYNDRO_SURV_EVENT_INFS.md) | `SYNDRO_SURV_EVENT_ID` | high |
| [SYNDRO_SURV_EVENT_ORDERS](SYNDRO_SURV_EVENT_ORDERS.md) | `SYNDRO_SURV_EVENT_ID` | high |
| [SYNDRO_SURV_EVENT_PROBS](SYNDRO_SURV_EVENT_PROBS.md) | `SYNDRO_SURV_EVENT_ID` | high |

