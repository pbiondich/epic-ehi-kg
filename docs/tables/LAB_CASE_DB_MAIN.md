# LAB_CASE_DB_MAIN

> The main table for Lab Anatomic Pathology cases. It contains mostly items that do not change much over time.

**Primary key:** `CASE_ID`  
**Columns:** 25  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `CASE_ACCESSION_DTTM` | DATETIME (Local) |  | The instant that the case was accessioned. Currently, 'accessioned' means the time when the case is first accepted in Case Builder. |
| 3 | `CASE_RECEIVED_DTTM` | DATETIME (Local) |  | The instant that the case was received. This is equivalent to the instant when the first specimen on the case was received. |
| 4 | `CASE_OVERDUE_DTTM` | DATETIME (Local) |  | The instant when the case is considered overdue. This is equivalent to the Case Accession Instant plus the Case Expected Length. |
| 5 | `CASE_GROUPER_ID` | NUMERIC |  | Stores the Requisition Grouper record ID that this case is linked to. |
| 6 | `CASE_PAT_CONTACT` | VARCHAR |  | Stores the patient contact that this case is linked to. |
| 7 | `CASE_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 8 | `DATE_ENTR_DT` | DATETIME |  | Stores the date the case was created. |
| 9 | `CASE_COLL_DTTM` | DATETIME (Local) |  | The date and time when the case was first collected. |
| 10 | `CASE_SIGNOUT_DTTM` | DATETIME (Local) |  | The date and time when the case was completely signed out. |
| 11 | `CONTAINER_ID` | VARCHAR | FK→ | The unique identifier of the tracking container associated with this case record. |
| 12 | `CASE_TASK_ADD_DTTM` | DATETIME (Local) |  | The latest date and time when a task was added to the case. |
| 13 | `INSTANT_PAT_ASSOC_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the patient was associated with the case. |
| 14 | `CASE_SUBSPECIALTY_C_NAME` | VARCHAR | org | The subspecialty category identifier for the case. |
| 15 | `LAST_TASK_ADDED_UTC_DTTM` | DATETIME (UTC) |  | The last date and time in UTC that a task was added to this case. |
| 16 | `CASE_ACCESSION_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the case was accessioned, in UTC |
| 17 | `PRIMARY_SPECIMEN_ID` | VARCHAR |  | The unique ID of the primary specimen on the case. |
| 18 | `SERVICE_LINE_PROVIDERTEAM_ID` | NUMERIC |  | The unique ID of the provider team which represents the service line assigned to the case. |
| 19 | `SERVICE_LINE_PROVIDERTEAM_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |
| 20 | `PRIM_SPEC_OVRIDE_USER_ID` | VARCHAR |  | The unique ID of the user who overrode the primary specimen of this case. This column is frequently used to link to the CLARITY_EMP table. |
| 21 | `PRIM_SPEC_OVRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `PRIM_SPEC_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | UTC date and time of when the primary specimen was overridden by the user |
| 23 | `CTZN_OVRIDE_USER_ID` | VARCHAR |  | The unique ID of the user who overrode the categorization of this case. This column is frequently used to link to the CLARITY_EMP table. |
| 24 | `CTZN_OVRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 25 | `CTZN_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | UTC date and time of when either the subspecialty or service categorization of the case were overridden |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CONTAINER_ID` | [OVC_DB_MAIN](OVC_DB_MAIN.md) | sole_pk | high |

