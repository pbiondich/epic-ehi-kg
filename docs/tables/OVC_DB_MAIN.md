# OVC_DB_MAIN

> This table contains information about specimen containers. This includes information about what specimen it belongs to and its current location. This table was originally used to store submitter information. When looking at the SQL for this table you will see some columns still have "submitter" in their name even though this table now holds container information.

**Primary key:** `CONTAINER_ID`  
**Columns:** 7  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTAINER_ID` | VARCHAR | PK | The unique ID of the container record. |
| 2 | `PAT_LINK_ID` | VARCHAR |  | The unique ID of the patient (EPT) who is associated with the container record. |
| 3 | `CTNR_STATUS_C_NAME` | VARCHAR |  | The status category ID for the container. |
| 4 | `LINKED_RQG_RECORD_ID` | NUMERIC |  | The unique ID of the requisition grouper that is associated with the container record. |
| 5 | `NETWORK_EXT_IDENT` | VARCHAR |  | The ID for a container received over the Orders and Results Anywhere network, if a non-unique container ID was sent. |
| 6 | `NET_EXT_IDEN_ORG_ID` | NUMERIC |  | The unique ID of the organization who sent a container received over the Orders and Results Anywhere network, if a non-unique container ID was sent. |
| 7 | `NET_EXT_IDEN_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [LAB_CASE_DB_MAIN](LAB_CASE_DB_MAIN.md) | `CONTAINER_ID` | high |
| [OVC_EVENTS](OVC_EVENTS.md) | `CONTAINER_ID` | high |
| [RSLT_SEL_FROZEN_CONT](RSLT_SEL_FROZEN_CONT.md) | `CONTAINER_ID` | high |
| [SPEC_SEL_FROZEN_CONT](SPEC_SEL_FROZEN_CONT.md) | `CONTAINER_ID` | high |

