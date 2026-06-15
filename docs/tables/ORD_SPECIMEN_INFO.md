# ORD_SPECIMEN_INFO

> This table contains information on the associated specimen for the order including active status and the accessioning lab system.

**Primary key:** `ORDER_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `SPECIMEN_LAB_ID` | NUMERIC |  | The lab (LLB) record ID responsible for filing the specimen information through the interface. |
| 3 | `SPECIMEN_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 4 | `SPECIMEN_ACTIVE_C_NAME` | VARCHAR |  | A compiled item used to generate an index of which specimens have not been deactivated on the order. (Eg. have no deactivated instant filed) |
| 5 | `SPECIMEN_ACTIVE_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the specimen was first filed from the lab interface system. |
| 6 | `SPECIMEN_INACTIVE_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the specimen was rendered inactive in response to a laboratory information system (LIS) message or linked order status change. |
| 7 | `SPECIMEN_INACTIVE_C_NAME` | VARCHAR |  | Interface or order status event which resulted in the specimen being marked unavailable for collection. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

