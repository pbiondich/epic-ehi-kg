# PAT_GROUP

> The PAT_GROUP table contains information about patient groups. This table will hold groups used for scheduling as well as groups used for clinical documentation.

**Primary key:** `PAT_GROUP_ID`  
**Columns:** 9  
**Org-specific columns:** 1  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_GROUP_ID` | NUMERIC | PK | The unique ID of the patient group record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | This item stores the record status of the group record. |
| 3 | `PAT_GROUP_TYPE_C_NAME` | VARCHAR |  | This item defines the type of GRP record and whether or not this record stores a list of EPT IDs or a list of EPT CSNs. |
| 4 | `CONTACT_LIST_TYPE_C_NAME` | VARCHAR | org | This item describes the type of group that is being documented by clinical users. |
| 5 | `GROUP_START_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant that a group was started. |
| 6 | `GROUP_END_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when a group ended. |
| 7 | `CREATED_BY_USER_ID` | VARCHAR |  | This item stores the user ID for the user that created a group. |
| 8 | `CREATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `GROUP_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [GROUP_FACILITATORS](GROUP_FACILITATORS.md) | `PAT_GROUP_ID` | high |
| [PAT_GROUP_CLINICAL](PAT_GROUP_CLINICAL.md) | `PAT_GROUP_ID` | high |

