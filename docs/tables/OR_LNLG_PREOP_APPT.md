# OR_LNLG_PREOP_APPT

> This table contains the Preop Appointments information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `PREOP_APPT_UID` | VARCHAR |  | The unique ID of the pre-op appointment. |
| 3 | `PREOP_APPT_VT_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 4 | `PREOP_APPT_PROC_ID` | VARCHAR |  | The procedure ID of the pre-op appointment. |
| 5 | `PREOP_APPT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 6 | `PREOP_APPT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `PREOP_APPT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

