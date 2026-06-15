# ORGAN_TRACK

> Track changes to the organ record that occur as data is added and changed. A table for audit trailing the changes.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRACK_INST` | DATETIME (Local) |  | Instant that item was changed. |
| 4 | `TRACK_WHO_ID` | VARCHAR |  | ID of the user who changed the item. |
| 5 | `TRACK_WHO_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `TRACK_ORG_STAT_C_NAME` | VARCHAR | org | Track changes in organ status. |
| 7 | `TRACK_SOURCE_C_NAME` | VARCHAR | org | Track changes to the organ source. |
| 8 | `TRACK_HLA_MATCH_C_NAME` | VARCHAR | org | Track changes to the human leukocyte antigen (HLA) match type. |
| 9 | `TRACK_DONOR_CRIT_C_NAME` | VARCHAR | org | Track changes to the donation criteria. |
| 10 | `TRACK_AG_MATCHES` | INTEGER |  | Track changes to the antigen matches. |
| 11 | `TRACK_CDC_YN` | VARCHAR |  | Track changes to whether the donor had risk factors for blood-borne disease transmission. |
| 12 | `TRACK_MATCH_RUN` | VARCHAR |  | Track changes to match run ID. |
| 13 | `TRACK_OPO_RISK_YN` | VARCHAR |  | Track changes to whether the donor is considered high risk by the organ procurement organization. |
| 14 | `TRACK_LINK_ORG_ID` | NUMERIC |  | Track changes to the Organ ID to which the current organ is linked. |
| 15 | `TRACK_DNR_ID_UNOS` | VARCHAR |  | Track changes made to the donor ID from the United Network for Organ Sharing (UNOS). |
| 16 | `TRACK_DNR_ABO_C_NAME` | VARCHAR |  | Track changes to the donor's blood type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

