# HH_INTVTN_ENC

> Contains Home Health care plan intervention overtime single items information.

**Primary key:** `INTERVENTION_ID`, `CONTACT_DATE_REAL`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | Unique identifier for the care plan intervention. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | Unique identifier for this contact for this patient. |
| 3 | `CONTACT_NUM` | VARCHAR |  | Contact number. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the contact owner deployment for this record. Links to table CL_COMMUNTY_INSTNC. |
| 6 | `INT_START_DT` | DATETIME |  | Care plan intervention start date. |
| 7 | `INT_RESOLV_DT` | DATETIME |  | Care plan intervention resolved date. |
| 8 | `EDIT_USER_ID` | VARCHAR |  | User ID of person who edited care plan intervention data. Links to table CLARITY_EMP. |
| 9 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EDIT_INSTANT` | DATETIME (Local) |  | Instant at which care plan intervention was edited. |
| 11 | `INTV_FREQ_ID` | VARCHAR |  | Care plan intervention frequency ID. Links to table IP_FREQUENCY. |
| 12 | `INTV_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 13 | `SCHEDULED_VISITS` | VARCHAR |  | Care plan intervention scheduled visits. |
| 14 | `CARE_PLAN_CSN` | VARCHAR |  | Link to care plan contact. Used to recreate historic versions of care plan. |
| 15 | `HAS_PENDED_ORDER_YN` | VARCHAR |  | Determines whether the intervention order was created but not sent. This is set to Yes if any user created an intervention order without sending it; No if an order is not created or it was created and already sent. |
| 16 | `HOME_CARE_ORDER_ID` | VARCHAR |  | This item stores the supplemental order ID that is created or generated for care plan intervention edit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

