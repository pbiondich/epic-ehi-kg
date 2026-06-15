# SPEC_CHG_TRGR_TRACE

> This table contains trace information about a specimen's billing actions related to triggering a charge.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `ORDER_ID` | NUMERIC | shared | The unique ID of the order associated with the charge trace on the specimen. |
| 5 | `TRACE_DTTM` | DATETIME (Local) |  | The date and time when the charge on the specimen was triggered. |
| 6 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user whose action triggered the charge on the specimen. |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CHG_TRG_TRC_ACT_C_NAME` | VARCHAR |  | The charge trigger trace action category ID for the specimen. |
| 9 | `TRACE_COMMENT` | VARCHAR |  | The charge trigger trace comment entered by the system about the trigger action. |
| 10 | `TEST_LINE` | INTEGER |  | The test line that the charge on the specimen is associated with. |
| 11 | `RECORD_INFO` | VARCHAR |  | The trace information for a charge triggered on the specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

