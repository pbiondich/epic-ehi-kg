# RT_VOL_LAST_UPDATE_INFO

> Clarity table for Raidotherapy Volume update information, including internal version ID (I ORG 51200), internal last update instant (I ORG 51201), and external last update (I ORG 51202).

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INT_LAST_UPDATE_VERSION_NUM` | INTEGER |  | Stores the version ID of the most recent version of the record. This version is incremented each time the record receives an update through FHIR. For example, when a record is created, this item will be set to 1. For each subsequent update to this record, the value in this item will be incremented by 1. This value populates the Meta.versionId element in the outgoing BodyStructure FHIR resource. DLG 2233053 |
| 4 | `INT_LAST_UPDATE_VER_UTC_DTTM` | DATETIME (UTC) |  | This item stores the last update internal instant of the record, which is the instant when the version in ORG 51200 was filed. DLG 2233053 |
| 5 | `EXT_LAST_UPDATE_VERSION_DTTM` | DATETIME (Attached) |  | This item stores the last update instant of the resource that this record corresponds to, which is the instant when the external system last updated the contents of the resource, not necessarily the instant when the record was upated in Chronicles. This value comes from the Meta.lastUpdated element in the incoming BodyStructure FHIR resource. DLG 2233053 |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

