# DEVICE_TYPE_INFO

> This table contains basic information on device types. Each device type (FDV) record can be a group of devices or even as granular as a specific model, depending on how your organization has set up the system.

**Primary key:** `DEVICE_TYPE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DEVICE_TYPE_ID` | NUMERIC | PK | The unique identifier for the device type record. |
| 2 | `DEVICE_TYPE_ID_DEVICE_TYPE_NAME` | VARCHAR |  | The name of this Device Type. |
| 3 | `DEVICE_TYPE_NAME` | VARCHAR |  | The name of this Device Type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

