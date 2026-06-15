# SPEC_ARCHIVE_ORDER

> Contains information about orders that were archived as part of deceased patient archiving.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ARCH_ORDER_ID` | NUMERIC |  | The identifier of an order that has been archived as part of deceased patient archiving. Once the order is archived, all of the data from the order record is deleted and will not be available. This related group of items in the specimen record will be populated at the time of archiving by copying the most important pieces of information from the order record. |
| 4 | `ARCH_ORD_PROC_NAME` | VARCHAR |  | Name of an order that has been archived as part of deceased patient archiving. Once the order is archived, all of the data from the order record is deleted and will not be available. This related group of items in the specimen record will be populated at the time of archiving by copying the most important pieces of information from the order record. |
| 5 | `ARCH_ORD_PANEL_NAME` | VARCHAR |  | Name of an order panel that has been archived as part of deceased patient archiving. Once the order is archived, all of the data from the order record is deleted and will not be available. This related group of items in the specimen record will be populated at the time of archiving by copying the most important pieces of information from the order record. |
| 6 | `ARCH_ORD_USER_ID` | VARCHAR |  | The unique identifier of the ordering user for an order that has been archived as part of deceased patient archiving. Once the order is archived, all of the data from the order record is deleted and will not be available. This related group of items in the specimen record will be populated at the time of archiving by copying the most important pieces of information from the order record. |
| 7 | `ARCH_ORD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ARCH_ORD_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `ARCH_ORD_DTTM` | DATETIME (Local) |  | Prioritized instant for an order that has been archived as part of deceased patient archiving. Once the order is archived, all of the data from the order record is deleted and will not be available. This related group of items in the specimen record will be populated at the time of archiving by copying the most important pieces of information from the order record. |
| 10 | `ARCH_CSN_ID` | NUMERIC |  | Encounter contact serial number for an order that has been archived as part of deceased patient archiving. Once the order is archived, all of the data from the order record is deleted and will not be available. This related group of items in the specimen record will be populated at the time of archiving by copying the most important pieces of information from the order record. |
| 11 | `ARCH_AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

