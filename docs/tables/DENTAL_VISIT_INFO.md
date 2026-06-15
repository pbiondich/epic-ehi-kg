# DENTAL_VISIT_INFO

> The DENTAL_VISIT_INFO table contains information associated with dental visit records.

**Primary key:** `REGIMEN_ID`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The unique ID of the visit record for this row. |
| 2 | `VISIT_TREATMENT_ID` | NUMERIC |  | The unique ID of the treatment that contains a visit. |
| 3 | `VISIT_SPACING_DAYS` | INTEGER |  | The requested number of days between scheduled visits. |
| 4 | `VISIT_SCHE_INSTRUCT` | VARCHAR |  | The scheduling instructions for a visit. |
| 5 | `VISIT_APPT_LENGTH` | INTEGER |  | The requested appointment length for a visit. |
| 6 | `VISIT_APPOINTMENT` | NUMERIC |  | The unique contact serial number (CSN) for the appointment that is linked to a visit. |
| 7 | `VISIT_ORDER_NUMBER` | INTEGER |  | The relative order of a visit within the containing treatment. |
| 8 | `DENT_SCHED_STATUS_C_NAME` | VARCHAR |  | Indicates the scheduling status of a visit |
| 9 | `DENT_REQ_DATE` | DATETIME |  | Date requested by provider to schedule visit |
| 10 | `DENT_VISIT_TYPE_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 11 | `DENT_VISIT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `DENT_VISIT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 13 | `DENT_VIS_PROVTYPE_C_NAME` | VARCHAR | org | Requested provider type for dental visit |
| 14 | `DENT_VIS_STATUS_C_NAME` | VARCHAR |  | Status of dental visit |
| 15 | `VISIT_NAME` | VARCHAR |  | The name of the dental visit. |
| 16 | `PAT_ID` | VARCHAR | FK→ | The patient (EPT) ID for the patient that the dental visit is associated with |
| 17 | `REFERRAL_ORDER_ID` | NUMERIC |  | Linked referral order (ORD) for a dental visit. |
| 18 | `APPT_REQUEST_ID` | NUMERIC |  | Stores the ID of the linked appointment request. |
| 19 | `READY_FOR_SCHED_YN` | VARCHAR |  | Stores whether this visit should appear in scheduling workflows. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

