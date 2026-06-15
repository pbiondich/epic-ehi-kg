# ORDER_IMAGE_AVAIL_INFO

> This table has, for this imaging order, the image availability information for each of the image archives from which you receive Image Availability Notifications.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMAGE_LOCATION_C_NAME` | VARCHAR | org | The server name category ID that store images for the imaging order. |
| 4 | `IMG_AVAIL_YN` | VARCHAR |  | Indicates whether images are available at this location. 'Y' indicates that images are available. 'N' or NULL indicates that images are not available. |
| 5 | `IMG_AVAIL_DTTM` | DATETIME (Local) |  | The updated date and time of the image availability information for the related image storage location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

