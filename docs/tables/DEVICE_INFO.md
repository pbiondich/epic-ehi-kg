# DEVICE_INFO

> This table displays high-level information for device (DEV) records.

**Primary key:** `DEVICE_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DEVICE_ID` | VARCHAR | PK | The unique identifier for the device record. |
| 2 | `DEVICE_ID_DEVICE_NAME` | VARCHAR |  | The name for this device. |
| 3 | `DEVICE_NAME` | VARCHAR |  | The name for this device. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [IP_DEVICE_CAPTURE](IP_DEVICE_CAPTURE.md) | `DEVICE_ID` | high |
| [LNO_LAB_AUDIT_TRL](LNO_LAB_AUDIT_TRL.md) | `DEVICE_ID` | high |

