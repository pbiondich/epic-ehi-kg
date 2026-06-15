# OR_CASE_SURG_RSC

> The OR_CASE_SURG_RSC table contains OR management system case surgeons/staff/resources.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the lines of the surgical staff resource information in the case. |
| 3 | `SRG_STF_RSC_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `START_OFFSET` | INTEGER |  | The start time for the surgeon/staff/resource. It is measured in minutes relative to the beginning of the case. |
| 5 | `END_OFFSET` | INTEGER |  | The end time for the surgeon/staff/resource. It is measured in minutes relative to the beginning of the case. |
| 6 | `REQUIRED_YN` | VARCHAR |  | Yes/No flag which indicates whether the surgeon/staff/resource is required for the case. |
| 7 | `SURG_REC_TYPE_C_NAME` | VARCHAR |  | The category value which indicates the type of the surgeon/staff/resource. The possibilities are Surgeon, Anesthesia Staff, Operating Room, Surgical Staff, Surgical Equipment, Anesthesia Equipment, or Instrument. |
| 8 | `RESOURCE_TYPE` | VARCHAR |  | The specific type of the surgical resource within the case. |
| 9 | `LINE_INDEX` | INTEGER |  | Line index value of the surgeon/staff/resource within the case. |
| 10 | `BATCH_ASSIGN_YN` | VARCHAR |  | Yes/No flag which indicates whether or not the surgeon/staff/resource was assigned to the case through the batch assign method of the Assign Resources option within OR management system. |
| 11 | `MOD_START_OFFSET` | INTEGER |  | The start time of the resource, in minutes relative to the start of the case, if it has been shortened or lengthened. |
| 12 | `MOD_END_OFFSET` | INTEGER |  | The end time of the resource, in minutes relative to the start of the case, if it has been shortened or lengthened. |
| 13 | `IMPLANT_TRAY_ID` | NUMERIC |  | Stores the implant tray associated with the pool. |
| 14 | `IMPLANT_TRAY_ID_RECORD_NAME` | VARCHAR |  | Name of the implant tray |
| 15 | `AN_TEAM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

