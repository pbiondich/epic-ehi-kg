# VISIT_SET

> The VISIT_SET table contains high-level information about a single visit set, which is a template for recurring visits to address the care required for a patient. Most workflow-related information in VST is overtime and found in the VISIT_SET_VERSION table.

**Primary key:** `VISIT_SET_ID`  
**Columns:** 9  
**Org-specific columns:** 1  
**Joined by:** 15 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK | The unique identifier (.1 item) for the visit set record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...). Category values are stored in table ZC_RECORD_STATUS_2. |
| 3 | `RECORD_TYPE_VST_C_NAME` | VARCHAR |  | The type of this visit set record, used to differentiate various implementations of the VST masterfile. |
| 4 | `SCHEDULING_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `ORDER_COMMENT_NOTE_ID` | VARCHAR |  | The note record that contains order comments for all versions of the visit set. The order comment is reviewed and approved by a physician. |
| 6 | `SCHED_INSTRUCTIONS_NOTE_ID` | VARCHAR |  | The note record that contains scheduling instructions for all versions of the visit set. Scheduling instructions serve to provide additional context to schedulers and are neither reviewed nor approved by a physician. |
| 7 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created |
| 8 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient to whom this visit set belongs. This value is populated for visit sets associated with a Compass Rose episode. |
| 9 | `HOME_HEALTH_DISCIPLINE_C_NAME` | VARCHAR | org | The home health discipline associated with the visit set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (15)

| From | Column | Confidence |
|------|--------|------------|
| [HH_PAT_CERT_PERIOD](HH_PAT_CERT_PERIOD.md) | `VISIT_SET_ID` | high |
| [HOME_CARE_VISIT_SET_ORDER](HOME_CARE_VISIT_SET_ORDER.md) | `VISIT_SET_ID` | high |
| [SERVICE_PLAN_VISIT_SET](SERVICE_PLAN_VISIT_SET.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_CARE_PLAN_ELEM](VISIT_SET_CARE_PLAN_ELEM.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_DISCIPLINE](VISIT_SET_DISCIPLINE.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_HX_CHANGE](VISIT_SET_HX_CHANGE.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_HX_REVISION](VISIT_SET_HX_REVISION.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_POC_VER](VISIT_SET_POC_VER.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_ROUTE](VISIT_SET_ROUTE.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_ROUTE_DAYS_WEEK](VISIT_SET_ROUTE_DAYS_WEEK.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_SLOT](VISIT_SET_SLOT.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_SLOT_HX_CHANGE](VISIT_SET_SLOT_HX_CHANGE.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_SLOT_HX_RVSN](VISIT_SET_SLOT_HX_RVSN.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_VERSION](VISIT_SET_VERSION.md) | `VISIT_SET_ID` | high |
| [VISIT_SET_VISIT_PATTERN](VISIT_SET_VISIT_PATTERN.md) | `VISIT_SET_ID` | high |

