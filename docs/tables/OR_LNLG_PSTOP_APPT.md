# OR_LNLG_PSTOP_APPT

> This table contains the Postop Appointments information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `POSTOP_APPT_UID` | VARCHAR |  | The unique ID of the post-op appointment. |
| 3 | `POSTOP_APPT_VT_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 4 | `POSTOP_APPT_PRC_ID` | VARCHAR |  | The procedure ID of the post-op appointment. |
| 5 | `POSTOP_APPT_PRC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 6 | `POSTOP_APPT_PRV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `POSTOP_APPT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

