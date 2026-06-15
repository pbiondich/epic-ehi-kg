# CL_PLF

> This table extracts information from the PLF master file. PLF records represent the different areas that a patient can be in when using the Patient Location application. They can represent well known areas such as rooms and bed, or any location that the user wants to define. PLF records are also used for direction mapping in the Welcome kiosk.

**Primary key:** `RECORD_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 2 | `RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 3 | `DISPLAY_NAME` | VARCHAR |  | A patient/customer-friendly display name for the patient location. For example, this name will be displayed to patients using the Welcome kiosk. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

