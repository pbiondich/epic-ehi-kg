# PAT_ENC_APPT

> The PAT_ENC_APPT table contains basic information about the appointment records in your system. Since one patient encounter can be an appointment with multiple providers and resources (joint appointment), the primary key of this table comprises PAT_ENC_CSN_ID, and LINE in which LINE is used to identify each provider within the appointment.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | Used to identify the provider within one appointment. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date on which the encounter took place. |
| 4 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `PROV_START_TIME` | DATETIME (Local) |  | The date and time that the appointment is scheduled to begin with this provider, such as 01/10/2000 14:45. |
| 6 | `APPT_PROV_PRIMARY_SPECIALTY_C_NAME` | VARCHAR | org | The provider's primary specialty for this appointment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

